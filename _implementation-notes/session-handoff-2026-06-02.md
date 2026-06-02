# Session handoff — 2026-06-02

End-of-thread state across the IJH + FotH repos. All four repos are **clean and pushed**; nothing is left uncommitted.

| Repo | HEAD | Pages |
| --- | --- | --- |
| IJH dev (`…-dev`) | `b0edd30` | jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev |
| IJH prod (`Intentional-Journey-of-the-Heart`) | `d243158` | jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart |
| FotH dev (`…-cca-dev`) | `64f5db4` | — |
| FotH prod (`…-cca`) | `60ee6f8` | — |

IJH **preview** repo was intentionally **not** touched this session (standing "stays stale until next major revision" rule).

## What shipped this session

1. **Reader anchor fix** — the reader never split a `#anchor` off the chapter path, so all 56 in-content anchor links were broken (cross-doc → "Chapter not found"; bare → dead-ends). Fixed in `reader.js` (split anchor, scroll to `h-`+slug, anchor-link class, delegated instant-scroll). IJH dev `43a2d53` → prod `f132675`.
2. **FotH reader brought up to date** — applied the same anchor fix, then spliced IJH's current markdown engine into FotH's (FotH's was an older snapshot) + ported the PDF-popup modal + CSS. FotH uses a *different* manifest API, so never whole-file-copy IJH's reader onto it — only the engine IIFE is interchangeable. FotH dev `4fab30c`/`64f5db4`.
3. **Open-trail pointers** — Vol 3 Open Trails + Vol 4 §5e now point to the Hearing-God Papers that advance them (OT-1→MSM, OT-4→CSM/CTG/BFP, OT-8→CTG; Minimum-Factor→CTG).
4. **Vol 6 Research Register** — new Council chapter (`docs/volume-6-governance/research-register.md`): a living register of investigations underway / recommended / proposed, two prioritization lenses, the one-bet recommendation. Wired into manifest, index, the hand-styled `Volume 6 Governance.html` "Further Council Documents" links, search.
5. **Mustard Seed investigation** — full Phase 0–6 analysis + an independent adversarial pass, in `_implementation-notes/mustard-seed-resolution/`. Conclusion: **Model B (proportionality) rejected; Model C adopted** (genuine faith = a quality threshold; above-floor magnitude via resonance/authority/obedient-capacity; bounded by sovereignty). Enacted in the claim registry (`vol1`/`vol3` YAML): V1.Exp8 70→80 (effective on comment close), V3.Exp3.Open1 in comment period, V3.Exp3 into the research-program track, new V3.Exp3.Open2 (gift-of-faith), V3.Exp8 corroborated.
6. **Worked-resolution chapter** — `docs/volume-6-governance/mustard-seed-worked-resolution.md`: reader-visible backstory + rationale, framed as the template for future open-question resolutions.
7. **Logo — "The Resonant Heart"** — `favicon.svg` / `logo-mark.svg` / `logo-roundel.svg`; favicon + an inline theme-adaptive SVG mark (replacing the crest dot) on all nine pages. IJH dev `2a10a2e` → prod `325dbf4`. See [[reference-ijh-logo-and-html-mirror-gotcha]] — **all IJH `*.html` carry a per-repo "Repo" link, so dev→prod HTML must be transformed in place, never `cp`-copied.**
8. **"Load-bearing" consistency pass** — reserved the technical term (Vol 3 analogy-class, Vol 6 §8, YAML schema) and varied the 22 narrative-prose uses.
9. **Research Register restructure** — Mustard Seed moved from §5 (reserve) to §3 Underway → "Awaiting comment-period close" callout. dev `b0edd30` / prod `d243158`.

## Open / pending (carry into next session)

- **Scheduled routine fires 2026-06-15 16:00 UTC** (id `trig_01TtC1ahUvy8GrzEeUqLSqdj`, manage at https://claude.ai/code/routines/trig_01TtC1ahUvy8GrzEeUqLSqdj): closes the Mustard Seed comment period — flips V3.Exp3.Open1 to resolved, confirms V1.Exp8 at 80, retitles the register admonition to "RESOLVED 2026-06-15" + renames the sub-heading to "Recently resolved", mirrors dev→prod. Remote sonnet agent; has a safety check (aborts if it finds a blocking objection in dev git log).
- **After 2026-06-15:** the routine defers `search-index.js` regeneration (its generator lives outside the repo) — run `node _work/_gen_search_index.js <abs repo path>` once locally for dev and prod to refresh the register chapter's search text.
- **Mustard Seed proposal** (`_implementation-notes/mustard-seed-resolution/phase-6-proposal-resolution.md`) is submission-ready; the only human gap is **John's signature** (the `[John: sign]` line). John is the sponsor; §3b is his witness.
- **Other recommended trails** (not started): OT-1 Affective-Taxonomy Measurement Protocol (the keystone, run in the FotH pilot) + the attachment-substrate correlation (near-free second result); OT-6 collective formation; the Minimum-Factor Protocol. See the Research Register.
- **Optional design tweak** offered on the logo (smoother resonance wave / heart/stroke sizing) — John was going to look at it live first.

## Useful pointers
- Reusable link/anchor audit scripts: `_implementation-notes/_link_audit.py`, `_html_audit.py`, `_anchor_audit.py` (run from repo root) — for the recurring "no broken links" check.
- search-index regen: `node _work/_gen_search_index.js "<abs path to repo>"` (pass an ABSOLUTE path; relative breaks the require()).
- Mirror discipline: `reader.js`/`app.js`/`styles.css`/`manifest.js`/claim-YAMLs mirror verbatim (diff-first); the `*.html` pages do NOT (per-repo Repo link); `Volume 6 Governance.html` is hand-styled and must be edited in place for any new Vol 6 chapter (its "Further Council Documents" links).
- Screenshot note: the Claude_Preview screenshot tool was flaky this session (frequent timeouts on healthy pages); DOM/computed-style evals were the reliable verification path, and the preview browser caches `reader.js`/`styles.css` per origin (bump the `http.server` port to load fresh JS/CSS).
