"""Branchepagina's V2: aanbevolen kleding per functie en een tip per branche.

Algemeen advies, geen beloftes over levertijden, prijzen of aantallen.
"""

# branche: ([(functie, korte uitleg, [productsleutels]), ...], tip)
PAKKETTEN = {
    "horeca": ([("Keuken", "Hygiënisch, stevig en goed wasbaar.", ["koksbuis", "koksbroek", "schort"]),
                ("Bediening", "Verzorgd en herkenbaar voor uw gasten.", ["polo", "schort", "cap"])],
               "Koksbuizen en schorten gaan vaak in de was. Een geborduurd logo blijft dan het langst mooi."),
    "bouw": ([("Op de bouwplaats", "Zichtbaar, warm en tegen een stootje bestand.", ["werkjas", "hesje", "werkbroek"]),
              ("Werkplaats en kantoor", "Comfortabel voor binnen, met uw logo.", ["tshirt", "hoodie"])],
             "Op veiligheidshesjes komt het logo zo dat de reflectiestrepen vrij blijven."),
    "garage": ([("Werkplaats", "Praktisch en bestand tegen vuil werk.", ["overall", "werkbroek", "bodywarmer"]),
                ("Balie en klantcontact", "Netjes en representatief.", ["polo", "softshell"])],
               "In de werkplaats vallen vlekken minder op bij donkere kleuren, zoals zwart, antraciet of marine."),
    "schoonmaak": ([("Op locatie", "Herkenbaar bij de klant, comfortabel tijdens het werk.", ["polo", "werkbroek", "fleece"]),
                    ("Onderweg en buiten", "Wind- en waterafstotend.", ["softshell"])],
                   "Een logo op borst én rug maakt medewerkers bij de klant meteen herkenbaar."),
    "zorg": ([("Zorg en praktijk", "Fris, licht en makkelijk te wassen.", ["tuniek", "fleece"]),
              ("Kapper en salon", "Beschermend en verzorgd.", ["kapschort", "polo"])],
             "Een klein geborduurd logo op de borst oogt verzorgd en professioneel."),
    "transport": ([("Chauffeurs en koeriers", "Warm en herkenbaar onderweg.", ["softshell", "bodywarmer", "polo"]),
                   ("Magazijn", "Zichtbaar en vrij in beweging.", ["hesje", "hoodie"])],
                  "Met een groot logo op de rug zijn chauffeurs ook van een afstand herkenbaar."),
    "kantoor": ([("Kantoor en receptie", "Representatief, met een klein logo.", ["overhemd", "trui"]),
                 ("Winkel en showroom", "Herkenbaar en comfortabel voor de hele dag.", ["polo", "bodywarmer"])],
                "Op overhemden en blouses past een klein geborduurd logo op de borst het best."),
    "sport": ([("Wedstrijd", "Ademend, met clubnaam, naam of rugnummer.", ["sportshirt"]),
               ("Training en onderweg", "De hele club in dezelfde stijl.", ["trainingsjas", "hoodie", "tas"]),
               ("Supporters en vrijwilligers", "Herkenbaar langs de lijn.", ["cap"])],
              "Namen en rugnummers worden meestal bedrukt, het clublogo wordt vaak geborduurd."),
    "particulier": ([("Cadeau", "Persoonlijk, met een naam of datum.", ["handdoek", "tas"]),
                     ("Voor uzelf", "Uw eigen tekst of afbeelding op kleding.", ["hoodie", "tshirt"])],
                    "Een naam of datum op een handdoek of badjas is een persoonlijk cadeau."),
}


def aanbevolen(k, menu, P, kleding):
    functies, tip = PAKKETTEN[k]
    blokken = "".join(f'''<article class="functie">
        <h3>{f}</h3>
        <p>{uitleg}</p>
        <ul class="functie__items">{"".join(f'<li><a href="#{pk}">{kleding(P[pk][1], "functie__img")}<span>{P[pk][0]}</span></a></li>' for pk in prods)}</ul>
      </article>''' for f, uitleg, prods in functies)
    return f'''<section class="section section--wit section--compact" aria-labelledby="functie-kop">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Aanbevolen</span><h2 id="functie-kop">Kleding per functie</h2>
      <p class="intro">Elke rol vraagt iets anders. Dit is een goed vertrekpunt; we stemmen het samen met u af.</p></div>
    <div class="functies">{blokken}</div>
    <aside class="tipblok"><strong>Tip</strong><p>{tip}</p></aside>
  </div>
</section>'''


def cta_branche(k, menu):
    return f'''<section class="cta">
  <div class="wrap">
    <div>
      <h2>Kleding voor {menu.lower()} met uw logo?</h2>
      <p>Stel het zelf samen of vraag direct een vrijblijvende offerte aan.</p>
    </div>
    <div class="knoppen">
      <a class="knop knop--hoofd" href="offerte.html?branche={k}">Offerte voor {menu.lower()}</a>
      <a class="knop knop--goud cta__tweede" href="samenstellen.html">Zelf samenstellen</a>
    </div>
  </div>
</section>'''
