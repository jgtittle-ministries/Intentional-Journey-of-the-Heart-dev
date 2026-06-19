# Task for JD — CI validation for the IJH claim registry

**From:** John (via the project's working notes)
**Status:** Proposed — ready to pick up. Self-contained; assumes no prior context.
**Good to land before:** the first Council meeting, **2026-06-28** (see "Why now" below).

---

## Context

The *Intentional Journey of the Heart* project keeps its claims in a machine-readable registry — four YAML files at the repo root: `vol1-claims.yml` through `vol4-claims.yml`. Right now nothing checks that new or edited entries conform to the schema, or that the dependency graph stays sane; it is all done by hand.

**Why now.** The project's Council meets for the first time on **June 28** and will vote to ratify the schema. A validator running green *before* that meeting turns the schema vote into a vote on something proven — and would catch any schema bugs ahead of time. This is the CI / technical-co-maintainer task named in Volume 6 Part 1 §13.6.

## Repo

`jgtittle-ministries/Intentional-Journey-of-the-Heart-dev` — work here (**dev-first**), not the prod repo. Same setup as the `nightly-mirror.yml` workflow you already maintain.

## What to build

### 1. A registry-validator script

Suggested path: `_implementation-notes/_schema_audit.py` (matches the existing audit-script convention). It loads all four `vol*-claims.yml` files **together** and enforces the rules in **§8 of the schema spec** — read it at `_implementation-notes/council-meeting-2026-06-28/draft-SCHEMA.md` (this file becomes the repo-root `SCHEMA.md` once the Council ratifies it). The schema's §4 and §7 list the controlled vocabularies.

Rules in brief:

- Every claim `id` is unique within its file and well-formed for its type (`V{vol}.{type}{n}` for axioms / explorations / minorities; `FL.{Roman}` for Foundational Laws).
- Every ID referenced in `upstream_dependencies`, `downstream_dependents`, `minority_positions`, and `parent_claim` resolves to a real entry, **and the dependency graph across all four files is a DAG (no cycles).**
  - Note: `downstream_dependents` may contain wildcard pseudo-IDs like `V1.All` / `V2.All`. Treat those as valid, not as missing references.
- `status`, `type`, and every enumerated field (`directionality`, `band`, `mirror_type`, `operator`, `layer`, `pt_period`, `pt_group`, `gateway`, etc.) hold a value from the controlled vocabulary in the spec. An unknown `type` is a failure.
- Every claim of the world has either `confidence` (integer 0–100) or `confidence_inherited_from`. Vol 4 methodology / instrument entries may have neither.
- Output a clear pass/fail summary and **exit non-zero on any failure** so CI fails.

### 2. A GitHub Actions workflow

Path: `.github/workflows/validate.yml` (the directory exists but is empty). Runs on `push` and `pull_request`, sets up Python, installs `PyYAML`, and runs:

- the new `_schema_audit.py`, and
- the three existing audit scripts in `_implementation-notes/`:
  - `_link_audit.py` — orphan files / manifest-vs-disk / broken `.md`/PDF/image links.
  - `_anchor_audit.py` — every `#fragment` link resolves to a real heading.
  - `_tier_audit.py` — each Foundational Law's certainty tier agrees across the **chapter**, the **Master Law Index**, the **Periodic Table**, and `vol1-claims.yml`.

Check each audit script's invocation (top of file or `--help`) and confirm it **exits non-zero on failure** — a couple may currently just print; if so, add a proper exit code so CI can detect failures.

## Guardrails

- **Structure only — do not edit claim content.** If the current registries fail validation, *report* the specific failures to John; the fix to any claim's data is his / the Council's call, not a CI auto-fix.
- Keep everything on the **dev** repo; don't touch prod or the deploy/mirror workflows.
- These are all **new files** (a script + a workflow), so conflict risk with John's content edits is low — but flag John on anything that touches shared files.

## Done looks like

- A green `validate.yml` run on a push to dev.
- The validator passing against all current claims — or a clean list of any real violations handed to John.
- The three existing audits wired into the same workflow and enforcing (exiting non-zero on failure).
