# Session handoff — START HERE (2026-06-12)

Self-contained pickup. Everything below is **shipped to dev + prod and in sync** unless marked otherwise. This session ran two big arcs: the **FotH peer-review remainder** and a **full nine-author peer review of IJH Vol 3 + its complete implementation**. Nothing is mid-flight.

## Repo states (all clean, in sync)
| Repo | Path | HEAD |
|---|---|---|
| **IJH dev** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` | `c1c7215` (+ handoff commits on top) |
| **IJH prod** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` | `26c113a` |
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

## ⚠ Open threads (carried forward — none blocking)
1. **Vol 3 equations PDF**: the 69-page typeset `tft-equations-reconstructed.pdf` still carries ~3 trailing "what would you like next?" OCR lines. Can't be scrubbed without a LaTeX source/toolchain (none on this machine). **John: accept-as-flagged** for now (the appendix is stamped "unverified AI-assisted transcription" + leads with TFT Challenged). Regenerate cleanly whenever a toolchain is on hand.
2. **FotH launch-blockers A1/B2/B4** — John/JD's lane (real-world facts: Companion contact, Virginia mandatory-reporting review + signatures, teen-leading-minors legal review). Drop into the existing `[fill in]` placeholders when the facts exist.
3. **IJH Vol 2 remainder** (from the 2026-06-11 handoff, still open): Tool-Map rewrite #3 + remaining Tier B softenings + 4 judgment calls.

---

## Conventions / gotchas (don't re-derive)
- **IJH mirror procedure**: baseline-check prod current == dev pre-edit (blob SHA, EOL-normalized); copy the changed `docs/*.md` dev→prod; if `manifest.js` changed, copy it too; **regen prod's own search index** via `node _work/_gen_search_index.js "<ABS prod path>"`; verify staged blobs == dev blobs (`git rev-parse`); commit "Mirror … from dev (<sha>)"; push. Mirror only on John's explicit "mirror." `_implementation-notes/` artifacts are dev-only (never mirrored).
- **`manifest.js` is hand-maintained** (no generator) and has **two structures**: the nested per-volume `chapters` nav list AND a flat per-page `prev`/`next` reading chain. Reordering nav means editing **both**, then `node --check manifest.js`.
- **No PDF toolchain here** (no LaTeX/reportlab/wkhtmltopdf/LibreOffice). Can't edit/regenerate PDFs; clean by converting to inline markdown instead.
- **Divine pronouns**: capitalized in book prose, **lowercase inside scripture quotes** (preserve ESV — e.g. "apart from me," "as he wills," "you are there"). Caught several this session.
- `autocrlf=true`, blobs stored LF; "byte-identical" = committed blob SHA, not working tree.
- The Vol 3 review artifact's per-concern data + verdicts are in the `.md` Part 2; the editor synthesis (Part 1/4) + physicist-disagreement section (Part 3) are the readable core.
