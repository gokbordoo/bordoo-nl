"""Samensteller v2: productfoto's waar beschikbaar, meerdere logoplekken via aanklikbare punten."""
import json
from config_garments import data, VAN_PRODUCT, PRODUCTEN, FOTOS
from samensteller import mini


def samensteller_body(tel, mail):
    knoppen = "".join(
        f'<label class="ss-product"><input type="radio" name="product" value="{p[0]}"{" checked" if p[0] == "polo" else ""}>{mini(p[0])}<span>{p[1]}</span></label>'
        for p in PRODUCTEN)
    return f"""<section class="kopstrook">
  <div class="wrap">
    <span class="eyebrow">Zelf samenstellen</span>
    <h1>Stel uw kleding samen</h1>
    <p class="intro">Kies een product, kleur en maten, upload uw logo en klik aan waar het moet komen. U ziet meteen hoe het eruitziet en vraagt met één klik een vrijblijvende offerte aan.</p>
  </div>
</section>

<section class="section section--compact">
  <div class="wrap samensteller">
    <div class="ss-voorbeeld">
      <div class="ss-buhne">
        <svg id="ss-svg" viewBox="0 0 120 120" role="img" aria-label="Voorbeeld van uw kledingstuk met logo"></svg>
        <span class="ss-label" id="ss-label"></span>
        <span class="ss-fotolabel" id="ss-fotolabel" hidden>Productfoto</span>
      </div>
      <div class="ss-bediening">
        <div class="seg" role="group" aria-label="Kant">
          <button type="button" data-kant="voor" aria-pressed="true">Voorkant</button>
          <button type="button" data-kant="achter" aria-pressed="false">Achterkant</button>
        </div>
        <button type="button" class="knop knop--rand knop--klein" id="ss-zoom" aria-pressed="false">Inzoomen op logo</button>
      </div>
      <p class="hint">Voorbeeld ter indruk. De echte kleur, stof en verhouding kunnen iets afwijken. U krijgt bij de offerte altijd eerst een proef te zien.</p>
    </div>

    <form class="form ss-form" id="ss-form" name="samenstelling" method="POST" action="bedankt.html" data-netlify="true" netlify-honeypot="website" enctype="multipart/form-data">
      <input type="hidden" name="form-name" value="samenstelling">
      <p class="verborgen"><label>Niet invullen: <input name="website"></label></p>
      <input type="hidden" name="kleur" id="h-kleur"><input type="hidden" name="logo_plekken" id="h-plekken">
      <input type="hidden" name="maten" id="h-maten"><input type="hidden" name="totaal" id="h-totaal">
      <input type="hidden" name="aanvraag" id="h-aanvraag"><input type="hidden" name="aantal_producten" id="h-aantalproducten">

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">1</span> Kies een product</legend>
        <div class="ss-producten">{knoppen}</div>
      </fieldset>

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">2</span> Kies een kleur <span class="ss-gekozen" id="ss-kleurnaam"></span></legend>
        <div class="ss-kleuren" id="ss-kleuren"></div>
      </fieldset>

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">3</span> Uw logo</legend>
        <div class="veld">
          <label for="logo">Upload uw logo</label>
          <input id="logo" name="logo" type="file" accept=".png,.jpg,.jpeg,.svg,.pdf,.ai,.eps,.webp">
          <span class="hint" id="ss-logohint">PNG, JPG, SVG of PDF ziet u meteen in het voorbeeld. Een EPS-bestand nemen we mee in de aanvraag.</span>
        </div>
        <div class="veld">
          <span class="veldlabel">Borduren of bedrukken?</span>
          <div class="keuzes">
            <label class="keuze"><input type="radio" name="techniek" value="Borduren" checked> Borduren</label>
            <label class="keuze"><input type="radio" name="techniek" value="Bedrukken"> Bedrukken</label>
            <label class="keuze"><input type="radio" name="techniek" value="Advies graag"> Advies graag</label>
          </div>
        </div>
      </fieldset>

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">4</span> Waar komt het logo? <span class="ss-gekozen">meerdere plekken mogelijk</span></legend>
        <div class="plekkiezer">
          <div class="plekkiezer__figuren" id="pk-figuren"></div>
          <div class="plekkiezer__lijst" id="pk-lijst" role="group" aria-label="Logoplekken"></div>
        </div>
        <div class="pk-gekozen" id="pk-gekozen"></div>
        <p class="ss-fout" id="pk-fout" hidden>Kies minstens één plek voor het logo.</p>
      </fieldset>

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">5</span> Maten en aantallen</legend>
        <div class="ss-maten" id="ss-maten"></div>
        <p class="ss-totaal">Totaal: <strong id="ss-totaal">0</strong> stuks</p>
        <p class="ss-fout" id="ss-fout" hidden>Vul bij minstens één maat een aantal in.</p>
      </fieldset>

      <div class="ss-mandbalk">
        <button type="button" class="knop knop--rand" id="ss-toevoegen">+ Toevoegen en nog een product kiezen</button>
        <p class="hint" id="ss-mandmelding" aria-live="polite">Meer dan één soort kleding? Voeg dit product toe aan uw aanvraag en stel daarna het volgende samen.</p>
      </div>

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">6</span> Uw gegevens</legend>
        <div class="veld--rij">
          <div class="veld"><label for="s-naam">Naam *</label><input id="s-naam" name="naam" type="text" autocomplete="name" required></div>
          <div class="veld"><label for="s-bedrijf">Bedrijf of vereniging</label><input id="s-bedrijf" name="bedrijf" type="text" autocomplete="organization"></div>
        </div>
        <div class="veld--rij">
          <div class="veld"><label for="s-email">E-mail *</label><input id="s-email" name="email" type="email" autocomplete="email" required></div>
          <div class="veld"><label for="s-tel">Telefoon</label><input id="s-tel" name="telefoon" type="tel" autocomplete="tel"></div>
        </div>
        <div class="veld"><label for="s-bericht">Opmerking</label><textarea id="s-bericht" name="bericht" placeholder="Bijv. een ander logo op de rug, of wanneer u het nodig heeft"></textarea></div>
      </fieldset>

      <div class="ss-samenvatting">
        <h3>Uw aanvraag</h3>
        <ol class="ss-mandlijst" id="ss-mandlijst"></ol>
        <h4 class="ss-huidig-kop" id="ss-huidig-kop">Product dat u nu samenstelt</h4>
        <dl id="ss-overzicht"></dl>
        <label class="akkoord"><input type="checkbox" id="s-akkoord" name="akkoord" required> <span>Ik ga akkoord dat Bordoo mijn gegevens gebruikt om deze aanvraag te beantwoorden, zoals beschreven in de <a href="privacy.html" target="_blank">privacyverklaring</a>. *</span></label>
        <button class="knop knop--hoofd" type="submit">Vraag offerte aan</button>
        <p class="hint">Vrijblijvend. U hoort meestal binnen twee werkdagen van ons. Vragen? Mail <a href="mailto:{mail}">{mail}</a>.</p>
      </div>
    </form>
  </div>
</section>

<script>
(function () {{
  var D = {json.dumps(data(), ensure_ascii=False)};
  var FOTOS = {json.dumps(FOTOS)};
  var VAN = {json.dumps(VAN_PRODUCT)};
  var MATEN = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL'];
  var CM_PER_EENHEID = 1.4;
  var $ = function (id) {{ return document.getElementById(id); }};
  var form = $('ss-form'), svg = $('ss-svg');
  var st = {{ p: null, kleur: null, plekken: [], actief: null, kant: 'voor', zoom: false, logo: null, logoNaam: null, aantallen: {{}}, mand: [] }};
  var OPSLAG = 'bordoo-aanvraag';
  try {{ st.mand = JSON.parse(localStorage.getItem(OPSLAG) || '[]') || []; }} catch (e) {{ st.mand = []; }}
  function bewaar() {{ try {{ localStorage.setItem(OPSLAG, JSON.stringify(st.mand)); }} catch (e) {{}} }}
  function esc(t) {{ return String(t).replace(/[&<>"]/g, function (c) {{ return {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }}[c]; }}); }}
  function regelTekst(r) {{ return r.product + ' – ' + r.kleur + ' – ' + r.techniek + ' – logo: ' + (r.plekken || 'nog kiezen') + ' – ' + r.totaal + ' stuks' + (r.maten ? ' (' + r.maten + ')' : ''); }}

  function naad(hex) {{ var r = parseInt(hex.substr(1, 2), 16), g = parseInt(hex.substr(3, 2), 16), b = parseInt(hex.substr(5, 2), 16);
    return (0.299 * r + 0.587 * g + 0.114 * b) > 150 ? 'rgba(0,0,0,.35)' : 'rgba(255,255,255,.35)'; }}
  function licht(hex) {{ return naad(hex).indexOf('0,0,0') > -1; }}
  function techniek() {{ var t = form.querySelector('input[name=techniek]:checked'); return t ? t.value : 'Borduren'; }}
  function pos(id) {{ return st.p.posities.find(function (q) {{ return q.id === id; }}); }}
  function foto(kant) {{ var f = FOTOS[st.p.id] && FOTOS[st.p.id][st.kleur]; return f && f[kant]; }}

  // ---------- product ----------
  function kiesProduct(id) {{
    st.p = D.producten.find(function (p) {{ return p.id === id; }}) || D.producten[1];
    form.querySelector('input[name=product][value="' + st.p.id + '"]').checked = true;
    if (st.p.kleuren.indexOf(st.kleur) < 0) st.kleur = st.p.kleuren[0];
    $('ss-kleuren').innerHTML = st.p.kleuren.map(function (k) {{
      var c = D.kleuren[k], heeftFoto = FOTOS[st.p.id] && FOTOS[st.p.id][k];
      return '<label class="ss-kleur" title="' + c.naam + '"><input type="radio" name="kleurkeuze" value="' + k + '"' + (k === st.kleur ? ' checked' : '') + '><span style="background:' + c.hex + '"></span><em>' + c.naam + (heeftFoto ? ' <b class="fototag">foto</b>' : '') + '</em></label>';
    }}).join('');
    var oud = st.plekken;
    st.plekken = oud.filter(function (pl) {{ return pos(pl.id); }}).map(function (pl) {{ var q = pos(pl.id); return {{ id: pl.id, cm: Math.min(q.max, Math.max(q.min, pl.cm)) }}; }});
    if (!st.plekken.length) st.plekken = [{{ id: st.p.posities[0].id, cm: st.p.posities[0].std }}];
    st.actief = st.plekken[st.plekken.length - 1].id;
    st.kant = pos(st.actief).kant;
    var lijst = st.p.maten === 'kleding' ? MATEN : ['Aantal'];
    $('ss-maten').innerHTML = lijst.map(function (m) {{
      var id = 'maat-' + m;
      return '<div class="ss-maat"><label for="' + id + '">' + m + '</label><input id="' + id + '" type="number" min="0" step="1" inputmode="numeric" value="' + (st.aantallen[m] || 0) + '" data-maat="' + m + '"></div>';
    }}).join('');
    document.querySelector('[data-kant=achter]').disabled = !st.p.achter;
    plekkiezer(); teken();
  }}

  // ---------- plekkiezer met aanklikbare punten ----------
  function plekkiezer() {{
    var kanten = st.p.achter ? ['voor', 'achter'] : ['voor'];
    $('pk-figuren').innerHTML = kanten.map(function (k) {{
      var punten = st.p.posities.filter(function (q) {{ return q.kant === k; }}).map(function (q) {{
        var aan = st.plekken.some(function (pl) {{ return pl.id === q.id; }});
        return '<button type="button" class="pk-punt' + (aan ? ' is-aan' : '') + '" data-plek="' + q.id + '" style="left:' + (q.x / 1.2) + '%;top:' + (q.y / 1.2) + '%" aria-pressed="' + aan + '" aria-label="' + q.naam + '"><span aria-hidden="true">' + (aan ? '✓' : '+') + '</span></button>';
      }}).join('');
      return '<div class="pk-figuur"><div class="pk-vlak"><svg viewBox="0 0 120 120" aria-hidden="true" style="--stof:#E7E2DF;--naad:rgba(0,0,0,.35)">' +
        (k === 'voor' ? st.p.voor : st.p.achter).replace(/rl-/g, 'rlp' + k + '-') + '</svg>' + punten + '</div><span class="pk-kant">' + (k === 'voor' ? 'Voorkant' : 'Achterkant') + '</span></div>';
    }}).join('');
    $('pk-lijst').innerHTML = st.p.posities.map(function (q) {{
      var aan = st.plekken.some(function (pl) {{ return pl.id === q.id; }});
      return '<button type="button" class="pk-chip' + (aan ? ' is-aan' : '') + '" data-plek="' + q.id + '" aria-pressed="' + aan + '"><span class="pk-vink" aria-hidden="true"></span>' + q.naam + '</button>';
    }}).join('');
    $('pk-gekozen').innerHTML = st.plekken.map(function (pl) {{
      var q = pos(pl.id);
      return '<div class="pk-rij' + (pl.id === st.actief ? ' is-actief' : '') + '" data-rij="' + pl.id + '"><span class="pk-rijnaam">' + q.naam + '</span>' +
        '<input type="range" min="' + q.min + '" max="' + q.max + '" step="1" value="' + pl.cm + '" data-cm="' + pl.id + '" aria-label="Breedte logo ' + q.naam + '">' +
        '<output>' + pl.cm + ' cm</output><button type="button" class="pk-weg" data-weg="' + pl.id + '" aria-label="' + q.naam + ' verwijderen">×</button></div>';
    }}).join('');
    $('pk-fout').hidden = st.plekken.length > 0;
  }}

  function wissel(id) {{
    var i = st.plekken.findIndex(function (pl) {{ return pl.id === id; }});
    if (i > -1) {{ st.plekken.splice(i, 1); if (st.actief === id) st.actief = st.plekken.length ? st.plekken[st.plekken.length - 1].id : null; }}
    else {{ st.plekken.push({{ id: id, cm: pos(id).std }}); st.actief = id; st.kant = pos(id).kant; }}
    plekkiezer(); teken();
  }}

  // ---------- voorbeeld tekenen ----------
  function teken() {{
    var hex = D.kleuren[st.kleur].hex;
    svg.style.setProperty('--stof', hex); svg.style.setProperty('--naad', naad(hex));
    var kant = st.kant === 'achter' && st.p.achter ? 'achter' : 'voor';
    var f = foto(kant), html = '<defs><filter id="borduur" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0.1" dy="0.15" stdDeviation="0.1" flood-opacity=".55"/></filter>' +
      '<filter id="borduur-foto" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx=".6" dy=".9" stdDeviation=".6" flood-opacity=".45"/></filter></defs>';
    var schaal, vb, plekXY;
    if (f) {{
      html += '<image href="' + f.src + '" x="0" y="0" width="' + f.w + '" height="' + f.h + '"/>';
      schaal = 1 / f.cmpx; vb = f.uitsnede;
      plekXY = function (q) {{ return f.pos[q.id]; }};
    }} else {{
      html += (kant === 'voor' ? st.p.voor : st.p.achter).replace(/rl-/g, 'rlm-');
      schaal = 1 / CM_PER_EENHEID; vb = [0, 0, 120, 120];
      plekXY = function (q) {{ return [q.x, q.y]; }};
    }}
    var filt = techniek() === 'Borduren' ? ' filter="url(#' + (f ? 'borduur-foto' : 'borduur') + ')"' : '';
    var zoomOp = null;
    st.plekken.forEach(function (pl) {{
      var q = pos(pl.id); if (q.kant !== kant) return;
      var xy = plekXY(q); if (!xy) return;
      var w = pl.cm * schaal, x = xy[0], y = xy[1];
      if (pl.id === st.actief || !zoomOp) zoomOp = [x, y, w];
      if (st.logo) {{
        html += '<image href="' + st.logo + '" x="' + (x - w / 2) + '" y="' + (y - w / 2) + '" width="' + w + '" height="' + w + '" preserveAspectRatio="xMidYMid meet"' + filt + '/>';
      }} else {{
        var ink = licht(hex) ? '#5E1424' : '#FFFFFF', h = w * 0.5;
        html += '<g' + filt + '><rect x="' + (x - w / 2) + '" y="' + (y - h / 2) + '" width="' + w + '" height="' + h + '" rx="' + (w * 0.06) + '" fill="none" stroke="' + ink + '" stroke-width="' + (w * 0.03) + '" stroke-dasharray="' + (w * 0.06) + ' ' + (w * 0.05) + '"/>' +
          '<text x="' + x + '" y="' + (y + h * 0.13) + '" text-anchor="middle" font-family="Archivo, Arial, sans-serif" font-weight="800" font-size="' + (w * 0.17) + '" fill="' + ink + '">UW LOGO</text></g>';
      }}
    }});
    svg.innerHTML = html;
    if (st.zoom && zoomOp) {{ var v = Math.max(zoomOp[2] * 3.2, vb[2] * 0.35); svg.setAttribute('viewBox', (zoomOp[0] - v / 2) + ' ' + (zoomOp[1] - v / 2) + ' ' + v + ' ' + v); }}
    else svg.setAttribute('viewBox', vb.join(' '));
    $('ss-fotolabel').hidden = !f;
    document.querySelectorAll('[data-kant]').forEach(function (b) {{ b.setAttribute('aria-pressed', b.dataset.kant === kant); }});
    $('ss-zoom').setAttribute('aria-pressed', st.zoom); $('ss-zoom').textContent = st.zoom ? 'Hele kledingstuk' : 'Inzoomen op logo';
    $('ss-kleurnaam').textContent = D.kleuren[st.kleur].naam;
    $('ss-label').textContent = st.p.naam + ' · ' + D.kleuren[st.kleur].naam + ' · ' + (kant === 'voor' ? 'voorkant' : 'achterkant');
    overzicht();
  }}

  function overzicht() {{
    var tot = 0, delen = [];
    document.querySelectorAll('[data-maat]').forEach(function (i) {{ var n = Math.max(0, parseInt(i.value, 10) || 0); st.aantallen[i.dataset.maat] = n; if (n) {{ tot += n; delen.push(i.dataset.maat + ': ' + n); }} }});
    $('ss-totaal').textContent = tot;
    var plekken = st.plekken.map(function (pl) {{ return pos(pl.id).naam + ' (' + pl.cm + ' cm)'; }}).join(', ');
    var rijen = [['Product', st.p.naam], ['Kleur', D.kleuren[st.kleur].naam], ['Techniek', techniek()], ['Logoplekken', plekken || 'nog kiezen'],
                 ['Logobestand', st.logoNaam || 'nog niet geüpload'], ['Aantal', tot ? tot + ' stuks' + (delen.length && st.p.maten === 'kleding' ? ' (' + delen.join(', ') + ')' : '') : 'nog in te vullen']];
    $('ss-overzicht').innerHTML = rijen.map(function (r) {{ return '<div><dt>' + r[0] + '</dt><dd>' + r[1] + '</dd></div>'; }}).join('');
    $('h-kleur').value = D.kleuren[st.kleur].naam; $('h-plekken').value = plekken;
    $('h-maten').value = delen.join(', '); $('h-totaal').value = tot;
    if (tot) $('ss-fout').hidden = true;
    st.huidig = {{ product: st.p.naam, kleur: D.kleuren[st.kleur].naam, techniek: techniek(), plekken: plekken, maten: st.p.maten === 'kleding' ? delen.join(', ') : '', totaal: tot }};
    $('ss-mandlijst').innerHTML = st.mand.map(function (r, i) {{
      return '<li><div><strong>' + esc(r.product) + '</strong> · ' + esc(r.kleur) + ' · ' + r.totaal + ' stuks<br><span>' + esc(r.techniek) + ', logo: ' + esc(r.plekken) + (r.maten ? ' · ' + esc(r.maten) : '') + '</span></div>' +
        '<button type="button" class="pk-weg" data-mandweg="' + i + '" aria-label="' + esc(r.product) + ' uit de aanvraag halen">×</button></li>';
    }}).join('');
    $('ss-mandlijst').hidden = !st.mand.length; $('ss-huidig-kop').hidden = !st.mand.length;
    var regels = st.mand.concat(tot ? [st.huidig] : []);
    $('h-aanvraag').value = regels.map(function (r, i) {{ return (i + 1) + '. ' + regelTekst(r); }}).join('\\n');
    $('h-aantalproducten').value = regels.length;
    return tot;
  }}

  $('ss-toevoegen').addEventListener('click', function () {{
    if (!st.plekken.length) {{ $('pk-fout').hidden = false; $('pk-figuren').scrollIntoView({{ block: 'center' }}); return; }}
    if (!overzicht()) {{ $('ss-fout').hidden = false; $('ss-maten').scrollIntoView({{ block: 'center' }}); return; }}
    st.mand.push(st.huidig); bewaar();
    st.aantallen = {{}}; document.querySelectorAll('[data-maat]').forEach(function (i) {{ i.value = 0; }});
    overzicht();
    $('ss-mandmelding').textContent = st.huidig.product + ' is toegevoegd. Kies nu het volgende product, of verstuur uw aanvraag onderaan.';
    document.querySelector('.ss-producten').scrollIntoView({{ block: 'start' }});
  }});
  $('ss-mandlijst').addEventListener('click', function (e) {{
    var b = e.target.closest('[data-mandweg]'); if (!b) return;
    st.mand.splice(+b.dataset.mandweg, 1); bewaar(); overzicht();
  }});

  // ---------- events ----------
  form.addEventListener('change', function (e) {{
    var t = e.target;
    if (t.name === 'product') kiesProduct(t.value);
    else if (t.name === 'kleurkeuze') {{ st.kleur = t.value; teken(); }}
    else if (t.name === 'techniek') teken();
    else if (t.id === 'logo') laadLogo(t.files[0]);
  }});
  form.addEventListener('input', function (e) {{
    var t = e.target;
    if (t.dataset.cm) {{ var pl = st.plekken.find(function (p) {{ return p.id === t.dataset.cm; }}); pl.cm = +t.value; t.nextElementSibling.textContent = pl.cm + ' cm';
      if (st.actief !== pl.id) {{ st.actief = pl.id; st.kant = pos(pl.id).kant; document.querySelectorAll('.pk-rij').forEach(function (r) {{ r.classList.toggle('is-actief', r.dataset.rij === pl.id); }}); }}
      teken(); }}
    else if (t.dataset.maat) overzicht();
  }});
  form.addEventListener('click', function (e) {{
    var b = e.target.closest('[data-plek]'), w = e.target.closest('[data-weg]');
    if (b) wissel(b.dataset.plek);
    else if (w) wissel(w.dataset.weg);
  }});
  document.querySelectorAll('[data-kant]').forEach(function (b) {{ b.addEventListener('click', function () {{ st.kant = b.dataset.kant; teken(); }}); }});
  $('ss-zoom').addEventListener('click', function () {{ st.zoom = !st.zoom; if (st.zoom && st.actief) st.kant = pos(st.actief).kant; teken(); }});

  // ---------- logo laden (ook PDF) ----------
  function melding(t) {{ $('ss-logohint').textContent = t; }}
  function nietTonen(file) {{ melding('Dit bestand (' + file.name + ') kunnen we niet in het voorbeeld tonen, maar we nemen het wel mee in uw aanvraag. Tip: upload ook een PNG of JPG voor het voorbeeld.'); teken(); }}
  function laadLogo(file) {{
    st.logo = null; st.logoNaam = file ? file.name : null;
    if (!file) {{ teken(); return; }}
    if (file.type === 'application/pdf' || /\\.(pdf|ai)$/i.test(file.name)) {{
      melding('Logo wordt geladen…');
      pdfNaarAfbeelding(file).then(function (url) {{ st.logo = url; melding('Logo geladen: ' + file.name + '. Klik hieronder aan waar het moet komen.'); teken(); }}).catch(function () {{ nietTonen(file); }});
      return;
    }}
    if (!/^image\\/(png|jpeg|svg\\+xml|webp|gif)$/.test(file.type)) {{ nietTonen(file); return; }}
    var r = new FileReader();
    r.onload = function () {{ st.logo = r.result; melding('Logo geladen: ' + file.name + '. Klik hieronder aan waar het moet komen.'); teken(); }};
    r.readAsDataURL(file);
  }}
  var PDFJS = 'js/';
  function laadPdfJs() {{
    if (window.pdfjsLib) return Promise.resolve(window.pdfjsLib);
    return new Promise(function (ok, fout) {{
      var sc = document.createElement('script'); sc.src = PDFJS + 'pdf.min.js';
      sc.onload = function () {{ window.pdfjsLib.GlobalWorkerOptions.workerSrc = PDFJS + 'pdf.worker.min.js'; ok(window.pdfjsLib); }};
      sc.onerror = fout; document.head.appendChild(sc);
    }});
  }}
  function pdfNaarAfbeelding(file) {{
    return Promise.all([laadPdfJs(), file.arrayBuffer()]).then(function (r) {{ return r[0].getDocument({{ data: new Uint8Array(r[1]) }}).promise; }})
      .then(function (pdf) {{ return pdf.getPage(1); }}).then(function (page) {{
        var v0 = page.getViewport({{ scale: 1 }}), schaal = Math.min(4, 1400 / Math.max(v0.width, v0.height));
        var vp = page.getViewport({{ scale: schaal }}), c = document.createElement('canvas');
        c.width = Math.ceil(vp.width); c.height = Math.ceil(vp.height);
        var ctx = c.getContext('2d', {{ willReadFrequently: true }});
        return page.render({{ canvasContext: ctx, viewport: vp, background: 'rgba(0,0,0,0)' }}).promise.then(function () {{ return bijsnijden(c, ctx); }});
      }});
  }}
  function bijsnijden(c, ctx) {{
    var W = c.width, H = c.height, img = ctx.getImageData(0, 0, W, H), d = img.data;
    var tel = {{}}, best = -1, bestN = 0, n = 0, r0 = Math.min(4, Math.floor(Math.min(W, H) / 10));
    function rand(x, y) {{ var i = (y * W + x) * 4; n++; if (d[i + 3] < 200) return; var k = (d[i] >> 4) + ',' + (d[i + 1] >> 4) + ',' + (d[i + 2] >> 4); tel[k] = (tel[k] || 0) + 1; if (tel[k] > bestN) {{ bestN = tel[k]; best = i; }} }}
    for (var x0 = r0; x0 < W - r0; x0 += 3) {{ rand(x0, r0); rand(x0, H - 1 - r0); }}
    for (var y0 = r0; y0 < H - r0; y0 += 3) {{ rand(r0, y0); rand(W - 1 - r0, y0); }}
    var ok = best >= 0 && bestN > n * 0.3, br = ok ? d[best] : -999, bg = ok ? d[best + 1] : -999, bb = ok ? d[best + 2] : -999;
    var minX = W, minY = H, maxX = -1, maxY = -1;
    for (var y = 0; y < H; y++) for (var x = 0; x < W; x++) {{
      var i = (y * W + x) * 4, diff = Math.abs(d[i] - br) + Math.abs(d[i + 1] - bg) + Math.abs(d[i + 2] - bb);
      if (d[i + 3] === 0 || diff < 40) d[i + 3] = 0;
      else {{ if (diff < 90) d[i + 3] = Math.round(d[i + 3] * (diff - 40) / 50); if (x < minX) minX = x; if (x > maxX) maxX = x; if (y < minY) minY = y; if (y > maxY) maxY = y; }}
    }}
    if (maxX < 0) throw new Error('leeg');
    ctx.putImageData(img, 0, 0);
    var u = document.createElement('canvas'), w = maxX - minX + 1, h = maxY - minY + 1;
    u.width = w; u.height = h; u.getContext('2d').drawImage(c, minX, minY, w, h, 0, 0, w, h);
    return u.toDataURL('image/png');
  }}

  form.addEventListener('submit', function (e) {{
    var fout = false, tot = overzicht();
    // een lege huidige samenstelling is goed als er al producten in de aanvraag staan
    if (tot && !st.plekken.length) {{ $('pk-fout').hidden = false; fout = true; }}
    if (!tot && !st.mand.length) {{ $('ss-fout').hidden = false; if (!st.plekken.length) $('pk-fout').hidden = false; fout = true; }}
    if (fout) {{ e.preventDefault(); e.stopImmediatePropagation(); (st.plekken.length ? $('ss-maten') : $('pk-figuren')).scrollIntoView({{ block: 'center' }}); return; }}
    try {{ localStorage.removeItem(OPSLAG); }} catch (x) {{}}
  }});

  var q = new URLSearchParams(location.search);
  var start = VAN[q.get('product')] || q.get('product') || 'polo';
  st.kleur = q.get('kleur') || (FOTOS[start] ? Object.keys(FOTOS[start])[0] : null);
  kiesProduct(start);
}})();
</script>"""
