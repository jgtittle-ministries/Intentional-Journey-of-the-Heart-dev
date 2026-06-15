import io, re

DOCS = r"C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev\docs"
rels = [
    r"volume-1-laws-of-the-spirit\taxonomy-key-how-this-volume-classifies-its.md",
    r"volume-2-knowing-to-doing\exploration-08-container.md",
    r"volume-2-knowing-to-doing\exploration-10-training-plan.md",
    r"volume-2-knowing-to-doing\exploration-o-the-christian-companions-framework-tool.md",
    r"volume-2-knowing-to-doing\taxonomy-key-how-this-volume-classifies-its.md",
    r"volume-4-testing-framework\section-4-small-group-spiritual-formation-testing.md",
    r"volume-5-references\bearing-fruit-with-patience-upper-levels.md",
    r"volume-5-references\introduction.md",
]

# match [LABEL](<anypath>source-pdfs/fc-formation-companion.pdf){: .pdf-popup data-pdf-label="FC..." }
pat = re.compile(
    r'\[([^\]]*)\]\([^)]*source-pdfs/fc-formation-companion\.pdf\)\{:\s*\.pdf-popup\s+data-pdf-label="FC[^"]*"\s*\}'
)

for rel in rels:
    fp = DOCS + "\\" + rel
    with io.open(fp, "r", encoding="utf-8") as f:
        txt = f.read()
    chap = "the-formation-companion.md" if "volume-5-references" in rel.replace("\\", "/") else "../volume-5-references/the-formation-companion.md"

    def repl(m):
        label = m.group(1).strip()
        if label == "(pdf)":
            return "[(mainline chapter)](%s)" % chap
        return "[%s](%s)" % (m.group(1), chap)

    new, n = pat.subn(repl, txt)
    if n:
        with io.open(fp, "w", encoding="utf-8") as f:
            f.write(new)
        print("updated (%d): %s" % (n, rel))
    else:
        print("NO MATCH: %s" % rel)
