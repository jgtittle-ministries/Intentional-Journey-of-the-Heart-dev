# Session Handoff — 2026-07-07 · START HERE

**Read this first in a new session.** It covers the 2026-07-07 session: one integrated Vol 3 draft paper built (awaiting John's verdict) and **ten of twelve Formation-Document foundational-assumptions peer reviews completed**. Supersedes nothing in the 2026-07-06 handoff for corpus matters — repos, held drafts, and all program state from that handoff are **unchanged**; read it alongside this one.

---

## 1. Repo state (verified at handoff)

| Repo | Commit | State |
|---|---|---|
| IJH **dev** | `3c56e0c` + this handoff | in sync with origin; clean tree |
| IJH **prod** | `dbd3175` | unchanged this session |
| FotH dev/prod | unchanged | per 07-02 handoff |

Nothing was committed to any repo this session except this handoff (dev-only). **All session deliverables live uncommitted in `C:\Users\jgtit\claude\_work\_docxbuild\`** — they are on disk and safe; nothing depends on git.

## 2. Deliverable 1 — the integrated drift paper (AWAITING JOHN'S VERDICT)

**"Drift and the Source: One Law at Three Scales"** — a single ~11,200-word integrated paper drawing together the four parked Vol 3 research packages (spiritual thermodynamics as the unifying law; desolation at soul scale; generations at household scale; seven-churches at congregation scale).

- Word doc: `_work\_docxbuild\Drift and the Source - integrated companion draft v1.docx`
- Markdown source: `_work\_docxbuild\integrated-drift-paper-draft.md`
- Discipline kept: book register, divine pronouns capitalized, all never-use guards excluded, unverified quotes paraphrased, confidence-tiered with certainty note.
- **Status: John has not yet given a verdict.** On his word: revise, or commit to dev as-is. Note the four full research packages remain parked in `_implementation-notes/` untouched — the paper *condenses* them; the standalone chapters remain writable later. Peer-review flags (biblical-studies bench for the Revelation material; quantitative bench for the thermodynamics) still apply before any mirror.

## 3. Deliverable 2 — the Formation Documents assumptions-review series (10 of 12 DONE)

**The program:** John's request — foundational-assumptions peer reviews of all twelve Formation Documents, one at a time, **panel proposed and approved by John before each review runs**, NO changes ever made to the papers ("they are what they are"), each review delivered as a Word document. Focus: challenges AND confirmations to the basic assumptions IJH is built on.

**Full state lives in memory:** `project_ijh_formation_docs_assumptions_review.md` (in the memory directory) carries per-document findings, verdicts, personas, and the proposed next panel. That file is the authoritative pickup point.

**Done (order approved by John):** TA · HFT · SST · MSFIG · ATB · 4Cs · MSM · CSM · CTG · BFP (the Hearing-God quartet complete). Each has a working folder `_work\_docxbuild\<doc>-assumptions-review\` (individual reviews 01-06, verification 07, front-synthesis 00, assembled md) and a delivered docx `"<DOC> Foundational-Assumptions Peer Review v1.docx"`. Extractions of the papers (`<doc>-extracted.txt`) are verified current against the Vol 5 source-pdfs.

**NEXT: Document 11 = FC (The Formation Companion).** Proposed panel awaiting John's approval: **Gregory the Great** (new — the Pastoral Rule; who-guards-the-guardian), **Benner** + **Langberg** (standing bench; LANGBERG-2's home paper), **Ignatius**, **Benedict**, **Fowler** (carries who-tells-the-founder). Then Document 12 = MSF (Measuring Spiritual Formation at Scale) closes the series — a scale/congregation panel will be proposed then (candidates: Newbigin returning, the corporate-person doc conventions, Krathwohl for instrument construction).

**Cumulative results (all adversarially verified):**
- **The hear-and-obey core: confirmed 10 consecutive times** — never once touched by a surviving finding; challenges repeatedly *converge on* it.
- **Quartet ledger** — ANSWERED: the Sower question (settled at CTG: co-present-conditions reading, held at sanctioned-application tier; one "grounds" verb to soften); the formator-in-principle (CTG: Companion under direction as "existential necessity"); Teresa's inversion (BFP: summit diagnostic given entirely to others); Fowler's shape-question (BFP: "I am satisfied"); Willard's indirection (CSM: the boundary sentence held); the humble regress (MSM/BFP: architecture); the group construct (BFP: hearing culture, lowest-stable-common-practice). PARTIAL: Edwards's kind-criteria (residue: one 1 Cor 13 paragraph at the summit); the desolation differential (posture answered; the signs unwritten).
- **OPEN items — the short list, with remedies mostly already drafted:** (1) **write the signs** (John of the Cross's card — the parked desolation-dynamics research contains the four-way differential verbatim); (2) **who tells the founder** (Fowler's "surgeon" document — the parked seven-churches research bears directly); (3) the vision square (Willard, narrowed at BFP); (4) the pots (Brother Lawrence: "put the kitchen in the paper"); (5) week eleven (CTG: FotH is the answer — a documentation gap, not a corpus gap); plus per-document paragraph-tier items in each synthesis.
- Notable single results: Krathwohl ruled MSM "the first paper in the series to use Handbook II as intended"; Fee's Spirit-agent-never-object guard held at both MSM and CSM; ATB = the senior-partner question substantially answered (Rom 5:1–5 spine) + the disorganized-attachment findings (keep the care, drop the classification; LANGBERG-2 raised); 4Cs = the anchor finding (dryness ≠ disconnection — one-slide fix).

**Archive decision open:** the review folders could be archived under `_implementation-notes/peer-review-*/` per Registry convention — offered, not yet requested. New personas added to the bench across the series (John can ask the Registry be updated): Wolff, Wright, Ware, Moreland, Charry, Krathwohl, Edwards, JKA Smith, Teresa, John of the Cross, Fowler, Bowlby, Granqvist, Julian of Norwich, Snodgrass, Bonhoeffer, Wesley, Calvin, Newbigin, Benedict, Foster(-in-series), Ignatius, Lewis(-in-series), Brother Lawrence.

## 4. Process mechanics (proven 10×; reuse verbatim)

1. Extract the paper: `pypdf` → `<doc>-extracted.txt` in `_docxbuild` (PYTHONUTF8=1); verify head/tail against the Vol 5 source-pdf.
2. Launch 6 persona agents in parallel (general-purpose, background): each gets persona reconstruction, the extraction path, IJH context, carry-forward findings from prior seatings, and the fixed 5-section output format (assumptions / affirmations / graded challenges F-S-M / confirmations / single biggest concern).
3. Save each review verbatim to the working folder as it arrives (notifications).
4. Launch ONE adversarial refuter with the consolidated findings AND any resolution claims to audit; it reads the paper and rules SURVIVES/WEAKENED/REFUTED per finding, plus a Meta (foundations vs paragraphs; convergences; corpus coverage — give it the known corpus facts explicitly; forbid inventing).
5. Write 00-front-synthesis (panel table, verified confirmations, verified challenges by tier, tensions, one-paragraph meaning-for-IJH) + 07-verification.
6. Assemble: cat 00→07 with `---` separators; run the nested-bold fix (split each line on `**`, strip `*` inside odd segments); `node md-to-docx.js <assembled>.md "<DOC> Foundational-Assumptions Peer Review v1.docx"`; validate (PYTHONUTF8=1 + the docx skill's validate.py); check zero stray asterisks + all reviewer names present via zipfile grep.
7. Update the memory file + MEMORY.md line; report to John with doc link + headlines + the next proposed panel.

Gotchas: agents sometimes emit ```markdown fences or missing headers — normalize when saving; the interrupt-kills-agents gotcha stands; Word lock files (`~$...`) in _docxbuild mean John has the file open — never overwrite a locked docx.

## 5. Standing corpus state (unchanged — see 07-06 handoff for detail)

Five held drafts parked dev-only awaiting John's go (desolation `b596c37` / generations `fd917b5` / seven-churches `73b1564` / thermodynamics `14ed5d0` / paper-4 in OneDrive) — **note the review series has now independently generated demand for two of them** (desolation = write-the-signs; seven-churches = who-tells-the-founder), which may inform John's sequencing decision. JSFSC: foundation resubmitted, awaiting Porter; companions deferred. FotH FC1 gated on CCA + Virginia legal review. JD pushes to dev — always fetch first. Mirror only on John's explicit "mirror."

## 6. Immediate pickup options

1. **John approves the FC panel** → run Document 11 per §4 (extraction: `fc-extracted.txt` already exists in _docxbuild from the earlier review cycle — verify against `fc-formation-companion.pdf` before use).
2. **John gives a verdict on the drift paper** → revise or commit to dev.
3. **John says go on a held draft** → its own START-HERE in `_implementation-notes/`.
4. **Archive the review series** into `_implementation-notes/peer-review-formation-docs-assumptions/` if John asks.
5. Nothing moves without John's word.
