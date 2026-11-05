"""Bordoo-website v2: menu per branche met producten, pagina per branche, uitleg met tekeningen."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from garments import img as kleding, G, TSHIRT, logo as oo, LIJN, bestand_svg, bestand_svg_achter, heeft_achterkant, _STIJL, BESTANDEN_MAP
import config_garments as CG
from branches_v2 import aanbevolen, cta_branche
from home import home_body
from samensteller2 import samensteller_body
from config_garments import VAN_PRODUCT
from privacy import PRIVACY

OUT = pathlib.Path(sys.argv[1])
TODO = lambda t: f'<span class="invullen">{t}</span>'
TEL, MAIL = '<a href="tel:+31648399904">+31 6 48 39 99 04</a>', "info@bordoo.nl"

# key: (naam, tekening, beschrijving, technieken)  B = borduren, D = bedrukken
P = {
    "koksbuis": ("Koksbuizen", "koksbuis", "Wit of zwart, met uw logo geborduurd op de borst. Stevig en goed wasbaar.", "B"),
    "schort": ("Schorten & sloven", "schort", "Lange schorten, halterschorten en korte sloven voor keuken en bediening.", "BD"),
    "koksbroek": ("Koksbroeken", "koksbroek", "Comfortabele broeken voor de keuken, ook in pied-de-poule. Eventueel met klein logo.", "B"),
    "polo": ("Polo's", "polo", "Verzorgd en makkelijk. Logo op de borst, eventueel tekst op de rug.", "BD"),
    "cap": ("Petten & caps", "cap", "Een geborduurd logo op de voorkant valt altijd op.", "B"),
    "werkjas": ("Werkjassen", "werkjas", "Warme, sterke jassen voor buiten. Logo op de borst en groot op de rug.", "BD"),
    "hesje": ("Veiligheidshesjes", "hesje", "Goed zichtbaar op de bouwplaats. Opdruk op de rug, zonder de reflectiestrepen te bedekken.", "D"),
    "werkbroek": ("Werkbroeken", "werkbroek", "Met kniezakken en gereedschapszakken. Klein logo op de pijp of zak.", "BD"),
    "hoodie": ("Sweaters & hoodies", "hoodie", "Warm voor tussendoor. Logo op de borst, groot op de rug.", "BD"),
    "tshirt": ("T-shirts", "tshirt", "Voordelig in grote aantallen, ideaal voor de zomer en evenementen.", "BD"),
    "bodywarmer": ("Bodywarmers", "bodywarmer", "Warm zonder mouwen, zodat u vrij kunt bewegen in de werkplaats.", "BD"),
    "softshell": ("Softshell jassen", "softshell", "Licht, wind- en waterafstotend. Zakelijk genoeg voor bij de klant.", "BD"),
    "overall": ("Overalls", "overall", "Eén stuk dat alles beschermt. Logo op borst en rug.", "BD"),
    "fleece": ("Fleecevesten", "fleece", "Zacht en warm, met rits. Het logo wordt meestal geborduurd.", "B"),
    "tuniek": ("Tunieken", "tuniek", "Voor zorg, praktijk en salon. Fris, makkelijk te wassen.", "B"),
    "kapschort": ("Kappers- en salonschorten", "schort", "Beschermt tegen haar en producten, met uw salonnaam erop.", "BD"),
    "overhemd": ("Overhemden & blouses", "overhemd", "Representatief voor kantoor en winkel, met een klein geborduurd logo.", "B"),
    "trui": ("Truien & sweaters", "hoodie", "Zakelijk en warm, met logo op de borst.", "BD"),
    "sportshirt": ("Sportshirts", "tshirt", "Ademende shirts met clubnaam, rugnummer of sponsor.", "D"),
    "trainingsjas": ("Trainingsjassen", "fleece", "Voor de hele club in dezelfde stijl, met logo op de borst.", "BD"),
    "tas": ("Tassen", "tas", "Sporttassen en draagtassen met naam of logo.", "BD"),
    "handdoek": ("Handdoeken & badjassen", "handdoek", "Met een naam of tekst geborduurd. Mooi als cadeau.", "B"),
}

# key: (menunaam, titel, intro, tegeltekst, icoon, producten)
B = [
    ("horeca", "Horeca", "Horecakleding met uw logo", "Voor restaurants, cafés, hotels en catering. Van de keuken tot de bediening, iedereen herkenbaar.",
     "Keuken en bediening", "koksbuis", ["koksbuis", "schort", "koksbroek", "polo", "cap"]),
    ("bouw", "Bouw", "Bouwkleding met uw logo", "Voor aannemers, installateurs en schilders. Stevige kleding die tegen een stootje kan.",
     "Aannemers en installateurs", "werkjas", ["werkjas", "hesje", "werkbroek", "hoodie", "tshirt"]),
    ("garage", "Garage & techniek", "Garage- en technische kleding met uw logo", "Voor autobedrijven, monteurs en de technische dienst. Praktisch in de werkplaats, netjes bij de klant.",
     "Werkplaats en monteurs", "bodywarmer", ["bodywarmer", "softshell", "overall", "werkbroek", "polo"]),
    ("schoonmaak", "Schoonmaak", "Schoonmaakkleding met uw logo", "Voor schoonmaak- en facilitaire bedrijven. Uw medewerkers zijn bij de klant meteen herkenbaar.",
     "Schoonmaak en facilitair", "fleece", ["polo", "fleece", "werkbroek", "softshell"]),
    ("zorg", "Zorg & beauty", "Zorg- en salonkleding met uw logo", "Voor thuiszorg, praktijken, kappers en schoonheidssalons. Fris, verzorgd en makkelijk te wassen.",
     "Zorg, kapper en salon", "tuniek", ["tuniek", "kapschort", "polo", "fleece"]),
    ("transport", "Transport", "Transport- en logistieke kleding met uw logo", "Voor chauffeurs, koeriers en magazijnen. Warm, zichtbaar en herkenbaar onderweg.",
     "Chauffeurs en magazijn", "softshell", ["softshell", "bodywarmer", "hesje", "polo", "hoodie"]),
    ("kantoor", "Kantoor & winkel", "Kantoor- en winkelkleding met uw logo", "Voor kantoor, winkel en showroom. Representatief, met een klein en strak logo.",
     "Kantoor en winkel", "overhemd", ["overhemd", "polo", "trui", "bodywarmer"]),
    ("sport", "Sport & clubs", "Clubkleding met uw logo", "Voor sportclubs, verenigingen en teams. Iedereen in dezelfde stijl, met naam of rugnummer.",
     "Clubs en verenigingen", "tshirt", ["sportshirt", "trainingsjas", "hoodie", "tas", "cap"]),
    ("particulier", "Particulier", "Persoonlijke kleding en cadeaus", "Een naam, tekst of afbeelding op kleding of handdoeken. Ook voor één stuk, bijvoorbeeld als cadeau.",
     "Cadeau en persoonlijk", "handdoek", ["handdoek", "hoodie", "tshirt", "tas"]),
]
TECH = {"B": "Borduren", "D": "Bedrukken"}


def tags(t):
    return "".join(f'<span class="tag">{TECH[c]}</span>' for c in t)


def megamenu():
    items = []
    for k, menu, titel, intro, tegel, icon, prods in B:
        links = "".join(
            f'<li><a href="branche-{k}.html#{pk}">{kleding(P[pk][1], "mini")}<span>{P[pk][0]}</span></a></li>' for pk in prods)
        items.append(f'''<li class="drop">
        <a class="drop__kop" href="branche-{k}.html">{menu}</a>
        <div class="drop__paneel">
          <div class="drop__intro"><span class="eyebrow">{tegel}</span><p>{intro}</p><a class="meer" href="branche-{k}.html">Alles voor {menu.lower()} →</a></div>
          <ul class="drop__lijst">{links}</ul>
        </div>
      </li>''')
    return "\n".join(items)


def mobielmenu():
    out = []
    for k, menu, *_rest in B:
        prods = _rest[-1]
        out.append(f'<details><summary>{menu}</summary><ul>' +
                   "".join(f'<li><a href="branche-{k}.html#{pk}">{P[pk][0]}</a></li>' for pk in prods) +
                   f'<li><a class="meer" href="branche-{k}.html">Alles voor {menu.lower()} →</a></li></ul></details>')
    return "\n".join(out)


NAMEN = {"bedrijfskleding.html": "Alle branches", "borduren-bedrukken.html": "Borduren &amp; bedrukken", "samenstellen.html": "Zelf samenstellen",
         "offerte.html": "Offerte &amp; contact", "privacy.html": "Privacyverklaring", "bedankt.html": "Bedankt"}


def kruimelpad(fn, branche):
    """Kruimelpad onder de kop (niet op de homepage)."""
    if fn == "index.html":
        return ""
    stappen = [("index.html", "Home")]
    if branche:
        stappen += [("bedrijfskleding.html", "Alle branches"), (fn, next(b[1] for b in B if b[0] == branche))]
    else:
        stappen.append((fn, NAMEN.get(fn, "")))
    items = "".join(f'<li><a href="{f}">{n}</a></li>' for f, n in stappen[:-1]) + f'<li aria-current="page">{stappen[-1][1]}</li>'
    return f'<nav class="kruimel" aria-label="Kruimelpad"><ol class="wrap">{items}</ol></nav>\n'


def page(fn, title, desc, body, branche=None):
    def cur(f):
        return ' aria-current="page"' if f == fn else ""
    mm = megamenu().replace(f'href="branche-{branche}.html">', f'href="branche-{branche}.html" aria-current="page">', 1) if branche else megamenu()
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="img/icoon.png">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skiplink" href="#inhoud">Naar de inhoud</a>
<header class="header">
  <div class="wrap topbalk">
    <nav class="toplinks" aria-label="Informatie">
      <a href="samenstellen.html"{cur("samenstellen.html")}>Zelf samenstellen</a>
      <a href="borduren-bedrukken.html"{cur("borduren-bedrukken.html")}>Borduren &amp; bedrukken</a>
      <a href="bedrijfskleding.html"{cur("bedrijfskleding.html")}>Alle branches</a>
    </nav>
    <a class="logo" href="index.html" aria-label="Bordoo – naar de homepage"><img src="img/logo-tekst.svg" alt="Bordoo – borduur &amp; druk" width="170" height="70"></a>
    <div class="topacties">
      <a class="toptel" href="tel:+31648399904" aria-label="Bel Bordoo: +31 6 48 39 99 04"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.6a1 1 0 0 1-.25 1z"/></svg><span>+31 6 48 39 99 04</span></a>
      <a class="knop knop--hoofd knop--klein" href="offerte.html"{cur("offerte.html")}>Offerte aanvragen</a>
      <button class="menuknop" type="button" aria-expanded="false" aria-controls="mobielmenu">Menu</button>
    </div>
  </div>
  <nav class="branchebalk" aria-label="Kleding per branche">
    <ul class="wrap">
      {mm}
    </ul>
  </nav>
  <nav class="mobielmenu" id="mobielmenu" aria-label="Menu">
    <div class="wrap">
      <p class="eyebrow">Kleding per branche</p>
      {mobielmenu()}
      <a class="mobiel-link" href="samenstellen.html">Zelf samenstellen</a>
      <a class="mobiel-link" href="borduren-bedrukken.html">Borduren &amp; bedrukken</a>
      <a class="mobiel-link" href="bedrijfskleding.html">Alle branches</a>
      <a class="mobiel-link" href="offerte.html">Offerte &amp; contact</a>
      <a class="mobiel-link" href="tel:+31648399904">Bel ons: +31 6 48 39 99 04</a>
    </div>
  </nav>
</header>
<main id="inhoud">
{kruimelpad(fn, branche)}{body}
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__raster">
      <div class="stack">
        <img src="img/logo-negatief.svg" alt="Bordoo – borduur &amp; druk" width="120" height="49">
        <p>Bedrijfskleding met uw logo, geborduurd of bedrukt. Voor bedrijven, clubs en particulieren.</p>
      </div>
      <div>
        <h3>Branches</h3>
        <ul>{"".join(f'<li><a href="branche-{b[0]}.html">{b[1]}</a></li>' for b in B)}</ul>
      </div>
      <div>
        <h3>Diensten</h3>
        <ul>
          <li><a href="samenstellen.html">Zelf samenstellen</a></li>
          <li><a href="offerte.html">Offerte aanvragen</a></li>
          <li><a href="borduren-bedrukken.html">Borduren &amp; bedrukken</a></li>
          <li><a href="bedrijfskleding.html">Alle branches</a></li>
        </ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li>{TEL}</li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li><a href="offerte.html">Contactformulier</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__onder">
      <span>© 2026 Bordoo</span>
      <span><a href="privacy.html">Privacyverklaring</a> · bordoo.nl</span>
    </div>
  </div>
</footer>
<script>
  var k = document.querySelector('.menuknop'), m = document.getElementById('mobielmenu');
  k.addEventListener('click', function () {{ var o = m.classList.toggle('open'); k.setAttribute('aria-expanded', o); k.textContent = o ? 'Sluiten' : 'Menu'; }});
  document.addEventListener('keydown', function (e) {{
    if (e.key !== 'Escape') return;
    var d = document.activeElement && document.activeElement.closest('.drop');
    if (d) {{ d.querySelector('.drop__kop').focus(); d.classList.add('dicht'); }}
    if (m.classList.contains('open')) {{ m.classList.remove('open'); k.setAttribute('aria-expanded', false); k.textContent = 'Menu'; k.focus(); }}
  }});
  document.querySelectorAll('.drop').forEach(function (d) {{ d.addEventListener('mouseleave', function () {{ d.classList.remove('dicht'); }}); d.addEventListener('focusout', function (e) {{ if (!d.contains(e.relatedTarget)) d.classList.remove('dicht'); }}); }});
</script>
</body>
</html>
"""


def foto(label, licht=False):
    return f'<div class="foto{" foto--licht" if licht else ""}" role="img" aria-label="Plek voor foto: {label}"><span class="foto__label">Foto volgt: {label}</span></div>'


CTA = """<section class="cta">
  <div class="wrap">
    <div>
      <h2>Kleding met uw logo?</h2>
      <p>Vertel ons wat u zoekt. U krijgt vrijblijvend een prijs op maat.</p>
    </div>
    <a class="knop knop--hoofd" href="offerte.html">Vraag een offerte aan</a>
  </div>
</section>"""


def tegels():
    out = []
    for k, menu, titel, intro, tegel, icon, prods in B:
        lijst = " · ".join(P[pk][0] for pk in prods[:4])
        out.append(f'''<a class="tegel" href="branche-{k}.html">
      <div class="tegel__beeld">{kleding(icon)}</div>
      <div class="tegel__tekst"><h3>{menu}</h3><p>{lijst}</p></div>
    </a>''')
    return f'<div class="tegels">{"".join(out)}</div>'


# ---------- Illustraties borduren / bedrukken ----------
def doorsnede():
    def stof(x0):
        weef = "".join(f'<line x1="{x}" y1="132" x2="{x}" y2="150" stroke="rgba(0,0,0,.12)" stroke-width="1"/>' for x in range(x0 + 4, x0 + 236, 6))
        return f'<rect x="{x0}" y="132" width="240" height="18" rx="2" fill="#D9CFC4"/>{weef}'
    satijn = "".join(f'<line x1="{x}" y1="{132 - 0}" x2="{x + 10}" y2="104" stroke="rgba(255,255,255,.35)" stroke-width="1.2"/>' for x in range(76, 200, 7))
    return f'''<svg class="illustratie" viewBox="0 0 560 240" role="img" aria-label="Doorsnede: bij borduren zit het garen in de stof met reliëf, bij bedrukken ligt een dunne laag op de stof">
  <text x="20" y="28" class="ill-kop">Borduren</text>
  {stof(20)}
  <rect x="58" y="150" width="164" height="7" rx="2" fill="#EEEAE7" stroke="rgba(0,0,0,.12)"/>
  <path d="M70 132 C70 96 210 96 210 132 Z" fill="#5E1424"/>{satijn}
  <path d="M70 132 L70 152 M210 132 L210 152 M110 132 L110 150 M170 132 L170 150" stroke="#5E1424" stroke-width="2.4"/>
  <line x1="140" y1="100" x2="140" y2="58" class="ill-lijn"/><text x="140" y="50" text-anchor="middle" class="ill-tekst">Garen met voelbaar reliëf</text>
  <line x1="40" y1="141" x2="40" y2="196" class="ill-lijn"/><text x="20" y="212" class="ill-tekst">De stof</text>
  <line x1="200" y1="157" x2="200" y2="196" class="ill-lijn"/><text x="250" y="212" text-anchor="end" class="ill-tekst">Steunlaag binnenin</text>

  <text x="300" y="28" class="ill-kop">Bedrukken</text>
  {stof(300)}
  <rect x="350" y="125" width="140" height="7" rx="1.5" fill="#5E1424"/>
  <line x1="420" y1="124" x2="420" y2="58" class="ill-lijn"/><text x="420" y="50" text-anchor="middle" class="ill-tekst">Dunne laag op de stof</text>
  <line x1="320" y1="141" x2="320" y2="196" class="ill-lijn"/><text x="300" y="212" class="ill-tekst">De stof</text>
  <text x="540" y="212" text-anchor="end" class="ill-tekst">Glad en plat</text>
</svg>'''


def stapbeeld(soort):
    W = 'fill="#fff" stroke="rgba(0,0,0,.25)" stroke-width="1.4"'
    if soort == "digitaal":
        punten = "".join(f'<circle cx="{x}" cy="{y}" r="1.3" fill="#B88F52"/>' for x in range(36, 86, 6) for y in (40, 60))
        return f'<svg viewBox="0 0 120 100" aria-hidden="true"><rect x="20" y="16" width="80" height="54" rx="4" {W}/><path d="M50 82 L70 82 M60 70 L60 82" stroke="rgba(0,0,0,.3)" stroke-width="2"/>{oo(50, 43, "#5E1424", 3)}{punten}</svg>'
    if soort == "machine":
        return f'''<svg viewBox="0 0 120 100" aria-hidden="true"><circle cx="60" cy="66" r="26" fill="#F3F1EF" stroke="rgba(0,0,0,.3)" stroke-width="3"/>
        {oo(52, 66, "#5E1424", 2.2)}<path d="M60 8 L60 50" stroke="#5E1424" stroke-width="1.4" stroke-dasharray="3 3"/><path d="M58 10 L62 10 L61 48 L60 54 L59 48 Z" fill="#9C9596"/>
        <rect x="80" y="10" width="14" height="22" rx="3" fill="#5E1424"/><path d="M87 32 Q80 40 61 44" fill="none" stroke="#5E1424" stroke-width="1.2"/></svg>'''
    if soort == "ontwerp":
        return f'<svg viewBox="0 0 120 100" aria-hidden="true"><rect x="20" y="16" width="80" height="54" rx="4" {W}/><path d="M50 82 L70 82 M60 70 L60 82" stroke="rgba(0,0,0,.3)" stroke-width="2"/><rect x="34" y="28" width="18" height="18" fill="#5E1424"/><rect x="54" y="28" width="18" height="18" fill="#B88F52"/><rect x="74" y="28" width="12" height="18" fill="#1C1A1B"/><rect x="34" y="50" width="52" height="8" fill="#D9CFC4"/></svg>'
    if soort == "pers":
        return '''<svg viewBox="0 0 120 100" aria-hidden="true"><rect x="22" y="70" width="76" height="10" rx="2" fill="#2A2829"/><rect x="28" y="62" width="64" height="8" fill="#F3F1EF" stroke="rgba(0,0,0,.25)"/>
        <rect x="26" y="34" width="68" height="14" rx="3" fill="#9C9596"/><path d="M60 34 L60 16 L96 16" stroke="#2A2829" stroke-width="5" fill="none" stroke-linecap="round"/>
        <path d="M40 56 L40 50 M52 56 L52 50 M64 56 L64 50 M76 56 L76 50" stroke="#B88F52" stroke-width="2" stroke-linecap="round"/><rect x="44" y="64" width="32" height="4" fill="#5E1424"/></svg>'''
    if soort == "polo":
        return kleding("polo", "stapkleding")
    return kleding("tshirt", "stapkleding")


def plaatsing():
    def shirt(dx, achter):
        g = f'<g transform="translate({dx} 6) scale(2)"><path d="{TSHIRT}" fill="#fff" stroke="rgba(0,0,0,.3)" stroke-width="0.8" stroke-linejoin="round"/>'
        g += '<path d="M52 18 Q60 30 68 18" fill="none" stroke="rgba(0,0,0,.25)" stroke-width="0.8"/>' if not achter else '<path d="M52 18 Q60 22 68 18" fill="none" stroke="rgba(0,0,0,.25)" stroke-width="0.8"/>'
        return g + "</g>"
    zone = lambda x, y, w, h: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="rgba(94,20,36,.12)" stroke="#5E1424" stroke-width="1.4" stroke-dasharray="5 3"/>'
    lab = lambda x, y, t, s, a="start": f'<text x="{x}" y="{y}" text-anchor="{a}" class="ill-tekst"><tspan font-weight="600">{t}</tspan><tspan x="{x}" dy="16">{s}</tspan></text>'
    return f'''<svg class="illustratie" viewBox="0 0 560 270" role="img" aria-label="Gebruikelijke plekken voor een logo: borst 8 tot 10 cm, mouw 6 tot 8 cm, rug 25 tot 30 cm, nek 6 tot 8 cm">
  {shirt(10, False)}{shirt(290, True)}
  <text x="130" y="262" text-anchor="middle" class="ill-kop-klein">Voorkant</text><text x="410" y="262" text-anchor="middle" class="ill-kop-klein">Achterkant</text>
  {zone(140, 72, 24, 16)}{zone(64, 68, 16, 14)}
  {zone(372, 96, 76, 56)}{zone(398, 50, 24, 10)}
  <line x1="164" y1="80" x2="214" y2="80" class="ill-lijn"/>{lab(218, 76, "Borst", "8–10 cm")}
  <line x1="64" y1="75" x2="8" y2="120" class="ill-lijn"/>{lab(8, 136, "Mouw", "6–8 cm")}
  <line x1="448" y1="124" x2="500" y2="160" class="ill-lijn"/>{lab(470, 178, "Rug", "25–30 cm")}
  <line x1="422" y1="55" x2="476" y2="40" class="ill-lijn"/>{lab(480, 34, "Nek", "6–8 cm")}
</svg>'''


# ---------- Pagina's ----------
hero_beelden = "".join(f'<div class="herotegel">{kleding(n)}</div>' for n in ("koksbuis", "werkjas", "bodywarmer", "polo"))

home = f"""<section class="hero">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Bedrijfskleding met uw logo</span>
      <h1>Kleding voor uw vak, met uw logo erop.</h1>
      <p class="intro">Van koksbuis tot werkjas en van bodywarmer tot polo. Kies uw branche en zie meteen welke kleding er past. Wij borduren of bedrukken uw logo.</p>
      <div class="knoppen">
        <a class="knop knop--hoofd" href="#branches">Kies uw branche</a>
        <a class="knop knop--goud" href="offerte.html">Offerte aanvragen</a>
      </div>
    </div>
    <div class="herotegels" aria-hidden="true">{hero_beelden}</div>
  </div>
</section>

<section class="section" id="branches">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Kleding per branche</span>
      <h2>In welke branche werkt u?</h2>
      <p class="intro">Elke branche heeft eigen kleding nodig. Kies de uwe en bekijk wat er mogelijk is.</p>
    </div>
    {tegels()}
  </div>
</section>

<section class="section section--wit">
  <div class="wrap duo">
    <div class="stack">
      <span class="eyebrow">Borduren of bedrukken</span>
      <h2>Wat is het verschil?</h2>
      <p class="intro">Bij borduren zit het garen ín de stof: chique, met reliëf en het gaat jaren mee. Bij bedrukken ligt een dunne laag óp de stof: glad, kleurrijk en voordelig.</p>
      <div class="knoppen"><a class="knop knop--rand" href="borduren-bedrukken.html">Bekijk de uitleg</a></div>
    </div>
    <div class="illustratiekader">{doorsnede()}</div>
  </div>
</section>

<section class="section section--donker">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Zo werkt het</span>
      <h2>Van aanvraag tot levering</h2>
    </div>
    <ol class="stappen">
      <li><h3>Aanvraag</h3><p>U vult het offerteformulier in en stuurt uw logo mee.</p></li>
      <li><h3>Voorstel</h3><p>U krijgt een prijs en een voorbeeld van hoe het logo op de kleding komt.</p></li>
      <li><h3>Productie</h3><p>Na uw akkoord borduren of bedrukken wij de kleding.</p></li>
      <li><h3>Levering</h3><p>U haalt de kleding op of wij sturen het naar u toe.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Ons werk</span>
      <h2>Een greep uit ons werk</h2>
    </div>
    <div class="raster">
      {foto("geborduurd logo, close-up")}
      {foto("koksbuizen voor een restaurant", True)}
      {foto("werkjassen voor een bouwbedrijf")}
    </div>
  </div>
</section>

{CTA}"""

bb = f"""<section class="hero hero--klein">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Borduren &amp; bedrukken</span>
      <h1>Borduren of bedrukken: wat past bij u?</h1>
      <p class="intro">Allebei geven ze kleding met uw logo. Het verschil zit in hoe het logo op de stof komt. Hieronder ziet u het in beeld.</p>
    </div>
  </div>
</section>

<section class="section section--wit">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Het verschil</span>
      <h2>In de stof of op de stof</h2>
      <p class="intro">Bij borduren wordt garen dóór de stof gestikt, met een steunlaag aan de binnenkant. Bij bedrukken komt inkt of een transfer als dunne laag op de stof.</p>
    </div>
    <div class="illustratiekader illustratiekader--breed">{doorsnede()}</div>
  </div>
</section>

<section class="section" id="borduren">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Borduren</span>
      <h2>Zo wordt uw logo geborduurd</h2>
    </div>
    <ol class="processtappen">
      <li>{stapbeeld("digitaal")}<h3>Logo omzetten</h3><p>Uw logo wordt één keer omgezet naar een borduurpatroon: welke steek, welke kleur, in welke volgorde.</p></li>
      <li>{stapbeeld("machine")}<h3>De machine borduurt</h3><p>De stof wordt strak in een ring gespannen. De machine stikt het logo steek voor steek.</p></li>
      <li>{stapbeeld("polo")}<h3>Klaar</h3><p>Een logo met reliëf dat jaren mooi blijft. Nabestellen kan daarna snel, het patroon is er al.</p></li>
    </ol>
    <ul class="vinklijst vinklijst--naast">
      <li>Beste voor polo's, jassen, caps en handdoeken</li>
      <li>Chique uitstraling, slijt bijna niet</li>
      <li>Minder geschikt voor hele fijne details of kleurverlopen</li>
    </ul>
  </div>
</section>

<section class="section section--wit" id="bedrukken">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Bedrukken</span>
      <h2>Zo wordt uw logo bedrukt</h2>
    </div>
    <ol class="processtappen">
      <li>{stapbeeld("ontwerp")}<h3>Ontwerp klaarzetten</h3><p>Uw logo of ontwerp wordt op maat gemaakt voor het kledingstuk, met de juiste kleuren.</p></li>
      <li>{stapbeeld("pers")}<h3>Drukken of persen</h3><p>Het ontwerp wordt op de stof gedrukt of met warmte en druk op de stof geperst.</p></li>
      <li>{stapbeeld("tshirt")}<h3>Klaar</h3><p>Een glad, kleurrijk resultaat. Ook grote ontwerpen op de rug zijn mogelijk.</p></li>
    </ol>
    <ul class="vinklijst vinklijst--naast">
      <li>Beste voor T-shirts, hoodies, sportkleding en hesjes</li>
      <li>Veel kleuren en fijne details mogelijk</li>
      <li>Voordelig bij grote aantallen en evenementen</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap duo">
    <div class="stack">
      <span class="eyebrow">Waar komt het logo?</span>
      <h2>De gebruikelijke plekken en maten</h2>
      <p class="intro">Dit zijn de maten die we het meest gebruiken. In uw offerte stemmen we de plek en grootte samen af.</p>
      <p class="hint">Tip: voor onbelaste verstrekking van werkkleding geldt vaak een minimum van 70 cm² aan logo per kledingstuk. Vraag uw boekhouder wat voor u geldt.</p>
    </div>
    <div class="illustratiekader">{plaatsing()}</div>
  </div>
</section>

<section class="section section--wit">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Vergelijken</span>
      <h2>Het verschil in het kort</h2>
    </div>
    <div class="tabelwrap">
      <table>
        <thead><tr><th scope="col"></th><th scope="col">Borduren</th><th scope="col">Bedrukken</th></tr></thead>
        <tbody>
          <tr><th scope="row">Uitstraling</th><td>Luxe en professioneel, met reliëf</td><td>Glad, strak en kleurrijk</td></tr>
          <tr><th scope="row">Duurzaamheid</th><td>Zeer goed, slijt nauwelijks</td><td>Goed, afhankelijk van stof en wassen</td></tr>
          <tr><th scope="row">Beste voor</th><td>Kleine logo's op borst, mouw of cap</td><td>Grote ontwerpen op rug of voorkant</td></tr>
          <tr><th scope="row">Kleuren en details</th><td>Beperkt aantal garenkleuren, geen hele fijne details</td><td>Veel kleuren en fijne details mogelijk</td></tr>
          <tr><th scope="row">Stoffen</th><td>Stevige stoffen: polo's, sweaters, jassen</td><td>Ook dunne stoffen: T-shirts, sportkleding</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

{CTA}"""

overzicht = f"""<section class="hero hero--klein">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Alle branches</span>
      <h1>Bedrijfskleding voor elke branche</h1>
      <p class="intro">Kies uw branche om te zien welke kleding er past. Staat uw branche er niet tussen? Vraag het gerust, we denken graag mee.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">{tegels()}</div>
</section>
<section class="section section--wit">
  <div class="wrap duo">
    <div class="stack">
      <span class="eyebrow">Waarom Bordoo</span>
      <h2>Eén keer goed geregeld</h2>
      <ul class="vinklijst">
        <li>Uw logo wordt één keer klaargemaakt. Nabestellen is daarna snel en makkelijk.</li>
        <li>Advies over kleding, kleur en de plek van het logo</li>
        <li>Borduren en bedrukken onder één dak</li>
        <li>Ook kleine aantallen, bijvoorbeeld voor nieuwe medewerkers</li>
      </ul>
    </div>
    {foto("team in bedrijfskleding", True)}
  </div>
</section>
{CTA}"""


def productinfo(pk):
    """Kleuren, maten en logoplekken uit de samensteller, zodat beide altijd hetzelfde tonen."""
    cid = VAN_PRODUCT.get(pk)
    prod = next((p for p in CG.PRODUCTEN if p[0] == cid), None)
    if not prod:
        return ""
    kleuren = "".join(f'<span class="kleurstip" style="background:{CG.KLEUREN[k][1]}" title="{CG.KLEUREN[k][0]}"></span>' for k in prod[4])
    namen = ", ".join(CG.KLEUREN[k][0].lower() for k in prod[4])
    maten = "XS t/m 3XL" if prod[6] == "kleding" else "Eén maat"
    plekken = []
    for q in prod[5]:
        n = q[1].split(" (")[0]
        n = "Borst" if n.startswith("Borst") else "Mouw" if n.startswith("Mouw") else n
        if n not in plekken:
            plekken.append(n)
    return f'''<dl class="productinfo">
          <div><dt>Kleuren</dt><dd><span class="kleurstippen" role="img" aria-label="{namen}">{kleuren}</span></dd></div>
          <div><dt>Maten</dt><dd>{maten}</dd></div>
          <div><dt>Logo op</dt><dd>{" · ".join(plekken)}</dd></div>
        </dl>'''


def productbeeld(pk):
    naam = P[pk][1]
    if heeft_achterkant(naam):
        return (f'<div class="product__beeld heeft-achter">{kleding(naam)}'
                f'<img class="achterkant" src="{BESTANDEN_MAP}/{naam}-achter.svg" alt="" width="120" height="120" loading="lazy" decoding="async">'
                f'<span class="product__kant" aria-hidden="true">Voor · Achter</span></div>')
    return f'<div class="product__beeld">{kleding(naam)}</div>'


def branchepagina(k, menu, titel, intro, tegel, icon, prods):
    kaarten = "".join(f'''<article class="product" id="{pk}">
      {productbeeld(pk)}
      <div class="product__tekst">
        <h3>{P[pk][0]}</h3>
        <p>{P[pk][2]}</p>
        <div class="tags">{tags(P[pk][3])}</div>
        {productinfo(pk)}
        <div class="product__links">{f'<a class="knop knop--hoofd knop--klein" href="samenstellen.html?product={pk}">Stel samen</a>' if pk in VAN_PRODUCT else ''}<a class="meer" href="offerte.html?branche={k}&amp;product={pk}">Offerte aanvragen →</a></div>
      </div>
    </article>''' for pk in prods)
    andere = "".join(f'<a href="branche-{b[0]}.html">{b[1]}</a>' for b in B if b[0] != k)
    return f"""<section class="hero hero--branche">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">{tegel}</span>
      <h1>{titel}</h1>
      <p class="intro">{intro}</p>
      <div class="knoppen"><a class="knop knop--hoofd" href="offerte.html?branche={k}">Offerte voor {menu.lower()}</a></div>
    </div>
    <div class="herotegel herotegel--groot" aria-hidden="true">{kleding(icon)}</div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Producten</span>
      <h2>Wat we voor {menu.lower()} doen</h2>
      <p class="intro">Een greep uit wat we vaak maken. Bij elk product ziet u of we het meestal borduren, bedrukken of allebei.</p>
    </div>
    <div class="producten">{kaarten}</div>
    <p class="hint" style="margin-top:20px">Afbeeldingen zijn tekeningen ter illustratie. Merk, model en kleur kiest u samen met ons bij de offerte.</p>
  </div>
</section>
{aanbevolen(k, menu, P, kleding)}
{cta_branche(k, menu)}
<section class="section section--compact">
  <div class="wrap andere">
    <span class="eyebrow">Andere branches</span>
    <div class="andere__links">{andere}</div>
  </div>
</section>"""


opties_branche = "".join(f'<option value="{b[0]}">{b[1]}</option>' for b in B)
opties_product = "".join(f'<option value="{k}">{v[0]}</option>' for k, v in P.items())
off = f"""<section class="hero hero--klein">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Offerte &amp; contact</span>
      <h1>Vraag vrijblijvend een offerte aan</h1>
      <p class="intro">Vul in wat u zoekt en stuur uw logo mee. U hoort zo snel mogelijk van ons, meestal binnen twee werkdagen.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap duo" style="align-items:start">
    <form class="form" name="offerte" method="POST" action="bedankt.html" data-netlify="true" netlify-honeypot="website" enctype="multipart/form-data">
      <input type="hidden" name="form-name" value="offerte">
      <p class="verborgen"><label>Niet invullen: <input name="website"></label></p>
      <div class="veld--rij">
        <div class="veld"><label for="naam">Naam *</label><input id="naam" name="naam" type="text" autocomplete="name" required></div>
        <div class="veld"><label for="bedrijf">Bedrijf of vereniging</label><input id="bedrijf" name="bedrijf" type="text" autocomplete="organization"></div>
      </div>
      <div class="veld--rij">
        <div class="veld"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="veld"><label for="telefoon">Telefoon</label><input id="telefoon" name="telefoon" type="tel" autocomplete="tel"></div>
      </div>
      <div class="veld--rij">
        <div class="veld"><label for="branche">Branche</label><select id="branche" name="branche"><option value="">Kies uw branche</option>{opties_branche}<option value="anders">Anders</option></select></div>
        <div class="veld"><label for="product">Product</label><select id="product" name="product"><option value="">Kies een product</option>{opties_product}<option value="anders">Anders / meerdere</option></select></div>
      </div>
      <fieldset>
        <legend>Borduren of bedrukken? *</legend>
        <div class="keuzes">
          <label class="keuze"><input type="radio" name="dienst" value="Borduren" required> Borduren</label>
          <label class="keuze"><input type="radio" name="dienst" value="Bedrukken"> Bedrukken</label>
          <label class="keuze"><input type="radio" name="dienst" value="Advies graag"> Advies graag</label>
        </div>
      </fieldset>
      <div class="veld--rij">
        <div class="veld"><label for="aantal">Aantal stuks</label><input id="aantal" name="aantal" type="number" min="1" inputmode="numeric" placeholder="bijv. 25"></div>
        <div class="veld"><label for="datum">Wanneer nodig?</label><input id="datum" name="datum" type="date"></div>
      </div>
      <div class="veld">
        <label for="logo">Uw logo of ontwerp</label>
        <input id="logo" name="logo" type="file" accept=".png,.jpg,.jpeg,.svg,.pdf,.ai,.eps">
        <span class="hint">Liefst als PDF, SVG of AI. Een PNG of JPG mag ook.</span>
      </div>
      <div class="veld"><label for="bericht">Toelichting</label><textarea id="bericht" name="bericht" placeholder="Bijv. kleur van de kleding, maten, plek van het logo (borst, rug, mouw)"></textarea></div>
      <label class="akkoord"><input type="checkbox" id="akkoord" name="akkoord" required> <span>Ik ga akkoord dat Bordoo mijn gegevens gebruikt om deze aanvraag te beantwoorden, zoals beschreven in de <a href="privacy.html" target="_blank">privacyverklaring</a>. *</span></label>
      <div><button class="knop knop--hoofd" type="submit">Verstuur aanvraag</button></div>
    </form>
    <aside class="contactblok">
      <h2>Liever direct contact?</h2>
      <div class="contactregel"><span>E-mail</span><a href="mailto:{MAIL}">{MAIL}</a></div>
      <div class="contactregel"><span>Telefoon / WhatsApp</span>{TEL}</div>
      <hr class="goudlijn">
      <p class="hint">Particulier? Ook voor één kledingstuk met een naam of tekst kunt u ons een bericht sturen.</p>
    </aside>
  </div>
</section>
<script>
  (function () {{
    var q = new URLSearchParams(location.search);
    ['branche', 'product'].forEach(function (n) {{ var v = q.get(n), s = document.getElementById(n); if (v && s.querySelector('option[value="' + v + '"]')) s.value = v; }});
  }})();
</script>"""

bedankt = """<section class="hero hero--klein">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Aanvraag ontvangen</span>
      <h1>Bedankt voor uw aanvraag</h1>
      <p class="intro">We hebben uw aanvraag ontvangen en nemen zo snel mogelijk contact met u op, meestal binnen twee werkdagen.</p>
      <div class="knoppen"><a class="knop knop--goud" href="index.html">Terug naar de homepage</a></div>
    </div>
  </div>
</section>"""

files = {
    "index.html": ("Bordoo – Bedrijfskleding borduren en bedrukken", "Stel zelf uw kleding met logo samen: kies product, kleur en maten en upload uw logo. Bordoo borduurt en bedrukt bedrijfskleding voor elke branche.", home_body(B, P, kleding, doorsnede(), CTA, stapbeeld, TEL), None),
    "samenstellen.html": ("Zelf samenstellen – Bordoo", "Kies een kledingstuk, kleur en maten, upload uw logo en zie direct een voorbeeld. Vraag daarna vrijblijvend een offerte aan.", samensteller_body(TEL, MAIL), None),
    "borduren-bedrukken.html": ("Borduren of bedrukken? – Bordoo", "Het verschil tussen borduren en bedrukken van kleding in beeld uitgelegd, met de gebruikelijke plekken en maten voor uw logo.", bb, None),
    "bedrijfskleding.html": ("Bedrijfskleding per branche – Bordoo", "Bedrijfskleding met logo voor elke branche: horeca, bouw, garage, schoonmaak, zorg, transport, kantoor en sport.", overzicht, None),
    "offerte.html": ("Offerte aanvragen – Bordoo", "Vraag vrijblijvend een offerte aan voor geborduurde of bedrukte bedrijfskleding.", off, None),
    "bedankt.html": ("Bedankt – Bordoo", "Uw aanvraag is ontvangen.", bedankt, None),
    "privacy.html": ("Privacyverklaring – Bordoo", "Hoe Bordoo omgaat met uw persoonsgegevens: welke gegevens, waarvoor, hoe lang en uw rechten.", PRIVACY, None),
}
for b in B:
    files[f"branche-{b[0]}.html"] = (f"{b[2]} – Bordoo", b[3], branchepagina(*b), b[0])
(OUT / BESTANDEN_MAP).mkdir(parents=True, exist_ok=True)
for naam in _STIJL:
    (OUT / BESTANDEN_MAP / f"{naam}.svg").write_text(bestand_svg(naam), encoding="utf-8")
    if heeft_achterkant(naam):
        (OUT / BESTANDEN_MAP / f"{naam}-achter.svg").write_text(bestand_svg_achter(naam), encoding="utf-8")
for fn, (title, desc, body, br) in files.items():
    (OUT / fn).write_text(page(fn, title, desc, body, br), encoding="utf-8")
print("ok", len(files))
