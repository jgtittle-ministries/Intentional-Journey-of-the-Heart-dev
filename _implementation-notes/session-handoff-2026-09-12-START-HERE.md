# Session Handoff — 2026-09-12 · START HERE

**Read this first in a new session. The LIVE state is in Ghost Memory (call `context()` and `by_tag("nag-every-thread")` first); this file is the repo-side snapshot for John and JD. It covers 10–12 September 2026 and supersedes the 09-10 handoff.**

## 0. Heads and queues

| Repo | Dev head | Prod head | Mirror queue |
|---|---|---|---|
| IJH | this handoff's commit, after `2735ed9` | `f1ee579` | **Empty.** |
| FotH pilot | `8c87cab` | `c1ce508` | **Empty** — the evening section is LIVE on prod. |

All working trees clean at close. **fellowshipoftheheart.org/evening/ is the live invitation URL** — the FotH Evening section (landing with fall calendar, Evening Handbook, Sessions 1 and 5, change log) mirrored to prod and live-verified. Sessions 2–22 publish as each evening approaches, tuned at the planning lab first, dev → mirror each time. Bobby and Ryan deliberately unnamed on the site pending their answers.

## 1. The first evening is Tuesday, 15 September

Branch decided by who is in the room: newcomers → Session 1 (veterans lead); else Session 5. Materials all stand from the 09-10 handoff. After the evening: the leader debrief data, the branch taken, and the "Next evening" block on the site need updating (dev → mirror).

## 2. The EdD course-text review (complete, memo final)

All twelve courses checked by exact ISBN plus title sweep: **the only duplication in the program is two books, in the CLED 715 → DSMN 850 → DSMN 870 cluster** — *Ecologies of Faith* assigned three times, *Foundations of Spiritual Formation* twice, the eBook fee assessed each pass. One-page memo **"Doctorate - Course Text Duplication Review - 2026-09-10.docx"** in OneDrive `Documents/EdD/`, confirmed accurate by John, final. Data file beside it. Side finds: three Lencioni titles across 835+845; a Springer governance text mislisted in CLED 700; an invalid ISBN in CLED 855.

## 3. The Liberty proposal is at v7

`Documents/EdD/Doctorate - Independent Study Proposals for Liberty - 2026-09-10 v7.docx` (v5, v6 remain beside it). Since v5: deliverables-and-pace blocks in both Tier-1 sections (four-gate schedule on the 8-week sub-term; 8,000–10,000 words, 30+ sources, professor calibrates); the 870 note of standing (Ecologies third assignment; the fee grievance deliberately kept OUT — separate student-accounts conversation); **the pace discussion removed at John's word** (approval should not depend on a pace commitment); Barna/Cru/Youth Alpha grounding in 845; the scholarly layer in 870 (Bronfenbrenner, Reciprocating Self, Setran & Kiesling, Estep & Kim, Kirkpatrick/Granqvist); John's Hofstede/Chan cross-cultural follow-up note in 835; and **835's second live case: the local congregation as the body that develops, recognizes, and holds the formation-companion role.**

## 4. The Porter alignment (the span's biggest development)

John read three JSFSC pieces and we mapped them hard: the **Wang & Porter 19(S1) editorial**, the **Keasler & Porter PSFM social history** (three waves; fourth-wave projections: formation as publicly available knowledge, and as the local church's primary function; Weber's routinization), and **Porter 2025 on local congregations** (the final frontier; the poorly formed question; Zahl's "theory of change"; teach and bless). Verdict, John's words: *"Looks like we are in the right place."* Porter's own measurement line (Porter/Wang/Abernethy 2021) sits directly upstream of the in-press article. **Timeline: R2 resubmitted Aug 20; answer expected after Sept 20. JSFSC publishes ~Nov and ~May.**

## 5. The follow-on articles — all three redrafted, series settled at THREE

Sequence confirmed: **curriculum → companion → church**, and the sequence is real (each assumes its predecessors). Current heads in `…/Intentional Journey of the Heart/IJH edits/` (superseded versions in `_superseded/`; md sources + build pipeline in `_work/_docxbuild/`; the folder's CLAUDE.md conventions govern — edit docx directly, version each change):

- **"If a Teenager Can Use It - JSFSC Curriculum Article v2.docx"** — the fall re-scope story added (zero as data, teen-led evening relaunch), Porter 2025 not-a-program conviction, fourth-wave public-knowledge close, both tables intact.
- **"What Cannot Be Self-Cleared - JSFSC draft v3.docx"** — em-dash scrub (111→0), Calvin double-knowledge + Wang/Porter at self-opacity, the personal-strategy and anti-credentialing lineage paragraph, series dependence explicit, and the boundary: this article supplies training and development; **the local church is the body that approves a companion for operation** (article 3's subject). Blinding pass still needed at submission.
- **"Forming a Hearing Church - merged 1+3 draft v9.docx"** — Porter-2025 engagement woven through (theory of change, vessel/treasure), the misfit table restored, terminology unified to *formation companion*, **"The Lens of Revival"** section (CPR's five failure modes academically summarized: the form outlives the power, the fire housed in one man, the awakened never formed, the fire turned on itself, the dry season read as failure; Wesley's class meeting; Lovelace; the vessel built before the rain; CPR now an [Author] bib entry), and **"Holding the Role: The Church as the Body That Credentials."** Still open: John's three consulting-case [STORY] slots; the Turabian footnote pass (after prose finals).

## 6. The Porter package (ready, waiting on the yes)

In `Documents/EdD/`: **the email draft** ("Doctorate - Porter Email Draft - 2026-09-11.docx", John's baton folded — his revival and church-credentials framing in, mechanical fixes applied, "advance one program under supervision" softening) and **the one-pager** ("Doctorate - Porter Conversation - Article Series Proposal - 2026-09-11.docx", shareable as the call's leave-behind: alignment, offer table Spring 27 / Fall 27 / Spring 28, four asks). Email sends on acceptance; email earns the call; call gets the page. Note: the one-pager's horizon line still lists the ecological account, which John dropped from the email's offer — harmonize at his next baton if he cares.

## 7. Strategy note (John's own framing, 09-11)

The article series is more attractive to him than the EdD argument, but Liberty is not abandoned: the **double-duty design** makes the degree produce the series (835's directed study is the scholarly engine of the church article; 870's papers are the future ecological article). The dissertation-in-praxis intervention = curriculum + companion team; the church article is context and the strategic plan's adoption pathway, never the intervention.

## 8. Waiting on

Porter (R2, post-Sept 20 — triggers the email); Living Hope / Hammond (~Sept 20; Fremont fallback); Bobby (door out — decks-only sweep if Ryan); **the first evening, Tuesday Sept 15**; 4 October Council (changes note ours to draft near the date — it will be rich: the evening series, the site launch, the Porter alignment). Still John's: the [STORY] cases; blue rounds on all three articles; FL.XLIX rewrite; elective brackets; take-home S1 fit check.

## 9. Disciplines added this span

Word batons: check `d.tables` before rebuilding any docx from extracted text — paragraph extraction silently drops tables (the misfit table was lost in v7 and restored in v8). Never leave a generator script's OUT pointed at a live OneDrive path — retarget before any rerun (v6 was briefly clobbered and restored from backup). Academic scrub calibration: em dashes to zero in prose; en dashes live only in numeric and scripture ranges. The articles' md sources build via `_work/_docxbuild/md-to-docx.js`; after building, docx is canonical.

Standing nag: **reboot the Dell.**
