# Renders the hear-and-obey traceability overlay as an SVG grid on the Periodic Table layout.
# Data = the 2026-06-15 traceability note (46 laws) + FL.XLVII / FL.XLVIII (2026-09-04).
import html, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "traceability-grid.svg")

# (numeral, short name, period, group, tier, swing)
LAWS = [
    ("I", "Sowing-Reaping", 0, 6, "less", False),
    ("II", "Confession-Restoration", 1, 5, "adj", False),
    ("III", "Heart-Throne", 1, 2, "adj", False),
    ("IV", "Humility-Exaltation", 1, 3, "less", False),
    ("V", "Reciprocal Forgiveness", 2, 5, "less", False),
    ("VI", "Hear-and-Obey", 0, 5, "direct", False),
    ("VII", "Drawing-Near", 1, 1, "direct", True),
    ("VIII", "Desire-for-God", 1, 2, "adj", False),
    ("IX", "Generosity-Provision", 0, 5, "less", False),
    ("X", "Ask-Seek-Knock", 1, 1, "direct", True),
    ("XI", "Renewal-of-Mind", 1, 4, "adj", False),
    ("XII", "Honor-Authority", 2, 5, "less", False),
    ("XIII", "Pure-Heart Vision", 1, 2, "direct", True),
    ("XIV", "Vanity-of-Substitutes", 1, 2, "adj", False),
    ("XV", "Hardening", 0, 1, "direct", True),
    ("XVI", "Bondage", 0, 5, "direct", True),
    ("XVII", "Substitution-Cascade", 4, 2, "less", False),
    ("XVIII", "Bitter-Root Community", 3, 5, "less", False),
    ("XIX", "Spirit Anointing Transmission", 4, 1, "less", False),
    ("XX", "Gathered-Body Discernment", 3, 1, "direct", False),
    ("XXI", "Household Formation", 4, 2, "less", False),
    ("XXII", "Endurance-Hope", 1, 3, "less", False),
    ("XXIII", "Sabbath Rest", 0, 6, "less", False),
    ("XXIV", "Confession-in-Community", 3, 5, "less", True),
    ("XXV", "Restoration-of-the-Erring", 3, 5, "less", False),
    ("XXVI", "Doctrinal Calcification", 4, 4, "adj", True),
    ("XXVII", "Thick Practice Transmission", 4, 5, "less", False),
    ("XXVIII", "Generational Nested Structure", 4, 6, "less", False),
    ("XXIX", "Corporate Emotional Integration", 3, 3, "less", False),
    ("XXX", "Communal Soul-Care", 3, 3, "less", False),
    ("XXXI", "Corporate Scriptural Reception", 3, 4, "direct", False),
    ("XXXII", "Communal Worship Alignment", 3, 2, "adj", True),
    ("XXXIII", "Community Polity Structure", 3, 6, "less", False),
    ("XXXIV", "Marriage Covenant Architecture", 2, 6, "less", False),
    ("XXXV", "Trust-Substrate", 0, 2, "direct", True),
    ("XXXVI", "Eschatological Glory", 5, 2, "less", False),
    ("XXXVII", "Worship Alignment", 0, 2, "adj", True),
    ("XXXVIII", "Soul-Restoration", 0, 3, "less", True),
    ("XXXIX", "Surrender-Multiplication", 0, 5, "less", True),
    ("XL", "Abiding-Fruitfulness", 0, 1, "direct", True),
    ("XLI", "Defilement-Cleansing Reversal", 0, 6, "less", False),
    ("XLII", "Kingdom-Confrontation Authority", 0, 1, "adj", True),
    ("XLIII", "Cross-Boundary Faith-Access", 0, 6, "adj", True),
    ("XLIV", "Sign-as-Revelation", 0, 1, "direct", False),
    ("XLV", "Voice-Reaches-into-Death", 5, 1, "direct", False),
    ("XLVI", "Communal Truth-Telling", 3, 5, "less", False),
    ("XLVII", "Word's-Efficacy", 0, 4, "direct", False),      # added 2026-09-04
    ("XLVIII", "Image-Bearing", 0, 5, "adj", True),           # added 2026-09-04 (call flagged as swing)
]

PERIODS = [
    (0, "Period 0", "Scale-invariant"),
    (1, "Period 1", "Individual"),
    (2, "Period 2", "Dyadic / small group"),
    (3, "Period 3", "Community / congregation"),
    (4, "Period 4", "Generational / historical"),
    (5, "Period 5", "Cosmic / eschatological"),
]
GROUPS = [
    (1, "Group I", "Spirit"),
    (2, "Group II", "Heart"),
    (3, "Group III", "Soul"),
    (4, "Group IV", "Mind & Will"),
    (5, "Group V", "Body & Action"),
    (6, "Group VI", "Structural Frame"),
]

TIER = {
    "direct": dict(fill="#dfeedd", stroke="#3c7a3a", text="#1f4d1e", label="Direct"),
    "adj":    dict(fill="#f6e6c3", stroke="#b7791f", text="#5a3c07", label="Adjacent (one step removed)"),
    "less":   dict(fill="#ececec", stroke="#9a9a9a", text="#4a4a4a", label="Less (a different mechanism)"),
}

# geometry
LEFT, TOP = 190, 205
CW, CH = 240, 150         # cell width/height
CHIP_H, CHIP_GAP = 24, 5
W = LEFT + 6 * CW + 40
H = TOP + 6 * CH + 150

def esc(s): return html.escape(s, quote=True)

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Georgia, \'Times New Roman\', serif">')
svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="18" fill="#faf8f3" stroke="#d9d4c7"/>')
svg.append(f'<text x="{W/2}" y="52" text-anchor="middle" font-size="30" font-weight="bold" fill="#2a2a2a">Traceability to “Hear and Obey God” — the 48 Foundational Laws on the Periodic Table</text>')
svg.append(f'<text x="{W/2}" y="84" text-anchor="middle" font-size="17" fill="#6b6b6b">an interpretive overlay on the Scale × Dimension grid · from the 2026-06-15 diagnostic, extended to FL.XLVII–XLVIII on 2026-09-04 · DRAFT</text>')

# legend
lx = LEFT
for key in ("direct", "adj", "less"):
    t = TIER[key]
    svg.append(f'<rect x="{lx}" y="108" width="22" height="22" rx="5" fill="{t["fill"]}" stroke="{t["stroke"]}" stroke-width="1.5"/>')
    svg.append(f'<text x="{lx+30}" y="125" font-size="16" fill="#333">{esc(t["label"])}</text>')
    lx += 340
svg.append(f'<text x="{lx}" y="125" font-size="16" fill="#333">★ = swing law (tier could defensibly move)</text>')

# column headers
for gi, (g, gname, gdim) in enumerate(GROUPS):
    x = LEFT + gi * CW + CW / 2
    svg.append(f'<text x="{x}" y="{TOP-28}" text-anchor="middle" font-size="16" font-weight="bold" fill="#2a2a2a">{esc(gname)}</text>')
    svg.append(f'<text x="{x}" y="{TOP-9}" text-anchor="middle" font-size="15" fill="#6b6b6b">{esc(gdim)}</text>')

# row headers + cells
for pi, (p, pname, pdesc) in enumerate(PERIODS):
    y = TOP + pi * CH
    svg.append(f'<text x="{LEFT-14}" y="{y+CH/2-4}" text-anchor="end" font-size="16" font-weight="bold" fill="#2a2a2a">{esc(pname)}</text>')
    svg.append(f'<text x="{LEFT-14}" y="{y+CH/2+16}" text-anchor="end" font-size="13" fill="#6b6b6b">{esc(pdesc)}</text>')
    for gi, (g, _, _) in enumerate(GROUPS):
        x = LEFT + gi * CW
        cell = [l for l in LAWS if l[2] == p and l[3] == g]
        empty_by_design = (p == 4 and g == 3)
        fill = "#ffffff" if cell else ("#f3f1ec" if not empty_by_design else "#f7f5f0")
        svg.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" fill="{fill}" stroke="#cfc9bb"/>')
        if empty_by_design:
            svg.append(f'<text x="{x+CW/2}" y="{y+CH/2+5}" text-anchor="middle" font-size="12" fill="#9a9a9a" font-style="italic">empty by design</text>')
        # chips
        n = len(cell)
        total_h = n * CHIP_H + (n - 1) * CHIP_GAP
        cy = y + (CH - total_h) / 2
        for (num, name, _, _, tier, swing) in cell:
            t = TIER[tier]
            cx = x + 8
            cw = CW - 16
            svg.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{CHIP_H}" rx="6" fill="{t["fill"]}" stroke="{t["stroke"]}" stroke-width="1.4"/>')
            label = f'{num}  {name}' + ('  ★' if swing else '')
            fs = 13 if len(label) <= 27 else (11.5 if len(label) <= 33 else 10.5)
            svg.append(f'<text x="{cx+8}" y="{cy+16.5}" font-size="{fs}" fill="{t["text"]}">{esc(label)}</text>')
            cy += CHIP_H + CHIP_GAP

# footer tallies
fy = TOP + 6 * CH + 40
counts = {k: sum(1 for l in LAWS if l[4] == k) for k in TIER}
svg.append(f'<text x="{LEFT}" y="{fy}" font-size="16" fill="#2a2a2a">Tally: Direct {counts["direct"]} · Adjacent {counts["adj"]} · Less {counts["less"]}  —  strict line {counts["direct"]} / {48-counts["direct"]} · inclusive line {counts["direct"]+counts["adj"]} / {counts["less"]}</text>')
svg.append(f'<text x="{LEFT}" y="{fy+26}" font-size="14" fill="#6b6b6b">Cells follow the Vol 5 Periodic Table reference list. V1.Open Miracle Frame (an Exploration, not a Foundational Law) also sits at P0/GI and is omitted here. Chips inside a cell are in numeral order, not rank.</text>')
svg.append(f'<text x="{LEFT}" y="{fy+50}" font-size="14" fill="#6b6b6b">The Periodic Table is organized by Scale × Dimension, not by relation to hear-and-obey; this colouring is a judgment laid over it, not something the catalog asserts.</text>')
svg.append('</svg>')

open(OUT, "w", encoding="utf8").write("\n".join(svg))
print("wrote", OUT, "laws", len(LAWS), counts)
