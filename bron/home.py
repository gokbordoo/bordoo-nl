"""Homepage BORDOO V2: zakelijke boodschap, diensten, voorbeeldweergaven, branches en werkwijze.

Gebruikt alleen beloftes die al op de V1-site stonden; nieuwe claims pas na akkoord van Bordoo.
"""
import itertools
import realistisch as R
from garments import _licht

_teller = itertools.count(1)
LOGO_LICHT, LOGO_DONKER = "img/logo-negatief.svg", "img/logo-tekst.svg"  # voor donkere / lichte stof
VERHOUDING = 120 / 292  # hoogte / breedte van het logo


def weergave(naam, hexk, logo_x, logo_y, breedte, kant="voor", uitsnede="0 0 120 120", techniek="Borduren", label=""):
    """Kledingstuk met het Bordoo-logo erop, als voorbeeldweergave."""
    n = next(_teller)
    teken = R.voorkant(naam) if kant == "voor" else R.achterkant(naam)
    naad = "rgba(0,0,0,.35)" if _licht(hexk) else "rgba(255,255,255,.35)"
    logo = LOGO_DONKER if _licht(hexk) else LOGO_LICHT
    h = breedte * VERHOUDING
    filt = f' filter="url(#vb{n}-steek)"' if techniek == "Borduren" else ""
    return (f'<svg viewBox="{uitsnede}" role="img" aria-label="{label}" style="--stof:{hexk};--naad:{naad}">'
            f'<defs><filter id="vb{n}-steek" x="-10%" y="-10%" width="120%" height="120%">'
            f'<feDropShadow dx=".12" dy=".18" stdDeviation=".12" flood-opacity=".5"/></filter></defs>'
            f'{teken.replace("rl-", f"vb{n}-")}'
            f'<image href="{logo}" x="{logo_x - breedte / 2:.2f}" y="{logo_y - h / 2:.2f}" width="{breedte}" height="{h:.2f}"{filt}/></svg>')


def home_body(branches, P, kleding, doorsnede, CTA, stapbeeld, tel_link):
    teaser = weergave("polo", "#5E1424", 68, 41, 9.5, uitsnede="18 8 84 84", label="Bordeaux polo met geborduurd logo op de borst")
    kleuren = ["#5E1424", "#1F1E1F", "#1F2C44", "#FAFAF8", "#1F4A35"]
    stippen = "".join(f'<span style="background:{k}"></span>' for k in kleuren)

    voorbeelden = [
        ("Borduren", "Logo op de borst", "Polo, geborduurd, ca. 9 cm breed",
         weergave("polo", "#5E1424", 68, 41, 6.6, uitsnede="50 24 34 34", label="Geborduurd logo op een bordeaux polo")),
        ("Bedrukken", "Groot op de rug", "Werkjas, bedrukt, ca. 25 cm breed",
         weergave("werkjas", "#1F2C44", 60, 50, 22, kant="achter", uitsnede="14 6 92 92", techniek="Bedrukken",
                  label="Bedrukt logo op de rug van een marineblauwe werkjas")),
        ("Borduren", "Voorkant van de pet", "Cap, geborduurd, ca. 7 cm breed",
         weergave("cap", "#1F1E1F", 47, 58, 7.2, uitsnede="20 26 80 80", label="Geborduurd logo op een zwarte pet")),
        ("Borduren", "Koksbuis op de borst", "Koksbuis, geborduurd, ca. 7 cm breed",
         weergave("koksbuis", "#FAFAF8", 73, 37, 5.2, uitsnede="58 22 30 30", label="Geborduurd logo op een witte koksbuis")),
    ]
    vb_html = "".join(f'''<figure class="vb">
        <div class="vb__beeld">{svg}</div>
        <figcaption><span class="tag">{tech}</span><strong>{titel}</strong><span>{sub}</span></figcaption>
      </figure>''' for tech, titel, sub, svg in voorbeelden)

    def brkaart(b):
        k, menu, titel, intro, tegel, icon, prods = b
        tweede = P[prods[1]][1] if P[prods[1]][1] != icon else P[prods[2]][1]
        lijst = " · ".join(P[pk][0] for pk in prods[:3])
        return f'''<a class="brkaart" href="branche-{k}.html">
        <div class="brkaart__beeld">{kleding(icon, "br-hoofd")}{kleding(tweede, "br-bij")}</div>
        <div class="brkaart__tekst"><span class="brkaart__sub">{tegel}</span><h3>{menu}</h3><p>{lijst}</p></div>
        <span class="brkaart__pijl" aria-hidden="true">→</span>
      </a>'''
    kaarten = "".join(brkaart(b) for b in branches)

    return f"""<section class="v2-hero">
  <div class="wrap v2-hero__raster">
    <div class="v2-hero__tekst">
      <span class="eyebrow">Bedrijfskleding · Borduren · Bedrukken</span>
      <h1>Bedrijfskleding met uw logo, geborduurd of bedrukt.</h1>
      <p class="intro">Voor bedrijven, teams en verenigingen. Kies uw kleding, upload uw logo en zie direct hoe het wordt. Daarna ontvangt u een offerte op maat.</p>
      <div class="knoppen">
        <a class="knop knop--hoofd" href="samenstellen.html">Stel uw kleding samen</a>
        <a class="knop knop--goud" href="offerte.html">Vraag een offerte aan</a>
      </div>
      <p class="v2-hero__bel">Liever even overleggen? Bel {tel_link}</p>
    </div>
    <a class="v2-teaser" href="samenstellen.html" aria-label="Probeer zelf samenstellen">
      <div class="v2-teaser__beeld">{teaser}</div>
      <div class="v2-teaser__info">
        <span class="v2-teaser__titel">Polo · Bordeaux · Logo borst links</span>
        <span class="teaser__stippen">{stippen}</span>
        <span class="teaser__link">Probeer het met uw eigen logo →</span>
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

<section class="section section--wit section--compact" id="branches" aria-labelledby="br-kop">
  <div class="wrap">
    <div class="kop kop--rij">
      <div><span class="eyebrow">Kleding per branche</span><h2 id="br-kop">Kleding die past bij uw vak</h2></div>
      <a class="meer" href="bedrijfskleding.html">Alle branches →</a>
    </div>
    <div class="brkaarten">{kaarten}</div>
  </div>
</section>

<section class="section section--compact" aria-labelledby="vb-kop">
  <div class="wrap">
    <div class="kop kop--rij">
      <div><span class="eyebrow">Voorbeelden</span><h2 id="vb-kop">Zo komt uw logo op de kleding</h2></div>
      <a class="meer" href="samenstellen.html">Probeer het met uw logo →</a>
    </div>
    <div class="voorbeelden">{vb_html}</div>
    <p class="hint vb__noot">Voorbeeldweergaven met het Bordoo-logo. Maten zijn gebruikelijke richtlijnen.</p>
  </div>
</section>

<section class="section section--wit section--compact" aria-labelledby="diensten-kop">
  <div class="wrap">
    <div class="dienst-intro">
      <div class="kop"><span class="eyebrow">Wat we doen</span><h2 id="diensten-kop">Twee technieken, één aanspreekpunt</h2>
        <p class="intro">Borduren zit ín de stof: chique, met reliëf en het gaat jaren mee. Bedrukken ligt óp de stof: glad, kleurrijk en voordelig. Welke techniek past, hangt af van uw logo, de kleding en het aantal stuks. We adviseren u graag.</p>
        <div><a class="meer" href="borduren-bedrukken.html">Bekijk de uitleg met tekeningen →</a></div></div>
      <div class="illustratiekader">{doorsnede}</div>
    </div>
    <div class="diensten">
      <article class="dienst">
        <div class="dienst__beeld">{stapbeeld("machine")}</div>
        <div class="dienst__tekst">
          <h3>Borduren</h3>
          <p>Het logo wordt met garen in de stof gestikt. Chique, met reliëf en lang mooi.</p>
          <ul class="vinklijst"><li>Polo's, jassen, fleece en caps</li><li>Kleine logo's op borst of mouw</li></ul>
          <a class="meer" href="borduren-bedrukken.html#borduren">Meer over borduren →</a>
        </div>
      </article>
      <article class="dienst">
        <div class="dienst__beeld">{stapbeeld("pers")}</div>
        <div class="dienst__tekst">
          <h3>Bedrukken</h3>
          <p>Het ontwerp komt als dunne laag op de stof. Glad, kleurrijk en voordelig.</p>
          <ul class="vinklijst"><li>T-shirts, hoodies, sport en hesjes</li><li>Grote ontwerpen op de rug</li></ul>
          <a class="meer" href="borduren-bedrukken.html#bedrukken">Meer over bedrukken →</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--donker section--compact" aria-labelledby="werk-kop">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Zo werkt het</span><h2 id="werk-kop">In vier stappen naar uw bedrijfskleding</h2></div>
    <ol class="stappen">
      <li><h3>Samenstellen of aanvragen</h3><p>Kies kleding, kleur en maten en upload uw logo. Of stuur een aanvraag.</p></li>
      <li><h3>Voorstel</h3><p>U krijgt een prijs en een voorbeeld van hoe het logo op de kleding komt.</p></li>
      <li><h3>Productie</h3><p>Na uw akkoord borduren of bedrukken wij de kleding.</p></li>
      <li><h3>Levering</h3><p>U haalt de kleding op of wij sturen het naar u toe.</p></li>
    </ol>
    <div class="knoppen" style="margin-top:28px;align-items:center"><a class="knop knop--hoofd v2-knop-licht" href="samenstellen.html">Begin met samenstellen</a><a class="meer v2-meer-licht" href="werkwijze.html">Meer over onze werkwijze →</a></div>
  </div>
</section>

{CTA}"""
