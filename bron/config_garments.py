"""Kledingtekeningen voor de samensteller: kleur via var(--stof), naden via var(--naad). Voor- en achterkant."""
from garments import TSHIRT, LANG, VEST

S, N = "var(--stof)", "var(--naad)"


def body(d):
    return f'<path d="{d}" fill="{S}" stroke="{N}" stroke-width="1" stroke-linejoin="round"/>'


def ln(d, w=1, kleur=N, dash=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{kleur}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{da}/>'


KRAAG_RITS = f'<path d="M50 20 L50 12 L70 12 L70 20 Q60 24 50 20 Z" fill="{S}" stroke="{N}" stroke-width="1"/>'
ACHTER_KRAAG = ln("M50 14 L70 14")

# id: naam, voorkant, achterkant (None = geen), kleuren, posities, maten
SHIRT_POS = [("borst-links", "Borst links", "voor", 68, 41, (6, 12, 9)), ("borst-midden", "Borst midden", "voor", 60, 40, (8, 22, 14)),
             ("mouw", "Mouw", "voor", 31, 40, (5, 9, 7)), ("rug", "Rug", "achter", 60, 54, (15, 30, 25))]
LANG_POS = [("borst-links", "Borst links", "voor", 68, 40, (6, 12, 9)), ("borst-midden", "Borst midden", "voor", 60, 42, (8, 22, 14)),
            ("mouw", "Mouw", "voor", 30, 52, (5, 9, 7)), ("rug", "Rug", "achter", 60, 54, (15, 30, 25))]
JAS_POS = [p for p in LANG_POS if p[0] != "borst-midden"]
VEST_POS = [("borst-links", "Borst links", "voor", 68, 40, (6, 12, 9)), ("rug", "Rug", "achter", 60, 56, (15, 30, 25))]

ALG = ["zwart", "antraciet", "marine", "bordeaux", "rood", "kobalt", "grijs", "wit"]
JAS = ["zwart", "antraciet", "marine", "bordeaux", "rood", "kobalt", "flessengroen"]

PRODUCTEN = [
    ("tshirt", "T-shirt", body(TSHIRT) + ln("M52 18 Q60 30 68 18"), body(TSHIRT) + ln("M52 18 Q60 22 68 18"), ALG + ["zand", "flessengroen"], SHIRT_POS, "kleding"),
    ("polo", "Polo", body(TSHIRT) + f'<path d="M52 18 L56 30 L60 24 L64 30 L68 18 Q60 22 52 18 Z" fill="{S}" stroke="{N}" stroke-width="1"/>' + ln("M60 24 L60 40")
     + f'<circle cx="60" cy="31" r="1" fill="{N}"/><circle cx="60" cy="37" r="1" fill="{N}"/>',
     body(TSHIRT) + ln("M52 18 L52 15 Q60 13 68 15 L68 18"), ALG + ["zand", "flessengroen"], SHIRT_POS, "kleding"),
    ("hoodie", "Hoodie", body(LANG) + f'<path d="M50 22 Q50 6 60 6 Q70 6 70 22 Q60 28 50 22 Z" fill="{S}" stroke="{N}" stroke-width="1"/>' + ln("M56 24 L55 36 M64 24 L65 36")
     + ln("M46 74 L74 74 L78 90 L42 90 Z"), body(LANG) + f'<path d="M48 22 Q48 4 60 4 Q72 4 72 22 Q60 26 48 22 Z" fill="{S}" stroke="{N}" stroke-width="1"/>',
     ALG + ["zand", "flessengroen"], [("borst-links", "Borst links", "voor", 68, 42, (6, 12, 9)), ("borst-midden", "Borst midden", "voor", 60, 50, (8, 22, 16)),
                                      ("mouw", "Mouw", "voor", 30, 52, (5, 9, 7)), ("rug", "Rug", "achter", 60, 56, (15, 30, 25))], "kleding"),
    ("sweater", "Sweater", body(LANG) + ln("M52 18 Q60 28 68 18") + ln("M40 96 L80 96"), body(LANG) + ln("M52 18 Q60 22 68 18") + ln("M40 96 L80 96"),
     ALG + ["zand"], LANG_POS, "kleding"),
    ("softshell", "Softshell jas", body(LANG) + KRAAG_RITS + ln("M60 18 L60 100") + ln("M44 66 L52 80 M76 66 L68 80"), body(LANG) + ACHTER_KRAAG,
     JAS, JAS_POS, "kleding"),
    ("werkjas", "Werkjas", body(LANG) + KRAAG_RITS + ln("M60 18 L60 100") + ln("M44 46 L56 46 L56 58 L44 58 Z M64 46 L76 46 L76 58 L64 58 Z")
     + ln("M40 84 L80 84", 3, "#A9A3A4"), body(LANG) + ACHTER_KRAAG + ln("M40 84 L80 84", 3, "#A9A3A4"), ["zwart", "antraciet", "marine", "rood", "kobalt"], JAS_POS, "kleding"),
    ("bodywarmer", "Bodywarmer", body(VEST) + KRAAG_RITS + ln("M60 18 L60 100") + "".join(ln(f"M36 {y} L84 {y}", .8) for y in (52, 64, 76, 88)),
     body(VEST) + ACHTER_KRAAG + "".join(ln(f"M36 {y} L84 {y}", .8) for y in (52, 64, 76, 88)), JAS, VEST_POS, "kleding"),
    ("fleece", "Fleecevest", body(LANG) + KRAAG_RITS + ln("M60 18 L60 100") + ln("M40 96 L80 96"), body(LANG) + ACHTER_KRAAG + ln("M40 96 L80 96"),
     JAS + ["grijs"], JAS_POS, "kleding"),
    ("hesje", "Veiligheidshesje", body(VEST) + ln("M35 70 L85 70 M35 82 L85 82", 4.5, "#B9B6B4") + ln("M46 24 L46 100 M74 24 L74 100", 3.5, "#B9B6B4") + ln("M60 30 L60 100"),
     body(VEST) + ln("M35 70 L85 70 M35 82 L85 82", 4.5, "#B9B6B4") + ln("M46 22 L46 100 M74 22 L74 100", 3.5, "#B9B6B4"),
     ["fluogeel", "fluooranje"], [("borst-links", "Borst links", "voor", 66, 50, (6, 10, 8)), ("rug", "Rug", "achter", 60, 48, (15, 25, 20))], "kleding"),
    ("koksbuis", "Koksbuis", body(LANG) + f'<path d="M50 20 L50 13 L70 13 L70 20 Q60 24 50 20 Z" fill="{S}" stroke="{N}" stroke-width="1"/>'
     + "".join(f'<circle cx="{x}" cy="{y}" r="1.5" fill="{N}"/>' for x in (53, 67) for y in (34, 48, 62, 76)),
     body(LANG) + ln("M50 15 L70 15"), ["wit", "zwart", "antraciet"], [("borst-links", "Borst links", "voor", 69, 29, (5, 10, 7)), ("mouw", "Mouw", "voor", 30, 52, (5, 9, 7)), ("rug", "Rug", "achter", 60, 50, (15, 25, 20))], "kleding"),
    ("overhemd", "Overhemd / blouse", body(LANG) + f'<path d="M52 18 L56 28 L60 22 L64 28 L68 18 Q60 22 52 18 Z" fill="{S}" stroke="{N}" stroke-width="1"/>' + ln("M60 22 L60 100")
     + "".join(f'<circle cx="60" cy="{y}" r="1" fill="{N}"/>' for y in (34, 48, 62, 76, 90)), body(LANG) + ln("M52 17 Q60 14 68 17"),
     ["wit", "lichtblauw", "zwart", "marine", "antraciet"], [("borst-links", "Borst links", "voor", 68, 40, (5, 9, 7)), ("mouw", "Mouw", "voor", 30, 52, (5, 9, 6))], "kleding"),
    ("tuniek", "Tuniek", body("M42 22 L52 18 L60 32 L68 18 L78 22 L94 36 L87 48 L80 44 L80 104 L40 104 L40 44 L33 48 L26 36 Z") + ln("M40 94 L44 104 M80 94 L76 104 M44 70 L56 70 L56 82 L44 82 Z"),
     body("M42 22 L52 18 Q60 22 68 18 L78 22 L94 36 L87 48 L80 44 L80 104 L40 104 L40 44 L33 48 L26 36 Z"), ["wit", "marine", "zwart", "bordeaux", "lichtblauw"],
     [("borst-links", "Borst links", "voor", 69, 42, (5, 10, 7)), ("rug", "Rug", "achter", 60, 54, (15, 25, 20))], "kleding"),
    ("schort", "Schort", ln("M48 24 Q60 4 72 24", 2.2, "#2A2829") + body("M48 24 L72 24 L72 42 Q86 46 88 54 L88 104 L32 104 L32 54 Q34 46 48 42 Z") + ln("M32 58 L18 66 M88 58 L102 66", 2.2, "#2A2829")
     + ln("M44 72 L76 72 L76 86 L44 86 Z"), None, ["zwart", "antraciet", "bordeaux", "wit", "zand", "marine"],
     [("borst", "Borst", "voor", 60, 34, (6, 14, 9)), ("onder", "Onder (zak)", "voor", 60, 79, (8, 25, 15))], "one"),
    ("cap", "Cap", body("M28 74 Q28 38 60 36 Q92 38 92 74 Z") + f'<path d="M60 74 L106 76 Q102 86 60 82 Z" fill="{S}" stroke="{N}" stroke-width="1"/>' + ln("M60 36 L60 74"),
     None, ALG, [("voorkant", "Voorkant", "voor", 48, 58, (5, 10, 7))], "one"),
    ("tas", "Tas", ln("M44 46 Q44 20 60 20 Q76 20 76 46", 3, "#2A2829") + body("M32 44 L88 44 L92 102 L28 102 Z"), None, ["zand", "zwart", "marine", "bordeaux", "wit"],
     [("midden", "Midden", "voor", 60, 72, (10, 25, 15))], "one"),
]

KLEUREN = {
    "zwart": ("Zwart", "#1F1E1F"), "antraciet": ("Antraciet", "#3B3E44"), "marine": ("Marine", "#1F2C44"), "bordeaux": ("Bordeaux", "#5E1424"),
    "rood": ("Rood", "#B3202A"), "kobalt": ("Kobaltblauw", "#2353A4"), "grijs": ("Grijs gemêleerd", "#A3A3A5"), "wit": ("Wit", "#FAFAF8"),
    "zand": ("Zand", "#D8CBB5"), "flessengroen": ("Flessengroen", "#1F4A35"), "lichtblauw": ("Lichtblauw", "#C9DAEE"),
    "fluogeel": ("Fluo geel", "#E3EA3A"), "fluooranje": ("Fluo oranje", "#F2742B"),
}

# welk configuratorproduct hoort bij een product uit het branchemenu
VAN_PRODUCT = {"koksbuis": "koksbuis", "schort": "schort", "polo": "polo", "cap": "cap", "werkjas": "werkjas", "hesje": "hesje", "hoodie": "hoodie",
               "tshirt": "tshirt", "bodywarmer": "bodywarmer", "softshell": "softshell", "fleece": "fleece", "tuniek": "tuniek", "kapschort": "schort",
               "overhemd": "overhemd", "trui": "sweater", "sportshirt": "tshirt", "trainingsjas": "fleece", "tas": "tas"}


def data():
    return {
        "producten": [{"id": i, "naam": n, "voor": v, "achter": a, "kleuren": k,
                       "posities": [{"id": p[0], "naam": p[1], "kant": p[2], "x": p[3], "y": p[4], "min": p[5][0], "max": p[5][1], "std": p[5][2]} for p in pos],
                       "maten": m} for i, n, v, a, k, pos, m in PRODUCTEN],
        "kleuren": {k: {"naam": v[0], "hex": v[1]} for k, v in KLEUREN.items()},
    }


# Realistischere tekeningen gebruiken (zelfde posities, nieuwe vormen)
import realistisch as _R
PRODUCTEN = [(i, n, _R.voorkant(i), _R.achterkant(i), k,
              [(("borst-links", "Borst links", "voor", 73, 37, (5, 10, 7)) if (i == "koksbuis" and p[0] == "borst-links") else p) for p in pos], m)
             for (i, n, v, a, k, pos, m) in PRODUCTEN]


# ---------- Logoplekken (meerdere te kiezen) ----------
def _p(i, naam, kant, x, y, maat):
    return (i, naam, kant, x, y, maat)

BL, BR, BM = (6, 12, 9), (6, 12, 9), (8, 22, 14)
MOUW, RUG, NEK = (5, 9, 7), (15, 30, 25), (5, 9, 6)
_SHIRT = [_p("borst-links", "Borst links", "voor", 68, 41, BL), _p("borst-rechts", "Borst rechts", "voor", 52, 41, BR),
          _p("borst-midden", "Borst midden", "voor", 60, 44, BM), _p("mouw-links", "Mouw links", "voor", 89, 40, MOUW),
          _p("mouw-rechts", "Mouw rechts", "voor", 31, 40, MOUW), _p("nek", "Nek", "achter", 60, 25, NEK), _p("rug", "Rug", "achter", 60, 56, RUG)]
_LANG = [_p("borst-links", "Borst links", "voor", 68, 40, BL), _p("borst-rechts", "Borst rechts", "voor", 52, 40, BR),
         _p("borst-midden", "Borst midden", "voor", 60, 44, BM), _p("mouw-links", "Mouw links", "voor", 90, 52, MOUW),
         _p("mouw-rechts", "Mouw rechts", "voor", 30, 52, MOUW), _p("nek", "Nek", "achter", 60, 25, NEK), _p("rug", "Rug", "achter", 60, 56, RUG)]
_JAS = [p for p in _LANG if p[0] != "borst-midden"]
_JAS = [(_p("nek", "Nek", "achter", 60, 22, NEK) if p[0] == "nek" else p) for p in _JAS]
_VEST = [_p("borst-links", "Borst links", "voor", 68, 40, BL), _p("borst-rechts", "Borst rechts", "voor", 52, 40, BR),
         _p("nek", "Nek", "achter", 60, 22, NEK), _p("rug", "Rug", "achter", 60, 56, RUG)]
_POS = {
    "tshirt": _SHIRT, "polo": [p for p in _SHIRT if p[0] != "borst-midden"] + [], "sweater": _LANG,
    "hoodie": [_p("borst-links", "Borst links", "voor", 68, 42, BL), _p("borst-rechts", "Borst rechts", "voor", 52, 42, BR),
               _p("borst-midden", "Borst midden", "voor", 60, 52, BM), _p("mouw-links", "Mouw links", "voor", 90, 52, MOUW),
               _p("mouw-rechts", "Mouw rechts", "voor", 30, 52, MOUW), _p("rug", "Rug", "achter", 60, 58, RUG)],
    "softshell": _JAS, "werkjas": [(_p("borst-links", "Borst links", "voor", 70, 39, BL) if p[0] == "borst-links" else
                                    _p("borst-rechts", "Borst rechts", "voor", 50, 39, BR) if p[0] == "borst-rechts" else p) for p in _JAS],
    "fleece": _JAS, "bodywarmer": _VEST,
    "hesje": [_p("borst-links", "Borst links", "voor", 65, 52, (6, 10, 8)), _p("borst-rechts", "Borst rechts", "voor", 55, 52, (6, 10, 8)),
              _p("rug", "Rug", "achter", 60, 50, (15, 25, 20))],
    "koksbuis": [_p("borst-links", "Borst links", "voor", 73, 37, (5, 10, 7)), _p("mouw-links", "Mouw links", "voor", 90, 52, MOUW),
                 _p("mouw-rechts", "Mouw rechts", "voor", 30, 52, MOUW), _p("rug", "Rug", "achter", 60, 52, (15, 25, 20))],
    "overhemd": [_p("borst-links", "Borst links (zak)", "voor", 69, 45, (5, 9, 7)), _p("borst-rechts", "Borst rechts", "voor", 51, 38, (5, 9, 7)),
                 _p("mouw-links", "Mouw links", "voor", 90, 52, MOUW), _p("mouw-rechts", "Mouw rechts", "voor", 30, 52, MOUW)],
    "tuniek": [_p("borst-links", "Borst links", "voor", 68, 34, (5, 10, 7)), _p("borst-rechts", "Borst rechts", "voor", 51, 36, (5, 10, 7)),
               _p("nek", "Nek", "achter", 60, 25, NEK), _p("rug", "Rug", "achter", 60, 56, (15, 25, 20))],
    "schort": [_p("borst", "Borst", "voor", 60, 33, (6, 14, 9)), _p("onder", "Onder (zak)", "voor", 60, 79, (8, 25, 15))],
    "cap": [_p("voorkant", "Voorkant", "voor", 46, 57, (5, 10, 7))],
    "tas": [_p("midden", "Midden", "voor", 60, 73, (10, 25, 15))],
}
PRODUCTEN = [(i, n, v, a, k, _POS.get(i, pos), m) for (i, n, v, a, k, pos, m) in PRODUCTEN]

# ---------- Productfoto's (vervangen de tekening als er een foto is) ----------
# per product -> kleur -> kant: bestand, afmeting, uitsnede (x, y, b, h), cm per pixel, logoplekken in pixels
FOTOS = {
    "polo": {"wit": {"voor": {"src": "img/producten/polo-wit-voor.png", "w": 650, "h": 515, "uitsnede": [110, 50, 400, 470], "cmpx": 0.25,
                              "pos": {"borst-links": [360, 178], "borst-rechts": [256, 178], "mouw-links": [444, 196], "mouw-rechts": [176, 196]}}}},
}
