import re, os, glob
from urllib.parse import unquote

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def norm(p):
    return p.replace('\\', '/')

manifest = open('manifest.js', encoding='utf-8').read()
manifest_paths = set(norm(p) for p in re.findall(r'"path":\s*"([^"]+)"', manifest))

html_files = sorted(glob.glob('*.html'))
print("ROOT HTML FILES:", html_files)
print()

missing_file = []
not_in_manifest = []
broken_local_href = []
checked = 0

for hf in html_files:
    text = open(hf, encoding='utf-8').read()
    for m in re.finditer(r'(?:href|src)\s*=\s*"([^"]+)"', text):
        raw = m.group(1)
        if raw.startswith(('http://','https://','mailto:','#','data:','//')):
            continue
        # reader.html#docs%2F... style -> the fragment is the real content path
        if 'reader.html#' in raw:
            frag = raw.split('#',1)[1]
            decoded = norm(unquote(frag)).split('?',1)[0]
            checked += 1
            if not os.path.isfile(decoded):
                missing_file.append((hf, raw, decoded))
            elif decoded not in manifest_paths:
                not_in_manifest.append((hf, decoded))
        else:
            # plain relative href to a local asset/page
            path_part = norm(unquote(raw.split('#',1)[0].split('?',1)[0]))
            if not path_part:
                continue
            checked += 1
            if not os.path.isfile(path_part):
                broken_local_href.append((hf, raw, path_part))

print("=== HTML reader-links whose target FILE is missing ===")
for hf, raw, dec in missing_file:
    print(f"  {hf}: {raw}\n     -> {dec}")
print(f"  ({len(missing_file)} missing)\n")

print("=== HTML reader-links whose target exists but is NOT in manifest ===")
for hf, dec in not_in_manifest:
    print(f"  {hf}: {dec}")
print(f"  ({len(not_in_manifest)} not-in-manifest)\n")

print("=== HTML plain hrefs to missing local files ===")
for hf, raw, pp in broken_local_href:
    print(f"  {hf}: {raw} -> {pp}")
print(f"  ({len(broken_local_href)} broken)\n")

print(f"--- checked {checked} HTML local links ---")
