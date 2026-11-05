"""Vertrouwenspagina's V2: Over Bordoo, Werkwijze, Veelgestelde vragen en 404.

Neutrale teksten zonder verzonnen ervaring, aantallen, levertijden of prijzen.
Plekken die Bordoo later aanvult staan gemarkeerd met AANVULLEN in de broncode.
"""


def kop(eyebrow, titel, intro):
    return f'''<section class="kopstrook">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{titel}</h1>
    <p class="intro">{intro}</p>
  </div>
</section>'''


def over(tel, mail, cta):
    # AANVULLEN: persoonlijk verhaal van Gök (waarom Bordoo, achtergrond), eventueel een foto
    return kop("Over Bordoo", "Over Bordoo",
               "Bordoo borduurt en bedrukt bedrijfskleding met uw logo. Voor bedrijven, teams, verenigingen en particulieren.") + f'''
<section class="section section--compact">
  <div class="wrap duo" style="align-items:start">
    <div class="tekstpagina">
      <h2>Wie we zijn</h2>
      <p>Bordoo is opgericht door Gök Karakas. Bij Bordoo kunt u terecht voor kleding met uw logo, naam of tekst: geborduurd of bedrukt, van één stuk tot kleding voor uw hele team.</p>
      <h2>Waar we voor staan</h2>
      <ul class="vinklijst">
        <li><strong>Persoonlijk contact.</strong> U heeft direct contact met de eigenaar, per telefoon, WhatsApp of e-mail.</li>
        <li><strong>Eerlijk advies.</strong> We adviseren welke kleding en techniek het beste past bij uw logo en uw gebruik.</li>
        <li><strong>Eerst een voorbeeld.</strong> U ziet hoe het logo op de kleding komt voordat we gaan maken.</li>
        <li><strong>Netjes afgewerkt.</strong> Kleding waar u en uw medewerkers mee voor de dag kunnen komen.</li>
      </ul>
    </div>
    <aside class="bevestiging__kaart">
      <span class="kw__label">Bedrijfsgegevens</span>
      <strong style="font-family:var(--display);font-size:20px">Bordoo</strong>
      <dl class="productinfo" style="border:0;padding:0">
        <div><dt>Eigenaar</dt><dd>Gök Karakas</dd></div>
        <div><dt>Telefoon</dt><dd>{tel}</dd></div>
        <div><dt>E-mail</dt><dd><a href="mailto:{mail}">{mail}</a></dd></div>
        <div><dt>Website</dt><dd>bordoo.nl</dd></div>
      </dl>
      <!-- AANVULLEN: KvK-nummer en vestigingsplaats zodra bekend -->
    </aside>
  </div>
</section>
{cta}'''


def werkwijze(cta):
    stap = lambda n, titel, tekst, punten: f'''<li class="ww-stap">
        <span class="ww-nr" aria-hidden="true">{n}</span>
        <div><h2>{titel}</h2><p>{tekst}</p><ul class="vinklijst">{"".join(f"<li>{p}</li>" for p in punten)}</ul></div>
      </li>'''
    return kop("Werkwijze", "Zo werken wij",
               "Van uw eerste vraag tot de levering van uw kleding, in vier duidelijke stappen.") + f'''
<section class="section section--compact">
  <div class="wrap">
    <ol class="ww">
      {stap(1, "Aanvraag", "Stel uw kleding zelf samen of stuur een offerteaanvraag. U kunt ook bellen of mailen.",
            ["Kies kleding, kleur, maten en de plek van het logo", "Upload uw logo, liefst als PDF, SVG of AI", "Twijfelt u over techniek of kleding? Kies 'Advies graag'"])}
      {stap(2, "Voorstel", "U ontvangt een offerte op maat, met een voorbeeld van hoe het logo op de kleding komt.",
            ["Prijs per product en per logoplek", "Voorbeeld van plek en grootte van het logo", "Vragen of wijzigingen? Die verwerken we eerst"])}
      {stap(3, "Productie", "Na uw akkoord borduren of bedrukken wij de kleding.",
            ["Bij borduren wordt uw logo eerst omgezet naar een borduurpatroon", "Bij nabestellingen gebruiken we dezelfde instellingen"])}
      {stap(4, "Levering", "U haalt de kleding op of wij sturen het naar u toe.",
            ["De mogelijkheden en eventuele kosten hoort u bij de offerte"])}
    </ol>
    <div class="tipblok" style="margin-top:28px"><strong>Handig</strong><p>Heeft u al een aanvraagnummer? Noem dat als u contact met ons opneemt, dan kunnen we u sneller helpen.</p></div>
  </div>
</section>
{cta}'''


# (vraag, antwoord) – AANVULLEN: minimale aantallen, levertijden, verzendkosten en prijsindicaties zodra bekend
FAQ = [
    ("Bestellen en prijzen", [
        ("Wat kost kleding met een logo?", "Dat hangt af van de kleding, het aantal stuks, de techniek en de grootte en plek van het logo. U ontvangt altijd eerst een vrijblijvende offerte op maat."),
        ("Is er een minimum aantal?", "Ook voor kleine aantallen kunt u een aanvraag doen, en particulieren kunnen terecht vanaf één stuk. Wat per product en techniek mogelijk is, hoort u bij de offerte."),
        ("Kan ik meerdere soorten kleding in één aanvraag zetten?", "Ja. In de samensteller kiest u 'Toevoegen en nog een product kiezen', en in het offerteformulier klikt u op '+ Nog een product'."),
        ("Kan ik later nabestellen?", "Ja. Uw logo is dan al klaargezet, zodat nabestellen, bijvoorbeeld voor nieuwe medewerkers, eenvoudig is."),
    ]),
    ("Logo en techniek", [
        ("In welk bestandsformaat lever ik mijn logo aan?", "Het liefst als PDF, SVG of AI (vectorbestand). Een PNG of JPG mag ook; dan kijken we of de kwaliteit voldoende is."),
        ("Borduren of bedrukken: wat moet ik kiezen?", "Borduren is chique en gaat lang mee, ideaal voor kleine logo's op polo's, jassen en caps. Bedrukken is geschikt voor grote ontwerpen en veel kleuren. Gebruik de keuzewijzer op de pagina Borduren & bedrukken, of vraag ons om advies."),
        ("Zie ik eerst hoe het eruit komt te zien?", "Ja. U krijgt een voorbeeld van de plek en grootte van het logo voordat we gaan maken. In de samensteller ziet u ook direct een voorbeeldweergave."),
        ("Mag ik elk logo laten borduren of bedrukken?", "U moet het recht hebben om het logo te gebruiken, bijvoorbeeld omdat het van uw eigen bedrijf of vereniging is."),
    ]),
    ("Levering en onderhoud", [
        ("Hoe lang duurt het voordat ik mijn kleding heb?", "Dat hangt af van de kleding, het aantal en de techniek. De verwachte levertijd hoort u bij uw offerte. Heeft u een vaste datum, vul die dan in bij 'Wanneer nodig?'."),
        ("Kan ik de kleding ophalen of laten bezorgen?", "U haalt de kleding op of wij sturen het naar u toe. De mogelijkheden en eventuele kosten hoort u bij de offerte."),
        ("Hoe was ik geborduurde of bedrukte kleding?", "Volg het waslabel van de kleding. Was bedrukte kleding binnenstebuiten en strijk niet direct over de opdruk. Zo blijft uw logo het langst mooi."),
    ]),
]


def faq(cta):
    groepen = "".join(f'''<div class="faq-groep">
      <h2>{titel}</h2>
      {"".join(f'<details class="faq"><summary>{v}</summary><p>{a}</p></details>' for v, a in vragen)}
    </div>''' for titel, vragen in FAQ)
    return kop("Veelgestelde vragen", "Veelgestelde vragen",
               "Antwoorden op de vragen die we het vaakst krijgen. Staat uw vraag er niet bij? Neem gerust contact met ons op.") + f'''
<section class="section section--compact">
  <div class="wrap faq-wrap">{groepen}
    <div class="tipblok"><strong>Vraag?</strong><p>Bel of WhatsApp ons via de belknop bovenaan, of stuur een bericht via het <a href="offerte.html">contactformulier</a>.</p></div>
  </div>
</section>
{cta}'''


def niet_gevonden():
    return kop("Pagina niet gevonden", "Deze pagina bestaat niet (meer)",
               "Misschien is de link verouderd of zit er een typfout in. Hieronder vindt u de belangrijkste pagina's.") + '''
<section class="section section--compact">
  <div class="wrap">
    <div class="knoppen">
      <a class="knop knop--hoofd" href="/">Naar de homepage</a>
      <a class="knop knop--rand" href="/samenstellen.html">Zelf samenstellen</a>
      <a class="knop knop--rand" href="/bedrijfskleding.html">Alle branches</a>
      <a class="knop knop--rand" href="/offerte.html">Offerte aanvragen</a>
    </div>
  </div>
</section>'''
