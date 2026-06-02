# Session handoff — 2026-06-02 (evening)

End-of-session state. **All six repos clean and pushed.** Supersedes the morning `session-handoff-2026-06-02.md`. Two standing project memories carry the durable detail and auto-load next session: `project_fierce_conversations_integration.md` and `project_convene_content_mining.md`.

| Repo | HEAD | Pages |
| --- | --- | --- |
| IJH dev | `dfe97a3` | jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev |
| IJH prod | `04e2b52` | jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart |
| FotH dev | `b357343` | …/fellowship-of-the-heart-pilot-at-cca-dev |
| FotH prod | `3ca2429` | …/fellowship-of-the-heart-pilot-at-cca |
| BSCP dev | `671843c` | …/balanced-scorecard-process-dev |
| BSCP prod | `5870a55` | …/balanced-scorecard-process |

IJH **preview** intentionally untouched (standing "stale until next major revision" rule).

## What shipped this session

1. **Mustard Seed proposal signed + action closed** — `/s/ John G. Tittle` on the Phase-6 proposal; "pending signature" language flipped to "signed and submitted" in the proposal + Research Register. (The 2026-06-15 comment-period routine still runs.) Plus a **process-retrospective** added to `_implementation-notes/mustard-seed-resolution/`.
2. **Fierce Conversations integration — COMPLETE across all three projects, dev + prod** (see `project_fierce_conversations_integration.md`):
   - IJH: **Interrogating Reality** protocol (Vol 5 tool cluster) + **Scott bibliography** entry + **Research Register** trail (§4 #5) + **FL.XLVI Communal Truth-Telling Law** (new Foundational Law, P3/GV — full canonization: FL chapter, manifest, claim YAML, Periodic Table cell/counts/triplet→quartet, Master Law Index, catalog-history admission record) + **Vol 6 catalog-history** entry.
   - FotH: **Interrogating Reality card** (shared materials, anchored to Wk 8).
   - BSCP: **Interrogating Reality appendix** (consulting voice, scripture implicit).
3. **Convene content mining — clusters 1 & 2 done** (see `project_convene_content_mining.md`):
   - **Cluster 1 (Spiritual Intelligence):** Vol 6 **"Genesis of the project"** note (the July-2011 *"Miracles in the Natural"* outline = documented origin; pre-figures the resonance/Mustard-Seed model) + **King SISRI-24** → Vol 5 bibliography.
   - **Cluster 2 (developmental-stage models):** **Beck/Cowan, Joiner, Rooke & Torbert** → Vol 5 Part I bibliography (structural corroboration, not doctrine) + a "transcend-and-include corroborates integration-not-replacement" note in the Vol 5 intro admonition.

## NEXT SESSION — resume here (Convene Cluster 3)

Source library: `C:\Users\jgtit\OneDrive\Documents\A JGT Transformation Engineering\Convene\Content\`. Mode: process one cluster at a time, in order; **investigate → report fit → John decides what to act on** (don't auto-commit content without his nod). Two clusters remain:

- **Cluster 3 — TrueFaced** (`Convene\Content\True Faced\` — affirmation/acceptance/facing-expectations/"am I experiencing acceptance" PDFs). Hypothesis: grace-and-identity formation → the **Trust-Substrate Law (FL.XXXV)**, the **false-self** work (V2.Exp2a), the heart-formation core. (TrueFaced = Thrall/McNicol/Lynch — trust vs. pleasing, the two "rooms.")
- **Cluster 4 — Convene "Processing an Issue"** (`Processing an Issue.doc` + Content Forum's *Issue Identification* / *Goals* / OD Road Map / One2One). Hypothesis: a mature Christian-leader **group-discernment process** → corroborates/extends **FL.XLVI** + the Interrogating Reality protocol + FotH group work.

(Also flagged but not yet triaged: a fuller Fierce corpus in `Firece Material\`/`Church Series\` — the *other* FC principles Be Present / Make It Real / Tackle Tough Challenges, + John's own *Content Interrogating Reality*; John's **HPO Survey** + **CEO Self-Assessment** → BSCP/Vol 4.)

## Working conventions used this session (for the next steward)

- **Mirror discipline:** push to dev first; mirror to prod **diff-first, verbatim** for content/registry files; FotH and BSCP `manifest`/config files have **env-specific divergences** (FotH `build-manifest.mjs` envLabel/repo; BSCP `mkdocs.yml` site_name/url/repo + `custom_dir`) — never whole-copy those; copy the content file + run the repo's own build.
- **IJH search regen:** `node _work/_gen_search_index.js "<ABS repo path>"` (absolute path; run for dev and prod after content changes). 168 chapters currently.
- **IJH `manifest.js`** has TWO objects: `window.VOLUME_CHAPTERS` (volume→chapters list) and `window.PATH_TO_INFO` (per-path nav with prev/next) — hand-edited, both must stay consistent; validate with `node -e "global.window={};require('./manifest.js')"`.
- **FotH** reader manifest is **generated** (`tools/build-manifest.mjs` + `build-search-index.mjs`); register card titles in `tools/titles.mjs` TITLE_OVERRIDES; do NOT hand-edit `manifest.js`.
- **BSCP** is MkDocs (`mkdocs.yml` nav); deploys via `.github/workflows/deploy.yml` on push; verify with `mkdocs build`.
- **PDF text extraction:** `pypdf` is available in the system Python (`C:\Users\jgtit\AppData\Local\Programs\Python\Python313\python`); the Read tool's PDF *image* path fails (no `pdftoppm`) but text-layer PDFs read fine. `.docx` extract via `zipfile`+regex on `word/document.xml`.
- Pages deploy lag is ~36–48s; cache-bust with a `?cb=` query when verifying live. CRLF/LF git warnings are benign.
- Divine-pronoun capitalization applies to IJH/FotH book content (He/Him for Father/Jesus/Spirit); the Hearing-God Papers are the lowercase exception.
