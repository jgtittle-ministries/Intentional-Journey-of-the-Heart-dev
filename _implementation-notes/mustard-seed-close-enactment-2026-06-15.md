# Enactment checklist — Mustard Seed Resolution comment-period close (2026-06-15)

**Trigger:** the V1.Exp8 / V3.Exp3.Open1 (threshold-vs-proportionality) resolution's **14-day public comment period closes 2026-06-15.** This is the small, hand-applied enactment to run on/after close. Nothing auto-enacts — the registries and Research Register are hand-maintained.

## 0. PRECONDITION — confirm before enacting
- Confirm the comment period produced **no objection that changes the synthesis outcome.** Evidentiary trail: `_implementation-notes/mustard-seed-resolution/`.
- **If a substantive objection arrived,** do NOT enact — return it to Council review instead. (This is the real check; the steps below assume a clean close.)

## 1. `vol1-claims.yml` — V1.Exp8
- Confidence is **already `80`** (set 2026-06-01, "effective on close"). Confirm it stays 80 and remove/clean any "effective on close" wording in its `confidence_rationale` so it reads as final, not pending.

## 2. `vol3-claims.yml` — V3.Exp3.Open1  (id at ~line 271; title "Threshold vs. Proportionality — The Mustard Seed Question")
- Change `status: open` → `status: resolved`.
- Annotate with the adopted synthesis: a **quality threshold on genuine trust** (`f()` as a near-step floor), with above-floor magnitude carried by **resonance, authority, and obedient capacity** (`g()`/`h()`), bounded by divine sovereignty.
- **Leave `V3.Exp3.Open2` (the differential "gift of faith," 1 Cor 12:9) OPEN** — it was deliberately preserved as its own question. Do not close it.

## 3. `docs/volume-6-governance/research-register.md`
- Update the `!!! note "Mustard Seed Resolution — in its 14-day comment period · closes 2026-06-15"` admonition: change it to **resolved / Reported** status — V1.Exp8 confirmed at 80, V3.Exp3.Open1 resolved. Move it out of the "Awaiting comment-period close" framing in §3.

## 4. Build + mirror (standard workflow)
- `node C:\Users\jgtit\claude\_work\_gen_search_index.js "<dev repo abs path>"` (the §3 Register edit is a docs change).
- Commit + push **dev**; on review, **mirror to prod** (cp the changed files, regen prod index, `sha256sum` to confirm byte-identical, commit "Mirror … from dev", push).
- Files touched: `vol1-claims.yml`, `vol3-claims.yml`, `docs/volume-6-governance/research-register.md`, `search-index.js`.

## Notes
- Owner: John or JD (Epithetical handles the governance/cron side) — assigned via dev-repo **issue #8**.
- Integrity note: V1.Exp8 already shows 80 *before* close. John reviewed this 2026-06-09 and chose to **let it ride** (treating the comment period as confirmatory). No pre-close registry change.
- On enactment, also consider folding `mustard-seed-resolution/phase-7-gospel-faith-cases-corroboration.md` into the worked-resolution doc **§5 "The witness behind it"** — it was deliberately held out of the under-comment doc during the comment period.
- A one-time reminder fires **2026-06-16 09:00 ET** (morning after close) pointing here.
