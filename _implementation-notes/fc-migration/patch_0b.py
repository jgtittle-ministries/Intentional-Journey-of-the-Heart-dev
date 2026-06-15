import io

CH = r"C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev\docs\volume-5-references\the-formation-companion.md"
with io.open(CH, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

START = "Vol 2 — Exploration OB — Foundational Practice (Operating Ground)"
END = "# Conclusion"

si = next(i for i, l in enumerate(lines) if l.strip() == START)
ei = next(i for i, l in enumerate(lines) if l.strip() == END)

pointer = [
    "# Exploration 0B: The Contemplative Substrate",
    "",
    "*The Formation-Companion paper introduced the contemplative substrate — the four practices (fixed-hour prayer, lectio divina, silent waiting, and vigilantia cordis) that condition the soul beneath all the diagnostic, tool-application, and developmental work. That material has since been promoted to a standalone, refined chapter and now lives canonically at [V2.Exp0B — The Contemplative Substrate](../volume-2-knowing-to-doing/exploration-0b-contemplative-substrate.md). It is not repeated here, to keep one source of truth.*",
    "",
    "*What the Formation Companion adds is only this: the substrate is not merely the **participant's** preparation — it is the **Companion's own** non-negotiable ground. A Companion whose practice has become disconnected from fixed-hour prayer, lectio, silent waiting, and watchfulness of the heart is practicing from diminishing capital. The four practices are the soil-conditioning that keeps a soul present to do the work — in the Companion before the pilgrim. See [V2.Exp0B](../volume-2-knowing-to-doing/exploration-0b-contemplative-substrate.md) for the full treatment, including the Open Trails and the connections to the Vol 1 Foundational Laws.*",
    "",
]

new = lines[:si] + pointer + lines[ei:]
with io.open(CH, "w", encoding="utf-8") as f:
    f.write("\n".join(new))

print("spliced 0B section: removed lines %d-%d (%d lines), inserted pointer (%d lines)" % (si + 1, ei, ei - si, len(pointer)))
print("new total lines:", len(new))
