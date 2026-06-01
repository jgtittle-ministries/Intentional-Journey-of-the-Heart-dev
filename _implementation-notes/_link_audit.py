import re, os, glob

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def norm(p):
    return p.replace('\\', '/')

manifest = open('manifest.js', encoding='utf-8').read()
paths = set(norm(p) for p in re.findall(r'"path":\s*"([^"]+)"', manifest))
docs_md = set(norm(p) for p in glob.glob('docs/**/*.md', recursive=True))

print("=== ORPHAN md files (in docs/, not referenced in manifest) ===")
for o in sorted(docs_md - paths):
    print("  ORPHAN:", o)
print("=== manifest paths missing from disk ===")
for p in sorted(paths):
    if not os.path.isfile(p):
        print("  MISSING-FILE:", p)
print()

# Collect link targets from markdown-link syntax and html href/src
md_link = re.compile(r'\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
html_attr = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']')

broken_local = []
checked_local = 0
all_targets = {}  # target -> list of (file, raw)

for md in sorted(docs_md):
    text = open(md, encoding='utf-8').read()
    base = os.path.dirname(md)
    raws = md_link.findall(text) + html_attr.findall(text)
    for rel in raws:
        rel = rel.strip()
        if rel.startswith(('http://','https://','mailto:','tel:','#','data:')):
            continue
        # split anchor
        path_part = rel.split('#',1)[0]
        if not path_part:
            continue
        target = norm(os.path.normpath(os.path.join(base, path_part)))
        all_targets.setdefault(target, []).append((md, rel))
        # only verify local file-like targets (pdf, md, png, jpg, etc.)
        if re.search(r'\.(pdf|md|png|jpe?g|gif|svg|webp|html|css|js|yml|yaml|docx?)$', path_part, re.I):
            checked_local += 1
            if not os.path.isfile(target):
                broken_local.append((md, rel, target))

print("=== BROKEN local file links in docs/*.md (pdf/md/img/etc) ===")
for md, rel, target in broken_local:
    print(f"  MISSING: {rel}")
    print(f"    in: {md}")
    print(f"    -> {target}")
print(f"--- checked {checked_local} local-file links, {len(broken_local)} broken ---")
