/* Bordoo – controle-overzicht vóór het versturen van een aanvraag (samensteller en offerteformulier). */
(function () {
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function waarde(f, n) { var el = f.querySelector('[name="' + n + '"]'); return el ? String(el.value || '').trim() : ''; }
  function gekozen(f, n) { var el = f.querySelector('[name="' + n + '"]:checked'); return el ? el.value : ''; }
  function bestand(f, n) { var el = f.querySelector('[name="' + n + '"]'); return el && el.files && el.files[0] ? el.files[0] : null; }
  function rij(label, w) { return w ? '<div><dt>' + label + '</dt><dd>' + esc(w) + '</dd></div>' : ''; }
  var oudeUrls = [];

  function product(beelden, titel, rijen) {
    return '<li class="controle__product"><div class="controle__beelden">' + (beelden || '<div class="controle__geenbeeld" aria-hidden="true">?</div>') + '</div>' +
      '<div class="controle__tekst"><strong>' + esc(titel) + '</strong><dl class="controle__lijst">' + rijen + '</dl></div></li>';
  }

  // logo's: voorbeeld als het een afbeelding is, anders alleen de bestandsnaam
  function logoblok(f, voorbeeld) {
    oudeUrls.forEach(function (u) { URL.revokeObjectURL(u); }); oudeUrls = [];
    var delen = [['logo', 'Logo'], ['logo_2', 'Tweede logo']].map(function (x) {
      var b = bestand(f, x[0]); if (!b) return '';
      var src = x[0] === 'logo' && voorbeeld ? voorbeeld : (/^image\/(png|jpeg|svg\+xml|webp|gif)$/.test(b.type) ? URL.createObjectURL(b) : '');
      if (src && src.indexOf('blob:') === 0) oudeUrls.push(src);
      return '<figure class="controle__logo">' + (src ? '<img src="' + src + '" alt="">' : '<span class="controle__bestand" aria-hidden="true">' + esc((b.name.split('.').pop() || '').toUpperCase()) + '</span>') +
        '<figcaption><strong>' + x[1] + '</strong>' + esc(b.name) + '</figcaption></figure>';
    }).join('');
    return '<section class="controle__blok"><h3>Uw logo</h3>' + (delen ? '<div class="controle__logos">' + delen + '</div>' : '<p class="hint">Geen logo meegestuurd. U kunt het later ook mailen naar info@bordoo.nl.</p>') + '</section>';
  }

  function gegevens(f) {
    var b = waarde(f, 'bericht');
    return '<section class="controle__blok"><h3>Uw gegevens</h3><dl class="controle__lijst">' +
      rij('Naam', waarde(f, 'naam')) + rij('Bedrijf', waarde(f, 'bedrijf')) + rij('E-mail', waarde(f, 'email')) + rij('Telefoon', waarde(f, 'telefoon')) + '</dl></section>' +
      (b ? '<section class="controle__blok"><h3>Opmerking</h3><p class="controle__bericht">' + esc(b) + '</p></section>' : '');
  }

  function kop(aantal, stuks) {
    return '<h3>Uw kleding <span>' + aantal + (aantal === 1 ? ' product' : ' producten') + (stuks ? ', ' + stuks + ' stuks in totaal' : '') + '</span></h3>';
  }

  // offerteformulier: alles uit het formulier zelf halen
  function offerte(f) {
    var items = [], stuks = 0;
    f.querySelectorAll('.regel').forEach(function (r) {
      var sel = r.querySelector('select'), a = r.querySelector('input[type=number]').value, m = r.querySelector('input[type=text]').value.trim();
      if (!sel.value && !a) return;
      var opt = sel.options[sel.selectedIndex], beeld = opt && opt.getAttribute('data-beeld');
      stuks += parseInt(a, 10) || 0;
      items.push(product(beeld ? '<figure><img src="' + beeld + '" alt=""></figure>' : '', sel.value ? opt.text : 'Product nog niet gekozen',
        rij('Aantal', a ? a + ' stuks' : 'nog niet ingevuld') + rij('Maten', m)));
    });
    var datum = waarde(f, 'datum'), br = f.querySelector('[name=branche]');
    return '<section class="controle__blok">' + kop(items.length, stuks) +
      (items.length ? '<ol class="controle__producten">' + items.join('') + '</ol>' : '<p class="hint">Geen product gekozen. Geen probleem: beschrijf in de toelichting wat u zoekt.</p>') +
      '<dl class="controle__lijst">' + rij('Techniek', gekozen(f, 'dienst')) + rij('Branche', br && br.value ? br.options[br.selectedIndex].text : '') +
      rij('Nodig op', datum ? datum.split('-').reverse().join('-') : '') + '</dl></section>' + logoblok(f) + gegevens(f);
  }

  var dlg = null;
  function maak() {
    dlg = document.createElement('dialog');
    dlg.className = 'controle'; dlg.setAttribute('aria-labelledby', 'controle-kop');
    dlg.innerHTML = '<div class="controle__top"><div><span class="eyebrow">Laatste stap</span><h2 id="controle-kop">Controleer uw aanvraag</h2>' +
      '<p class="hint">Klopt alles? Dan versturen we uw aanvraag. Dit is nog geen bestelling: u ontvangt eerst een vrijblijvende offerte met een voorbeeld.</p></div>' +
      '<button type="button" class="controle__sluit" data-terug aria-label="Sluiten">×</button></div>' +
      '<div class="controle__inhoud"></div>' +
      '<div class="controle__knoppen"><button type="button" class="knop knop--rand" data-terug>Aanpassen</button><button type="button" class="knop knop--hoofd" data-ok>Klopt, verstuur aanvraag</button></div>';
    document.body.appendChild(dlg);
    dlg.addEventListener('click', function (e) {
      if (e.target.closest('[data-terug]') || e.target === dlg) dlg.close();
      else if (e.target.closest('[data-ok]')) { var f = dlg._form; dlg.close(); f._bevestigd = true; f.requestSubmit ? f.requestSubmit() : f.submit(); }
    });
  }
  function open(f, html) {
    if (typeof HTMLDialogElement !== 'function') { f._bevestigd = true; f.requestSubmit(); return; }
    if (!dlg) maak();
    dlg._form = f;
    var inhoud = dlg.querySelector('.controle__inhoud'); inhoud.innerHTML = html; inhoud.scrollTop = 0;
    dlg.showModal(); dlg.querySelector('[data-ok]').focus();
  }
  // true = doorgaan met versturen; false = eerst het overzicht tonen
  function akkoord(e, f, html) {
    if (f._bevestigd) { f._bevestigd = false; return true; }
    e.preventDefault(); e.stopImmediatePropagation(); open(f, typeof html === 'function' ? html() : html); return false;
  }
  window.BordooControle = { esc: esc, rij: rij, product: product, kop: kop, logoblok: logoblok, gegevens: gegevens, offerte: offerte, akkoord: akkoord };
})();
