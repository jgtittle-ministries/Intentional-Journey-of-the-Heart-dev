# START HERE — Session Handoff, 2026-07-01

*Dev-only working note (never mirrored). Deep detail lives in the auto-loaded memory files — this is the "where we are right now + what's awaiting John" snapshot.*

---

## ⚡ IMMEDIATE STATE

- **IJH dev HEAD `8140c50` / prod HEAD `9b55e10`.**
- **ONE thing unmirrored:** the new front-piece **"Country of the Heart" map** (dev `8140c50`). Everything else this session is already mirrored + in sync.
- **JD (`Epithetical`) pushes to dev — always `git fetch` / rebase before pushing.** Surface conflicts to John.
- **Mirror discipline:** push to dev only; mirror to prod **ONLY** on John's explicit "mirror." Baseline-check each file (dev-pre-edit == prod-current) + verify staged==dev.
- **Canonical edition = v5.8**, tag `v5.8-baseline` in both repos (dev `76794f0` / prod `107746e`). Old `v5.7.2-baseline` kept as historical. See [[reference_ijh_version_baseline]].

## ⏳ AWAITING JOHN'S DECISION (start here on return)

1. **The front-piece map (dev `8140c50`, UNMIRRORED).** New Introduction chapter `docs/introduction/how-to-read-this-book-the-map.md` + SVG + manifest/search-index wiring. John was about to review it live on dev. **Three open questions:**
   - Does the map read cleanly at dev-site width + land for a 15–16 y/o?
   - Is **"Country of the Heart"** the right central metaphor, or try a more biblical one (journey to the wedding feast / river system / the body growing up)?
   - Then: **"mirror"** to prod? And does he want the **one-page printable handout** (teen 5-sentences + parent guide)?
2. **The meta-law layer / candidate-law program (3 design docs in `…\IJH edits\`, PROPOSAL-ONLY, nothing edits the manuscript yet).** John's call on whether/how to implement:
   - `IJH_Vol1_Law_Expansion_and_Table_Test_v1.docx` — stress-test: the Word-Stewardship cycle is a **meta-law**, not a peer-row; recommends **one** atomic new element, the **Voiced-Word Law (candidate FL.XLVIII)**, + hold the cycle as a connective essay.
   - `IJH_Vol5_Meta-Law_Layer_Proposal_v1.docx` — a Meta-Law Layer (4 types: Governing/Binding/Pathway/Frame), 13-law roster, 12 already-implicit.
   - `IJH_Meta-Law_Vol3_Reconciliation_v1.docx` — **most of it already lives in Vol 3** (CLD Set's six rules = governing meta-laws; its loops = pathways; Role Atlas "3 addresses"). Move = **index don't duplicate**: add a 4th address (loop), thin cross-registry, harvest CLD Rules 2/5/6 + name Scale-Transfer, draw Word-Stewardship as a new CLD loop. Qualified reviewer needed only on the **dynamical seam** (Vensim/REVEAL), not doctrine.
   - Full context: [[reference_power_of_words_evidence_base]].
3. **JSFSC — awaiting Porter.** Foundation `Heart_Formation_Revised v22a.docx` **resubmitted to ScholarOne 2026-06-29** (JSF-26-0039); awaiting editor Porter's decision. **Two companions DEFERRED until Porter's decision lands** — don't nudge early. Possible **3rd companion** (institutional scale) carved from the existing MSF paper. See [[project_jsfsc_measuring_maturity_rnr]], [[project_jsfsc_companion_series]].

## ✅ DONE + MIRRORED THIS SESSION (dev+prod in sync)

- **IJH Vol-1 image series COMPLETE** — batch 8 (XLIII–XLVII) placed + mirrored; all ~47 Foundational Laws now illustrated. [[project_ijh_chapter_images_vol1_2]].
- **IJH Vol-2 image batch COMPLETE** — 5 main/frame chapters (0B, 09, 10, Expl-0, larger-story) mirrored.
- **v5.8 edition bump + baseline reset** — whole corpus re-stamped v5.7.2→v5.8 for the Council; tagged `v5.8-baseline` both repos. Bump tool `_work/_docxbuild/bump_version_5_8.py`.
- **The "power of words" arc** (all mirrored): FL.XLVII closing note **"Our Words, and His"** (vetted human-words research — Gottman/nocebo/Teicher/Dweck/Fredrickson; **Emoto water claims DECLINED as pseudoscience — never cite**); cross-refs at FL.XLVI + A24; Vol-3 Grammar-of-Creation section **"Thinking His Thoughts After Him"** (Kepler/Rom 1:20; the words arc closed). [[reference_power_of_words_evidence_base]].
- **JSFSC v22a**: Foster *Celebration of Discipline* (1978, 150–59) added at Vol-2 Level-4 group section (fn); SOKA footnotes 27–30 made blue; response-letter "significant changes in blue" bullet.

## ⚠️ WATCH-OUTS / GOTCHAS

- **manifest.js has TWO structures:** `window.VOLUME_CHAPTERS` (nav) **and** `window.PATH_TO_INFO` (a prev/next linked list). The **search-index generator reads PATH_TO_INFO** — when adding/removing a chapter, update BOTH, then regenerate `search-index.js`. **The generator lives at the CLAUDE-level `_work\` (i.e. `C:\Users\jgtit\claude\_work\_gen_search_index.js`), NOT inside the repo, and it `require()`s the repo's manifest.js — so it needs an ABSOLUTE repo-root path:** `cd /c/Users/jgtit/claude/_work && node _gen_search_index.js "C:/Users/jgtit/claude/_work/Intentional-Journey-of-the-Heart-dev"` (a bare/relative dir name throws MODULE_NOT_FOUND on the require).
- **Reader embeds SVG as flat `![](x.svg)` images — not clickable.** "Doorways" into deeper material = a text link-list beside the figure, not links inside the SVG.
- **search-index must be regenerated for TEXT changes** (not for image/version-stamp-only changes). Prod's index can go stale — regenerate on the prod side too during a mirror of text.
- **dev-only, never mirror:** `docs/index.md` DEV banner + `_implementation-notes/`. Word renumbers footnote ids on docx save (benign).
- Two stray dev-only working files sit uncommitted in `_implementation-notes/` (a `~$…docx` Word lock + an untracked peer-review docx) — not mine, leave them out of commits.

## 📂 KEY PATHS

- IJH repos: dev `…\_work\Intentional-Journey-of-the-Heart-dev`, prod `…\_work\Intentional-Journey-of-the-Heart`.
- JSFSC + design docs: `…\OneDrive\Documents\Intentional Journey of the Heart\IJH edits\`.
- Front-piece: `docs/introduction/how-to-read-this-book-the-map.md` + `docs/introduction/images/country-of-the-heart-map.svg`.
