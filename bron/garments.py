"""Lijntekeningen van kledingstukken (viewBox 0 0 120 120) met een klein logo op de borst."""

DONKER, BORDEAUX, WIT, GEEL, GRIJS, ZAND = "#2A2829", "#5E1424", "#FAF8F6", "#E6E04A", "#9C9596", "#D9CFC4"
LIJN = "rgba(0,0,0,.28)"

TSHIRT = "M42 22 L52 18 Q60 26 68 18 L78 22 L96 36 L88 50 L80 45 L80 100 L40 100 L40 45 L32 50 L24 36 Z"
LANG = "M42 22 L52 18 Q60 26 68 18 L78 22 L92 34 L100 86 L89 88 L80 52 L80 100 L40 100 L40 52 L31 88 L20 86 L28 34 Z"
VEST = "M44 20 L52 18 Q60 30 68 18 L76 20 Q78 34 86 42 L86 100 L34 100 L34 42 Q42 34 44 20 Z"
BROEK = "M38 18 L82 18 L86 102 L66 102 L60 50 L54 102 L34 102 Z"


def logo(x, y, kleur, s=1.0):
    r = 3.2 * s
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{kleur}" stroke-width="{1.6*s}"/>'
            f'<circle cx="{x+r*1.25}" cy="{y}" r="{r}" fill="none" stroke="{kleur}" stroke-width="{1.6*s}"/>')


def p(d, fill, stroke=LIJN, w=1.4):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'


def l(d, kleur=LIJN, w=1.4, dash=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{kleur}" stroke-width="{w}" stroke-linecap="round"{da}/>'


def _rits(top=22, kleur="rgba(255,255,255,.35)"):
    return l(f"M60 {top} L60 100", kleur, 1.4)


G = {}
G["tshirt"] = lambda: p(TSHIRT, DONKER) + l("M52 18 Q60 30 68 18", "rgba(255,255,255,.25)") + logo(66, 40, WIT)
G["polo"] = lambda: (p(TSHIRT, BORDEAUX) + p("M52 18 L56 30 L60 24 L64 30 L68 18 Q60 22 52 18 Z", BORDEAUX, "rgba(255,255,255,.4)")
                     + l("M60 24 L60 42", "rgba(255,255,255,.35)") + '<circle cx="60" cy="32" r="1.2" fill="#fff"/><circle cx="60" cy="38" r="1.2" fill="#fff"/>'
                     + logo(68, 44, WIT))
G["overhemd"] = lambda: (p(LANG, WIT) + p("M52 18 L56 28 L60 22 L64 28 L68 18 Q60 22 52 18 Z", WIT)
                         + l("M60 22 L60 100") + "".join(f'<circle cx="60" cy="{y}" r="1.1" fill="{GRIJS}"/>' for y in (34, 48, 62, 76, 90))
                         + logo(68, 42, BORDEAUX))
G["hoodie"] = lambda: (p(LANG, DONKER) + p("M50 22 Q50 6 60 6 Q70 6 70 22 Q60 28 50 22 Z", DONKER, "rgba(255,255,255,.25)")
                       + l("M56 24 L55 38 M64 24 L65 38", "rgba(255,255,255,.4)") + p("M46 72 L74 72 L78 88 L42 88 Z", "none", "rgba(255,255,255,.25)")
                       + logo(56, 52, WIT, 1.2))
G["werkjas"] = lambda: (p(LANG, DONKER) + p("M50 20 L50 12 L70 12 L70 20 Q60 24 50 20 Z", DONKER, "rgba(255,255,255,.3)") + _rits(18)
                        + p("M44 46 L56 46 L56 58 L44 58 Z", "none", "rgba(255,255,255,.3)") + p("M64 46 L76 46 L76 58 L64 58 Z", "none", "rgba(255,255,255,.3)")
                        + l("M40 84 L80 84", GRIJS, 3) + logo(68, 36, WIT))
G["softshell"] = lambda: (p(LANG, "#3B3E44") + p("M50 20 L50 11 L70 11 L70 20 Q60 24 50 20 Z", "#3B3E44", "rgba(255,255,255,.3)") + _rits(18)
                          + l("M44 66 L52 80 M76 66 L68 80", "rgba(255,255,255,.35)") + logo(68, 38, WIT))
G["fleece"] = lambda: (p(LANG, BORDEAUX) + p("M50 20 L50 12 L70 12 L70 20 Q60 24 50 20 Z", BORDEAUX, "rgba(255,255,255,.3)") + _rits(18)
                       + l("M40 96 L80 96 M24 84 L30 86 M96 84 L90 86", "rgba(255,255,255,.3)") + logo(68, 38, WIT))
G["bodywarmer"] = lambda: (p(VEST, DONKER) + p("M50 20 L50 12 L70 12 L70 20 Q60 26 50 20 Z", DONKER, "rgba(255,255,255,.3)") + _rits(18)
                           + "".join(l(f"M36 {y} L84 {y}", "rgba(255,255,255,.12)") for y in (52, 64, 76, 88)) + logo(68, 38, WIT))
G["hesje"] = lambda: (p(VEST, GEEL) + l("M35 70 L85 70 M35 82 L85 82", GRIJS, 4.5) + l("M46 24 L46 100 M74 24 L74 100", GRIJS, 3.5)
                      + l("M60 30 L60 100", "rgba(0,0,0,.18)") + logo(64, 52, DONKER, .9))
G["koksbuis"] = lambda: (p(LANG, WIT) + p("M50 20 L50 13 L70 13 L70 20 Q60 24 50 20 Z", WIT)
                         + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="{GRIJS}"/>' for x in (53, 67) for y in (34, 48, 62, 76))
                         + l("M48 22 L72 100", "rgba(0,0,0,.12)") + logo(70, 30, BORDEAUX, .9))
G["schort"] = lambda: (l("M48 24 Q60 4 72 24", DONKER, 2.2) + p("M48 24 L72 24 L72 42 Q86 46 88 54 L88 104 L32 104 L32 54 Q34 46 48 42 Z", DONKER)
                       + l("M32 58 L18 66 M88 58 L102 66", DONKER, 2.2) + p("M44 72 L76 72 L76 86 L44 86 Z", "none", "rgba(255,255,255,.25)")
                       + logo(57, 36, WIT))
G["koksbroek"] = lambda: (p(BROEK, DONKER) + "".join(l(f"M38 {y} L82 {y}", "rgba(255,255,255,.12)", 1) for y in range(28, 100, 8))
                          + "".join(l(f"M{x} 20 L{x} 46", "rgba(255,255,255,.12)", 1) for x in range(42, 82, 8))
                          + l("M38 26 L82 26", "rgba(255,255,255,.3)"))
G["werkbroek"] = lambda: (p(BROEK, "#3B3E44") + p("M37 64 L51 64 L50 78 L36 78 Z", "#2A2829") + p("M69 64 L83 64 L84 78 L70 78 Z", "#2A2829")
                          + l("M38 26 L82 26", "rgba(255,255,255,.3)") + p("M76 32 L84 32 L85 50 L77 50 Z", "none", "rgba(255,255,255,.3)")
                          + logo(44, 36, WIT, .9))
G["overall"] = lambda: (p("M44 14 L76 14 L76 40 L84 40 L88 104 L68 104 L60 64 L52 104 L32 104 L36 40 L44 40 Z", "#24364F")
                        + l("M44 14 L40 4 M76 14 L80 4", "#24364F", 3) + p("M50 22 L70 22 L70 34 L50 34 Z", "none", "rgba(255,255,255,.3)")
                        + l("M38 80 L50 80 M70 80 L82 80", GRIJS, 3) + logo(57, 28, WIT, .9))
G["tuniek"] = lambda: (p("M42 22 L52 18 L60 32 L68 18 L78 22 L94 36 L87 48 L80 44 L80 104 L40 104 L40 44 L33 48 L26 36 Z", WIT)
                       + l("M40 94 L44 104 M80 94 L76 104") + p("M44 70 L56 70 L56 82 L44 82 Z", "none") + logo(68, 42, BORDEAUX))
G["cap"] = lambda: (p("M28 74 Q28 38 60 36 Q92 38 92 74 Z", BORDEAUX) + p("M60 74 L106 76 Q102 86 60 82 Z", BORDEAUX, "rgba(0,0,0,.35)")
                    + l("M60 36 L60 74", "rgba(255,255,255,.2)") + '<circle cx="60" cy="37" r="2" fill="#fff" opacity=".5"/>' + logo(48, 58, WIT, 1.1))
G["tas"] = lambda: (l("M44 46 Q44 20 60 20 Q76 20 76 46", DONKER, 3) + p("M32 44 L88 44 L92 102 L28 102 Z", ZAND) + logo(56, 72, BORDEAUX, 1.6))
G["handdoek"] = lambda: (p("M26 74 L94 74 L94 96 L26 96 Z", WIT) + p("M30 56 L90 56 L90 74 L30 74 Z", ZAND) + p("M34 38 L86 38 L86 56 L34 56 Z", BORDEAUX)
                         + l("M26 90 L94 90", "rgba(0,0,0,.12)", 2) + logo(54, 85, BORDEAUX, .9))


# Realistische tekeningen voor branchepagina's en menu: (kleur, logo-x, logo-y)
import realistisch as _R
import itertools
_TELLER = itertools.count(1)
_KLEUR = {"oranje": "#F26A1B", "zwart": "#1F1E1F", "antraciet": "#3B3E44", "marine": "#1F2C44", "bordeaux": "#5E1424", "wit": "#FAFAF8", "fluogeel": "#E3EA3A", "zand": "#D8CBB5"}
_STIJL = {"tshirt": ("zwart", 68, 41), "polo": ("bordeaux", 68, 41), "overhemd": ("wit", 69, 35), "hoodie": ("antraciet", 60, 50),
          "werkjas": ("oranje", 70, 38), "softshell": ("antraciet", 68, 36), "fleece": ("bordeaux", 68, 38), "bodywarmer": ("zwart", 68, 40),
          "hesje": ("fluogeel", 64, 54), "koksbuis": ("wit", 73, 37), "schort": ("zwart", 60, 33), "koksbroek": ("zwart", None, None),
          "werkbroek": ("antraciet", 44, 34), "korte_werkbroek": ("antraciet", 41, 58), "overall": ("marine", 60, 27), "tuniek": ("wit", 68, 36), "cap": ("bordeaux", 47, 57),
          "tas": ("zand", 60, 74), "handdoek": ("bordeaux", 60, 46)}


def _licht(hexk):
    h = hexk.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (0.299 * r + 0.587 * g + 0.114 * b) > 150


def svg(naam, cls="kledingtekening"):
    kleur, x, y = _STIJL[naam]
    hexk = _KLEUR[kleur]
    naadk = "rgba(0,0,0,.35)" if _licht(hexk) else "rgba(255,255,255,.35)"
    mark = logo(x, y, BORDEAUX if _licht(hexk) else WIT, .8) if x else ""
    return (f'<svg class="{cls}" viewBox="0 0 120 120" aria-hidden="true" focusable="false" style="--stof:{hexk};--naad:{naadk}">'
            f'{_R.voorkant(naam).replace("rl-", f"rl{next(_TELLER)}-")}{mark}</svg>')


# Kledingtekeningen als losse bestanden (V2): de browser laadt elk bestand één keer
BESTANDEN_MAP = "img/kleding"


def bestand_svg(naam):
    """Inhoud van img/kleding/<naam>.svg: zelfde tekening als svg(), als zelfstandig bestand."""
    kleur, x, y = _STIJL[naam]
    hexk = _KLEUR[kleur]
    naadk = "rgba(0,0,0,.35)" if _licht(hexk) else "rgba(255,255,255,.35)"
    mark = logo(x, y, BORDEAUX if _licht(hexk) else WIT, .8) if x else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" '
            f'style="--stof:{hexk};--naad:{naadk}">{_R.voorkant(naam)}{mark}</svg>\n')


def img(naam, cls="kledingtekening"):
    return f'<img class="{cls}" src="{BESTANDEN_MAP}/{naam}.svg" alt="" width="120" height="120" loading="lazy" decoding="async">'


def bestand_svg_achter(naam):
    """Achterkant (zonder logo) als los bestand, alleen voor kleding met een achterkant."""
    kleur, _, _ = _STIJL[naam]
    hexk = _KLEUR[kleur]
    naadk = "rgba(0,0,0,.35)" if _licht(hexk) else "rgba(255,255,255,.35)"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" '
            f'style="--stof:{hexk};--naad:{naadk}">{_R.achterkant(naam)}</svg>\n')


def heeft_achterkant(naam):
    return naam in _R.VOOR_ACHTER and _R.VOOR_ACHTER[naam]()[1] is not None
