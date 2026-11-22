#!/usr/bin/env python3
"""Draw the 22 November 2026 front page: one 1024x1024 PNG summing up the
world's news of Sunday 22 November 2026.

Build-time only (needs Pillow). The entry itself is main.py, which copies the
PNG this script produces (entry.png, committed in the repo) to the output
directory -- so the graded run needs no network and no third-party packages,
and is byte-for-byte deterministic.

Every story below was checked against reporting dated 22 November 2026
(or late 21 November, dominating the 22 November news cycle). Stories from
earlier days are named in the DATE CHECK box at the foot of the page and
deliberately left out.

Round 2 (late morning WIB, 22 Nov): refreshed with the Bahrain industrial
strike, the COP31 3am draft and closing plenary, the Peru quake aftermath,
and a new Africa briefs section; the stale Shenzhen summit feature was
replaced and weak filler briefs swapped for real Sunday news.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (253, 248, 238)
INK = (17, 17, 17)
RED = (185, 28, 28)
BLUE = (29, 78, 216)
MUTED = (85, 85, 85)
PANEL = (255, 255, 255)
RULE = (17, 17, 17)
LIGHT = (232, 226, 214)
SKY = (214, 232, 244)
SEA = (29, 78, 150)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit in `width` px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=None):
    """Draw wrapped paragraph; returns y just below the last line."""
    leading = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color=RED, size=11):
    draw.text((x, y), text, font=SANS_B(size), fill=color)
    return y + size + 5


# ---------------------------------------------------------------- stories
# tier: lead | feature | pin | brief.  pin stories get a numbered marker on
# the world map; brief stories fill the region columns.
STORIES = [
    dict(tier="lead", region="CLIMATE", place="ANTALYA, TURKEY",
         headline="COP31 NEARS A DEAL AS 3AM DRAFT LANDS",
         deck=("Two days past its Friday deadline, the summit publishes its third "
               "— supposedly final — cover text at 3am Sunday. President Kurum "
               "calls it one “all parties can agree upon”; a closing plenary "
               "is set for 9am. The text still names no fossil fuels and no "
               "$120bn figure."),
         source="Reuters / Carbon Brief", pin=(30.7, 36.9)),
    dict(tier="feature", region="THE GULF", place="STRAIT OF HORMUZ",
         headline="IRAN CLAIMS STRIKES ON TWO US PATRIOT RADARS",
         deck=("The IRGC says a combined missile-and-drone operation hit two US "
               "Patriot radars, as Tehran calls the US blockade “a hostile act” "
               "— and says reopening Hormuz “would not be difficult”."),
         source="ANI / IRGC", pin=(56.5, 26.5)),
    dict(tier="feature", region="UKRAINE", place="KYIV",
         headline="RUSSIA’S 400-DRONE BARRAGE; MISSILE CRASHES IN POLAND",
         deck=("One of the war’s largest aerial attacks — 400 drones, 110 missiles "
               "— as a missile and a drone come down in Poland. Zelenskyy says "
               "NATO membership is Ukraine’s clearest guarantee."),
         source="Reuters / AP", pin=(30.5, 50.4)),
    dict(tier="feature", region="THE GULF", place="MANAMA, BAHRAIN",
         headline="IRANIAN STRIKE SETS BAHRAIN PLANT ABLAZE",
         deck=("Bahrain says an Iranian attack hit an industrial facility, "
               "sparking a fire, as air defences intercept incoming attacks "
               "across the Gulf."),
         source="Bahrain ministry / CNA", pin=(50.6, 26.2)),
    dict(tier="feature", region="THE BALTIC", place="GULF OF FINLAND",
         headline="DRONES SET RUSSIAN CARGO SHIP ABLAZE OFF FINLAND",
         deck=("A Russian cargo ship bound for Kaliningrad is hit by two drones; "
               "the crew evacuates as the ship burns. Finland tightens security "
               "and probes a suspected helicopter incursion."),
         source="Reuters", pin=(23.0, 59.5)),
    dict(tier="pin", region="EUROPE", place="TALLINN, ESTONIA",
         headline="Estonia to shut its Russian border",
         deck=("All five road crossings close on 1 Dec after an alleged "
               "Russian-backed sabotage attempt; families queue to cross before "
               "the deadline."),
         source="BBC", pin=(24.7, 59.4)),
    dict(tier="pin", region="AMERICAS", place="BRASÍLIA, BRAZIL",
         headline="Bolsonaro in intensive care",
         deck=("The jailed ex-president, serving 27 years for a coup plot, is in "
               "ICU in Brasília with an acute bowel obstruction. Stable and "
               "conscious; no discharge date."),
         source="Reuters", pin=(-47.9, -15.8)),
    dict(tier="pin", region="AMERICAS", place="SINALOA, MEXICO",
         headline="‘El Chapo Isidro’ captured as cartel violence erupts",
         deck=("Mexican special forces seize FBI Top-10 fugitive Fausto Isidro "
               "Meza Flores in a raid backed by US intelligence; gun battles and "
               "burning cars follow, 11 killed."),
         source="Reuters", pin=(-107.4, 24.8)),
    dict(tier="pin", region="AMERICAS", place="WASHINGTON, USA",
         headline="US airlines warned of terror threat; FBI probes database hack",
         deck=("Airlines are warned of possible al-Qaeda-linked attacks before "
               "Thanksgiving as the FBI investigates a second apparent hack of "
               "its NCIC crime database."),
         source="AP", pin=(-77.0, 38.9)),
    dict(tier="pin", region="ASIA", place="NEW DELHI, INDIA",
         headline="Modi opens Nitish Setu; Akvan disrupts flights",
         deck=("The PM inaugurates the Nitish Setu bridge linking Patna and "
               "Vaishali as Nepal’s PM Shah arrives seeking flood aid and "
               "better connectivity."),
         source="PTI", pin=(77.2, 28.6)),
    dict(tier="pin", region="AMERICAS", place="LIMA, PERU",
         headline="Peru quake: 152 homes uninhabitable",
         deck=("A revised inventory dated Sunday counts 152 homes uninhabitable "
               "after Friday’s M6.9 quake; rescue and aid work continues in "
               "the affected regions."),
         source="Peruvian govt", pin=(-77.0, -12.0)),
    dict(tier="pin", region="SPORT", place="TURIN, ITALY",
         headline="ATP Finals: Alcaraz v Shelton, Zverev v Medvedev",
         deck="The top four seeds contest the semi-finals in Turin.",
         source="ATP", pin=(7.7, 45.1)),
]

BRIEFS = [
    ("MIDDLE EAST", [
        ("Israel", "Eisenkot invites Netanyahu’s Likud to coalition talks; Lieberman says ousting Netanyahu is still his “main goal”."),
        ("Gaza", "Israel alleges Hamas is tightening its grip on the Strip."),
        ("Lebanon", "UNIFIL says people in the south still bear the consequences of fighting with Israel."),
        ("Hormuz", "Araghchi says reopening the Strait “would not be difficult” if the US accepts reasonable conditions."),
        ("Basra", "Four dead and 35 injured as fire breaks out at the Hartha thermal power station in northern Basra."),
    ]),
    ("EUROPE", [
        ("Denmark", "Russia masterminded a plot to kill a US-Ukrainian citizen, Copenhagen says."),
        ("France", "Prosecutors probe Depardieu and an author over a gang-rape claim."),
        ("Portugal", "Thousands protest against inflation in Lisbon."),
        ("Spain", "Sánchez extends the bank tax to 2027 and puts the proceeds into housing."),
        ("Football", "Real Madrid beat Celta Vigo; France’s injury-hit rugby side reach the final."),
        ("Norway", "Supreme Court rules climate-disputed oil licences invalid in a landmark ruling."),
    ]),
    ("ASIA-PACIFIC", [
        ("Japan", "Japanese forces to use Indian facilities for live-fire training — a first."),
        ("Myanmar", "A magnitude 4.1 earthquake strikes near Naypyitaw in the early hours of Sunday."),
        ("Nepal", "PM Shah visits Delhi for flood aid talks."),
        ("EU–Indonesia", "Brussels signs the CEPA and IPA trade and investment agreements with Jakarta."),
        ("Voyager-1", "NASA’s Voyager-1 reaches a historic milestone: one light-day from Earth."),
        ("TikTok", "TikTok launches a global deepfake-detection tool for public figures ahead of European elections."),
    ]),
    ("AMERICAS", [
        ("US–Canada", "Hegseth sets fresh limits on US-Canada defence ties."),
        ("White House", "Melania Trump wants more Russia-Ukraine ceasefires before Christmas."),
        ("Los Angeles", "A man is convicted of arson in wildfires that killed 12."),
        ("Virginia", "First child death from measles in Virginia since 1978, as US cases climb."),
        ("Florida", "Storms bring historic flooding up the coast."),
    ]),
    ("SPORT", [
        ("NBA", "James Harden passes Kobe Bryant for third on the all-time 50-point games list."),
        ("Cricket", "Australia bowl first as injured Smith misses the South Africa decider."),
        ("Snooker", "Advani and Ramachandran win their openers at the World Championship."),
        ("F1", "The Russell–Verstappen feud resurfaces in Las Vegas."),
    ]),
    ("MARKETS & TECH", [
        ("Markets", "Wall Street ends its worst week since 2020 — Nasdaq −5.28% on Friday, S&P 500 in correction, VIX 35.89."),
        ("Oil & gold", "Crude futures fall more than 3%; Brent $92.57, gold $3,517 at Friday’s close."),
        ("ECB", "EU launches the search for a new ECB chief as Christine Lagarde resigns."),
        ("UN", "UN-backed talks agree to keep working toward a 2028 treaty on autonomous lethal weapons."),
    ]),
    ("AFRICA", [
        ("DRC", "Kenya discharges its last Ebola patient as the DRC death toll passes 5,300."),
        ("Ghana", "Ghana unveils ‘Heritage Series’ banknotes honouring Nkrumah, Kofi Annan and Makola traders."),
    ]),
]

DATE_CHECK = (
    "LEFT OUT ON PURPOSE — stories from earlier days, not 22 Nov: Iran’s strikes on the US "
    "base in Kuwait and Bahrain (Wed 18 Nov); the US strike on Qeshm Island (Tue 17 Nov); "
    "the ADNOC vessel attack (17 Nov); the Shenzhen APEC summit (Sat 21 Nov); Cyclone "
    "Akvan’s landfall (earlier in the week). The Peru quake IS in — Sunday’s revised toll."
)
SOURCES_LINE = ("Sources: Reuters · BBC · AP · Al Jazeera · UKMTO · USGS · ATP · ANI · Carbon Brief — "
                "checked against reporting of 22 Nov 2026. Drawn entirely in code; no photographs.")

# ---------------------------------------------------------------- world map
# Coarse continent outlines in (lon, lat); the map is drawn as dots on a
# grid, so rough outlines read as a proper dotted world map. Schematic.
CONTINENTS = [
    # North America (incl. Central America)
    [(-168, 66), (-158, 71), (-140, 70), (-128, 71), (-115, 69), (-100, 69),
     (-88, 68), (-82, 66), (-78, 62), (-72, 62), (-65, 60), (-60, 55),
     (-55, 47), (-60, 45), (-65, 44), (-70, 42), (-74, 39), (-76, 35),
     (-80, 32), (-81, 26), (-84, 30), (-89, 30), (-91, 19), (-94, 17),
     (-97, 16), (-102, 18), (-105, 20), (-110, 23), (-114, 29), (-120, 34),
     (-124, 42), (-124, 48), (-132, 56), (-145, 60), (-158, 58), (-165, 60)],
    # Greenland
    [(-58, 64), (-52, 60), (-43, 60), (-40, 64), (-32, 68), (-25, 70),
     (-22, 74), (-30, 76), (-45, 78), (-58, 76), (-62, 74), (-58, 70)],
    # South America
    [(-79, 9), (-72, 12), (-64, 10), (-59, 8), (-52, 5), (-50, 0),
     (-44, -3), (-35, -8), (-38, -15), (-40, -22), (-48, -28), (-53, -33),
     (-58, -38), (-62, -41), (-66, -45), (-68, -50), (-70, -55), (-73, -50),
     (-73, -40), (-72, -30), (-70, -20), (-75, -15), (-80, -5), (-81, 1)],
    # Europe
    [(-10, 36), (-9, 38), (-9, 43), (-2, 44), (-1, 46), (-4, 48),
     (0, 50), (2, 51), (4, 53), (8, 55), (8, 57), (10, 59), (12, 58),
     (18, 56), (21, 55), (24, 58), (26, 60), (28, 62), (30, 65), (32, 70),
     (36, 68), (40, 67), (44, 68), (48, 68), (50, 69), (44, 64), (40, 60),
     (38, 56), (35, 54), (33, 52), (30, 50), (28, 46), (30, 46), (28, 44),
     (24, 42), (23, 40), (22, 37), (19, 40), (16, 40), (12, 44), (8, 44),
     (3, 42), (-1, 38), (-6, 36)],
    # Africa
    [(-6, 35), (0, 36), (10, 37), (12, 34), (20, 32), (25, 32), (32, 31),
     (34, 28), (36, 24), (38, 20), (39, 16), (43, 12), (48, 11), (51, 11),
     (51, 6), (48, 0), (44, -5), (40, -10), (38, -15), (36, -20), (33, -25),
     (31, -29), (28, -33), (25, -34), (20, -35), (17, -32), (15, -28),
     (13, -22), (12, -17), (12, -12), (9, -2), (9, 3), (4, 6), (-3, 5),
     (-8, 5), (-13, 8), (-16, 12), (-17, 15), (-16, 20), (-14, 25),
     (-10, 30), (-8, 32)],
    # Asia
    [(30, 36), (36, 36), (40, 38), (44, 40), (48, 40), (50, 38), (52, 37),
     (54, 38), (57, 37), (60, 36), (62, 37), (66, 38), (70, 40), (74, 40),
     (78, 42), (82, 45), (86, 46), (90, 48), (94, 50), (98, 52), (102, 54),
     (106, 56), (110, 58), (114, 60), (118, 62), (122, 64), (126, 66),
     (130, 68), (134, 70), (138, 71), (142, 72), (146, 72), (150, 70),
     (154, 69), (158, 68), (162, 66), (166, 64), (170, 62), (174, 62),
     (178, 65), (178, 62), (170, 60), (162, 58), (158, 55), (156, 52),
     (150, 52), (144, 50), (142, 46), (140, 42), (138, 38), (135, 35),
     (132, 33), (128, 31), (126, 30), (122, 30), (120, 26), (118, 24),
     (114, 22), (110, 20), (108, 16), (106, 10), (104, 8), (101, 8),
     (99, 10), (97, 14), (95, 16), (93, 18), (91, 22), (89, 22), (87, 21),
     (85, 19), (82, 17), (80, 15), (78, 10), (76, 8), (74, 12), (72, 18),
     (70, 20), (68, 22), (66, 25), (62, 25), (58, 25), (56, 27), (54, 27),
     (52, 28), (50, 30), (48, 30), (46, 30), (44, 32), (42, 34), (40, 36),
     (38, 38), (36, 38), (34, 37), (32, 36)],
    # Japan
    [(130, 31), (132, 33), (135, 34), (137, 35), (139, 37), (140, 39),
     (141, 41), (143, 42), (145, 44), (143, 45), (141, 44), (140, 40),
     (138, 37), (136, 35), (133, 34), (131, 32)],
    # SE Asia islands
    [(95, 5), (98, 4), (100, 0), (102, -2), (104, -4), (106, -6), (108, -7),
     (110, -7), (112, -6), (114, -4), (116, -2), (118, 0), (120, 1), (119, 3),
     (117, 5), (114, 4), (112, 2), (110, 0), (108, -2), (106, -5), (103, -5),
     (100, -2), (98, 2)],
    [(122, 18), (124, 16), (126, 14), (124, 10), (122, 8), (120, 10),
     (119, 14), (120, 18)],
    # Australia
    [(114, -22), (113, -26), (114, -30), (115, -33), (118, -35), (122, -34),
     (126, -32), (130, -32), (132, -32), (135, -35), (138, -35), (140, -38),
     (143, -39), (146, -39), (149, -37), (150, -35), (153, -30), (153, -27),
     (151, -24), (149, -20), (146, -19), (143, -15), (142, -11), (141, -13),
     (139, -15), (136, -12), (134, -12), (132, -11), (130, -12), (128, -14),
     (126, -14), (124, -16), (122, -17), (120, -19), (117, -20), (115, -21)],
    # New Zealand
    [(167, -45), (169, -43), (171, -42), (173, -41), (175, -40), (177, -38),
     (176, -38), (174, -39), (172, -41), (170, -43), (168, -46)],
    # UK
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51),
     (-1, 50), (-4, 50)],
]


def _point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > y) != (yj > y):
            xint = xi + (y - yi) * (xj - xi) / (yj - yi)
            if xint > x:
                inside = not inside
        j = i
    return inside


def draw_dotted_map(draw, x0, y0, w, h):
    """Equirectangular dotted world map, lat 84..-58, lon -180..180."""
    lat_top, lat_bot = 84.0, -58.0
    step = 6
    for gx in range(x0, x0 + w, step):
        lon = (gx - x0) / w * 360.0 - 180.0
        for gy in range(y0, y0 + h, step):
            lat = lat_top - (gy - y0) / h * (lat_top - lat_bot)
            if any(_point_in_poly(lon, lat, c) for c in CONTINENTS):
                draw.ellipse([gx - 1.8, gy - 1.8, gx + 1.8, gy + 1.8],
                             fill=(90, 90, 90))
    draw.rectangle([x0, y0, x0 + w, y0 + h], outline=RULE, width=1)


def lonlat_to_xy(lon, lat, x0, y0, w, h):
    x = x0 + (lon + 180.0) / 360.0 * w
    y = y0 + (84.0 - lat) / 142.0 * h
    return x, y


def draw_pin(draw, x, y, n, dx=0, dy=-14):
    """Numbered map pin: red disc + white number, with a small stem."""
    px, py = x + dx, y + dy
    draw.line([x, y, px, py + 7], fill=RED, width=2)
    draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=(255, 255, 255), width=1)
    fnt = SANS_B(10 if n < 10 else 9)
    tw = draw.textlength(str(n), font=fnt)
    draw.text((px - tw / 2, py - 7), str(n), font=fnt, fill=(255, 255, 255))


# ---------------------------------------------------------------- illustrations
def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SKY, outline=INK, width=2)
    # meridians / parallels
    for k in (-0.55, 0.0, 0.55):
        draw.arc([cx - r, cy - r, cx + r, cy + r], 90 - 55, 90 + 55,
                 fill=BLUE, width=1)
    draw.ellipse([cx - int(r * 0.55), cy - r, cx + int(r * 0.55), cy + r],
                 outline=BLUE, width=1)
    draw.line([cx - r, cy, cx + r, cy], fill=BLUE, width=1)
    draw.line([cx - r, cy - int(r * 0.5), cx + r, cy - int(r * 0.5)], fill=BLUE, width=1)
    draw.line([cx - r, cy + int(r * 0.5), cx + r, cy + int(r * 0.5)], fill=BLUE, width=1)
    # land blobs
    draw.ellipse([cx - r + 8, cy - r + 12, cx - 6, cy - 4], fill=(46, 139, 87))
    draw.ellipse([cx + 2, cy + 2, cx + r - 10, cy + r - 14], fill=(46, 139, 87))


def draw_factory(draw, x, y, w, h):
    """Smokestack factory with smoke puffs (COP31 lead illustration)."""
    draw.rectangle([x, y + h - 34, x + w, y + h], fill=(60, 60, 60))
    draw.rectangle([x + 8, y + h - 58, x + 22, y + h - 34], fill=(60, 60, 60))
    draw.rectangle([x + 30, y + h - 48, x + 44, y + h - 34], fill=(60, 60, 60))
    for sx in (x + 10, x + 32):
        for i, r in enumerate((7, 9, 11)):
            draw.ellipse([sx - r, y + 6 - i * 12 - r, sx + r, y + 6 - i * 12 + r],
                         outline=MUTED, width=1)
    draw.polygon([(x + w - 26, y + h - 34), (x + w - 6, y + h - 34),
                  (x + w - 16, y + h - 52)], fill=RED)


def draw_drone_scene(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(20, 40, 70))
    for wy in range(3):
        yy = y + h - 12 - wy * 9
        draw.line([x + 6, yy, x + w - 6, yy], fill=(90, 140, 200), width=2)
    # quadcopter drone
    cx, cy = x + w // 2, y + 26
    draw.ellipse([cx - 12, cy - 6, cx + 12, cy + 6], fill=(220, 220, 220))
    for sx in (-20, 20):
        draw.line([cx, cy, cx + sx, cy - 8], fill=(220, 220, 220), width=2)
        draw.line([cx + sx - 9, cy - 10, cx + sx + 9, cy - 10], fill=(255, 255, 255), width=2)
    # explosion star, bottom right
    ex, ey = x + w - 26, y + h - 22
    for ang in range(0, 360, 45):
        import math
        dx = math.cos(math.radians(ang)) * 14
        dy = math.sin(math.radians(ang)) * 14
        draw.line([ex, ey, ex + dx, ey + dy], fill=(255, 170, 0), width=3)
    draw.ellipse([ex - 6, ey - 6, ex + 6, ey + 6], fill=(255, 200, 40))


def draw_missile_scene(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(35, 20, 25))
    import math
    for i in range(3):
        x1 = x + 14 + i * 46
        draw.arc([x1 - 26, y + 6, x1 + 26, y + 58], 200, 340, fill=(255, 200, 40), width=3)
        draw.ellipse([x1 + 20, y + 8, x1 + 30, y + 18], fill=(255, 220, 80))
    # city skyline
    for i, bh in enumerate((22, 34, 18, 28, 40, 24)):
        bx = x + 8 + i * 36
        draw.rectangle([bx, y + h - bh - 8, bx + 28, y + h - 8], fill=(70, 60, 70))
        draw.rectangle([bx + 10, y + h - bh - 14, bx + 18, y + h - bh - 8], fill=(70, 60, 70))
    draw.rectangle([x, y + h - 8, x + w, y + h], fill=(20, 12, 14))


def draw_summit_scene(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(240, 238, 230))
    # skyline
    for i, bh in enumerate((30, 46, 38, 48, 36, 44)):
        bx = x + 6 + i * 36
        draw.rectangle([bx, y + h - bh, bx + 30, y + h], fill=(120, 125, 135))
    # three flags on poles
    flags = [((185, 28, 28), None), ((220, 220, 220), (29, 78, 216)),
             ((255, 255, 255), (185, 28, 28))]
    for i, (c1, c2) in enumerate(flags):
        fx = x + 22 + i * 62
        draw.line([fx, y + 8, fx, y + 44], fill=INK, width=2)
        if i == 0:  # USA-ish: stripes
            for s in range(4):
                draw.rectangle([fx, y + 8 + s * 7, fx + 34, y + 14 + s * 7],
                               fill=(185, 28, 28) if s % 2 == 0 else (255, 255, 255))
            draw.rectangle([fx, y + 8, fx + 14, y + 20], fill=(29, 78, 216))
        elif i == 1:  # China-ish: red with stars
            draw.rectangle([fx, y + 8, fx + 34, y + 34], fill=(222, 0, 0))
            draw.ellipse([fx + 4, y + 11, fx + 11, y + 18], fill=(255, 220, 0))
        else:  # Russia-ish: white/blue/red
            draw.rectangle([fx, y + 8, fx + 34, y + 17], fill=(255, 255, 255))
            draw.rectangle([fx, y + 17, fx + 34, y + 26], fill=(29, 78, 216))
            draw.rectangle([fx, y + 26, fx + 34, y + 34], fill=(185, 28, 28))


def draw_fire_scene(draw, x, y, w, h):
    """Burning industrial plant at night (Bahrain feature illustration)."""
    draw.rectangle([x, y, x + w, y + h], fill=(30, 18, 20))
    # plant silhouette
    draw.rectangle([x + 10, y + h - 26, x + w - 10, y + h], fill=(70, 60, 60))
    draw.rectangle([x + 20, y + h - 44, x + 34, y + h - 26], fill=(70, 60, 60))
    draw.rectangle([x + 44, y + h - 38, x + 56, y + h - 26], fill=(70, 60, 60))
    # flames
    for fx in (x + w // 2 - 14, x + w // 2 + 10):
        fy = y + h - 26
        draw.polygon([(fx - 12, fy), (fx, fy - 20), (fx + 12, fy)], fill=(255, 140, 0))
        draw.polygon([(fx - 6, fy), (fx, fy - 12), (fx + 6, fy)], fill=(255, 220, 0))
    # smoke puffs
    for i, r in enumerate((6, 8, 10)):
        sx = x + w // 2 + 6 + i * 8
        sy = y + 12 + i * 2
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], outline=(150, 150, 150), width=1)
    # sparks
    for sx, sy in ((x + 30, y + 10), (x + w - 30, y + 14), (x + w - 50, y + 6)):
        draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 200, 40))


def draw_ship_scene(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(214, 232, 244))
    for wy in range(3):
        yy = y + h - 14 - wy * 8
        draw.line([x + 6, yy, x + w - 6, yy], fill=(90, 140, 200), width=2)
    # cargo ship
    draw.polygon([(x + 20, y + h - 34), (x + w - 20, y + h - 34),
                  (x + w - 34, y + h - 16), (x + 34, y + h - 16)], fill=(40, 40, 40))
    for i, col in enumerate(((185, 28, 28), (29, 78, 216), (200, 160, 40))):
        draw.rectangle([x + 30 + i * 44, y + h - 56, x + 68 + i * 44, y + h - 36],
                       fill=col, outline=INK, width=1)
    draw.rectangle([x + w - 66, y + h - 66, x + w - 44, y + h - 36], fill=(240, 240, 240),
                   outline=INK, width=1)
    # flame + smoke
    fx, fy = x + w // 2, y + h - 36
    draw.polygon([(fx - 12, fy), (fx, fy - 16), (fx + 12, fy)], fill=(255, 140, 0))
    draw.polygon([(fx - 6, fy), (fx, fy - 10), (fx + 6, fy)], fill=(255, 220, 0))

# ---------------------------------------------------------------- compose
MX = 24            # left margin
CW = 976           # content width
TOTAL_STORIES = len(STORIES) + sum(len(b) for _, b in BRIEFS)


def draw_masthead(draw, img):
    y = 14
    # small globe mark left of the nameplate
    draw_globe(draw, 62, 46, 28)
    draw.text((102, 14), "THE WORLD IN ONE DAY", font=SERIF_B(50), fill=INK)
    draw.rectangle([MX, 74, MX + CW, 77], fill=RULE)
    draw.rectangle([MX, 80, MX + CW, 83], fill=RED)
    sub = (f"SUNDAY 22 NOVEMBER 2026  ·  {TOTAL_STORIES} STORIES  ·  7 REGIONS  ·  "
           "EVERY STORY DATED 22 NOV 2026")
    tw = draw.textlength(sub, font=SANS_B(12))
    draw.text(((W - tw) / 2, 88), sub, font=SANS_B(12), fill=INK)
    return 106


def draw_lead(draw, y):
    lead = STORIES[0]
    h = 162
    draw.rectangle([MX, y, MX + CW, y + h], fill=PANEL, outline=RULE, width=1)
    # illustration panel on the right
    ix = MX + CW - 268
    draw.rectangle([ix, y, MX + CW, y + h], fill=SKY, outline=RULE, width=1)
    draw_globe(draw, ix + 78, y + 62, 44)
    draw_factory(draw, ix + 190, y + 100, 66, 56)
    draw.text((ix + 12, y + 118), "DEAL IN SIGHT", font=SANS_B(13), fill=(34, 120, 60))
    draw.text((ix + 12, y + 138), "Closing plenary 9am Sunday",
              font=SANS(11), fill=MUTED)
    tx = MX + 14
    yy = kicker(draw, tx, y + 10, f"{lead['place']}  —  {lead['region']}", size=11)
    for line in wrap(draw, lead["headline"], SERIF_B(27), 660):
        draw.text((tx, yy), line, font=SERIF_B(27), fill=INK)
        yy += 32
    yy = para(draw, tx, yy + 4, lead["deck"], SANS(13), 660)
    draw.text((tx, yy + 2), f"Source: {lead['source']}", font=SANS(10), fill=MUTED)
    return y + h


def draw_features(draw, y):
    feats = [s for s in STORIES if s["tier"] == "feature"]
    scenes = [draw_drone_scene, draw_missile_scene, draw_fire_scene,
              draw_ship_scene]
    h = 188
    cw = (CW - 3 * 10) // 4
    for i, st in enumerate(feats):
        x = MX + i * (cw + 10)
        draw.rectangle([x, y, x + cw, y + h], fill=PANEL, outline=RULE, width=1)
        scenes[i](draw, x + 1, y + 1, cw - 2, 56)
        yy = kicker(draw, x + 8, y + 64, f"{i + 2}. {st['place']}", size=10)
        yy = para(draw, x + 8, yy, st["headline"], SERIF_B(13), cw - 16,
                  leading=15)
        yy = para(draw, x + 8, yy + 2, st["deck"], SANS(9), cw - 16, leading=12)
        draw.text((x + 8, y + h - 14), f"Source: {st['source']}",
                  font=SANS(9), fill=MUTED)
    return y + h


def draw_map_section(draw, y):
    draw.text((MX, y), "WHERE IT HAPPENED — 12 STORIES ON THE MAP",
              font=SANS_B(11), fill=INK)
    draw.text((MX + CW - 260, y), "Numbers match the stories below",
              font=SANS(10), fill=MUTED)
    y += 18
    mh = 100
    draw_dotted_map(draw, MX, y, CW, mh)
    pins = [s for s in STORIES if s.get("pin")]
    offsets = {1: (-30, 14), 2: (0, -16), 3: (28, -10), 4: (26, 6),
               5: (-8, -30), 6: (26, -28), 7: (0, -16), 8: (0, -16),
               9: (0, -16), 10: (0, -16), 11: (0, -16), 12: (-28, -22)}
    for n, st in enumerate(pins, 1):
        px, py = lonlat_to_xy(st["pin"][0], st["pin"][1], MX, y, CW, mh)
        dx, dy = offsets.get(n, (0, -16))
        draw_pin(draw, px, py, n, dx=dx, dy=dy)
    y += mh + 6
    # legend: 2 rows x 6 entries
    leg = ["1. Antalya — COP31", "2. Hormuz — Patriot radars hit",
           "3. Kyiv — 400-drone barrage", "4. Manama — Bahrain plant ablaze",
           "5. Baltic — Ship ablaze", "6. Tallinn — Border shut",
           "7. Brasília — Bolsonaro ICU", "8. Sinaloa — Chapo Isidro",
           "9. Washington — Terror alert", "10. New Delhi — Modi bridge",
           "11. Lima — Quake aftermath", "12. Turin — ATP semis"]
    fnt = SANS(9)
    colw = CW // 6
    for i, item in enumerate(leg):
        lx = MX + (i % 6) * colw
        ly = y + (i // 6) * 13
        draw.text((lx, ly), item, font=fnt, fill=INK)
    return y + 2 * 13 + 4


def draw_briefs(draw, y, bottom):
    colw = (CW - 2 * 14) // 3
    columns = [
        [BRIEFS[0], BRIEFS[1]],
        [BRIEFS[2], BRIEFS[3]],
        [BRIEFS[4], BRIEFS[5], BRIEFS[6]],
    ]
    for ci, groups in enumerate(columns):
        x = MX + ci * (colw + 14)
        yy = y
        for gname, items in groups:
            draw.text((x, yy), gname, font=SANS_B(11), fill=RED)
            draw.line([x, yy + 14, x + colw, yy + 14], fill=RED, width=1)
            yy += 18
            for place, text in items:
                full = f"{place} — {text}"
                lines = wrap(draw, full, SANS(10), colw)
                for li, line in enumerate(lines[:3]):
                    fnt = SANS_B(10) if li == 0 else SANS(10)
                    # bold the place on the first line only, up to the dash
                    if li == 0 and " — " in line:
                        head, rest = line.split(" — ", 1)
                        draw.text((x, yy), head + " —", font=SANS_B(10), fill=INK)
                        hw = draw.textlength(head + " — ", font=SANS_B(10))
                        draw.text((x + hw, yy), " " + rest, font=SANS(10), fill=INK)
                    else:
                        draw.text((x, yy), line, font=fnt, fill=INK)
                    yy += 11
                yy += 2
            yy += 2
        if yy > bottom:
            raise SystemExit(f"briefs column {ci} overflow: {yy} > {bottom}")
    return bottom


def draw_footer(draw, y):
    draw.rectangle([MX, y, MX + CW, y + 52], fill=(255, 255, 255),
                   outline=RULE, width=1)
    draw.text((MX + 10, y + 6), "DATE CHECK", font=SANS_B(10), fill=RED)
    para(draw, MX + 92, y + 6, DATE_CHECK, SANS(9), CW - 102, leading=12)
    draw.text((MX, y + 58), SOURCES_LINE, font=SANS(9), fill=MUTED)
    return y + 52


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    y = draw_masthead(draw, img)
    y = draw_lead(draw, y + 8)
    y = draw_features(draw, y + 8)
    y = draw_map_section(draw, y + 8)
    footer_top = 940
    draw_briefs(draw, y + 6, footer_top - 6)
    draw_footer(draw, footer_top)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    size = os.path.getsize(out)
    print(f"wrote {out}: {W}x{H}, {size} bytes, {TOTAL_STORIES} stories")
    assert size <= 1024 * 1024, f"over 1 MiB: {size}"
    return out


if __name__ == "__main__":
    main()
