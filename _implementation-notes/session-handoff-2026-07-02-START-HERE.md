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

---

## 📐 2026-07-03 (evening) — SITE-WIDE READABILITY PASS, dev only, MERGED

**PR #11 merged to dev main (`c286da0`, branch `style/readability-pass`, kept). Rollback tag: `pre-readability-2026-07-03` (= `31dcf1e`). NOT mirrored to prod — John reviews the dev Pages site first (morning of 07-04).**

Presentation-only (verified: zero `docs/*.md` in the diff; only-docs files touched = 2 SVGs, label positions only):

- **Adaptive tables** — `sizeTables()` in reader.js + 3-mode CSS in reader.html: fits (clean book table) / squeeze (width:100%, cells wrap) / scrolls (boxed scroll region, ≥2.5× column or <130px/col). Killed 23/28 table scrollbars + all right-edge mid-word clipping.
- **Mobile reflow** — `.shell` 800px breakpoint now `minmax(0,1fr)` (styles.css) + `overflow-wrap` on reader prose (reader.html): 18 sideways-scrolling pages → 0.
- **Dark mode** — hard-coded cream surfaces got `:root[data-theme="dark"]` overrides in styles.css (masthead was invisible-title before) + chapter-banner override in reader.html.
- **Renderer fixes (reader.js)** — nested bold/italic (`**a — *b***`), `<ol start>` preserves source step numbers, trailing `\` stripped in table cells, `&amp;`-style double-escapes collapsed.
- **Figures** — `fitFigureImages()`: small rasters render native-size (fig-native class), no more 2.5× blur; NEW figure lightbox (click any figure → full-size overlay, Esc closes).
- **Landing pages** — index.html + Vol 6 Governance.html reg-tables wrapped in `.table-wrap` (new class in styles.css) + `.reg-table th { white-space: nowrap }`; Four-Connects grid auto-fits; topnav-vols mobile fade hint; thin scrollbars on outline/search.
- **SVGs** — word-stewardship-loop.svg + cld-engine.svg: master-switch subtitle split to 2 lines inside a 62px box, legend moved to top-right (was colliding bottom-right). If these are ever regenerated, keep that layout.

**Verification:** headless-Edge audit of all 190 pages × desktop+mobile, before + after (scripts recreated in the session scratchpad; approach: puppeteer-core + local `python -m http.server 8747`). After: 0 doc-overflow pages both viewports; modes fits 4 / squeeze 22 / scrolls 5.

**Content-side issues FOUND but NOT touched (John's call; from the 18-agent visual audit):**
1. Home page hero says **"Forty-seven foundational laws"** — catalog is 48 post-mirror (index.html prose).
2. Source markup typos (unbalanced `*`/`**` in md): exploration-09a, exploration-02-emotional-knots, exploration-06b, b11/b15 (nested-bold "core" weight-drop). Renderer now handles balanced nesting; these are genuinely malformed in source.
3. Hand-typed `•` bullets as plain paragraphs: b15-pull-out-work, part-vi-tool-protocols (wrap flush-left).
4. Volume index.md TOC entries read "Title — Title" (duplicated link text + description) — vol1/vol2/intro indexes.
5. Low-res/clip-art/watermarked images flagged: connecting-the-dots (ArkansasOutside watermark), exploration-06 word-cloud, exploration-02a/03/04 thumbnails, TFT PowerPoint slide (exp-02), chemistry periodic-table photo (periodic-table-see-volume-5) — ties into the chapter-images project (batch 8 next).
6. Introduction.html repeats the C.S. Lewis map quote twice in one screenful.
7. a25 TOC first entry is the full 5-line subtitle (manifest title length).
8. FL.XLIV has a ~40-line unbroken italic paragraph (fatiguing; content choice).
9. Minor SVG nits left alone: engine "liquid" label behind dot; glory-attractor curve through label; overview-of-work clipped Op1/Mn1 chips; image-bearing-word fine-print small at mobile width (lightbox now mitigates).

**FotH note:** IJH's table system now EXCEEDS FotH's `.table-scroll`. If John wants parity, port sizeTables + 3-mode CSS to FotH dev later.

**2026-07-04 follow-up (John's review feedback):** Periodic Table page restored to the slim whole-table-in-one-glance format via a new `compact` table mode — reader.js marks pages in `COMPACT_TABLE_PAGES` (currently just the Periodic Table); their tables force-squeeze with `table-layout: fixed` + 12.5px type so the full grid always fits the column; phones fall back to the boxed scroll. To give any other reference-matrix page the same treatment, add its path to `COMPACT_TABLE_PAGES` in reader.js.
