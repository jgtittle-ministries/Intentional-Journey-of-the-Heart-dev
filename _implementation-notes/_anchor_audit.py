import re, os, glob

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def norm(p): return p.replace('\\','/')

def slugify(text):
    # mirror reader.js: lowercase, [^a-z0-9]+ -> '-', trim leading/trailing '-'
    s = text.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'^-|-$', '', s)
    return s

# Gather heading slugs per file (reader assigns ids to h2/h3 i.e. ## and ###)
def headings_for(path):
    slugs = set()
    if not os.path.isfile(path):
        return slugs
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^(#{2,3})\s+(.+?)\s*#*\s*$', line)
        if m:
            slugs.add(slugify(m.group(2)))
    return slugs

heading_cache = {}
def get_headings(path):
    if path not in heading_cache:
        heading_cache[path] = headings_for(path)
    return heading_cache[path]

docs_md = sorted(norm(p) for p in glob.glob('docs/**/*.md', recursive=True))
link_re = re.compile(r'\[[^\]]*\]\(\s*([^)\s]+?)\s*\)')

problems = []
ok = 0
for md in docs_md:
    base = os.path.dirname(md)
    text = open(md, encoding='utf-8').read()
    for m in link_re.finditer(text):
        url = m.group(1)
        if url.startswith(('http://','https://','mailto:','data:')):
            continue
        if '#' not in url:
            continue
        path_part, anchor = url.split('#', 1)
        if not anchor:
            continue
        if path_part == '':
            target_file = md  # intra-doc
        else:
            target_file = norm(os.path.normpath(os.path.join(base, path_part)))
        slugs = get_headings(target_file)
        # reader id is 'h-'+slug; author anchor is the bare slug
        anchor_slug = anchor  # already a slug in these docs
        if anchor_slug in slugs:
            ok += 1
        else:
            problems.append((md, url, target_file, anchor_slug, os.path.isfile(target_file)))

print(f"=== ANCHOR LINK TARGET CHECK ===")
print(f"resolved OK: {ok}")
print(f"problems:    {len(problems)}\n")
for md, url, tf, anc, exists in problems:
    print(f"  LINK: {url}")
    print(f"    in:        {md}")
    print(f"    target md: {tf} (exists={exists})")
    print(f"    anchor slug not found among that file's ## / ### headings: '{anc}'")
    # show near-miss suggestions
    cand = [s for s in get_headings(tf) if anc[:8] in s or s[:8] in anc]
    if cand:
        print(f"    nearest headings: {cand[:4]}")
    print()
