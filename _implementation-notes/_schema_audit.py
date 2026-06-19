#!/usr/bin/env python3
"""
_schema_audit.py — IJH claim-registry schema validator.

Enforces the rules in §8 of the schema spec at:
  _implementation-notes/council-meeting-2026-06-28/draft-SCHEMA.md

Run from repo root:
  python _implementation-notes/_schema_audit.py

Exits non-zero if any violations are found so CI can detect failure.
Does NOT modify claim data — violations are reported for John / the Council.
"""
import sys, os, re, glob
import yaml

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------------------------------------------------------------------------
# Controlled vocabularies (spec §4 and §7)
# ---------------------------------------------------------------------------
VALID_STATUSES = {'core', 'minority', 'open'}

VALID_TYPES = {
    # Claims of the world (Vol 1–3)
    'axiom', 'opening_exploration', 'structural_law', 'operational_law',
    'foundational_law', 'diagnostic_law', 'developmental_law', 'dynamic_law',
    'kinematic_law', 'eschatological_law', 'gateway_law', 'modeling_law',
    'tool_application_law', 'governing_premise', 'structural_and_operational_law',
    'quantitative', 'qualitative', 'qualitative_visual', 'analytical_equation',
    'conservation_hypothesis', 'mixed',
    # Dissent & inquiry
    'minority_dissent', 'open_question',
    # Methodology (Vol 4)
    'methodological_principle', 'testable_hypothesis', 'research_question',
    'protocol', 'open_trail',
}

# Types that may omit both confidence and confidence_inherited_from.
# Vol 4 methodology types and dissent/inquiry entries are exempt per spec §3.
CONFIDENCE_EXEMPT_TYPES = {
    'methodological_principle', 'testable_hypothesis', 'research_question',
    'protocol', 'open_trail', 'minority_dissent', 'open_question',
}

# Types that don't carry a `status` field in current data (use status_in_v4 etc.)
STATUS_EXEMPT_TYPES = {'open_trail', 'research_question', 'protocol'}

VALID_DIRECTIONALITY = {'V', 'H', 'B', 'I'}
VALID_MIRROR_TYPE = {
    'statement', 'constitutive', 'constitutive_bidirectional',
    'christological_condition', 'orientation_neutral',
}
VALID_OPERATOR = {'P', 'S+P', 'C', 'C+P', 'T+P', 'C+T'}
VALID_LAYER = {'substrate', 'operation'}
VALID_PT_PERIOD = {'P0', 'P1', 'P2', 'P3', 'P4', 'P5'}
VALID_PT_GROUP = {'GI', 'GII', 'GIII', 'GIV', 'GV', 'GVI'}

# Enumerated fields: only validated when the field is actually present.
ENUM_FIELDS = {
    'directionality': VALID_DIRECTIONALITY,
    'mirror_type': VALID_MIRROR_TYPE,
    'operator': VALID_OPERATOR,
    'layer': VALID_LAYER,
    'pt_period': VALID_PT_PERIOD,
    'pt_group': VALID_PT_GROUP,
}

# ---------------------------------------------------------------------------
# Pseudo-ID allowlist for dependency fields
# ---------------------------------------------------------------------------
# V{n}.All — wildcard "depends on all claims in volume n"
# Formation.* — forward-references to the formation program (out-of-scope IDs)
PSEUDO_ID_RE = re.compile(r'^(V[1-4]\.All|Formation\.\w+)$')

# Well-formed FL.{Roman}: roman numeral characters only
FL_ID_RE = re.compile(r'^FL\.[IVXLC]+$')

# Well-formed V{n}.*: starts with V1–V4 prefix
VN_ID_RE = re.compile(r'^V[1-4]\.')

# ---------------------------------------------------------------------------
# Dependency fields to validate for reference resolution (§8 rule 2)
# ---------------------------------------------------------------------------
DEP_FIELDS = ('upstream_dependencies', 'downstream_dependents', 'minority_positions')

# ---------------------------------------------------------------------------
# Collect failures and warnings
# ---------------------------------------------------------------------------
failures = []
warnings = []

def fail(msg):
    failures.append(msg)

def warn(msg):
    warnings.append(msg)

# ---------------------------------------------------------------------------
# Load all four registry files
# ---------------------------------------------------------------------------
registry_files = sorted(glob.glob('vol[1-4]-claims.yml'))
if len(registry_files) != 4:
    print(f"ERROR: Expected 4 vol*-claims.yml files at repo root, found {len(registry_files)}: {registry_files}")
    sys.exit(1)

all_claims = {}   # id -> claim dict with '_source_file' key added
per_file_ids = {} # filepath -> set of ids in that file

for filepath in registry_files:
    with open(filepath, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    claims_list = data.get('claims') or []
    file_ids = set()
    per_file_ids[filepath] = file_ids

    for claim in claims_list:
        cid = claim.get('id')
        if not cid:
            fail(f"[{filepath}] Claim missing 'id' field: title={claim.get('title', '<none>')}")
            continue

        if cid in file_ids:
            fail(f"[{filepath}] Duplicate id within file: '{cid}'")
        file_ids.add(cid)

        if cid in all_claims:
            warn(f"id '{cid}' appears in both {all_claims[cid]['_source_file']} and {filepath}")

        entry = dict(claim)
        entry['_source_file'] = filepath
        all_claims[cid] = entry

all_ids = set(all_claims.keys())

# ---------------------------------------------------------------------------
# §8 Rule 1 — ID well-formedness
# ---------------------------------------------------------------------------
for cid in all_ids:
    src = all_claims[cid]['_source_file']
    if FL_ID_RE.match(cid):
        pass  # FL.{Roman} — strict format; regex is the full check
    elif VN_ID_RE.match(cid):
        pass  # V{n}.* — permissive; uniqueness enforced above, pattern is open
    else:
        fail(f"[{src}] Malformed id '{cid}' — expected FL.{{Roman}} or V{{1-4}}.{{...}}")

# ---------------------------------------------------------------------------
# §8 Rule 2 — Reference resolution and DAG (no cycles)
# ---------------------------------------------------------------------------
def is_valid_ref(ref_id):
    return ref_id in all_ids or bool(PSEUDO_ID_RE.match(ref_id))

# Build upstream-dependency graph for cycle detection.
# Only upstream_dependencies form directed edges (A depends on B → edge A→B).
dep_graph = {cid: set() for cid in all_ids}

for cid, claim in all_claims.items():
    src = claim['_source_file']

    for field in DEP_FIELDS:
        refs = claim.get(field) or []
        if isinstance(refs, str):
            refs = [refs]
        for ref in refs:
            if not is_valid_ref(ref):
                fail(f"[{src}] {cid}: unresolved reference in '{field}': '{ref}'")

    parent = claim.get('parent_claim')
    if parent and not is_valid_ref(parent):
        fail(f"[{src}] {cid}: unresolved 'parent_claim': '{parent}'")

    upstream = claim.get('upstream_dependencies') or []
    if isinstance(upstream, str):
        upstream = [upstream]
    for dep in upstream:
        if dep in all_ids:  # only real IDs form edges; pseudo-IDs are skipped
            dep_graph[cid].add(dep)

# Cycle detection via iterative DFS (avoids Python recursion-limit issues)
def find_cycles(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    found = []

    for start in sorted(graph):
        if color[start] != WHITE:
            continue
        stack = [(start, iter(sorted(graph.get(start, []))))]
        path = [start]
        color[start] = GRAY

        while stack:
            node, neighbors = stack[-1]
            try:
                nxt = next(neighbors)
                if nxt not in color:
                    continue
                if color[nxt] == GRAY:
                    idx = path.index(nxt)
                    cycle = path[idx:] + [nxt]
                    if cycle not in found:
                        found.append(cycle)
                elif color[nxt] == WHITE:
                    color[nxt] = GRAY
                    path.append(nxt)
                    stack.append((nxt, iter(sorted(graph.get(nxt, [])))))
            except StopIteration:
                color[node] = BLACK
                stack.pop()
                if path and path[-1] == node:
                    path.pop()

    return found

cycles = find_cycles(dep_graph)
for cycle in cycles:
    fail(f"Dependency cycle detected: {' -> '.join(cycle)}")

# ---------------------------------------------------------------------------
# §8 Rule 3 — Controlled vocabulary: type, status, enumerated fields
# ---------------------------------------------------------------------------
for cid, claim in all_claims.items():
    src = claim['_source_file']

    # type — unknown type is a failure per spec §7
    ctype = claim.get('type')
    if ctype not in VALID_TYPES:
        fail(f"[{src}] {cid}: unknown type '{ctype}' — must be ratified per spec §7")

    # status — required for most types; some Vol 4 types use status_in_v4 instead
    status = claim.get('status')
    if status is not None:
        if status not in VALID_STATUSES:
            fail(f"[{src}] {cid}: invalid status '{status}' — must be one of {sorted(VALID_STATUSES)}")
    elif ctype not in STATUS_EXEMPT_TYPES:
        warn(f"[{src}] {cid}: missing 'status' field (expected one of {sorted(VALID_STATUSES)})")

    # band — 1, 2, 3, or null
    band = claim.get('band')
    if band is not None and band not in (1, 2, 3):
        fail(f"[{src}] {cid}: invalid 'band' value '{band}' — must be 1, 2, 3, or null")

    # gateway — boolean only
    gateway = claim.get('gateway')
    if gateway is not None and not isinstance(gateway, bool):
        fail(f"[{src}] {cid}: 'gateway' must be true/false, got {gateway!r}")

    # other enumerated fields (validated only when present — optional for non-FL entries)
    for field, valid_set in ENUM_FIELDS.items():
        val = claim.get(field)
        if val is not None and val not in valid_set:
            fail(f"[{src}] {cid}: invalid '{field}' value '{val}' — valid: {sorted(str(v) for v in valid_set)}")

# ---------------------------------------------------------------------------
# §8 Rule 4 — confidence or confidence_inherited_from for claims of the world
# ---------------------------------------------------------------------------
for cid, claim in all_claims.items():
    src = claim['_source_file']
    ctype = claim.get('type')

    if ctype in CONFIDENCE_EXEMPT_TYPES:
        continue  # Vol 4 methodology / dissent / inquiry entries are exempt

    has_confidence = ('confidence' in claim) and (claim['confidence'] is not None)
    has_inherited = bool(claim.get('confidence_inherited_from'))

    if has_confidence:
        conf = claim['confidence']
        if not isinstance(conf, int) or not (0 <= conf <= 100):
            fail(f"[{src}] {cid}: 'confidence' must be integer 0–100, got {conf!r}")
    elif not has_inherited:
        fail(f"[{src}] {cid}: claim of the world (type='{ctype}') must have "
             f"'confidence' (0–100) or 'confidence_inherited_from'")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print()
print("=" * 64)
print("  IJH Registry Schema Audit — §8 Validation")
print("=" * 64)
print(f"  Files : {', '.join(registry_files)}")
print(f"  Claims: {len(all_claims)} total across all files")
print()

if warnings:
    print(f"WARNINGS ({len(warnings)})")
    for w in warnings:
        print(f"  WARN  {w}")
    print()

if failures:
    print(f"FAILURES ({len(failures)})")
    for msg in failures:
        print(f"  FAIL  {msg}")
    print()
    print(f"RESULT: FAILED — {len(failures)} violation(s). "
          f"Fix or refer to John / the Council before ratification.")
    sys.exit(1)

print("RESULT: PASSED — all §8 rules satisfied.")
sys.exit(0)
