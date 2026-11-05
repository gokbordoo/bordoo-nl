"""SEO V2: canonical, Open Graph, structured data, sitemap en robots.txt."""
import json
from datetime import date

SITE = "https://bordoo.nl/"
NIET_INDEXEREN = {"bedankt.html", "404.html"}


def url(fn):
    return SITE if fn == "index.html" else SITE + fn


def organisatie(tel_nummer, mail):
    return {"@context": "https://schema.org", "@type": "Organization", "name": "Bordoo", "url": SITE,
            "logo": SITE + "img/icoon.png", "email": mail, "telephone": tel_nummer,
            "description": "Bedrijfskleding met uw logo, geborduurd of bedrukt.",
            "founder": {"@type": "Person", "name": "Gök Karakas"},
            "contactPoint": {"@type": "ContactPoint", "telephone": tel_nummer, "email": mail, "contactType": "customer service",
                             "availableLanguage": "Dutch"}}


def kruimel_data(stappen):
    """stappen: [(bestand, naam), ...] zoals in het kruimelpad."""
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i, "name": n.replace("&amp;", "&"), "item": url(f)}
                                for i, (f, n) in enumerate(stappen, 1)]}


def faq_data(groepen):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": v, "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for _, vragen in groepen for v, a in vragen]}


def kop_extra(fn, title, desc, data):
    robots = '<meta name="robots" content="noindex">\n' if fn in NIET_INDEXEREN else ""
    ld = "".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>\n' for d in data)
    return (f'{robots}<link rel="canonical" href="{url(fn)}">\n'
            f'<meta name="theme-color" content="#5E1424">\n'
            f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="Bordoo">\n<meta property="og:locale" content="nl_NL">\n'
            f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n'
            f'<meta property="og:url" content="{url(fn)}">\n<meta property="og:image" content="{SITE}img/delen.jpg">\n'
            f'<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n{ld}')


def sitemap(bestanden):
    vandaag = date.today().isoformat()
    regels = "".join(f"  <url><loc>{url(f)}</loc><lastmod>{vandaag}</lastmod></url>\n"
                     for f in sorted(bestanden, key=lambda f: (f != "index.html", f)) if f not in NIET_INDEXEREN)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{regels}</urlset>\n'


ROBOTS = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n"
