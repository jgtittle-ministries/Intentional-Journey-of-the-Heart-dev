# Session Handoff — 2026-09-08 · START HERE

**Read this first in a new session. The LIVE state is in Ghost Memory (call `context()` and `by_tag("nag-every-thread")` first); this file is the repo-side snapshot for John and JD. It covers 7–8 September 2026 and supersedes the 09-07 handoff.**

## 0. Heads and queues

| Repo | Dev head | Prod head | Mirror queue |
|---|---|---|---|
| IJH | this handoff's commit, after `db57d6f` | `f1ee579` | **Empty.** |
| FotH pilot | `60ba779` | `c23b8b8` | Nothing. The elective proposal is implementation-notes only (never published). |

All working trees clean at close.

## 1. Volume 6 landing page — simplified and mirrored

The one structural exception among the six volumes is gone. `Volume 6 Governance.html` was a 731-line self-contained article baking in the front piece, Part 2, and Part 3; it is now a 170-line doorway in the sibling shape (dev `8243427`, prod `f1ee579` by whole-file copy with the Repo-link divergence re-applied; live-verified). **From now on a Volume 6 content change is a markdown-only mirror like any other volume.** A Tell for the 4 October changes note.

## 2. The theory-of-action sentence — refined twice, canonical

John refined the sentence on 8 September, both times confirmed as the sentence itself, not audience variants. Current canonical form (foundations-inserts draft, Part B): *"…that if you want to hear and obey Christ, and you bring what blocks you into the light, with the Word open, a few brothers or sisters beside you, and someone over you who can see your life, the door will be open for the Holy Spirit to clear the way as he wills, and the laws I wrote down in Volume 1 will start to work in you the way they were written such that you are on an intentional path to grow up into Christ, into hearing and obeying Christ in everything."* The inserts draft's header carries a dated revision note so the Council answers ask 3 on the current wording and sees the change; propagated through the October placements draft and its Word copies (`45da737`, `db57d6f`). John notes it is getting long — the Council may speak to length at ask 3.

## 3. The October packet (folder `council-meeting-2026-10-04`)

First item done and baton-approved: **draft-theory-of-action-placements.md** + Word copy (repo dashed / OneDrive `2026 Meetings/Oct Council/` no-dash). Two channels per John's governance clarification (2026-09-07): **the IJH Council does not govern FotH** — FotH sits with John, Council advises only. Part I (Vol 4 §5a insert mapping the five RQs to the sentence's clauses; a Note-on-Proof pointer) extends held ask 3 for decision; Part II (precohort expectation statement; handbook "why the meeting has this shape") goes for counsel only. Still to build nearer the meeting: the monthly changes note (told / asking / waiting) from commit history since 6 September.

## 4. FotH — the re-launch has three shapes; the elective is drafted

- **Option 1, prototype-group evening series** (first starting point): biweekly, 90 min, teens possibly without parents (consent + named sponsor + covering chain); **individual teen role-holders** — one teen holds the container, one carries content, the two roles rotating through participants as ready and willing (John corrected this from my two-teams reading), labs + a ~30-min phone planning session; John + parents oversight, Bill Fairback / Ryan Hammond as covering (answer ≈ 20 September).
- **Option 2, the Andrea club at John's home** — likely converges with Option 1 (one fellowship, two doors).
- **Option 3, the CCA elective — DRAFTED, not submitted:** FotH dev `_implementation-notes/cca-elective-proposal.md` + Word baton beside it (`60ba779`). "The Intentional Heart," 17 weekly periods, one credit (registrar's call), pass/fail on participation only; opens with the fall's honest story (approved club, legal-reviewed consent, zero signups, interview-found barriers); classroom boundaries in writing; bright line kept; week 17 invites into the evening fellowship. Brackets John's: semester, date, instructor arrangement. Next builds if Andrea engages: full syllabus + parent letter + consent draft.
- New facts: the consent form got a legal review in fall-launch prep; the administration was enthusiastic.

## 5. EdD (not in a repo — OneDrive `Documents/EdD/`)

- **"Doctorate - Independent Study Proposals for Liberty - 2026-09-08 v4.docx"** — standalone (three questions embedded; two-conversations doc not referenced). Three-tier ask from reading all five courses' text lists: Tier 1 formal directed research CLED 835 + 845; Tier 2 aimed projects CLED 855 (design project = the elective) + DSMN 870 (papers = ecological account of FotH); Tier 3 DSMN 860 as designed (15 primary sources). Praxis = dissertation-in-praxis; the FotH pilot is the intended artifact/site; early-IRB ask; AI-use disclosure as ask 7. Two baton rounds folded (health-year sabbath, zero-signup honesty, legal review, Burton & Obel / Cameron & Quinn / Levi & Askay, teen-role design).
- **Two-conversations doc** aligned (A.2 now "first cohorts are now launching").
- **Everything gates on the JSFSC decision** (JSF-26-0039, R2 with editor Porter). On acceptance: Liberty conversation with v4; Porter conversation re the three follow-on articles.

## 6. Waiting on

Porter's decision (JSFSC); the Living Hope answer ≈ 20 September (Fairback + Hammond — Option 1's covering); Dave Smith ↔ Tom Wooten in October; the 4 October Council (asks 3, 5, 6 answered; second Log entry after). Still John's: the FL.XLIX chapter rewrite; the elective proposal brackets and submission timing; the October changes note is ours to draft near the date.

## 7. Disciplines (the standing ones hold)

Mirror only on John's explicit word; baton = John edits Word, says "closed," diff with `pandoc -t plain --wrap=none` (reconstruct the baseline from session context if needed — it worked byte-faithfully twice); shared checkout: `git diff` the exact file before every `git add`; cache-bypassing fetch to verify deploys; `git show` emits LF vs CRLF checkouts; landing pages are hand-written (but Volume 6 is now a doorway — only chapter-list changes touch it). Word deliverables: plain pandoc; one folder per meeting; no-dash dates in OneDrive filenames.

Standing nag: **reboot the Dell.**
