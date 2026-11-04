"""Samensteller-pagina en nieuwe homepage."""
import json
from config_garments import data, VAN_PRODUCT, PRODUCTEN, KLEUREN


def naadkleur(hexkleur):
    h = hexkleur.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "rgba(0,0,0,.35)" if (0.299 * r + 0.587 * g + 0.114 * b) > 150 else "rgba(255,255,255,.35)"


_TEL = 0


def mini(pid, kleur=None):
    prod = next(p for p in PRODUCTEN if p[0] == pid)
    hexk = KLEUREN[kleur or prod[4][0]][1]
    global _TEL
    _TEL += 1
    return (f'<svg viewBox="0 0 120 120" aria-hidden="true" style="--stof:{hexk};--naad:{naadkleur(hexk)}">{prod[2].replace("rl-", f"rls{_TEL}-")}</svg>')


def samensteller_body(tel, mail):
    D = data()
    knoppen = "".join(
        f'<label class="ss-product"><input type="radio" name="product" value="{p[0]}"{" checked" if p[0] == "polo" else ""}>{mini(p[0])}<span>{p[1]}</span></label>'
        for p in PRODUCTEN)
    return f"""<section class="kopstrook">
  <div class="wrap">
    <span class="eyebrow">Zelf samenstellen</span>
    <h1>Stel uw kleding samen</h1>
    <p class="intro">Kies een product, kleur en maten en upload uw logo. U ziet meteen hoe het eruitziet en vraagt met één klik een vrijblijvende offerte aan.</p>
  </div>
</section>

<section class="section section--compact">
  <div class="wrap samensteller">
    <div class="ss-voorbeeld">
      <div class="ss-buhne">
        <svg id="ss-svg" viewBox="0 0 120 120" role="img" aria-label="Voorbeeld van uw kledingstuk met logo"></svg>
        <span class="ss-label" id="ss-label"></span>
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
      <input type="hidden" name="kleur" id="h-kleur"><input type="hidden" name="logo_plek" id="h-plek"><input type="hidden" name="logo_breedte_cm" id="h-cm">
      <input type="hidden" name="maten" id="h-maten"><input type="hidden" name="totaal" id="h-totaal">

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
          <input id="logo" name="logo" type="file" accept=".png,.jpg,.jpeg,.svg,.pdf,.ai,.eps">
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
        <div class="veld">
          <span class="veldlabel">Plek van het logo</span>
          <div class="keuzes" id="ss-posities"></div>
        </div>
        <div class="veld">
          <label for="ss-cm">Breedte van het logo: <strong id="ss-cmtekst"></strong></label>
          <input type="range" id="ss-cm" min="5" max="30" step="1" value="9">
        </div>
      </fieldset>

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">4</span> Maten en aantallen</legend>
        <div class="ss-maten" id="ss-maten"></div>
        <p class="ss-totaal">Totaal: <strong id="ss-totaal">0</strong> stuks</p>
        <p class="ss-fout" id="ss-fout" hidden>Vul bij minstens één maat een aantal in.</p>
      </fieldset>

      <fieldset class="ss-stap">
        <legend><span class="ss-nr">5</span> Uw gegevens</legend>
        <div class="veld--rij">
          <div class="veld"><label for="s-naam">Naam *</label><input id="s-naam" name="naam" type="text" autocomplete="name" required></div>
          <div class="veld"><label for="s-bedrijf">Bedrijf of vereniging</label><input id="s-bedrijf" name="bedrijf" type="text" autocomplete="organization"></div>
        </div>
        <div class="veld--rij">
          <div class="veld"><label for="s-email">E-mail *</label><input id="s-email" name="email" type="email" autocomplete="email" required></div>
          <div class="veld"><label for="s-tel">Telefoon</label><input id="s-tel" name="telefoon" type="tel" autocomplete="tel"></div>
        </div>
        <div class="veld"><label for="s-bericht">Opmerking</label><textarea id="s-bericht" name="bericht" placeholder="Bijv. een tweede logo op de rug, of wanneer u het nodig heeft"></textarea></div>
      </fieldset>

      <div class="ss-samenvatting">
        <h3>Uw samenstelling</h3>
        <dl id="ss-overzicht"></dl>
        <label class="akkoord"><input type="checkbox" id="s-akkoord" name="akkoord" required> <span>Ik ga akkoord dat Bordoo mijn gegevens gebruikt om deze aanvraag te beantwoorden. *</span></label>
        <button class="knop knop--hoofd" type="submit">Vraag offerte aan</button>
        <p class="hint">Vrijblijvend. U hoort meestal binnen twee werkdagen van ons. Vragen? Mail <a href="mailto:{mail}">{mail}</a>.</p>
      </div>
    </form>
  </div>
</section>

<script>
(function () {{
  var D = {json.dumps(data(), ensure_ascii=False)};
  var VAN = {json.dumps(VAN_PRODUCT)};
  var MATEN = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL'];
  var CM_PER_EENHEID = 1.4;
  var $ = function (id) {{ return document.getElementById(id); }};
  var form = $('ss-form'), svg = $('ss-svg');
  var st = {{ p: null, kleur: null, pos: null, cm: 9, kant: 'voor', zoom: false, logo: null, aantallen: {{}} }};

  function naad(hex) {{ var r = parseInt(hex.substr(1, 2), 16), g = parseInt(hex.substr(3, 2), 16), b = parseInt(hex.substr(5, 2), 16);
    return (0.299 * r + 0.587 * g + 0.114 * b) > 150 ? 'rgba(0,0,0,.35)' : 'rgba(255,255,255,.35)'; }}
  function licht(hex) {{ return naad(hex).indexOf('0,0,0') > -1; }}
  function techniek() {{ var t = form.querySelector('input[name=techniek]:checked'); return t ? t.value : 'Borduren'; }}

  function kiesProduct(id) {{
    st.p = D.producten.find(function (p) {{ return p.id === id; }}) || D.producten[1];
    form.querySelector('input[name=product][value="' + st.p.id + '"]').checked = true;
    if (st.p.kleuren.indexOf(st.kleur) < 0) st.kleur = st.p.kleuren[0];
    $('ss-kleuren').innerHTML = st.p.kleuren.map(function (k) {{
      var c = D.kleuren[k];
      return '<label class="ss-kleur" title="' + c.naam + '"><input type="radio" name="kleurkeuze" value="' + k + '"' + (k === st.kleur ? ' checked' : '') + '><span style="background:' + c.hex + '"></span><em>' + c.naam + '</em></label>';
    }}).join('');
    var oudePos = st.pos && st.pos.id;
    st.pos = st.p.posities.find(function (q) {{ return q.id === oudePos; }}) || st.p.posities[0];
    $('ss-posities').innerHTML = st.p.posities.map(function (q) {{
      return '<label class="keuze"><input type="radio" name="plekkeuze" value="' + q.id + '"' + (q.id === st.pos.id ? ' checked' : '') + '> ' + q.naam + '</label>';
    }}).join('');
    zetPositie(st.pos.id, oudePos === st.pos.id);
    var lijst = st.p.maten === 'kleding' ? MATEN : ['Aantal'];
    $('ss-maten').innerHTML = lijst.map(function (m) {{
      var id = 'maat-' + m;
      return '<div class="ss-maat"><label for="' + id + '">' + m + '</label><input id="' + id + '" type="number" min="0" step="1" inputmode="numeric" value="' + (st.aantallen[m] || 0) + '" data-maat="' + m + '"></div>';
    }}).join('');
    document.querySelector('[data-kant=achter]').disabled = !st.p.achter;
    teken();
  }}

  function zetPositie(id, houdMaat) {{
    st.pos = st.p.posities.find(function (q) {{ return q.id === id; }});
    var r = $('ss-cm'); r.min = st.pos.min; r.max = st.pos.max;
    if (!houdMaat || st.cm < st.pos.min || st.cm > st.pos.max) st.cm = st.pos.std;
    r.value = st.cm; st.kant = st.pos.kant;
  }}

  function teken() {{
    var hex = D.kleuren[st.kleur].hex;
    svg.style.setProperty('--stof', hex); svg.style.setProperty('--naad', naad(hex));
    var kant = st.kant === 'achter' && st.p.achter ? 'achter' : 'voor';
    var html = '<defs><filter id="borduur" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0.1" dy="0.15" stdDeviation="0.1" flood-opacity=".55"/></filter></defs>';
    html += (kant === 'voor' ? st.p.voor : st.p.achter).replace(/rl-/g, 'rlm-');
    var w = st.cm / CM_PER_EENHEID, x = st.pos.x, y = st.pos.y;
    if (st.pos.kant === kant) {{
      var f = techniek() === 'Borduren' ? ' filter="url(#borduur)"' : '';
      if (st.logo) {{
        html += '<image href="' + st.logo + '" x="' + (x - w / 2) + '" y="' + (y - w / 2) + '" width="' + w + '" height="' + w + '" preserveAspectRatio="xMidYMid meet"' + f + '/>';
      }} else {{
        var ink = licht(hex) ? '#5E1424' : '#FFFFFF', h = w * 0.5;
        html += '<g' + f + '><rect x="' + (x - w / 2) + '" y="' + (y - h / 2) + '" width="' + w + '" height="' + h + '" rx="' + (w * 0.06) + '" fill="none" stroke="' + ink + '" stroke-width="' + (w * 0.03) + '" stroke-dasharray="' + (w * 0.06) + ' ' + (w * 0.05) + '"/>' +
          '<text x="' + x + '" y="' + (y + h * 0.13) + '" text-anchor="middle" font-family="Archivo, Arial, sans-serif" font-weight="800" font-size="' + (w * 0.17) + '" fill="' + ink + '">UW LOGO</text></g>';
      }}
    }}
    svg.innerHTML = html;
    var z = st.zoom && st.pos.kant === kant;
    var v = Math.max(w * 3.2, 42);
    svg.setAttribute('viewBox', z ? (x - v / 2) + ' ' + (y - v / 2) + ' ' + v + ' ' + v : '0 0 120 120');
    document.querySelectorAll('[data-kant]').forEach(function (b) {{ b.setAttribute('aria-pressed', b.dataset.kant === kant); }});
    $('ss-zoom').setAttribute('aria-pressed', st.zoom); $('ss-zoom').textContent = st.zoom ? 'Hele kledingstuk' : 'Inzoomen op logo';
    $('ss-cmtekst').textContent = st.cm + ' cm';
    $('ss-kleurnaam').textContent = D.kleuren[st.kleur].naam;
    $('ss-label').textContent = st.p.naam + ' · ' + D.kleuren[st.kleur].naam + ' · ' + (kant === 'voor' ? 'voorkant' : 'achterkant');
    overzicht();
  }}

  function overzicht() {{
    var tot = 0, delen = [];
    document.querySelectorAll('[data-maat]').forEach(function (i) {{ var n = Math.max(0, parseInt(i.value, 10) || 0); st.aantallen[i.dataset.maat] = n; if (n) {{ tot += n; delen.push(i.dataset.maat + ': ' + n); }} }});
    $('ss-totaal').textContent = tot;
    var rijen = [['Product', st.p.naam], ['Kleur', D.kleuren[st.kleur].naam], ['Logo', techniek() + ', ' + st.pos.naam.toLowerCase() + ', ' + st.cm + ' cm breed'],
                 ['Logobestand', st.logoNaam || 'nog niet geüpload'], ['Aantal', tot ? tot + ' stuks' + (delen.length && st.p.maten === 'kleding' ? ' (' + delen.join(', ') + ')' : '') : 'nog in te vullen']];
    $('ss-overzicht').innerHTML = rijen.map(function (r) {{ return '<div><dt>' + r[0] + '</dt><dd>' + r[1] + '</dd></div>'; }}).join('');
    $('h-kleur').value = D.kleuren[st.kleur].naam; $('h-plek').value = st.pos.naam; $('h-cm').value = st.cm;
    $('h-maten').value = delen.join(', '); $('h-totaal').value = tot;
    if (tot) $('ss-fout').hidden = true;
    return tot;
  }}

  form.addEventListener('change', function (e) {{
    var t = e.target;
    if (t.name === 'product') kiesProduct(t.value);
    else if (t.name === 'kleurkeuze') {{ st.kleur = t.value; teken(); }}
    else if (t.name === 'plekkeuze') {{ zetPositie(t.value, false); teken(); }}
    else if (t.name === 'techniek') teken();
    else if (t.id === 'logo') laadLogo(t.files[0]);
  }});
  form.addEventListener('input', function (e) {{
    if (e.target.id === 'ss-cm') {{ st.cm = +e.target.value; teken(); }}
    else if (e.target.dataset.maat) overzicht();
  }});
  document.querySelectorAll('[data-kant]').forEach(function (b) {{ b.addEventListener('click', function () {{ st.kant = b.dataset.kant; teken(); }}); }});
  $('ss-zoom').addEventListener('click', function () {{ st.zoom = !st.zoom; if (st.zoom) st.kant = st.pos.kant; teken(); }});

  function laadLogo(file) {{
    st.logo = null; st.logoNaam = file ? file.name : null;
    var hint = $('ss-logohint');
    if (!file) {{ teken(); return; }}
    var isPdf = file.type === 'application/pdf' || /\\.(pdf|ai)$/i.test(file.name);
    if (isPdf) {{
      hint.textContent = 'Logo wordt geladen…';
      pdfNaarAfbeelding(file).then(function (url) {{
        st.logo = url; hint.textContent = 'Logo geladen: ' + file.name + '. Kies hieronder de plek en de grootte.'; teken();
      }}).catch(function () {{
        hint.textContent = 'Dit bestand (' + file.name + ') kunnen we niet in het voorbeeld tonen, maar we nemen het wel mee in uw aanvraag. Tip: upload ook een PNG of JPG voor het voorbeeld.';
        teken();
      }});
      return;
    }}
    if (!/^image\\/(png|jpeg|svg\\+xml|webp|gif)$/.test(file.type)) {{
      hint.textContent = 'Dit bestand (' + file.name + ') kunnen we niet in het voorbeeld tonen, maar we nemen het wel mee in uw aanvraag. Tip: upload ook een PNG of JPG voor het voorbeeld.';
      teken(); return;
    }}
    var r = new FileReader();
    r.onload = function () {{ st.logo = r.result; hint.textContent = 'Logo geladen: ' + file.name + '. Kies hieronder de plek en de grootte.'; teken(); }};
    r.readAsDataURL(file);
  }}

  // PDF (of AI): eerste pagina tekenen, achtergrondkleur doorzichtig maken en strak bijsnijden
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
    return Promise.all([laadPdfJs(), file.arrayBuffer()]).then(function (r) {{
      return r[0].getDocument({{ data: new Uint8Array(r[1]) }}).promise;
    }}).then(function (pdf) {{ return pdf.getPage(1); }}).then(function (page) {{
      var v0 = page.getViewport({{ scale: 1 }}), schaal = Math.min(4, 1400 / Math.max(v0.width, v0.height));
      var vp = page.getViewport({{ scale: schaal }}), c = document.createElement('canvas');
      c.width = Math.ceil(vp.width); c.height = Math.ceil(vp.height);
      var ctx = c.getContext('2d', {{ willReadFrequently: true }});
      return page.render({{ canvasContext: ctx, viewport: vp, background: 'rgba(0,0,0,0)' }}).promise.then(function () {{ return bijsnijden(c); }});
    }});
  }}
  function bijsnijden(c) {{
    var ctx = c.getContext('2d'), W = c.width, H = c.height, img = ctx.getImageData(0, 0, W, H), d = img.data;
    // achtergrondkleur = meest voorkomende kleur langs de rand
    var tel = {{}}, best = -1, bestN = 0, n = 0;
    function rand(x, y) {{ var i = (y * W + x) * 4; n++; if (d[i + 3] < 200) return; var k = (d[i] >> 4) + ',' + (d[i + 1] >> 4) + ',' + (d[i + 2] >> 4); tel[k] = (tel[k] || 0) + 1; if (tel[k] > bestN) {{ bestN = tel[k]; best = i; }} }}
    var r0 = Math.min(4, Math.floor(Math.min(W, H) / 10));
    for (var x0 = r0; x0 < W - r0; x0 += 3) {{ rand(x0, r0); rand(x0, H - 1 - r0); }}
    for (var y0 = r0; y0 < H - r0; y0 += 3) {{ rand(r0, y0); rand(W - 1 - r0, y0); }}
    var heeftAchtergrond = best >= 0 && bestN > n * 0.3;
    var br = heeftAchtergrond ? d[best] : -999, bg = heeftAchtergrond ? d[best + 1] : -999, bb = heeftAchtergrond ? d[best + 2] : -999, minX = W, minY = H, maxX = -1, maxY = -1;
    for (var y = 0; y < H; y++) for (var x = 0; x < W; x++) {{
      var i = (y * W + x) * 4, diff = Math.abs(d[i] - br) + Math.abs(d[i + 1] - bg) + Math.abs(d[i + 2] - bb);
      if (d[i + 3] === 0 || diff < 40) {{ d[i + 3] = 0; }}
      else {{ if (diff < 90) d[i + 3] = Math.round(d[i + 3] * (diff - 40) / 50); if (x < minX) minX = x; if (x > maxX) maxX = x; if (y < minY) minY = y; if (y > maxY) maxY = y; }}
    }}
    if (maxX < 0) throw new Error('leeg');
    ctx.putImageData(img, 0, 0);
    var u = document.createElement('canvas'), w = maxX - minX + 1, h = maxY - minY + 1;
    u.width = w; u.height = h; u.getContext('2d').drawImage(c, minX, minY, w, h, 0, 0, w, h);
    return u.toDataURL('image/png');
  }}

  form.addEventListener('submit', function (e) {{
    if (!overzicht()) {{ e.preventDefault(); e.stopImmediatePropagation(); $('ss-fout').hidden = false; $('ss-maten').scrollIntoView({{ block: 'center' }}); }}
  }});

  var q = new URLSearchParams(location.search);
  kiesProduct(VAN[q.get('product')] || q.get('product') || 'polo');
}})();
</script>"""


def home_body(branches, P, kleding, doorsnede, CTA):
    teaser_kleuren = ["bordeaux", "zwart", "marine", "wit", "flessengroen"]
    stippen = "".join(f'<span style="background:{KLEUREN[k][1]}"></span>' for k in teaser_kleuren)
    chips = "".join(
        f'<a class="branchechip" href="branche-{b[0]}.html">{kleding(b[5], "chipicoon")}<span><strong>{b[1]}</strong><small>{" · ".join(P[pk][0] for pk in b[6][:3])}</small></span></a>'
        for b in branches)
    return f"""<section class="intro-hero">
  <div class="wrap intro-hero__raster">
    <div class="intro-hero__tekst">
      <span class="eyebrow">Borduren · Bedrukken · Bedrijfskleding</span>
      <h1>Uw logo op kleding. Zelf samengesteld, netjes gemaakt.</h1>
      <p class="intro">Kies een kledingstuk, een kleur en de maten, upload uw logo en zie direct hoe het wordt. Wij borduren of bedrukken het voor u.</p>
      <div class="knoppen">
        <a class="knop knop--hoofd" href="samenstellen.html">Stel uw kleding samen</a>
        <a class="knop knop--rand" href="#branches">Kleding per branche</a>
      </div>
    </div>
    <a class="teaser" href="samenstellen.html" aria-label="Naar zelf samenstellen">
      <div class="teaser__beeld">{mini("polo", "bordeaux")}</div>
      <div class="teaser__info">
        <span class="teaser__titel">Polo · Bordeaux</span>
        <span class="teaser__stippen">{stippen}</span>
        <span class="teaser__link">Probeer het zelf →</span>
      </div>
    </a>
  </div>
</section>

<section class="usp">
  <div class="wrap usp__raster">
    <div><hr class="goudlijn"><strong>Borduren én bedrukken</strong><span>Alles onder één dak</span></div>
    <div><hr class="goudlijn"><strong>Ook kleine aantallen</strong><span>Vanaf één stuk voor particulieren</span></div>
    <div><hr class="goudlijn"><strong>Eerst een voorbeeld</strong><span>U ziet het resultaat voordat we maken</span></div>
    <div><hr class="goudlijn"><strong>Snel een prijs</strong><span>Meestal binnen twee werkdagen</span></div>
  </div>
</section>

<section class="section section--compact" id="branches">
  <div class="wrap">
    <div class="kop kop--rij">
      <div><span class="eyebrow">Kleding per branche</span><h2>In welke branche werkt u?</h2></div>
      <a class="meer" href="bedrijfskleding.html">Alle branches →</a>
    </div>
    <div class="branchechips">{chips}</div>
  </div>
</section>

<section class="section section--wit section--compact">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Zo werkt samenstellen</span><h2>In vier stappen naar uw offerte</h2></div>
    <ol class="stappen stappen--licht">
      <li><h3>Kies een product</h3><p>Polo, jas, schort, cap en meer.</p></li>
      <li><h3>Kleur en maten</h3><p>Kies de kleur en hoeveel stuks per maat.</p></li>
      <li><h3>Upload uw logo</h3><p>Kies de plek en grootte en zie het voorbeeld.</p></li>
      <li><h3>Ontvang uw offerte</h3><p>Vrijblijvend, met een proef voordat we maken.</p></li>
    </ol>
    <div class="knoppen" style="margin-top:28px"><a class="knop knop--hoofd" href="samenstellen.html">Begin met samenstellen</a></div>
  </div>
</section>

<section class="section section--compact">
  <div class="wrap duo">
    <div class="stack">
      <span class="eyebrow">Borduren of bedrukken</span>
      <h2>Wat is het verschil?</h2>
      <p class="intro">Borduren zit ín de stof: chique, met reliëf en het gaat jaren mee. Bedrukken ligt óp de stof: glad, kleurrijk en voordelig.</p>
      <div><a class="meer" href="borduren-bedrukken.html">Bekijk de uitleg met tekeningen →</a></div>
    </div>
    <div class="illustratiekader">{doorsnede}</div>
  </div>
</section>

{CTA}"""
