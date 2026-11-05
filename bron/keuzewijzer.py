"""Borduren & bedrukken V2: keuzewijzer, voorbeelden en techniek per product."""
from home import weergave

VRAGEN = [
    ("kleding", "Op welke kleding komt het logo?", [
        ("B", "Polo, overhemd, jas of fleece"), ("B", "Cap of handdoek"),
        ("D", "T-shirt of sportshirt"), ("D", "Veiligheidshesje"), ("", "Weet ik nog niet")]),
    ("grootte", "Hoe groot wordt het logo?", [
        ("B", "Klein, op borst of mouw"), ("D", "Groot, op de rug of voorkant"), ("", "Weet ik nog niet")]),
    ("logo", "Hoe ziet uw logo eruit?", [
        ("B", "Strak, met een paar kleuren"), ("D", "Veel kleuren, kleurverloop of een foto"), ("D", "Hele fijne details of kleine tekst"), ("", "Weet ik nog niet")]),
]


def keuzewijzer():
    vragen = "".join(f'''<fieldset class="kw-vraag">
        <legend><span class="ss-nr">{i}</span> {vraag}</legend>
        <div class="keuzes">{"".join(f'<label class="keuze"><input type="radio" name="kw-{sleutel}" value="{waarde}"> {tekst}</label>' for waarde, tekst in opties)}</div>
      </fieldset>''' for i, (sleutel, vraag, opties) in enumerate(VRAGEN, 1))
    return f'''<section class="section section--wit section--compact" id="keuzewijzer" aria-labelledby="kw-kop">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Keuzewijzer</span><h2 id="kw-kop">Borduren of bedrukken? Drie vragen</h2>
      <p class="intro">Beantwoord drie korte vragen en zie welke techniek het beste bij u past. Twijfelt u daarna nog, dan adviseren we u graag.</p></div>
    <div class="kw">
      <div class="kw__vragen">{vragen}</div>
      <div class="kw__advies" id="kw-advies" aria-live="polite">
        <span class="kw__label">Ons advies</span>
        <strong id="kw-titel">Beantwoord de vragen</strong>
        <p id="kw-tekst">Na uw eerste antwoord ziet u hier ons advies.</p>
        <div class="knoppen"><a class="knop knop--hoofd knop--klein" href="samenstellen.html">Stel uw kleding samen</a><a class="meer" href="offerte.html">Advies aanvragen →</a></div>
      </div>
    </div>
  </div>
</section>
<script>
(function () {{
  var vragen = document.querySelectorAll('.kw-vraag');
  var titel = document.getElementById('kw-titel'), tekst = document.getElementById('kw-tekst'), vak = document.getElementById('kw-advies');
  var uitleg = {{
    B: ['Borduren', 'Borduren past goed: een luxe uitstraling met reliëf, en het blijft lang mooi. Ideaal voor kleine logo\\'s op polo\\'s, jassen en caps.'],
    D: ['Bedrukken', 'Bedrukken past goed: ook grote ontwerpen, veel kleuren en fijne details zijn mogelijk, en het is voordelig bij grotere aantallen.'],
    BD: ['Allebei mogelijk', 'Uw keuzes passen bij beide technieken. We kijken graag samen naar uw logo en adviseren wat het mooiste resultaat geeft.']
  }};
  function bereken() {{
    var b = 0, d = 0, n = 0;
    vragen.forEach(function (v) {{ var c = v.querySelector('input:checked'); if (!c) return; n++; if (c.value === 'B') b++; if (c.value === 'D') d++; }});
    if (!n) return;
    var k = b > d ? 'B' : d > b ? 'D' : 'BD';
    titel.textContent = uitleg[k][0]; tekst.textContent = uitleg[k][1];
    vak.className = 'kw__advies is-' + k.toLowerCase();
  }}
  document.querySelector('.kw__vragen').addEventListener('change', bereken);
}})();
</script>'''


def voorbeelden():
    items = [
        ("Borduren", "Garen met reliëf", "Polo, borst links",
         weergave("polo", "#1F2C44", 68, 41, 6.6, uitsnede="50 24 34 34", label="Geborduurd logo op een marineblauwe polo")),
        ("Bedrukken", "Glad en plat", "T-shirt, borst links", 
         weergave("tshirt", "#1F2C44", 68, 41, 6.6, uitsnede="50 24 34 34", techniek="Bedrukken", label="Bedrukt logo op een marineblauw T-shirt")),
        ("Borduren", "Klein op de cap", "Cap, voorkant",
         weergave("cap", "#5E1424", 47, 58, 7.2, uitsnede="20 26 80 80", label="Geborduurd logo op een bordeaux pet")),
        ("Bedrukken", "Groot op de rug", "Hoodie, rug",
         weergave("hoodie", "#3B3E44", 60, 56, 20, kant="achter", uitsnede="14 4 92 92", techniek="Bedrukken", label="Bedrukt logo op de rug van een hoodie")),
    ]
    html = "".join(f'''<figure class="vb">
        <div class="vb__beeld">{svg}</div>
        <figcaption><span class="tag">{tech}</span><strong>{titel}</strong><span>{sub}</span></figcaption>
      </figure>''' for tech, titel, sub, svg in items)
    return f'''<section class="section section--compact" aria-labelledby="bbvb-kop">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Voorbeelden</span><h2 id="bbvb-kop">Hetzelfde logo, twee technieken</h2>
      <p class="intro">Borduren geeft reliëf en een chique uitstraling. Bedrukken is glad en strak, en geschikt voor grote ontwerpen.</p></div>
    <div class="voorbeelden">{html}</div>
    <p class="hint vb__noot">Voorbeeldweergaven met het Bordoo-logo.</p>
  </div>
</section>'''


def per_product(P, kleding):
    groepen = [("B", "Meestal geborduurd"), ("D", "Meestal bedrukt"), ("BD", "Allebei goed")]
    gezien, kolommen = set(), []
    for code, titel in groepen:
        items = []
        for pk, (naam, tekening, _, tech) in P.items():
            if tech == code and naam not in gezien:
                gezien.add(naam)
                items.append(f'<li>{kleding(tekening, "pp-img")}<span>{naam}</span></li>')
        kolommen.append(f'<div class="pp-groep"><h3>{titel}</h3><ul>{"".join(items)}</ul></div>')
    return f'''<section class="section section--compact" aria-labelledby="pp-kop">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Per product</span><h2 id="pp-kop">Welke techniek bij welke kleding?</h2>
      <p class="intro">Dit is wat we meestal adviseren. Uw logo en wensen bepalen uiteindelijk de beste keuze.</p></div>
    <div class="pp">{"".join(kolommen)}</div>
  </div>
</section>'''
