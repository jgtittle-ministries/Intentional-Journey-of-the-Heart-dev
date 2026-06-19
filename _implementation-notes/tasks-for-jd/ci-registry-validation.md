# Task for JD — CI validation for the IJH claim registry

**From:** John (via the project's working notes)
**Status:** Implementation complete — ready for final wiring. See "Done looks like" below.
**Good to land before:** the first Council meeting, **2026-06-28** (see "Why now" below).

---

## Context

The *Intentional Journey of the Heart* project keeps its claims in a machine-readable registry — four YAML files at the repo root: `vol1-claims.yml` through `vol4-claims.yml`. Right now nothing checks that new or edited entries conform to the schema, or that the dependency graph stays sane; it is all done by hand.

**Why now.** The project's Council meets for the first time on **June 28** and will vote to ratify the schema. A validator running green *before* that meeting turns the schema vote into a vote on something proven — and would catch any schema bugs ahead of time. This is the CI / technical-co-maintainer task named in Volume 6 Part 1 §13.6.

## Repo

`jgtittle-ministries/Intentional-Journey-of-the-Heart-dev` — work here (**dev-first**), not the prod repo. Same setup as the `nightly-mirror.yml` workflow you already maintain.

## What to build

### 1. A registry-validator script — ✅ DONE

Script is at `_implementation-notes/_schema_audit.py`. It loads all four `vol*-claims.yml` files **together** and enforces the rules in **§8 of the schema spec** at `_implementation-notes/council-meeting-2026-06-28/draft-SCHEMA.md`.

**Implementation notes and corrections from the review:**

- **ID well-formedness**: `FL.{Roman}` entries are strictly checked against `FL.[IVXLC]+`. For `V{n}.*` entries, the format is permissive — uniqueness is enforced but the exact suffix pattern is not constrained, because the existing registry contains many valid variants (e.g., `V1.OE`, `V2.Exp2A`, `V2.Exp9.Open1`, `V4.LotS-H1`, `V4.RQ1`, `V4.OT1`) that would all fail a simplified regex.

- **Pseudo-ID allowlist**: `V{n}.All` wildcards are allowed in dependency fields. **`Formation.HFT`, `Formation.SST`, and `Formation.MSFIG`** are also allowed — they are valid forward-references to the formation program, not broken references. The original brief mentioned only `V{n}.All`; adding `Formation.*` prevents false CI failures.

- **Confidence**: Claims of the world must have `confidence` (0–100) or `confidence_inherited_from`. Types exempt from this requirement: `methodological_principle`, `testable_hypothesis`, `research_question`, `protocol`, `open_trail`, `minority_dissent`, `open_question`.

- **Schema version**: vol2, vol3, and vol4 are at `schema_version: 0.2`, not 0.3. The validator handles this correctly — it validates enumerated fields only when they are present, so older files that legitimately omit v0.3-only PT fields are not penalized.

- **Rule 5 of §8** ("a revised canonical claim retains its prior version as a `formerly_canonical` minority") is **not validated by this script**. It is a workflow invariant, not a structural constraint — it requires comparing the current registry to a prior version, which is a git-history check, not a YAML-schema check. This is an intentional omission; the CI validator enforces rules 1–4 and 6 (rule 6 via `_tier_audit.py`).

### 2. A GitHub Actions workflow — ⚠️ MANUAL STEP REQUIRED

The proposed workflow file is at:
```
_implementation-notes/tasks-for-jd/validate.yml.proposed
```

Copy it to `.github/workflows/validate.yml` and commit. **You must do this via direct git push** — the Claude GitHub App cannot write files in `.github/workflows/` due to GitHub App permission restrictions.

The directory `.github/workflows/` **already contains** `claude.yml` and `claude-code-review.yml`. Add `validate.yml` alongside them.

The workflow runs on `push` and `pull_request`, installs `PyYAML`, and runs:
- `_implementation-notes/_schema_audit.py` — the new registry validator
- `_implementation-notes/_link_audit.py` — orphan files / broken links
- `_implementation-notes/_anchor_audit.py` — heading-anchor link check
- `_implementation-notes/_tier_audit.py` — Foundational Law tier consistency

**All four audit scripts now exit non-zero on failure.** The original brief said "a couple may currently just print" — in fact all three existing scripts had this problem. All three have been fixed.

There is also a fourth audit script (`_implementation-notes/_html_audit.py`) that checks HTML reader-links and `href`/`src` attributes in root `.html` files. It is not included in `validate.yml` since it was not in the original task scope, but wiring it in would be easy if desired.

## Guardrails

- **Structure only — do not edit claim content.** If the current registries fail validation, *report* the specific failures to John; the fix to any claim's data is his / the Council's call, not a CI auto-fix.
- Keep everything on the **dev** repo; don't touch prod or the deploy/mirror workflows.
- These are all **new files** (a script + a workflow), so conflict risk with John's content edits is low — but flag John on anything that touches shared files.

## Done looks like

- `_implementation-notes/_schema_audit.py` — written and committed. ✅
- All three audit scripts now exit non-zero on failure. ✅
- `validate.yml` placed at `.github/workflows/validate.yml` (manual git push). ⬜
- A green `validate.yml` run on a push to dev, OR a clean list of real violations handed to John. ⬜

## Known violations to hand to John

Run `python _implementation-notes/_schema_audit.py` from the repo root to get the current list. At time of writing, at least one known violation exists in the data:

- **`V3.Exp3.Open1` has `status: resolved`** — `resolved` is not in the schema's controlled vocabulary for `status` (`{core, minority, open}`). This entry was marked resolved after the 14-day comment period closed. John / the Council should decide whether to add `resolved` to the vocabulary (a two-thirds vote), or change the entry's status to `open` with a note, or another approach.

Any other violations found by the validator should be treated the same way: data fixes are Council decisions, not CI auto-fixes.
