# START HERE — Session Handoff, 2026-07-02

*Dev-only working note (never mirrored). Deep detail lives in the auto-loaded memory files — this is the "where we are + what's awaiting John" snapshot.*

---

## ⚡ IMMEDIATE STATE

- **IJH dev HEAD `e8c691d` / prod HEAD `9b55e10`.** **The ENTIRE session's IJH work is UNMIRRORED** — prod is still at the pre-session baseline. A large mirror is pending on John's word.
- **FotH dev `e0d62ac` / prod `29bf83d` — DONE + MIRRORED, in sync** (only the 5 intended dev/prod divergences: 3 IJH-cross-link files + `docs/index.md` DEV banner + `start-here.md`).
- **IJH catalog is now 48 Foundational Laws (38 wide-consent + 10 newer) on DEV**; prod still says 47 until the mirror. **Do NOT "fix" prod's 47 — it's correct pre-mirror.**
- Canonical edition **v5.8** (tag `v5.8-baseline`, both repos). **JD (`Epithetical`) pushes to IJH dev — `git fetch`/rebase before pushing.**

## ⏳ AWAITING JOHN'S DECISION (start here on return)

1. **MIRROR the whole IJH dev batch to prod — the big one.** Everything from `a9525d1` through `e8c691d` is on dev, unreviewed-on-prod. On explicit **"mirror"**: mirror content **and** reader machinery, regenerate prod `search-index.js`, baseline-check each file (dev-pre-edit == prod-current), and preserve the standing dev-only divergences (`docs/index.md` DEV banner; `_implementation-notes/` never mirrored). This is a *large* mirror. What's in the batch:
   - **Meta-law integration program — COMPLETE (all 5 phases + follow-ups).** Minted **FL.XLVIII "The Image-Bearing Law"** (catalog 47→**48**, re-counted corpus-wide); added the **Meta-Law Layer** to the Vol 5 Periodic Table (16-entry cross-registry); named **Scale-Invariance & Transfer** (CLD Rule 7) which resolved the Skill-Development anomaly; wrote the connective essay **"The Image-Bearing Word"** + drew the **Word-Stewardship loop** in the CLD Set; **redrew the CLD map-of-maps** to include it; updated the Research Register. Index-don't-duplicate throughout. Full detail: [[project_ijh_meta_law_integration]].
   - **Mustard Seed resolution propagated** into the teaching chapters (exp-08 Prayer-as-Resonance re-tiered **70→80**; spiritual-force-energy recast trust as an access threshold; Vol 3 Open Trails marked resolved). Exploration-03 left as-is per John.
   - **Vol 3 epilogue:** spiritual distance now operationalized via the **Affective Taxonomy** (linked to Exploration 4).
   - **Reader machinery upgrades (`reader.js` + `reader.html`):** wide-table overflow fix, then upgraded to FotH-parity `.table-scroll` (accessible scroll region, right-edge fade hint, styled scrollbar, mobile full-bleed). **These must go in the mirror.**
2. **Country-of-the-Heart front-piece map** — *still pending from the 2026-07-01 handoff, NOT touched this session.* Dev `8140c50`, unmirrored; awaiting John's metaphor call + review + mirror decision + the printable-handout question. See the 2026-07-01 handoff.
3. **Qualified reviewer for the meta-law dynamical seam** — logged in the Research Register (§5, "held in reserve"), not actioned. A scripturally-grounded mathematical physicist for the Word-Stewardship loop + Scale-Transfer as Vensim/REVEAL stock-flow-delay claims. Doctrine stays at assigned tiers; only the simulation claim waits.
4. **JSFSC — awaiting Porter** (unchanged this session). Foundation resubmitted 2026-06-29; two companions deferred until his decision. See [[project_jsfsc_measuring_maturity_rnr]], [[project_jsfsc_companion_series]].

## ✅ DONE + MIRRORED THIS SESSION (FotH — dev+prod in sync)

- **FotH open-ended-scheduling generalization — COMPLETE across all three series + shared materials.** The pilot is no longer summer→fall→spring: the starting series launches in any term, follow-ons run back-to-back or gapped; season-as-series shorthand → series names (summer→Getting Started, fall→Going Deeper, spring→Going Out); CCA kept as the pilot with a not-CCA-specific note. Narrative/scripture/verbs/life-prompts/college-summer-programs preserved. See [[reference_foth_dev_prod_repos]].
- **FotH fixes:** handbook Formation-Companion reference → live IJH Vol 5 link; a prod→IJH-dev link leak fixed (going-out); the misplaced participant safety footer removed from `start-here.md` (it already lives on all 4 participant materials); **Four Connects diagram added** (week-01 Block 3 + handbook "big idea"; God box = "hearing and connecting with Him"). FotH's reader already had a richer `.table-scroll` than IJH — no change needed there (IJH was upgraded to match it instead).

## ⚠️ WATCH-OUTS / GOTCHAS

- **search-index generator lives at the CLAUDE-level `_work\` (`C:\Users\jgtit\claude\_work\_gen_search_index.js`), needs an ABSOLUTE repo-root path** (`cd /c/Users/jgtit/claude/_work && node _gen_search_index.js "C:/Users/jgtit/claude/_work/<repo>"`). Regenerate after any text change; regenerate on the prod side too during a mirror.
- **manifest.js has TWO structures** (`VOLUME_CHAPTERS` nav + `PATH_TO_INFO` chain) — update both when adding/removing a chapter, then regen search. (FL.XLVIII + the essay were wired into both.)
- **Reader embeds SVG as flat `![](x.svg)` figures** (alt→figcaption). The new SVGs: `docs/volume-1-laws-of-the-spirit/images/word-stewardship-loop.svg`, and the redrawn `docs/volume-3-quantitative-framework/images/cld-map-of-maps.svg`.
- **FotH↔IJH deep links** (relevant only if editing FotH): FotH-dev→IJH-dev, FotH-prod→IJH-prod; the "read the published book" invitation always → IJH-prod.
- **dev-only, never mirror:** `docs/index.md` DEV banner + `_implementation-notes/`.
- `preview_screenshot` times out on the IJH/FotH reader (heavy fixed gradient/backdrop-blur) — verify with `preview_eval`/`preview_inspect` instead.

## 📂 KEY PATHS

- IJH repos: dev `…\_work\Intentional-Journey-of-the-Heart-dev`, prod `…\Intentional-Journey-of-the-Heart`.
- FotH repos: dev `…\_work\fellowship-of-the-heart-pilot-at-cca-dev`, prod `…\fellowship-of-the-heart-pilot-at-cca`.
- JSFSC + design docs: `…\OneDrive\Documents\Intentional Journey of the Heart\IJH edits\`.
- Local preview servers (`.claude/launch.json`): `ijh-dev-static` (8747), `foth-dev-static` (8751).
