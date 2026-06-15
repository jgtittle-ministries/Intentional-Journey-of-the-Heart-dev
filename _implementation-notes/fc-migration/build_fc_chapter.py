import io

SRC = r"C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev\_implementation-notes\fc-migration\fc-extracted.md"
OUT = r"C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev\docs\volume-5-references\the-formation-companion.md"

with io.open(SRC, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# Drop any extracted-footnotes trailer (none expected)
body = []
skip = False
for ln in lines:
    if ln.strip() == "## Footnotes (extracted)":
        skip = True
    if skip:
        continue
    body.append(ln)

# The first 5 lines are the title block:
# 0 The Formation Companion
# 1 A Synthesis Role, ...
# 2 John G. Tittle
# 3 Intentional Journey of the Heart — Formation Document v5_5_6
# 4 Draft — April 2026
title = body[0].strip()
subtitle = body[1].strip()
author = body[2].strip()
prov1 = body[3].strip()
prov2 = body[4].strip()
rest = body[5:]

front = [
    "---",
    'title: "The Formation Companion"',
    "volume: 5",
    'source: "The Formation Companion (Formation Document); migrated to mainline 2026-06-13"',
    "---",
    "",
    "# The Formation Companion",
    "",
    "*%s*" % subtitle,
    "",
    "*%s — %s. %s*" % (author, prov1, prov2),
    "",
]

# "Introduction: The Who of Formation" lost its heading level in extraction -> restore as H1
out_rest = []
for ln in rest:
    if ln.strip() == "Introduction: The Who of Formation":
        out_rest.append("# Introduction: The Who of Formation")
    else:
        out_rest.append(ln)

text = "\n".join(front + out_rest).rstrip() + "\n"

with io.open(OUT, "w", encoding="utf-8") as f:
    f.write(text)

print("wrote", OUT)
print("chars:", len(text))
print("first heading line of body:", out_rest[0][:60] if out_rest else "")
