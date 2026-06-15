# Session handoff — START HERE (2026-06-15)

Self-contained pickup. Everything below is **shipped to dev + prod and in sync** unless marked otherwise. The previously mid-flight **FL-traceability analysis is now DONE** (§1) — finished as a dev-only note; no open mid-flight task remains.

## Repo states
| Repo | Path | HEAD |
|---|---|---|
| **IJH dev** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` | `9970cca` (+ this handoff commit on top) |
| **IJH prod** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` | `5e93e2b` — **in sync** |
| **FotH / BSCP** | (unchanged this session) | — |

IJH dev↔prod in sync except the intentional `docs/index.md` DEV banner + dev-only `_implementation-notes/`. FC chapter blob `eea0ce72…` on both.

---

## §1 ✅ DONE — FL traceability to the "hear and obey God" core

**RESOLVED 2026-06-15.** Full analysis written as a dev-only note: `_implementation-notes/fl-traceability-to-hear-and-obey-2026-06-15.md` (verified against each Reference-List mechanism, not law names). **Result: Direct 12 / Adjacent 10 / Less 24 → strict line 12 / 34, inclusive line 22 / 24.** Verification moved exactly one law off the provisional pass below — **FL.XVI Bondage → Direct** (it's the obey-mechanism inverted, the explicit Mirror of FL.VI). Diagnostic only; no catalog edits. The provisional pass below is retained for history but is **superseded by the note.**

**John's question:** Of the **46 Foundational Laws (FL.I–FL.XLVI)**, how many **directly trace** to IJH's basic "hear and obey God" focus, and how many are **less than directly traceable**?

**Where the data lives:** `docs/volume-5-references/periodic-table-of-spiritual-laws-a-summing.md` (1014 lines, ~71k tokens — read in pages). The **Slim-Format grid** (~lines 101–108) arrays all 46 FLs by Period (scale: 0 scale-invariant → 5 cosmic) × Group (dimension: GI Spirit / GII Heart / GIII Soul / GIV Mind&Will / GV Body&Action / GVI Structural-Frame). The **per-FL reference list** is in the back half (~lines 250–1014) — that's where each law's core cause→effect claim sits. Note the catalog's own family label: *"the faith-family at GII Trust-Substrate and GV Hear-and-Obey,"* and the GV "obedience-and-authority" family — useful but the catalog is organized by Scale×Dimension, **not** by relation-to-hear-and-obey, so the count is an interpretive judgment.

**Method that was about to run (your call whether to keep it):** I was launching an **Explore agent** to extract each FL's one-line core claim from the reference list (so classification rests on content, not names). John interrupted it only to stop for this handoff — not as a method critique. Next session: either re-launch that Explore extraction, or read the reference list inline (3 pages). Then finalize the classification and give John the counts + reasoning, **explicitly flagging that "directly traceable" is a line-drawing judgment.**

**PROVISIONAL first-pass classification (from the grid + the chapter's structural commentary — NOT yet verified against each reference-list entry; verify the borderline ones before reporting):**

- **Directly traces to hear-and-obey (~11)** — mechanism *is* receiving God's word/voice and/or obeying it, or the faith/trust that conditions it: FL.VI Hear-and-Obey Blessing (the core), FL.VII Drawing-Near Reciprocity, FL.X Ask-Seek-Knock, FL.XIII Pure-Heart Vision, FL.XV Hardening (blocked reception), FL.XX Gathered-Body Discernment (corporate hearing), FL.XXXI Corporate Scriptural Reception, FL.XXXV Trust-Substrate, FL.XL Abiding-Fruitfulness, FL.XLIV Sign-as-Revelation, FL.XLV Voice-of-Christ-Reaches-into-Death.
- **Adjacent / instrumental (~11)** — conditions, blockages, fruit, or heart-postures that closely serve hearing-obeying: FL.II Confession-Restoration, FL.III Heart-Throne, FL.VIII Desire-for-God, FL.XI Renewal-of-Mind, FL.XIV Vanity-of-Substitutes, FL.XVI Bondage, FL.XXVI Doctrinal Calcification, FL.XXXII Communal Worship Heart-Alignment, FL.XXXVII Worship Alignment, FL.XLII Kingdom-Confrontation Authority, FL.XLIII Cross-Boundary Faith-Access.
- **Less directly traceable (~24)** — other dynamics (forgiveness/offense, generational transmission, community structure, marriage, sabbath, sowing-reaping, suffering, provision, polity, eschatology): FL.I Sowing-and-Reaping, FL.IV Humility-Exaltation, FL.V Reciprocal Forgiveness, FL.IX Generosity-Provision, FL.XII Honor-Authority Flourishing, FL.XVII Substitution-Cascade, FL.XVIII Bitter-Root Community, FL.XIX Spirit Anointing Transmission, FL.XXI Household Formation, FL.XXII Endurance-Hope, FL.XXIII Sabbath Rest, FL.XXIV Confession-in-Community, FL.XXV Restoration-of-the-Erring, FL.XXVII Thick Practice Transmission, FL.XXVIII Generational Nested Structure, FL.XXIX Corporate Emotional Integration, FL.XXX Communal Soul-Care, FL.XXXIII Community Polity Structure, FL.XXXIV Marriage Covenant Architecture, FL.XXXVI Eschatological Glory, FL.XXXVIII Soul-Restoration, FL.XXXIX Surrender-Multiplication, FL.XLI Defilement-Cleansing Reversal, FL.XLVI Communal Truth-Telling.

So the headline depends on the line: **strict ≈ 11 direct / 35 less-direct**; **direct+adjacent ≈ 22 / 24 less-direct.** Present both and let John pick the boundary. Borderline calls to verify against the reference-list claims: FL.XV, FL.XX, FL.XXXI, FL.XXXV, FL.XL, FL.XLII, FL.XLIII, FL.XLIV, FL.XLV, FL.XIII, FL.XXVI, FL.XLVI. (Diagnostic only — no edits intended unless John asks.)

---

## §2 ✅ Done this session (shipped dev+prod; durable records noted)

- **FC development-structure peer review (8 reviewers) — RUN + fully implemented + mirrored.** HIGH finding (LANGBERG-1, capstone trauma-safety inversion) + all **11 actionable mediums** + the **35 lows** (≈half absorbed by mediums; 8 clusters implemented) + the new **Receive→Practice→Reproduce sublevel** in the level/matrix structure (dev `9970cca`→prod `5e93e2b`). Only **LANGBERG-2 (safeguarding architecture)** is left open, deliberately deferred to John's **Council / Character-Prerequisites** pass. Full design + artifact: `_implementation-notes/peer-review-fc-development-structure/` (DESIGN-START-HERE.md has the complete log).
- **Vol 5 index completeness fix.** The static `Volume 5.html` landing page + the `volume-5-references/index.md` overview had drifted from `manifest.js`; added the missing cards (The Formation Companion, Key to Acronyms, Interrogating Reality) and reconciled index.md to all 35 chapters. Lesson recorded in `[[reference_ijh_dev_repo]]`: a chapter add/migration must update FOUR hand-maintained surfaces (manifest nav + prev/next, `Volume N.html` cards, the volume `index.md`, search-index) — verify by diffing landing-page hrefs vs manifest.
- **Dmitri Bilgere correction.** He is a **Christian** (author of *Gateways to God*), NOT a secular source — corrected across IJH dev+prod (FC chapter credentialing + References, a29 Any Doubts, the review design doc) and saved as memory `[[reference_dmitri_bilgere_is_christian]]`. Only the *methods'* Jungian origins are secular.
- **Memory consolidation.** `MEMORY.md` trimmed 26KB→10KB (dropped superseded handoff pointers, tightened lines); added the Bilgere note.

## §3 ✅ Academic-articles arc (the big one) — full state in `[[reference_ijh_edits_formation_companion.md]]`
Follow-ons to the accepted **MSM** measurement paper, **two alternative venue targets** (same content, different framing/format — submit to ONE, no dual-submission):
- **JSFSC (canonical):** *What Cannot Be Self-Cleared: …Impediments… and the Formation Companion Who Addresses Them* — Turabian footnotes, ~7.2k words, Part I (impediments taxonomy) → hinge (what-can't-be-self-measured-can't-be-self-cleared) → Part II (the Companion). Source `_work/_docxbuild/merged-article-draft.md`; build `build-fc-article.js`.
- **CEJ (logged 2026-06-15 as target):** *Forming the Formation Companion: A Developmental, Three-Domain Model…* — **APA** author-date + References, **≤75-word abstract**, **no byline** (blind review), self-contained **MSM primer**, education/training focus, "Implications for Educational Ministry" section, Trentham foregrounded. **CEJ limit 6,000 (confirmed by John);** current body ~4.9k + refs ~0.5k ≈ 5.4k (under either way — room to expand). Source `_work/_docxbuild/cej-article-draft.md`; build `build-cej-article.js` (copy of build-fc-article.js: treats `## References` as hanging-indent + omits byline).
- **Superseded standalones** moved to `…/IJH edits/_superseded/`: "The Formation Companion - JSFSC follow-on draft v1/v2", "Impediments… JSFSC draft v1".

## §4 ⚠ Open housekeeping (not blocking)
1. **Three files still in the IJH-edits root that John asked to move to `_superseded/` — the move was interrupted, NOT done:** "Impediments to Hearing and Obeying God - JSFSC draft v2.docx", "What Cannot Be Self-Cleared - merged JSFSC draft v1a.docx", and "…v2.docx". **Important:** these are **John's OWN in-progress edits** (v1a/v2), and those edits are **NOT reflected in the markdown sources** (`merged-article-draft.md`). Before treating my built "…v1.docx" as truly canonical, **reconcile John's v1a/v2 edits back into the source** — then move the extras. Re-confirm with John (he interrupted the move).
2. **LANGBERG-2 safeguarding** → John/Council pass (see §2).
3. **FotH launch-blockers A1/B2/B4** → John/JD's lane (carried from prior handoffs).

## §5 Conventions / gotchas (don't re-derive)
- **IJH = static "warm reader"** (index.html/reader.js/manifest.js/search-index.js), NOT MkDocs. `manifest.js` hand-maintained with BOTH a nav list AND a prev/next chain; `Volume N.html` landing pages + each volume `index.md` are ALSO hand-maintained (see §2 lesson).
- **Mirror only on John's explicit "mirror":** baseline-check prod blob == dev pre-edit → copy changed `docs/*.md` → regen prod's own `search-index.js` (`node _work/_gen_search_index.js "<ABS prod path>"`) → verify staged blobs == dev → commit "Mirror … from dev (<sha>)" → push. **Root `*.html` mirror in place via targeted Edit, never `cp`** (per-repo "Repo" link / envLabel divergence).
- **Academic-paper register:** lowercase divine pronouns (opposite of the IJH books); ESV quotes preserved. Build pipeline + no-PDF-toolchain notes in `[[reference_ijh_edits_formation_companion]]`.
- `_implementation-notes/` artifacts are dev-only, never mirrored.
