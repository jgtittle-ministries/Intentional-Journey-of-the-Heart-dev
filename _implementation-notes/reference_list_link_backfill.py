"""Phase 5 Finding I (rest): backfill chapter links into the Vol 5 PT reference list.

For each `**P{N}/G{X} · {PREFIX} — {LawName} ...**` entry-header line, wrap the
law name as a markdown link to the corresponding Vol 1 / Vol 2 chapter file.

Speculatives, SST Stage entries, the V2.Exp10 anomaly, and Suffering-as-Formation Loop
have no chapter and are left as-is.

Usage:
  python _implementation-notes/reference_list_link_backfill.py

Idempotent: skips headers that already contain a markdown link.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PT_CHAPTER = REPO / "docs" / "volume-5-references" / "periodic-table-of-spiritual-laws-a-summing.md"

# FL Roman -> chapter file (Vol 1, all 45 FLs)
FL_CHAPTERS = {
    "I":      "foundational-law-i-the-sowing-and-reaping.md",
    "II":     "foundational-law-ii-the-confession-restoration-law.md",
    "III":    "foundational-law-iii-the-heart-throne-law.md",
    "IV":     "foundational-law-iv-the-humility-exaltation-law.md",
    "V":      "foundational-law-v-the-reciprocal-forgiveness-law.md",
    "VI":     "foundational-law-vi-the-hear-and-obey.md",
    "VII":    "foundational-law-vii-the-drawing-near-reciprocity.md",
    "VIII":   "foundational-law-viii-the-desire-for-god.md",
    "IX":     "foundational-law-ix-the-generosity-provision-law.md",
    "X":      "foundational-law-x-the-ask-seek-knock.md",
    "XI":     "foundational-law-xi-the-renewal-of-mind.md",
    "XII":    "foundational-law-xii-the-honor-authority-flourishing.md",
    "XIII":   "foundational-law-xiii-the-pure-heart-vision.md",
    "XIV":    "foundational-law-xiv-the-vanity-of-substitutes-law.md",
    "XV":     "foundational-law-xv-the-hardening-law.md",
    "XVI":    "foundational-law-xvi-the-bondage-law.md",
    "XVII":   "foundational-law-xvii-the-substitution-cascade-law.md",
    "XVIII":  "foundational-law-xviii-the-bitter-root-community-law.md",
    "XIX":    "foundational-law-xix-the-spirit-anointing-transmission-law.md",
    "XX":     "foundational-law-xx-the-gathered-body-discernment-law.md",
    "XXI":    "foundational-law-xxi-the-household-formation-law.md",
    "XXII":   "foundational-law-xxii-the-endurance-hope-law.md",
    "XXIII":  "foundational-law-xxiii-the-sabbath-rest-law.md",
    "XXIV":   "foundational-law-xxiv-the-confession-in-community-law.md",
    "XXV":    "foundational-law-xxv-the-restoration-of-the-erring-law.md",
    "XXVI":   "foundational-law-xxvi-the-doctrinal-calcification-law.md",
    "XXVII":  "foundational-law-xxvii-the-thick-practice-transmission-law.md",
    "XXVIII": "foundational-law-xxviii-the-generational-nested-structure-law.md",
    "XXIX":   "foundational-law-xxix-corporate-emotional-integration-law.md",
    "XXX":    "foundational-law-xxx-communal-soul-care-for-the-wounded-law.md",
    "XXXI":   "foundational-law-xxxi-corporate-scriptural-reception-law.md",
    "XXXII":  "foundational-law-xxxii-communal-worship-heart-alignment-law.md",
    "XXXIII": "foundational-law-xxxiii-community-polity-structure-law.md",
    "XXXIV":  "foundational-law-xxxiv-marriage-covenant-architecture-law.md",
    "XXXV":   "foundational-law-xxxv-the-trust-substrate-law.md",
    "XXXVI":  "foundational-law-xxxvi-the-eschatological-glory-law.md",
    "XXXVII": "foundational-law-xxxvii-the-worship-alignment-law.md",
    "XXXVIII":"foundational-law-xxxviii-the-soul-restoration-law.md",
    "XXXIX":  "foundational-law-xxxix-the-surrender-multiplication-law.md",
    "XL":     "foundational-law-xl-the-abiding-fruitfulness-law.md",
    "XLI":    "foundational-law-xli-the-defilement-cleansing-reversal-law.md",
    "XLII":   "foundational-law-xlii-the-kingdom-confrontation-authority-law.md",
    "XLIII":  "foundational-law-xliii-the-cross-boundary-faith-access-law.md",
    "XLIV":   "foundational-law-xliv-the-sign-as-revelation-law.md",
    "XLV":    "foundational-law-xlv-the-voice-of-christ-reaches-into-death-law.md",
}

# Vol 1 Explorations + Opening
V1_EXP_CHAPTERS = {
    "1":   "exploration-01-how-to-get-faith.md",
    "2":   "exploration-02-my-spirit-heart-soul-and.md",
    "3":   "exploration-03-relationship-of-faith-hope-and.md",
    "4":   "exploration-04-wisdom-knowledge-understanding-and-discernment.md",
    "5":   "exploration-05-gateway-condition.md",
    "6":   "exploration-06-obedience-channel.md",
    "7":   "exploration-07-spiritual-authority.md",
    "8":   "exploration-08-prayer-as-resonance-phenomenon.md",
}
V1_OPEN = "opening-miracle-frame.md"

# Vol 2 Explorations
V2_EXP_CHAPTERS = {
    "1":  "exploration-01-heart-soil.md",
    "2":  "exploration-02-emotional-knots.md",
    "3":  "exploration-03-believing-lie.md",
    "4":  "exploration-04-confession-and-restoration.md",
    "5":  "exploration-05-four-connects.md",
    "6":  "exploration-06-tool-map.md",
    "7":  "exploration-07-hearing-with-understanding.md",
    "8":  "exploration-08-container.md",
    "9":  "exploration-09-community-as-amplifier.md",
    "10": "exploration-10-training-plan.md",
}

V1_PATH = "../volume-1-laws-of-the-spirit/"
V2_PATH = "../volume-2-knowing-to-doing/"

HEADER_RE = re.compile(
    r"^(\*\*P\d+/G[IV]+ · )"      # leading "**P{N}/G{X} · "
    r"(FL\.[IVXL]+ \(Foundational\)|V1\.Exp\d+|V1\.Open|V2\.Exp\d+)"  # prefix
    r"( (?:\(\w+\) )?— )"          # " — " or " (Gateway) — "
    r"([^*\[]+?)"                       # law name (greedy halt before tag / link)
    r"( \([A-Z;+ ,\d]+\)(?:, [A-Z][a-z]+ [A-Z][a-z]+(?: \(Band \d\))?)?(?:.*?)?\*\*)"  # rest
)

def chapter_for(prefix: str) -> str | None:
    """Return the chapter path for a prefix, or None if no chapter exists."""
    m = re.match(r"FL\.([IVXL]+) \(Foundational\)", prefix)
    if m:
        roman = m.group(1)
        fname = FL_CHAPTERS.get(roman)
        return f"{V1_PATH}{fname}" if fname else None
    m = re.match(r"V1\.Exp(\d+)", prefix)
    if m:
        fname = V1_EXP_CHAPTERS.get(m.group(1))
        return f"{V1_PATH}{fname}" if fname else None
    if prefix == "V1.Open":
        return f"{V1_PATH}{V1_OPEN}"
    m = re.match(r"V2\.Exp(\d+)", prefix)
    if m:
        fname = V2_EXP_CHAPTERS.get(m.group(1))
        return f"{V2_PATH}{fname}" if fname else None
    return None


def process_line(line: str) -> tuple[str, bool]:
    """Return (new_line, changed)."""
    if "[" in line and "](" in line:
        # already linked; skip
        return line, False
    m = HEADER_RE.match(line)
    if not m:
        return line, False
    leading, prefix, dash, name, rest = m.groups()
    chapter = chapter_for(prefix)
    if not chapter:
        return line, False
    new = f"{leading}{prefix}{dash}[{name.strip()}]({chapter}){rest}"
    return new, True


def main() -> None:
    text = PT_CHAPTER.read_text(encoding="utf-8")
    lines = text.split("\n")
    in_reflist = False
    changes = []
    for i, line in enumerate(lines):
        if line.startswith("## Reference List for the Periodic Table"):
            in_reflist = True
            continue
        if in_reflist and line.startswith("## ") and not line.startswith("## Reference List"):
            in_reflist = False
        if not in_reflist:
            continue
        new, changed = process_line(line)
        if changed:
            lines[i] = new
            # log: show prefix only (line numbers in original)
            changes.append((i + 1, line[:80]))
    if not changes:
        print("No changes.")
        return
    PT_CHAPTER.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated {len(changes)} reference-list entry headers:")
    for lineno, snip in changes:
        print(f"  line {lineno}: {snip}...")


if __name__ == "__main__":
    main()
