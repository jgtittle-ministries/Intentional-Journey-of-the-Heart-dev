# Repository Hygiene — v5_6_0_20 Push Package

This push package implements the v5_6_0_20 consistency-edit pass on the IJH repository, addressing the **repository hygiene** findings from the Phase 1 consistency report — specifically F7 (revised), F16, and F17. The pass is the third and final of the three consistency-edit push packages identified at Phase 1; v5_6_0_18 (Vol 5 PT chapter refresh) and v5_6_0_19 (Vol 3 refresh) have already landed.

The pass operates on the live repository rather than on any specific content chapter. The pass has three concerns:

1. **Orphan file deletion (F16, F7 revised):** Ten obsolete Vol 1 overview files remain reachable at their URLs on production. Each presents a pre-expansion-arc headline count to any reader who lands on its URL ("Thirteen Operational Laws," "Seventeen Operational Laws," etc.) — counts that contradict the catalog's current state of thirty-eight Foundational Laws. The files were superseded by the canonical `foundational-laws-thirty-eight-operational-laws-of-wide` file but were never removed when the catalog grew past their counts.

2. **MkDocs nav verification (F17):** The mkdocs left navigation has been observed to be inconsistent across pages on production — the canonical "Thirty-Eight" link appears on pages that were re-touched during recent push sequences (v5_6_0_14 through v5_6_0_19), while pages not re-touched still showed the older "Thirteen" link in their nav. The likely cause is that mkdocs only re-renders the nav into each page's HTML when the source markdown is touched. The v5_6_0_18 and v5_6_0_19 pushes will have refreshed many pages, but a force-rebuild is the canonical fix to ensure all pages' nav HTML matches the canonical mkdocs.yml configuration.

3. **Force rebuild (F17):** After deletions and any mkdocs.yml updates, the package specifies a full `mkdocs build --clean` operation (or equivalent) to ensure the published site reflects the deletions and the consistent canonical nav across every page.

The pass does not modify any chapter content. The pass does not modify any content the readers receive when they reach a canonical URL. The pass only removes orphan URLs that should not be reachable and ensures the navigation across all canonical URLs is consistent.

## Operations

The operations are sequenced; each step's verification must pass before proceeding to the next:

### Step 1 — Pre-deletion verification

For each of the ten orphan files listed below, verify the URL is currently live (returns 200 with content) on production. If any URL already returns 404, the file may have been deleted in a prior operation — flag it for review but proceed (the deletion is a no-op for that file).

| # | File (in `docs/volume-1-laws-of-the-spirit/`) | Production URL |
|---|---|---|
| 1 | `foundational-laws-thirteen-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirteen-operational-laws-of-wide/ |
| 2 | `foundational-laws-seventeen-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-seventeen-operational-laws-of-wide/ |
| 3 | `foundational-laws-twenty-one-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-one-operational-laws-of-wide/ |
| 4 | `foundational-laws-twenty-two-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-two-operational-laws-of-wide/ |
| 5 | `foundational-laws-twenty-six-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-six-operational-laws-of-wide/ |
| 6 | `foundational-laws-twenty-seven-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-seven-operational-laws-of-wide/ |
| 7 | `foundational-laws-twenty-eight-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-eight-operational-laws-of-wide/ |
| 8 | `foundational-laws-thirty-two-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirty-two-operational-laws-of-wide/ |
| 9 | `foundational-laws-thirty-three-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirty-three-operational-laws-of-wide/ |
| 10 | `foundational-laws-thirty-four-operational-laws-of-wide.md` | https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirty-four-operational-laws-of-wide/ |

The canonical file `foundational-laws-thirty-eight-operational-laws-of-wide.md` is **NOT** in the deletion list — it is the current canonical overview at v5_6_0_17 state and is what the canonical nav reference should point to.

**Verification command (use this or equivalent):**

```bash
for url in \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirteen-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-seventeen-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-one-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-two-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-six-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-seven-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-twenty-eight-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirty-two-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirty-three-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirty-four-operational-laws-of-wide/" ; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  echo "$code  $url"
done
```

Expected output before deletion: each row should return `200`. After deletion + rebuild, each row should return `404`. The same script run twice (before and after) produces the verification record.

### Step 2 — File deletion from repository source

Locate the orphan files in the repository source. Per the canonical mkdocs project layout, they should be in `docs/volume-1-laws-of-the-spirit/`. Confirm presence:

```bash
cd <repo-root>
ls docs/volume-1-laws-of-the-spirit/foundational-laws-*-operational-laws-of-wide.md
```

Expected: eleven files (the ten orphans plus the canonical `foundational-laws-thirty-eight-operational-laws-of-wide.md`).

Delete the ten orphan files. Use `git rm` to preserve the deletion in version history:

```bash
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-thirteen-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-seventeen-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-twenty-one-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-twenty-two-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-twenty-six-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-twenty-seven-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-twenty-eight-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-thirty-two-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-thirty-three-operational-laws-of-wide.md
git rm docs/volume-1-laws-of-the-spirit/foundational-laws-thirty-four-operational-laws-of-wide.md
```

Confirm only the canonical file remains:

```bash
ls docs/volume-1-laws-of-the-spirit/foundational-laws-*-operational-laws-of-wide.md
```

Expected: one file — `foundational-laws-thirty-eight-operational-laws-of-wide.md`.

### Step 3 — mkdocs.yml nav verification

Open `mkdocs.yml` at the repository root and locate the Volume 1 nav section. The Foundational Laws overview entry should reference only the canonical thirty-eight file:

**Expected (canonical):**

```yaml
- "Foundational Laws: Thirty-Eight Operational Laws of Wide Consent": volume-1-laws-of-the-spirit/foundational-laws-thirty-eight-operational-laws-of-wide.md
```

If any of the deleted file references remain in `mkdocs.yml` (e.g., a residual line referencing `foundational-laws-thirteen-...md`), remove those references. The mkdocs build will fail if `mkdocs.yml` references a file that does not exist, so any stale references must be cleaned up before the build proceeds.

**Verification command:**

```bash
grep -E "foundational-laws-(thirteen|seventeen|twenty-one|twenty-two|twenty-six|twenty-seven|twenty-eight|thirty-two|thirty-three|thirty-four)" mkdocs.yml
```

Expected: no matches. If any match, remove the matching line(s) from `mkdocs.yml`.

Confirm the canonical reference is present and well-formed:

```bash
grep -E "foundational-laws-thirty-eight-operational-laws-of-wide" mkdocs.yml
```

Expected: exactly one match.

### Step 4 — Force clean mkdocs rebuild

Force a full rebuild of the mkdocs site to ensure all pages' nav HTML is regenerated and the deletions are reflected in the build output:

```bash
cd <repo-root>
mkdocs build --clean
```

The `--clean` flag deletes the `site/` directory before rebuilding, ensuring no stale HTML from prior builds remains. After the rebuild completes, verify the build succeeded without warnings about missing files:

```bash
mkdocs build --clean 2>&1 | grep -iE "WARNING|ERROR" || echo "Clean build — no warnings or errors"
```

### Step 5 — Commit and deploy

Commit the deletions and any mkdocs.yml changes:

```bash
git add -A
git commit -m "v5_6_0_20: Repository hygiene — delete 10 orphan Vol 1 overview files; force clean mkdocs rebuild

- Deletes foundational-laws-thirteen-operational-laws-of-wide.md (F16)
- Deletes nine additional intermediate-count overview files (F7 revised):
  seventeen, twenty-one, twenty-two, twenty-six, twenty-seven, twenty-eight,
  thirty-two, thirty-three, thirty-four
- Verifies mkdocs.yml references only the canonical thirty-eight file
- Forces clean mkdocs rebuild to refresh stale-nav HTML on all pages (F17)

Closes the three-package consistency-edit pass (v5_6_0_18 Vol 5 PT chapter
refresh, v5_6_0_19 Vol 3 refresh, v5_6_0_20 repository hygiene) identified
at Phase 1 of the consistency-edit pass against v5_6_0_17 catalog state."
git push
```

Deploy to GitHub Pages per the repository's standard deployment workflow.

### Step 6 — Post-deployment verification

After the GitHub Pages deployment completes (usually 1–3 minutes after push), re-run the verification script from Step 1:

```bash
for url in \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-thirteen-operational-laws-of-wide/" \
  "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-1-laws-of-the-spirit/foundational-laws-seventeen-operational-laws-of-wide/" \
  ... [same list as Step 1] ... ; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  echo "$code  $url"
done
```

Expected output: each row should return `404`. If any row returns `200`, the deletion did not propagate — investigate the build output and the deployment pipeline.

Spot-check three canonical pages for nav consistency:

```bash
# Home page
curl -s "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/" | grep "foundational-laws" | head -5

# Vol 5 PT chapter (previously had stale "Thirteen" link per F17)
curl -s "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-5-references/periodic-table-of-spiritual-laws-a-summing/" | grep "foundational-laws" | head -5

# Vol 3 Master Law Index (refreshed at v5_6_0_19, should have canonical nav)
curl -s "https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/volume-3-quantitative-framework/appendix-master-law-index/" | grep "foundational-laws" | head -5
```

Expected on each: nav references should all point to `foundational-laws-thirty-eight-operational-laws-of-wide` (or to specific FL chapter URLs). No references to `foundational-laws-thirteen` (or any of the intermediate-count names) should appear in any page's HTML.

## Verification checklist

After all six steps complete:

1. **Pre-deletion verification recorded:** Output of Step 1 verification script captured — confirms which of the ten URLs were live before deletion.
2. **All ten orphan files removed from repo source:** `ls docs/volume-1-laws-of-the-spirit/foundational-laws-*-operational-laws-of-wide.md` returns one file (the canonical thirty-eight).
3. **mkdocs.yml verified canonical:** No references to deleted files; one reference to the canonical thirty-eight file.
4. **Clean rebuild succeeded:** `mkdocs build --clean` completed without warnings about missing files.
5. **Commit recorded:** Single commit with descriptive message landing all ten deletions and any mkdocs.yml updates.
6. **GitHub Pages deploy completed:** Site live with the new build.
7. **Post-deployment URL verification:** All ten orphan URLs return `404`; canonical thirty-eight URL returns `200`.
8. **Nav consistency confirmed:** Spot-check on home page, Vol 5 PT chapter, and Vol 3 MLI page shows canonical `thirty-eight` nav references; no `thirteen` or intermediate-count references appear.

## Manifest entry

Append the following line to the implementation manifest (e.g., `PUSH_MANIFEST.md` or equivalent):

```
v5_6_0_20 | 2026-05-22 | Repository hygiene — delete 10 orphan Vol 1 overview files; force clean mkdocs rebuild | Deletes foundational-laws-{thirteen,seventeen,twenty-one,twenty-two,twenty-six,twenty-seven,twenty-eight,thirty-two,thirty-three,thirty-four}-operational-laws-of-wide.md; verifies mkdocs.yml canonical nav; force clean rebuild to refresh stale-nav HTML | Closes the three-package consistency-edit pass against v5_6_0_17 catalog state
```

## End of v5_6_0_20 Push Package

After the six steps complete and the verification checklist passes, the v5_6_0_20 push is complete. This is also the final push of the three-package consistency-edit pass identified at Phase 1 (v5_6_0_18 Vol 5 PT chapter refresh; v5_6_0_19 Vol 3 refresh; v5_6_0_20 repository hygiene). The repository at v5_6_0_20 reflects the catalog's v5_6_0_17 state across all canonical content surfaces, with no orphan URLs reachable, and consistent navigation across all pages.

## Residual items from Phase 1 not addressed by the three push packages

The following items were identified in the Phase 1 consistency-pass findings but were not scoped into v5_6_0_18 through v5_6_0_20. They are smaller-scope items that may be addressed as targeted future passes if subsequent review confirms they warrant attention:

- **S2 (Category G):** Period 0 row FL chapters (FL.I, FL.XV, FL.XVI, FL.XXIII, FL.X, FL.IX, FL.VI) predate the row's completion and may not name the row-completion pattern. Marked as "stale but contextually understandable" rather than factually false, since each chapter is articulating its own admission, not the row's overall state. Likely non-finding.

- **S3 (Category E):** Cross-references not yet added to older FL chapters. The two cross-reference files (`cross-references-v566.md` and `cross-references-to-existing-FL-chapters.md`) describe edits to FL.III, FL.V, FL.VI, FL.VIII, FL.XVII; as the catalog grew, additional cross-references may now be warranted. Spot-check needed: verify whether the published FL.III chapter cross-references the newer FL.XXXV–XXXVIII admissions; if not, generate a v5_6_0_21 cross-references delta document.

- **D1 (Category K):** Scripture citation format consistency. Spot check suggests already consistent; full audit deferred.

- **Phase 1 deferred audit scope:**
  - Vol 1 explorations (8 chapters + supplementals) — not checked
  - Vol 1 opening "What We Are Being Formed For" chapter — not checked
  - Vol 1 closing "A Word to My Kids at the End of This Volume" chapter — not checked (note: spot-check in Phase 1C found no catalog claims)
  - Vol 1 "Taxonomy Key" — not checked, likely currency-sensitive
  - Vol 1 "Connecting the Dots" exploration synthesis — not checked
  - Vol 1 FL.I through FL.XIII chapters — not checked
  - Full Vol 2 — not checked; likely targets: Tool Map (Exp 6), Training Plan (Exp 10), cross-references to Vol 1 laws
  - Full Vol 4 — not checked beyond Section 1 spot-check
  - Vol 6 — not checked

If a subsequent pass over the deferred scope surfaces additional findings, they would constitute a separate consistency-edit pass at a future revision (v5_6_0_21 or later).
