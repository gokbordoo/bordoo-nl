# Bordoo website

De website van [bordoo.nl](https://bordoo.nl): bedrijfskleding borduren en bedrukken.

## Mappen
- `site/` – de website zelf. Netlify zet deze map online (zie `netlify.toml`).
- `bron/` – scripts waarmee de pagina's in `site/` worden gemaakt.

## Pagina's opnieuw maken
```bash
python3 bron/build2.py site
```

- `bron/build2.py` – alle pagina's, menu, branches en producten
- `bron/samensteller2.py` – de pagina "Zelf samenstellen"
- `bron/samensteller.py` – de homepage
- `bron/config_garments.py` – producten, kleuren, logoplekken en productfoto's (`FOTOS`)
- `bron/realistisch.py` – de kledingtekeningen
- `bron/garments.py` – kleine tekeningen voor menu en branchepagina's

De opmaak staat in `site/css/style.css`.

## Productfoto's toevoegen
Zet de foto in `site/img/producten/` en voeg hem toe aan `FOTOS` in `bron/config_garments.py`, met de uitsnede, cm per pixel en de logoplekken in pixels.

## Online zetten
Elke wijziging op de `main`-branch zet Netlify automatisch online.
