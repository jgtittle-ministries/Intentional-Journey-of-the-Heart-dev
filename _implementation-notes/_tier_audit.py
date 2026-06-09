# Certainty-tier consistency audit for the IJH corpus.
# Confirms each Foundational Law's confidence tier agrees across all four places
# it is stated: the chapter, the Master Law Index, the Periodic Table, and the
# claim registry (vol1-claims.yml). Fixes often land in a chapter but not its
# summaries/registry — this catches that drift. Run after any doctrinal/tier edit.
# In-place: run from the repo (python _implementation-notes/_tier_audit.py).
import re, os, glob

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TIER = {'Clearly Taught': 'CT', 'Reasonably Inferred': 'RI', 'Speculative': 'Spec'}

def conf_to_tier(n):
    n = int(n)
    return 'CT' if n >= 85 else ('RI' if n >= 60 else 'Spec')

chapter = {}
for f in glob.glob('docs/volume-1-laws-of-the-spirit/foundational-law-*.md'):
    t = open(f, encoding='utf-8').read()
    mid = re.search(r'#\s*Foundational Law\s+([IVXLC]+)\s*:', t)
    mt = re.search(r'Certainty:\s*\**\s*(Clearly Taught|Reasonably Inferred|Speculative)', t)
    if mid and mt:
        chapter[mid.group(1)] = TIER[mt.group(1)]

mli = {}
mtext = open('docs/volume-3-quantitative-framework/appendix-master-law-index.md', encoding='utf-8').read()
for m in re.finditer(r'FL\.([IVXLC]+)\b[^\n]*?\[(Clearly Taught|Reasonably Inferred|Speculative)', mtext):
    mli.setdefault(m.group(1), TIER[m.group(2)])

pt = {}
ptext = open('docs/volume-5-references/periodic-table-of-spiritual-laws-a-summing.md', encoding='utf-8').read()
for m in re.finditer(r'FL\.([IVXLC]+)\s*\(Foundational\)[^\n]*?\([VHBI]\),?\s*(Clearly Taught|Reasonably Inferred|Speculative)', ptext):
    pt.setdefault(m.group(1), TIER[m.group(2)])

reg = {}
rtext = open('vol1-claims.yml', encoding='utf-8').read()
for m in re.finditer(r'id:\s*FL\.([IVXLC]+)\b.*?confidence:\s*(\d+)', rtext, re.S):
    reg.setdefault(m.group(1), (int(m.group(2)), conf_to_tier(m.group(2))))

def rval(r):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100}; tot=0
    for i,ch in enumerate(r):
        v=vals[ch]; tot += -v if i+1<len(r) and vals[r[i+1]]>v else v
    return tot

allids = sorted(set(chapter)|set(mli)|set(reg)|set(pt), key=rval)
print(f"{'FL':<7}{'chapter':<9}{'index':<8}{'perTbl':<8}{'registry':<14}  MISMATCH?")
mismatches=[]
for r in allids:
    c=chapter.get(r,'-'); i=mli.get(r,'-'); p=pt.get(r,'-'); rg=reg.get(r)
    rgt=f"{rg[1]}({rg[0]})" if rg else '-'
    tiers={x for x in [c,i,p,(rg[1] if rg else None)] if x and x!='-'}
    flag='X' if len(tiers)>1 else ''
    if flag: mismatches.append(r)
    print(f"FL.{r:<4}{c:<9}{i:<8}{p:<8}{rgt:<14}  {flag}")
print(f"\n{len(mismatches)} tier mismatch(es): {', '.join('FL.'+m for m in mismatches) or 'none'}")
