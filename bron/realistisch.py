"""Realistischere kledingtekeningen (viewBox 0 0 120 120): natuurlijke vorm, schaduw, plooien, stiksels.
Kleur via var(--stof); naden via var(--naad). Dunne lijnen schalen niet mee bij inzoomen."""

S, N = "var(--stof)", "var(--naad)"

DEFS = ('<defs>'
        '<linearGradient id="rl-h" x1="0" x2="1" y1="0" y2="0">'
        '<stop offset="0" stop-color="#000" stop-opacity=".26"/><stop offset=".16" stop-color="#000" stop-opacity="0"/>'
        '<stop offset=".45" stop-color="#fff" stop-opacity=".07"/><stop offset=".84" stop-color="#000" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#000" stop-opacity=".3"/></linearGradient>'
        '<linearGradient id="rl-v" x1="0" x2="0" y1="0" y2="1">'
        '<stop offset="0" stop-color="#fff" stop-opacity=".10"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#000" stop-opacity=".14"/></linearGradient>'
        '<linearGradient id="rl-puf" x1="0" x2="0" y1="0" y2="1">'
        '<stop offset="0" stop-color="#000" stop-opacity=".22"/><stop offset=".3" stop-color="#fff" stop-opacity=".10"/>'
        '<stop offset=".7" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".24"/></linearGradient>'
        '<linearGradient id="rl-refl" x1="0" x2="0" y1="0" y2="1">'
        '<stop offset="0" stop-color="#E9E9EA"/><stop offset=".5" stop-color="#B7B8BC"/><stop offset="1" stop-color="#D4D5D8"/></linearGradient>'
        '<filter id="rl-zacht" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation=".9"/></filter>'
        '</defs>')

NS = ' vector-effect="non-scaling-stroke"'


def lichaam(d):
    """Basisvorm met kleur, schaduw van opzij en van boven, en een dunne omlijning."""
    return (f'<path d="{d}" fill="{S}"/><path d="{d}" fill="url(#rl-h)"/><path d="{d}" fill="url(#rl-v)"/>'
            f'<path d="{d}" fill="none" stroke="{N}" stroke-width="1.1" stroke-linejoin="round"{NS}/>')


def deel(d, extra=""):
    """Los onderdeel (kraag, zak) in dezelfde stof, met omlijning."""
    return (f'<path d="{d}" fill="{S}"/><path d="{d}" fill="url(#rl-v)"/>'
            f'<path d="{d}" fill="none" stroke="{N}" stroke-width="1" stroke-linejoin="round"{NS}/>{extra}')


def naad(d, w=1):
    return f'<path d="{d}" fill="none" stroke="{N}" stroke-width="{w}" stroke-linecap="round"{NS}/>'


def stiksel(d):
    return f'<path d="{d}" fill="none" stroke="{N}" stroke-width=".8" stroke-dasharray="2 1.6" stroke-linecap="round"{NS}/>'


def plooien(*ds, licht=()):
    out = "".join(f'<path d="{d}" fill="none" stroke="#000" stroke-opacity=".22" stroke-width="1.6" stroke-linecap="round" filter="url(#rl-zacht)"/>' for d in ds)
    out += "".join(f'<path d="{d}" fill="none" stroke="#fff" stroke-opacity=".16" stroke-width="1.6" stroke-linecap="round" filter="url(#rl-zacht)"/>' for d in licht)
    return out


def knoop(x, y, r=1.25):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#EDEAE6" stroke="rgba(0,0,0,.35)" stroke-width=".5"{NS}/>'
            f'<circle cx="{x - r * .3}" cy="{y}" r="{r * .16}" fill="rgba(0,0,0,.45)"/><circle cx="{x + r * .3}" cy="{y}" r="{r * .16}" fill="rgba(0,0,0,.45)"/>')


def rits(y1, y2, x=60):
    return (f'<path d="M{x} {y1} L{x} {y2}" stroke="rgba(0,0,0,.45)" stroke-width="1.5"/>'
            f'<path d="M{x} {y1} L{x} {y2}" stroke="#C9C6C2" stroke-width=".9" stroke-dasharray=".5 .5"/>'
            f'<rect x="{x - 1.1}" y="{y1 + 1}" width="2.2" height="4.2" rx=".8" fill="#B9B6B2" stroke="rgba(0,0,0,.4)" stroke-width=".4"/>')


# ---------- silhouetten ----------
T = ("M44 21 Q49 18 53 16 Q60 23 67 16 Q71 18 76 21 L92 30 Q95 32 94 35 L88 49 Q87 51 84 50 L80 48 Q80.5 74 81 99 "
     "Q81 102 78 102 L42 102 Q39 102 39 99 Q39.5 74 40 48 L36 50 Q33 51 32 49 L26 35 Q25 32 28 30 Z")
T_ACHTER = T.replace("Q60 23 67 16", "Q60 19 67 16")
L = ("M44 21 Q49 18 53 16 Q60 23 67 16 Q71 18 76 21 Q85 25 89 33 Q93 52 98 84 Q98.5 87 96 87.5 L90 88.5 Q88 89 87.5 86.5 "
     "L82 56 Q81.5 78 81 99 Q81 102 78 102 L42 102 Q39 102 39 99 Q38.5 78 38 56 L32.5 86.5 Q32 89 30 88.5 L24 87.5 "
     "Q21.5 87 22 84 Q27 52 31 33 Q35 25 44 21 Z")
L_ACHTER = L.replace("Q60 23 67 16", "Q60 19 67 16")
V = ("M46 20 Q50 18 53 16 Q60 23 67 16 Q70 18 74 20 Q76 32 85 41 Q86 70 85 99 Q85 102 82 102 L38 102 Q35 102 35 99 "
     "Q34 70 35 41 Q44 32 46 20 Z")
V_ACHTER = V.replace("Q60 23 67 16", "Q60 19 67 16")

PLOOI_T = plooien("M47 58 Q45 75 47 93", "M73 57 Q75 74 72 91", "M41 50 Q45 55 44 63", "M79 50 Q75 55 76 63", licht=("M55 50 Q57 70 55 90",))
PLOOI_L = plooien("M47 60 Q45 76 47 93", "M73 59 Q75 75 72 91", "M33 45 Q30 60 30 78", "M87 45 Q90 60 90 78", "M40 56 Q44 60 43 68",
                  licht=("M55 50 Q57 70 55 90", "M26 60 Q25 70 25 80"))
PLOOI_V = plooien("M47 60 Q45 76 47 93", "M73 59 Q75 75 72 91", licht=("M55 50 Q57 70 55 90",))
MOUW_T = stiksel("M28.4 34.2 L34.2 47.6") + stiksel("M91.6 34.2 L85.8 47.6")
ZOOM_T = stiksel("M40 98.5 L80 98.5")
BOORD_L = naad("M23.2 82.6 L31.4 83.8", .9) + naad("M96.8 82.6 L88.6 83.8", .9) + naad("M39 96 L81 96", .9)


def ribkraag_rond(achter=False):
    d = "M53 16 Q60 19 67 16" if achter else "M53 16 Q60 23 67 16"
    d2 = "M54.5 15.6 Q60 18 65.5 15.6 L65.8 17 Q60 20.5 54.2 17 Z" if achter else "M54 15.4 Q60 21.6 66 15.4 L66.6 17.6 Q60 25.6 53.4 17.6 Z"
    return deel(d2) + naad(d, .9)


def polokraag(achter=False):
    if achter:
        return deel("M52.5 15.8 Q60 12.5 67.5 15.8 L68 19.5 Q60 16.8 52 19.5 Z") + stiksel("M52.6 18.4 Q60 15.8 67.4 18.4")
    band = deel("M53 16 Q60 12.8 67 16 L67 17.6 Q60 15.2 53 17.6 Z")
    links = deel("M53 16 Q51.6 21.5 49.6 25 Q53.5 28.5 57.6 30.4 L60 26 Q56 22 53 16 Z", naad("M50.6 24.6 Q54 27.6 57.4 29.2", .7))
    rechts = deel("M67 16 Q68.4 21.5 70.4 25 Q66.5 28.5 62.4 30.4 L60 26 Q64 22 67 16 Z", naad("M69.4 24.6 Q66 27.6 62.6 29.2", .7))
    knoopsluiting = deel("M57.6 25.2 L62.4 25.2 L62.4 42 L57.6 42 Z") + stiksel("M58.4 42 L61.6 42") + knoop(60, 31.5) + knoop(60, 37.2)
    return band + knoopsluiting + links + rechts


def opstaande_kraag(achter=False):
    if achter:
        return deel("M51 17 L51 10.5 Q60 9 69 10.5 L69 17 Q60 19.5 51 17 Z") + stiksel("M51.5 12.2 Q60 10.8 68.5 12.2")
    return deel("M51 17 L51 10.5 Q60 9 69 10.5 L69 17 Q60 20.5 51 17 Z") + stiksel("M51.6 12.4 Q60 11 68.4 12.4")


def capuchon(achter=False):
    if achter:
        return deel("M47 22 Q45 6 60 3.5 Q75 6 73 22 Q60 26 47 22 Z") + naad("M60 4 L60 24", .8)
    return (deel("M49 22 Q47 7 60 5 Q73 7 71 22 Q66 19 60 25 Q54 19 49 22 Z")
            + deel("M52.5 20 Q55 12 60 11.5 Q65 12 67.5 20 Q63.5 19.5 60 24 Q56.5 19.5 52.5 20 Z").replace(S, "rgba(0,0,0,.25)", 1)
            + naad("M56.5 24.5 L55.6 38", 1) + naad("M63.5 24.5 L64.4 38", 1)
            + '<circle cx="55.6" cy="38.6" r=".8" fill="#C9C6C2"/><circle cx="64.4" cy="38.6" r=".8" fill="#C9C6C2"/>')


def buidelzak():
    return deel("M45 72 L75 72 Q78 80 79 90 L41 90 Q42 80 45 72 Z") + naad("M45 72 Q43 80 42.2 89", .8) + naad("M75 72 Q77 80 77.8 89", .8)


def doorgestikt(ys, x1=35, x2=85, sil=V):
    """Bodywarmer-vakken: bolle banen tussen doorgestikte lijnen."""
    out = f'<clipPath id="rl-clip-v"><path d="{sil}"/></clipPath><g clip-path="url(#rl-clip-v)">'
    for a, b in zip(ys, ys[1:]):
        out += f'<rect x="{x1}" y="{a}" width="{x2 - x1}" height="{b - a}" fill="url(#rl-puf)"/>'
    out += "</g>"
    out += "".join(stiksel(f"M{x1 + 1} {y} Q60 {y + 1.4} {x2 - 1} {y}") for y in ys[1:-1])
    return out


# ---------- producten: (voorkant, achterkant) ----------
def polo():
    v = DEFS + lichaam(T) + PLOOI_T + MOUW_T + ZOOM_T + polokraag() + naad("M40.6 94.5 L40.4 102", .8) + naad("M79.4 94.5 L79.6 102", .8)
    a = DEFS + lichaam(T_ACHTER) + PLOOI_T + MOUW_T + ZOOM_T + polokraag(True)
    return v, a


def tshirt():
    return (DEFS + lichaam(T) + PLOOI_T + MOUW_T + ZOOM_T + ribkraag_rond(),
            DEFS + lichaam(T_ACHTER) + PLOOI_T + MOUW_T + ZOOM_T + ribkraag_rond(True))


def sweater():
    return (DEFS + lichaam(L) + PLOOI_L + BOORD_L + ribkraag_rond(),
            DEFS + lichaam(L_ACHTER) + PLOOI_L + BOORD_L + ribkraag_rond(True))


def hoodie():
    return (DEFS + lichaam(L) + PLOOI_L + BOORD_L + buidelzak() + capuchon(),
            DEFS + lichaam(L_ACHTER) + PLOOI_L + BOORD_L + capuchon(True))


def softshell():
    zakken = naad("M43 66 L47.5 82", 1.2) + naad("M77 66 L72.5 82", 1.2)
    panelen = stiksel("M31.5 38 Q45 44 57 41") + stiksel("M88.5 38 Q75 44 63 41")
    return (DEFS + lichaam(L) + PLOOI_L + naad("M23.2 82.6 L31.4 83.8", .9) + naad("M96.8 82.6 L88.6 83.8", .9) + panelen + zakken + stiksel("M39.5 98.5 L80.5 98.5")
            + rits(12, 102) + opstaande_kraag(),
            DEFS + lichaam(L_ACHTER) + PLOOI_L + stiksel("M31.5 38 Q60 46 88.5 38") + stiksel("M39.5 98.5 L80.5 98.5") + opstaande_kraag(True))


def fleece():
    return (DEFS + lichaam(L) + PLOOI_L + BOORD_L + naad("M43 66 L46.5 80", 1.1) + naad("M77 66 L73.5 80", 1.1) + rits(12, 96) + opstaande_kraag(),
            DEFS + lichaam(L_ACHTER) + PLOOI_L + BOORD_L + opstaande_kraag(True))


def werkjas():
    refl = '<path d="M38.6 82 L81.4 82 L81.5 86 L38.5 86 Z" fill="url(#rl-refl)" stroke="rgba(0,0,0,.25)" stroke-width=".5"/>'
    refl_mouw = '<path d="M24.6 74 L33.6 75.3 L33 79 L24 77.6 Z M95.4 74 L86.4 75.3 L87 79 L96 77.6 Z" fill="url(#rl-refl)" stroke="rgba(0,0,0,.25)" stroke-width=".5"/>'
    zak = lambda x: deel(f"M{x} 46 L{x + 12} 46 L{x + 12} 58 Q{x + 6} 59 {x} 58 Z") + deel(f"M{x - .5} 44 L{x + 12.5} 44 L{x + 12.5} 49 L{x - .5} 49 Z", stiksel(f"M{x} 47.6 L{x + 12} 47.6"))
    return (DEFS + lichaam(L) + PLOOI_L + BOORD_L + zak(44) + zak(64) + refl + refl_mouw + rits(12, 102) + opstaande_kraag(),
            DEFS + lichaam(L_ACHTER) + PLOOI_L + BOORD_L + refl + refl_mouw + stiksel("M31.5 38 Q60 46 88.5 38") + opstaande_kraag(True))


def bodywarmer():
    ys = [36, 47, 58, 69, 80, 91, 102]
    zakken = naad("M40 70 L43.5 84", 1.2) + naad("M80 70 L76.5 84", 1.2)
    return (DEFS + lichaam(V) + doorgestikt(ys) + PLOOI_V + zakken + rits(12, 102) + opstaande_kraag(),
            DEFS + lichaam(V_ACHTER) + doorgestikt(ys, sil=V_ACHTER) + PLOOI_V + opstaande_kraag(True))


def hesje():
    band = lambda y: f'<path d="M35 {y} L85 {y} L85 {y + 4.6} L35 {y + 4.6} Z" fill="url(#rl-refl)" stroke="rgba(0,0,0,.25)" stroke-width=".5"/>'
    schouder = '<path d="M46.5 21 L49.6 19.6 L49.6 102 L46.5 102 Z M73.5 21 L70.4 19.6 L70.4 102 L73.5 102 Z" fill="url(#rl-refl)" stroke="rgba(0,0,0,.25)" stroke-width=".5"/>'
    clip = f'<clipPath id="rl-clip-h"><path d="{V}"/></clipPath>'
    return (DEFS + lichaam(V) + clip + f'<g clip-path="url(#rl-clip-h)">{schouder}{band(68)}{band(82)}</g>' + naad("M60 23 L60 102", .9) + stiksel("M36 99 L84 99"),
            DEFS + lichaam(V_ACHTER) + clip + f'<g clip-path="url(#rl-clip-h)">{schouder.replace("19.6", "18.6")}{band(68)}{band(82)}</g>' + stiksel("M36 99 L84 99"))


def koksbuis():
    kraag = deel("M51 17 L51 11 Q60 9.5 69 11 L69 17 Q60 20.5 51 17 Z") + stiksel("M51.6 13 Q60 11.6 68.4 13")
    knopen = "".join(f'<circle cx="{x}" cy="{y}" r="1.35" fill="#EDEAE6" stroke="rgba(0,0,0,.4)" stroke-width=".5"{NS}/>' for x in (52.5, 67.5) for y in (30, 44, 58, 72))
    return (DEFS + lichaam(L) + PLOOI_L + naad("M63 18.5 Q68 50 66.5 102", 1) + stiksel("M64.6 19 Q69.6 50 68.1 102") + BOORD_L.replace(naad("M39 96 L81 96", .9), "")
            + stiksel("M39.5 98.5 L80.5 98.5") + knopen + kraag,
            DEFS + lichaam(L_ACHTER) + PLOOI_L + stiksel("M39.5 98.5 L80.5 98.5") + deel("M51 17 L51 11 Q60 9.5 69 11 L69 17 Q60 19 51 17 Z"))


def overhemd():
    kraag = (deel("M53 16 Q60 13 67 16 L67 18 Q60 15.6 53 18 Z")
             + deel("M53 16 L50.4 25 L58.2 24.2 L60 20.5 Q56 19.5 53 16 Z") + deel("M67 16 L69.6 25 L61.8 24.2 L60 20.5 Q64 19.5 67 16 Z"))
    knopen = "".join(knoop(61.6, y, 1) for y in (27, 39, 51, 63, 75, 87))
    zak = deel("M64 40 L74 40 L74 51 Q69 52.5 64 51 Z")
    return (DEFS + lichaam(L) + PLOOI_L + naad("M60.2 20.5 L60.2 102", .9) + naad("M63 22 L63 102", .7) + knopen + zak + BOORD_L.replace(naad("M39 96 L81 96", .9), "")
            + stiksel("M40 99 Q60 101 80 99") + kraag,
            DEFS + lichaam(L_ACHTER) + PLOOI_L + stiksel("M37 30 Q60 34 83 30") + deel("M53 16 Q60 13 67 16 L67 18.5 Q60 16 53 18.5 Z"))


TUNIEK = ("M44 21 Q49 18 53 16 L60 30 L67 16 Q71 18 76 21 L92 30 Q95 32 94 35 L88 49 Q87 51 84 50 L80 48 Q80.5 76 81 101 "
          "Q81 104 78 104 L42 104 Q39 104 39 101 Q39.5 76 40 48 L36 50 Q33 51 32 49 L26 35 Q25 32 28 30 Z")


def tuniek():
    zak = deel("M44 70 L56 70 L56 82 Q50 83.5 44 82 Z") + deel("M64 40 L73 40 L73 49 Q68.5 50 64 49 Z")
    return (DEFS + lichaam(TUNIEK) + PLOOI_T + MOUW_T + naad("M53 16 L60 30 L67 16", .9) + stiksel("M54.4 17 L60 28 L65.6 17") + zak
            + naad("M40.4 95 L40.2 104", .9) + naad("M79.6 95 L79.8 104", .9) + stiksel("M40 100.5 L80 100.5"),
            DEFS + lichaam(TUNIEK.replace("L60 30 L67 16", "Q60 19 67 16")) + PLOOI_T + MOUW_T + stiksel("M40 100.5 L80 100.5"))


SCHORT = "M48 24 L72 24 L72 40 Q73 44 84 47 Q89 49 89 54 L88.5 101 Q88.5 104 85.5 104 L34.5 104 Q31.5 104 31.5 101 L31 54 Q31 49 36 47 Q47 44 48 40 Z"


def schort():
    band = '<path d="M48 24 Q49 9 60 6 Q71 9 72 24" fill="none" stroke="#2A2829" stroke-width="2.2" stroke-linecap="round"/>'
    linten = '<path d="M31.5 56 Q22 60 14 70 M88.5 56 Q98 60 106 70" fill="none" stroke="#2A2829" stroke-width="2" stroke-linecap="round"/>'
    zak = deel("M42 70 L78 70 L78 86 Q60 88 42 86 Z", naad("M60 70 L60 87", .8))
    return (DEFS + band + linten + lichaam(SCHORT) + plooien("M45 60 Q43 80 45 100", "M75 60 Q77 80 75 100", licht=("M58 50 Q60 75 58 100",))
            + stiksel("M49.2 25.5 L70.8 25.5") + stiksel("M33 102.4 L87 102.4") + zak, None)


def cap():
    kroon = "M27 76 Q26 44 60 37 Q94 44 93 76 Q60 72 27 76 Z"
    klep = "M58 74 Q86 70 107 76 Q106 85 96 86 Q76 83 58 81 Z"
    return (DEFS + lichaam(kroon) + naad("M60 37.5 Q57 56 56 74.5", .9) + naad("M60 37.5 Q73 52 79 73", .9) + naad("M60 37.5 Q45 52 39 74.5", .9)
            + stiksel("M28.5 72 Q60 68.5 91.5 72") + '<circle cx="60" cy="38.4" r="2" fill="var(--stof)" stroke="var(--naad)" stroke-width=".8"' + NS + '/>'
            + f'<path d="{klep}" fill="{S}"/><path d="{klep}" fill="#000" fill-opacity=".22"/><path d="{klep}" fill="none" stroke="{N}" stroke-width="1"{NS}/>'
            + stiksel("M61 78.5 Q84 75 103 79.5") + plooien("M34 50 Q38 44 46 41", licht=("M62 44 Q70 47 74 54",)), None)


def tas():
    zak = "M30 44 L90 44 L93 100 Q93 103 90 103 L30 103 Q27 103 27 100 Z"
    hengsels = '<path d="M42 45 Q41 18 60 17 Q79 18 78 45" fill="none" stroke="var(--stof)" stroke-width="3.2"/><path d="M42 45 Q41 18 60 17 Q79 18 78 45" fill="none" stroke="rgba(0,0,0,.25)" stroke-width="3.2"/>'
    return (DEFS + hengsels + lichaam(zak) + stiksel("M30.4 48 L89.6 48") + plooien("M40 55 Q38 80 40 100", "M80 55 Q82 80 80 100"), None)


# Branchetekeningen die niet in de samensteller zitten
BROEK = "M38 16 L82 16 L84.5 99 Q84.5 102 82 102 L67 102 Q65 102 64.8 99.5 L60.6 48 L59.4 48 L55.2 99.5 Q55 102 53 102 L38 102 Q35.5 102 35.5 99 Z"


def broek(kniestukken=False, ruit=False):
    out = DEFS + lichaam(BROEK) + naad("M38 22 L82 22", .9) + naad("M60 22 L60 46", .9) + plooien("M45 30 Q44 60 46 95", "M75 30 Q76 60 74 95")
    if ruit:
        out += f'<clipPath id="rl-clip-b"><path d="{BROEK}"/></clipPath><g clip-path="url(#rl-clip-b)" opacity=".18">' + "".join(
            f'<path d="M30 {y} L90 {y}" stroke="#fff" stroke-width=".8"/>' for y in range(20, 104, 4)) + "".join(
            f'<path d="M{x} 16 L{x} 104" stroke="#fff" stroke-width=".8"/>' for x in range(34, 88, 4)) + "</g>"
    if kniestukken:
        out += deel("M37 62 L52.5 62 L52 76 L36.6 76 Z", stiksel("M37.6 63.5 L51.9 63.5")) + deel("M67.5 62 L83 62 L83.4 76 L68 76 Z", stiksel("M68.1 63.5 L82.4 63.5"))
        out += deel("M74 30 L83 30 L83.3 48 L74.4 48 Z")
    return out


def overall():
    sil = "M44 13 L76 13 L76 38 L83 38 L85 99 Q85 102 82 102 L67 102 Q65 102 64.8 99.5 L60.6 62 L59.4 62 L55.2 99.5 Q55 102 53 102 L38 102 Q35 102 35 99 L37 38 L44 38 Z"
    return (DEFS + '<path d="M45 14 L41 3 M75 14 L79 3" stroke="var(--stof)" stroke-width="3.4" stroke-linecap="round"/><path d="M45 14 L41 3 M75 14 L79 3" stroke="rgba(0,0,0,.25)" stroke-width="3.4" stroke-linecap="round"/>'
            + lichaam(sil) + deel("M50 20 L70 20 L70 33 Q60 34.5 50 33 Z") + naad("M37 40 L83 40", .9)
            + '<path d="M37 80 L52 80 L51.6 84 L36.8 84 Z M68 80 L83 80 L83.2 84 L68.4 84 Z" fill="url(#rl-refl)"/>' + plooien("M45 45 Q44 70 46 95", "M75 45 Q76 70 74 95"))


def handdoek():
    laag = lambda y, h, kleur: (f'<path d="M26 {y} L94 {y} Q96 {y} 96 {y + 2} L96 {y + h - 2} Q96 {y + h} 94 {y + h} L26 {y + h} Q24 {y + h} 24 {y + h - 2} L24 {y + 2} Q24 {y} 26 {y} Z" fill="{kleur}"/>'
                                f'<path d="M24 {y + h - 4} L96 {y + h - 4}" stroke="rgba(0,0,0,.15)" stroke-width="1.2"/>'
                                f'<path d="M26 {y} L94 {y} Q96 {y} 96 {y + 2} L96 {y + h - 2} Q96 {y + h} 94 {y + h} L26 {y + h} Q24 {y + h} 24 {y + h - 2} L24 {y + 2} Q24 {y} 26 {y} Z" fill="url(#rl-v)" stroke="rgba(0,0,0,.2)" stroke-width=".8"/>')
    return DEFS + laag(76, 22, "#FAF8F6") + laag(56, 20, "#D8CBB5") + laag(36, 20, "var(--stof)")


VOOR_ACHTER = {"polo": polo, "tshirt": tshirt, "sweater": sweater, "hoodie": hoodie, "softshell": softshell, "fleece": fleece, "werkjas": werkjas,
               "bodywarmer": bodywarmer, "hesje": hesje, "koksbuis": koksbuis, "overhemd": overhemd, "tuniek": tuniek, "schort": schort, "cap": cap, "tas": tas}
ALLEEN = {"werkbroek": lambda: broek(kniestukken=True), "koksbroek": lambda: broek(ruit=True), "overall": overall, "handdoek": handdoek}


def voorkant(naam):
    if naam in VOOR_ACHTER:
        return VOOR_ACHTER[naam]()[0]
    return ALLEEN[naam]()


def achterkant(naam):
    return VOOR_ACHTER[naam]()[1]
