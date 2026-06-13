# Session handoff — START HERE (2026-06-12)

Self-contained pickup. Everything below is **shipped to dev + prod and in sync** unless marked otherwise. This session ran two big arcs: the **FotH peer-review remainder** and a **full nine-author peer review of IJH Vol 3 + its complete implementation**. Nothing is mid-flight.

## Repo states (all clean, in sync)
| Repo | Path | HEAD |
|---|---|---|
| **IJH dev** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` | `6b6e7ee` (+ this handoff commit on top) |
| **IJH prod** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` | `0a20e21` — **in sync** |

> **All this session's content is mirrored to prod and in sync.** Mirror history: Vol 2 remainder → prod `345840f`; FL.II guard + Scripture-Grounding Standard → prod `04c93a4`; corporate-person-structure calibration → prod `056e9ec`. Diagnostic audit reports under `_implementation-notes/scripture-grounding-audit/` are dev-only (never mirrored).
| **FotH dev** | `C:\Users\jgtit\claude\_work\fellowship-of-the-heart-pilot-at-cca-dev` | `244d455` |
| **FotH prod** | `C:\Users\jgtit\claude\_work\fellowship-of-the-heart-pilot-at-cca` | `2c38754` |
| **BSCP dev / prod** | `…balanced-scorecard-process[-dev]` | `5c9236f` / `419d56e` (untouched this session) |

IJH dev↔prod in sync except the intentional `docs/index.md` DEV banner + the dev-only `_implementation-notes/` artifacts. FotH dev↔prod in sync except the standing `docs/start-here.md` + `docs/index.md` DEV-banner divergences.

---

## ✅ Arc 1 — FotH peer-review remainder (dev `244d455` → prod `2c38754`)
Closed the entire content remainder of the FotH eight-author review: the deferred Tier A micro-polish (A6 H8.2 canon line + Block 8 "not overruled" spoken close + GO-Wk8 Acts-13 humility note; A10/C5 body-sent-beyond "sent means opposed" — teaching-only; A13 gift-not-fixed + shame belovedness frame + Appendix D citation) **and** all draftable Tier C (C1 "A word on our words" + "drop the architecture"; C2 restrained cross beat in GS Wk1 — John's call; C3 Examen gratitude rebalance; C4 Keller *Generous Justice* reading — John's call; C5 at teaching-only level). **FotH content remainder is COMPLETE.** Only open FotH items are the **operational launch-blockers A1/B2/B4** (John/JD's lane — Companion-contact blank, Virginia mandatory-reporting review + signatures, Virginia teen-leading-minors legal review).

---

## ✅ Arc 2 — IJH Vol 3 nine-author peer review + FULL implementation (dev `90aa6d6` → prod `806240b`)

**The review.** Multi-agent workflow, **9 reviewers**: 5 theology (Keller, Lewis, Foster, Grudem, Willard) + 4 physicists holding genuinely *different* QFT interpretations (Weinberg field-realist / 't Hooft determinist / Penrose objective-collapse Platonist / Carroll Many-Worlds). Physicists scoped to physics-accuracy + analogy-integrity + fair-use of the QFT "meaning dispute," **barred from adjudicating theology**. Two-track verification (text-check + physics-fact-check). **80 concerns → 55 verified, 23 downgraded, 2 refuted** (the verifier correctly refuted two physics "errors": the static Euler-Lagrange sign, and Carroll's alleged curvature drop — his formula simplifies to the document's). Artifact (`.md` + `.docx`) at **`_implementation-notes/peer-review-vol3/`** (+ extracted TFT source text under `extracted-tft/`). Dev-only, diagnostic.

**Headline finding (the payload):** the theologians' "the Force equation relocates God's agency into operator-variables (works-righteousness in a lab coat)" and the physicists' "a multiplicative/resonance structure is deterministic — drive the inputs, the output is forced" are the **same observation**. And the physicists vindicated the epilogue's interpretive-pluralism move but converged that QFT's *meaning* floats on equations pinned to ~12 sig figs while Vol 3 has both math and meaning open — so it borrows the *posture*, not the predictive standing.

**Everything implemented and live on prod:**
- **Tier A** (11 line-fixes): entanglement recast as correlation+no-signaling (exp-01 & exp-04); tunneling → barrier-crossing + Lewis disclaimer; Wigner (not Feynman); dunamis/dynamite fallacy cut; `F=ma`; epilogue posture-not-vindication + "quantum theory"; James 5:16 middle/passive; energe- personal-not-quantitative; "mutually consistent not confirming"; analogical-resonance + appropriation caveat; time-translation.
- **TFT artifact cleanup**: the two prose appendices (Explained, Interpreted-Analogies) converted from PDF-popup stubs to **clean inline markdown** (chatbot scaffolding + garbled OCR removed; raw PDFs archived under `source-pdfs/`, unlinked). Two incidental name-drops trimmed (prana/chi/Dharma; kept ruach) — **John confirmed keep-trimmed**.
- **Tier B spine**: **B1** the non-operable sovereignty term — `F_s = G × [ f(trust) × g(authority) × h(resonance) × i(channel clarity) ]`, G = God's free self-giving, four factors = conditions of reception (Exod 33:19; 1 Cor 12:11; 2 Cor 12:8-9); **B2** "A Word for the Dry Season" ported into Exp 3 (cross-links Vol 1); **B3** Reformed sanctification grammar restored in Exp 9 (Spirit a Person not "the vector field"; Gal 5:25; Phil 2:12-13; Col 1:27).
- **Tier B mediums B4-B12**: prayer-resonance disclaimer; epilogue whole-arc Christological anchor; Affective-Taxonomy demoted to "proxy" + "measures formation, never standing" (Rom 8:1; 1 Sam 16:7); Talents re-rooted in distrust-of-Master; abundance-default qualified; miracle two-stage test grace; Mark 5:30 as the incarnate Son's act; worship/disciplines as means-of-grace not levers; "dimensionless placeholders, not physics" banner.
- **Divided points (author's calls)**: DP1 TFT appendix reordered to **lead with TFT Challenged** (manifest.js nav **and** prev/next chain) + equations stamped "unverified AI-assisted transcription"; DP2 local divine-freedom clause (John 3:8; Rom 9:15-16) in note-before-we-begin; DP3 miracles-horizon 2 Cor 12:9 counterweight in open-trails; DP4 targeted copula softening in Exp 2. Items 2 (equations PDF) & 3 (name-drops) decided — no edits.

---

## ✅ Arc 3 — Cross-volume consistency sweep after the Vol 3 review (Vol 4, then Vol 5/6)

**Vol 4** (dev `1bbef5f` → prod `f771fa7`). Audited the Testing Framework (the measurement volume, most exposed). It came through well — AT-integration-not-replacement and Spirit-as-uncontrollable-agent already propagated (§2), no stale dependency drift — but lacked the two guards Vol 3 made explicit for measurement. **Both ported:**
- **"Measures formation, never standing before God"** (Rom 8:1; 1 Sam 16:7) — §1 framing + §5d participant-care; a low/closure-flagged score is never a verdict on acceptance, said plainly when a profile is read back. Cross-links Vol 3 Exp 4.
- **Dry-season / spiral-trajectory caveat** — §3 OV1 + §3 Month-6 review + §4 Group OV1: a dipping/stalled profile may be roots driving deeper (a dark night's reorientation), not regression. Cross-links Vol 3 Exp 7.

**Vol 5 + Vol 6** (dev `c1c7215` → prod `26c113a`). Both came through well — the matured catalog had *absorbed* the Force-equation forward-reference, so the Periodic Table needs no change (the proportionality pattern + FL.IX/FL.XXXIX already carry the grace guards); TFT and Glory are absorbed/pastoral there; AT-integration is propagated. Three small fixes: (1) Vol 6 `mustard-seed-worked-resolution` Force equation updated to `F_s = G × [ f × g × h × i ]`; (2) Vol 5 MSF + MSM measurement chapters got the "measures formation, never standing before God" guard (Rom 8:1) in their integration admonition boxes (meta-box only; MSF body is "not on the revision path"); (3) Vol 6 `part-1-governance-model` notes V3.Exp3 now leads with the sovereignty term G (not an 11th dependency; tier unchanged).

**Net: all six IJH volumes + FotH are now internally consistent with the Vol 3 nine-author review.** The matured catalog did most of the insulating; the residual was small ports of language Vol 3 already established.

---

## ✅ Arc 4 — IJH Vol 2 peer-review remainder COMPLETE (dev `e5f2012` → prod `345840f`, 2026-06-12)
Closed the entire Vol 2 eight-author-review remainder in one dev→mirror cycle (12 docs + search index, byte-identical). John made the four divided-point calls live this session: **#3 Tool Map → restructure in place** (Spirit-clause to the front, plain-warm law statement, readable 3-dimension list, A24/A25/B11/B14 codes demoted to a closing practitioner parenthetical); **#13/#19 → one restrained line** (delegated authority Luke 10:19 grounded in Christ's finished victory Col 2:15 in Exp 2B, pointing to Exp 7's resistance; light generational nod Ezek 18:20 + Gal 3:13 under 7A in 2C); **#16/#21 → demote in place** ("read past the scaffolding" warm note heading the Taxonomy Key — Matt 11:25 / 1 Cor 8:1 / 2 Cor 11:3; session liturgy reframed "downstream of and under" the canon, certainty split gathering=CT / this-protocol=RI); **#10 → minimal inline repair** (woman's core question *Am I lovely? / Worth fighting for?* — Isa 62:4, Zeph 3:17 — + her portraits in 2A; "every man's heart" qualified to one lens; reserved fuller women's revision untouched). Plus the clear-cut items: **#6** Ps 66:18 reframed in its thanksgiving + dry/scrupulous guard; **#12** Container pause/decline/exit; **#8** Sower parable-governs-taxonomy (1 Cor 4:6) + 3-tier certainty + grace guard; **#15** proof-texts re-anchored (John 16:13; 2 Cor 4:4/11:3; 0b left as-is); **#20** Bilgere shadow/gold through the Exp 0 import discipline. Audits clean (link/anchor/tier). **This closes IJH Vol 2 entirely.** (Earlier-this-session #6 + #12 + the four judgment-call decisions were collected via AskUserQuestion before implementing.)

---

## ✅ Arc 5 — Scripture-grounding audit (Vols 1–3) + the Scripture-Grounding Standard (2026-06-12)
Answering John's "next best way to ground IJH better in Scripture." Ran an exegesis-in-context audit (generalizing the Vol 2 #15 proof-text fix) as a **POC on Vol 1's Foundational Laws**, then scaled it. **Result: the corpus is far better-grounded than feared.** Vol 1 laws are multi-witness, genre-aware, self-correcting (FL.VII/X/XIX exemplary). Vol 2 was already swept by #15 (light residue only). **Vol 3 — the most mechanism-heavy volume — is the BEST-grounded**, because the nine-author review forced an explicit "analogy I lay over the verse, not a claim it makes" discipline through every chapter (James 5:16, Talents, persistent widow, Mark 5:30). **One real gap in three volumes: FL.II lacked the dark-night guard its sibling FL.VII + its Vol 2 child carry → fixed (dev `711072d`).** The audit's durable product = the rubric itself, now codified as a new Vol 6 chapter **"The Scripture-Grounding Standard"** (five tests: multi-witness / genre-aware / analogy-vs-text / calibrated certainty / guarded-at-the-edge), wired to the Proposal Template as its enforcement hook (dev `1011f80`). **Sweep then COMPLETED across all six volumes** — Vols 4–6 came through consistent with 1–3 (Vol 4 low-density measurement methodology; Vol 5 mostly protocols + bibliography; Periodic Table a multi-witness derivative summary). One genuine MEDIUM finding in Vol 5's `corporate-person-structure-scriptural-definition.md` — its *systematic six-part* corporate anatomy was over-claimed as "direct scriptural, not inference" (line 9, echo 126) against its own "parallel/map-onto" framing → **calibrated** per the Standard's Tests 2+4 (individual elements direct; systematic parallel held as disciplined inference; body-of-Christ more-than-metaphor preserved). **Corpus-wide tally: exactly two real grounding fixes across six volumes — FL.II's dark-night guard and this corporate calibration — both done + mirrored.** Five diagnostic reports at `_implementation-notes/scripture-grounding-audit/` (vol1-POC, vol2, vol3, vol4-5-6-sweep). The PDFs (HFT/MSFIG/TA/SST/FC) were out of scope (historical / no toolchain). The one optional item — the **Vol 2 Exp 2 certainty split** (Emotional-Knots headline split #8-style: weight/sin = CT, knot-is-weight + release mechanism = RI, four-type taxonomy = working hypothesis) — is now **done + mirrored** too. **The Scripture-grounding arc is fully closed: nothing open. All grounding work mirrored to prod and in sync.**

---

## ✅ Arc 6 — Key to Acronyms & Abbreviations (2026-06-12/13, done + mirrored)
New **Vol 5 chapter "Key to Acronyms & Abbreviations"** (placed after the Introduction; wired into manifest nav + prev/next): ~40 acronyms in five grouped tables — Formation Documents, frameworks/source models, tools/processes/clearing methods, Vol 4 testing instruments, and project/structural notation. All expansions harvested from the corpus text (incl. **GATS** = Group Affective Taxonomy Stage, **CCA** = Covenant Christian Academy — the two that weren't expanded anywhere in the docs, supplied by John). Discovery pointers added in **read-me-first** and the **Vol 5 introduction**. Also fixed a standing **MSFIG-expansion inconsistency**: standardized corpus-wide to the no-article form "Model of Spiritual Formation for Individuals and Small Groups" (matches the acronym + filename; all 12 data-pdf-labels now uniform). Dev `6b6e7ee` → prod `0a20e21`, byte-identical, in sync. (If John ever wants the article form "A Model…" as the paper's title, it's a one-line flip.)

---

## ⚠ Open threads (carried forward — none blocking)
1. **Vol 3 equations PDF**: the 69-page typeset `tft-equations-reconstructed.pdf` still carries ~3 trailing "what would you like next?" OCR lines. Can't be scrubbed without a LaTeX source/toolchain (none on this machine). **John: accept-as-flagged** for now (the appendix is stamped "unverified AI-assisted transcription" + leads with TFT Challenged). Regenerate cleanly whenever a toolchain is on hand.
2. **FotH launch-blockers A1/B2/B4** — John/JD's lane (real-world facts: Companion contact, Virginia mandatory-reporting review + signatures, teen-leading-minors legal review). Drop into the existing `[fill in]` placeholders when the facts exist.
3. **IJH Vol 2 remainder — CLOSED 2026-06-12** (was: Tool-Map #3 + Tier B + 4 judgment calls). Only optional leftover: a deeper book-wide per-chapter "lead with the human reality, type-tag as a footnote" demotion sweep (the #16 "demote in place" was satisfied by the Taxonomy-Key orienting note + the tags already being quiet bottom-of-chapter footers). Not started; offer if John wants it.

---

## Conventions / gotchas (don't re-derive)
- **IJH mirror procedure**: baseline-check prod current == dev pre-edit (blob SHA, EOL-normalized); copy the changed `docs/*.md` dev→prod; if `manifest.js` changed, copy it too; **regen prod's own search index** via `node _work/_gen_search_index.js "<ABS prod path>"`; verify staged blobs == dev blobs (`git rev-parse`); commit "Mirror … from dev (<sha>)"; push. Mirror only on John's explicit "mirror." `_implementation-notes/` artifacts are dev-only (never mirrored).
- **`manifest.js` is hand-maintained** (no generator) and has **two structures**: the nested per-volume `chapters` nav list AND a flat per-page `prev`/`next` reading chain. Reordering nav means editing **both**, then `node --check manifest.js`.
- **No PDF toolchain here** (no LaTeX/reportlab/wkhtmltopdf/LibreOffice). Can't edit/regenerate PDFs; clean by converting to inline markdown instead.
- **Divine pronouns**: capitalized in book prose, **lowercase inside scripture quotes** (preserve ESV — e.g. "apart from me," "as he wills," "you are there"). Caught several this session.
- `autocrlf=true`, blobs stored LF; "byte-identical" = committed blob SHA, not working tree.
- The Vol 3 review artifact's per-concern data + verdicts are in the `.md` Part 2; the editor synthesis (Part 1/4) + physicist-disagreement section (Part 3) are the readable core.
