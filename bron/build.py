"""Bouwt de Bordoo-website: gedeelde header/footer + 4 pagina's."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])
TODO = lambda t: f'<span class="invullen">{t}</span>'
TEL = TODO("06 – nog invullen")
MAIL = "info@bordoo.nl"
KVK = TODO("KvK-nummer")
PLAATS = TODO("plaats")

PAGES = [
    ("index.html", "Home"),
    ("borduren-bedrukken.html", "Borduren & bedrukken"),
    ("bedrijfskleding.html", "Bedrijfskleding"),
    ("offerte.html", "Offerte & contact"),
]

def foto(label, licht=False, hoog=False, icoon=False):
    cls = "foto" + (" foto--licht" if licht else "") + (" foto--hoog" if hoog else "")
    ic = '<div class="foto__icoon" aria-hidden="true"><img src="img/icoon-wit.svg" alt=""></div>' if icoon else ""
    return f'<div class="{cls}" role="img" aria-label="Plek voor foto: {label}">{ic}<span class="foto__label">Foto volgt: {label}</span></div>'

def page(fn, title, desc, body):
    nav = "\n".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == fn else ""}>{n}</a>'
        for f, n in PAGES[:-1]
    )
    cur = ' aria-current="page"' if fn == "offerte.html" else ""
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="img/icoon.png">
<link rel="preload" href="fonts/archivo-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="header">
  <div class="wrap">
    <a class="header__logo" href="index.html" aria-label="Bordoo – naar de homepage"><img src="img/logo.svg" alt="Bordoo" width="110" height="34"></a>
    <button class="menuknop" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
    <nav class="nav" id="menu" aria-label="Hoofdmenu">
      {nav}
      <a class="knop knop--hoofd" href="offerte.html"{cur}>Offerte aanvragen</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__raster">
      <div class="stack">
        <img src="img/logo-negatief.svg" alt="Bordoo – borduur &amp; druk" width="132" height="54">
        <p>Borduren en bedrukken van bedrijfskleding, teamkleding en persoonlijke kleding.</p>
      </div>
      <div>
        <h3>Pagina's</h3>
        <ul>{"".join(f'<li><a href="{f}">{n}</a></li>' for f, n in PAGES)}</ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li>{TEL}</li>
          <li>{PLAATS}</li>
        </ul>
      </div>
    </div>
    <div class="footer__onder">
      <span>© 2026 Bordoo · KvK {KVK}</span>
      <span>bordoo.nl</span>
    </div>
  </div>
</footer>
<script>
  var k = document.querySelector('.menuknop'), m = document.getElementById('menu');
  k.addEventListener('click', function () {{ var o = m.classList.toggle('open'); k.setAttribute('aria-expanded', o); k.textContent = o ? 'Sluiten' : 'Menu'; }});
</script>
</body>
</html>
"""

CTA = """<section class="cta">
  <div class="wrap">
    <div>
      <h2>Uw logo op kleding?</h2>
      <p>Vertel ons wat u zoekt. U krijgt vrijblijvend een prijs op maat.</p>
    </div>
    <a class="knop knop--hoofd" href="offerte.html">Vraag een offerte aan</a>
  </div>
</section>"""

# ---------- Home ----------
home = f"""<section class="hero">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Borduren · Bedrukken · Bedrijfskleding</span>
      <h1>Uw logo, netjes op elk kledingstuk.</h1>
      <p class="intro">Polo's, jassen en werkkleding met uw logo, geborduurd of bedrukt. Voor bedrijven, verenigingen en particulieren.</p>
      <div class="knoppen">
        <a class="knop knop--hoofd" href="offerte.html">Vraag een offerte aan</a>
        <a class="knop knop--goud" href="borduren-bedrukken.html">Borduren of bedrukken?</a>
      </div>
    </div>
    {foto("geborduurde polo met logo", hoog=True, icoon=True)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Wat we doen</span>
      <h2>Eén adres voor kleding met uw naam erop</h2>
    </div>
    <div class="raster">
      <article class="kaart">
        <hr class="goudlijn">
        <h3>Borduren</h3>
        <p>Strak en duurzaam. Het logo zit in de stof en blijft mooi, ook na vele wasbeurten. Ideaal voor polo's, jassen en caps.</p>
        <a class="meer" href="borduren-bedrukken.html#borduren">Meer over borduren →</a>
      </article>
      <article class="kaart">
        <hr class="goudlijn">
        <h3>Bedrukken</h3>
        <p>Voor grote vlakken en logo's met veel kleuren. Snel en voordelig, ook voor T-shirts en evenementen.</p>
        <a class="meer" href="borduren-bedrukken.html#bedrukken">Meer over bedrukken →</a>
      </article>
      <article class="kaart">
        <hr class="goudlijn">
        <h3>Bedrijfskleding</h3>
        <p>Uw hele team in dezelfde stijl. Wij helpen met de kleding, het logo en nabestellen als het team groeit.</p>
        <a class="meer" href="bedrijfskleding.html">Meer over bedrijfskleding →</a>
      </article>
    </div>
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

<section class="section section--wit">
  <div class="wrap duo">
    <div class="stack">
      <span class="eyebrow">Voor wie</span>
      <h2>Voor bedrijven, clubs en particulieren</h2>
      <ul class="vinklijst">
        <li><strong>Bedrijven</strong>: werkkleding en representatieve kleding met uw logo</li>
        <li><strong>Verenigingen en sportclubs</strong>: teamkleding, trainingspakken, tassen</li>
        <li><strong>Particulieren</strong>: een naam, tekst of afbeelding op kleding of handdoeken, ook als cadeau</li>
      </ul>
      <div class="knoppen"><a class="knop knop--rand" href="bedrijfskleding.html">Bekijk bedrijfskleding</a></div>
    </div>
    {foto("team in bedrijfskleding", licht=True)}
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
      {foto("bedrukte T-shirts", licht=True)}
      {foto("jas met geborduurd logo")}
    </div>
  </div>
</section>

{CTA}"""

# ---------- Borduren & bedrukken ----------
bb = f"""<section class="hero hero--klein">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Borduren &amp; bedrukken</span>
      <h1>Borduren of bedrukken: wat past bij u?</h1>
      <p class="intro">Allebei geven ze kleding met uw logo. Het verschil zit in de uitstraling, de duurzaamheid en het soort logo. Twijfelt u? Wij denken graag mee.</p>
    </div>
  </div>
</section>

<section class="section section--wit" id="borduren">
  <div class="wrap duo">
    <div class="stack">
      <span class="eyebrow">Borduren</span>
      <h2>Chique en gaat jaren mee</h2>
      <p class="intro">Bij borduren wordt het logo met garen in de stof gestikt. Dat geeft een luxe, professionele uitstraling en het slijt bijna niet.</p>
      <ul class="vinklijst">
        <li>Polo's, overhemden, sweaters en jassen</li>
        <li>Caps, tassen en handdoeken</li>
        <li>Logo's, namen en initialen</li>
        <li>Blijft mooi, ook na vele wasbeurten</li>
      </ul>
    </div>
    {foto("borduurwerk op een polo", hoog=True)}
  </div>
</section>

<section class="section" id="bedrukken">
  <div class="wrap duo duo--omgekeerd">
    {foto("bedrukt T-shirt", licht=True, hoog=True)}
    <div class="stack">
      <span class="eyebrow">Bedrukken</span>
      <h2>Kleurrijk en voordelig</h2>
      <p class="intro">Bij bedrukken komt het ontwerp op de stof. Daarmee kunnen grote afbeeldingen, veel kleuren en fijne details.</p>
      <ul class="vinklijst">
        <li>T-shirts, hoodies en sportkleding</li>
        <li>Grote opdrukken op rug of borst</li>
        <li>Logo's met veel kleuren of kleurverloop</li>
        <li>Voordelig bij evenementen en acties</li>
      </ul>
    </div>
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

# ---------- Bedrijfskleding ----------
items = [("Polo's", "De klassieker voor representatieve bedrijfskleding."),
         ("T-shirts", "Voor in de werkplaats, op evenementen of als teamshirt."),
         ("Sweaters &amp; hoodies", "Warm en zakelijk, met logo op borst of rug."),
         ("Jassen &amp; bodywarmers", "Buiten herkenbaar, het hele jaar door."),
         ("Werkkleding", "Stevige kleding voor technische en bouwberoepen."),
         ("Caps &amp; tassen", "Accessoires die uw merk ook buiten laten zien.")]
kaarten = "\n".join(f'<article class="kaart"><h3>{t}</h3><p>{d}</p></article>' for t, d in items)
bk = f"""<section class="hero">
  <div class="wrap">
    <div class="hero__tekst">
      <span class="eyebrow">Bedrijfskleding</span>
      <h1>Uw team herkenbaar, van werkplaats tot klant.</h1>
      <p class="intro">Bedrijfskleding met uw logo, geborduurd of bedrukt. Van een paar polo's tot kleding voor het hele team.</p>
      <div class="knoppen"><a class="knop knop--hoofd" href="offerte.html">Vraag een offerte aan</a></div>
    </div>
    {foto("bedrijfskleding met logo", hoog=True, icoon=True)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="kop">
      <span class="eyebrow">Assortiment</span>
      <h2>Welke kleding kan er?</h2>
      <p class="intro">Een greep uit wat we vaak doen. Zoekt u iets anders? Vraag het gerust.</p>
    </div>
    <div class="raster">{kaarten}</div>
  </div>
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
      <p class="hint">Levertijd en minimale aantallen hoort u bij uw offerte.</p>
    </div>
    {foto("polo's met logo in een stapel", licht=True)}
  </div>
</section>

{CTA}"""

# ---------- Offerte & contact ----------
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

      <fieldset>
        <legend>Wat wilt u laten doen? *</legend>
        <div class="keuzes">
          <label class="keuze"><input type="radio" name="dienst" value="Borduren" required> Borduren</label>
          <label class="keuze"><input type="radio" name="dienst" value="Bedrukken"> Bedrukken</label>
          <label class="keuze"><input type="radio" name="dienst" value="Weet ik nog niet"> Weet ik nog niet</label>
        </div>
      </fieldset>

      <div class="veld--rij">
        <div class="veld">
          <label for="kleding">Soort kleding</label>
          <select id="kleding" name="kleding">
            <option>Polo's</option><option>T-shirts</option><option>Sweaters / hoodies</option><option>Jassen / bodywarmers</option>
            <option>Werkkleding</option><option>Caps / tassen</option><option>Handdoeken</option><option>Anders / meerdere</option>
          </select>
        </div>
        <div class="veld"><label for="aantal">Aantal stuks</label><input id="aantal" name="aantal" type="number" min="1" inputmode="numeric" placeholder="bijv. 25"></div>
      </div>

      <div class="veld"><label for="datum">Wanneer heeft u het nodig?</label><input id="datum" name="datum" type="date"></div>

      <div class="veld">
        <label for="logo">Uw logo of ontwerp</label>
        <input id="logo" name="logo" type="file" accept=".png,.jpg,.jpeg,.svg,.pdf,.ai,.eps">
        <span class="hint">Liefst als PDF, SVG of AI. Een PNG of JPG mag ook.</span>
      </div>

      <div class="veld"><label for="bericht">Toelichting</label><textarea id="bericht" name="bericht" placeholder="Bijv. kleur van de kleding, maten, plek van het logo (borst, rug, mouw)"></textarea></div>

      <label class="akkoord"><input type="checkbox" name="akkoord" required> <span>Ik ga akkoord dat Bordoo mijn gegevens gebruikt om deze aanvraag te beantwoorden. *</span></label>

      <div><button class="knop knop--hoofd" type="submit">Verstuur aanvraag</button></div>
    </form>

    <aside class="contactblok">
      <h2>Liever direct contact?</h2>
      <div class="contactregel"><span>E-mail</span><a href="mailto:{MAIL}">{MAIL}</a></div>
      <div class="contactregel"><span>Telefoon / WhatsApp</span><strong>{TEL}</strong></div>
      <div class="contactregel"><span>Locatie</span><strong>{PLAATS}</strong></div>
      <hr class="goudlijn">
      <p class="hint">Particulier? Ook voor één kledingstuk met een naam of tekst kunt u ons een bericht sturen.</p>
    </aside>
  </div>
</section>"""

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
    "index.html": ("Bordoo – Borduren, bedrukken en bedrijfskleding",
                   "Bordoo borduurt en bedrukt bedrijfskleding, teamkleding en persoonlijke kleding. Vraag vrijblijvend een offerte aan.", home),
    "borduren-bedrukken.html": ("Borduren of bedrukken? – Bordoo",
                   "Het verschil tussen borduren en bedrukken van kleding, en wat het beste past bij uw logo.", bb),
    "bedrijfskleding.html": ("Bedrijfskleding met logo – Bordoo",
                   "Polo's, jassen, werkkleding en meer met uw logo, geborduurd of bedrukt door Bordoo.", bk),
    "offerte.html": ("Offerte aanvragen – Bordoo",
                   "Vraag vrijblijvend een offerte aan voor geborduurde of bedrukte kleding.", off),
    "bedankt.html": ("Bedankt – Bordoo", "Uw aanvraag is ontvangen.", bedankt),
}
for fn, (title, desc, body) in files.items():
    (OUT / fn).write_text(page(fn, title, desc, body), encoding="utf-8")
print("ok", len(files))
