# Session Handoff — 2026-09-05 · START HERE

**Read this first in a new session. The LIVE state is in Ghost Memory (call `context()` and `by_tag("nag-every-thread")` first); this file is the repo-side snapshot for John and JD. It covers the IJH side of the 2026-09-04/05 session. The FotH pilot's own handoff, `fellowship-of-the-heart-pilot-at-cca-dev/_implementation-notes/session-handoff-2026-09-04-START-HERE.md`, still stands for the pilot; see §4 below for what changed on the FotH side since.**

## 0. Heads and queues

| Repo | Dev head | Prod head | Mirror queue |
|---|---|---|---|
| IJH | `fe2887e` (this session's last) | `8c01e50` | **Two published pages, after the 6 Sept meeting on John's word:** Part 3 Succession Letter (date of signing 6 September 2026; closing note now "signed before witnesses from the Council of Stewards"), and the Research Register's Fellowship-of-the-Heart row (the 2026 cohort did not form; trails 1, 2, 6 re-dated) — each with its search-index entry. Everything else this session is `_implementation-notes/` and never mirrors. |
| FotH pilot | `a95fd0c` | `c23b8b8` | Nothing. Three dev-only commits: the Church Authority briefing, the Host Profile, the spiritual-direction card. |

All working trees clean at close. JD pushed nothing during the session.

## 1. The Council meeting, Sunday 6 September 2026

The packet is in OneDrive: `Intentional Journey of the Heart/Current Documents/2026 Meetings/Council/` (15 files; `00 - Packet Contents.docx` is the index and reading order). Sources for every handout are in `council-meeting-2026-09-06/` here.

**Six asks**, in the changes note's suggested order: the four spiritual-authority candidates first (status, not decision) → confirm the June record → the signing → ask 2 (the light rule) and ask 3 (the two foundation inserts) → ask 6 (A34) → ask 1 (the Meta-Law Layer, the one retroactive ask) → the Register correction noted → the waiting list → draft the first Council Log entry before leaving.

- **The June record (John's recollection, no minutes exist):** FL.XLVII and FL.XLVIII, *Before You Measure*, and the Formation Companion credentialing limit were approved by consent on 28 June. The Meta-Law Layer was not discussed.
- **The signing:** John re-signs the Succession Letter before the Council, dated 6 September 2026, Council members as witnesses, no notary. David R. Smith = Theological Successor; John David Tittle = Literary Executor; alternates blank.
- **Spiritual authority, John's four candidates in preference order:** the Living Hope elders (Bill Fairbank, Ryan Hammond; Living Hope is their church); CCA's covering for evening meetings; AJ McGraw, executive pastor, Grace Covenant Church; The Crucible Project.

**After the meeting:** write the first Council Log entry (the light rule proposes `docs/volume-6-governance/council-log.md`, newest first); mirror the two queued pages on John's word; act on whatever the Council blessed.

## 2. What landed this session (IJH dev, all `_implementation-notes/`)

- `council-meeting-2026-09-06/`: **Governance for a Quiet Season** (the light rule: John steward; Council counsel + covering with a real "wait"; tell / ask / wait; git + mirror as the record plus a public Council Log; Part 1 shelved with a trigger); **Two Foundation Inserts** (Scripture as the unrated ground under the four principles, with its twin that God still speaks now; a new Vol 2 page "Before the Tools: What This Volume Assumes" — five assumptions, #4 now *"Formation is never solitary"* after the desert-fathers discussion; the Vol 4 split; theory-of-action sentence marked for John's rewrite); the **changes note** (told / asking / waiting since 28 June); the **Ask 1 handout**; the **packet index**.
- `covering-briefing/`: **IJH Briefing for a Covering**, eight sittings across all six volumes in the FotH pattern, 30 images. Word original is in the Council folder.
- `fl-traceability-to-hear-and-obey-2026-06-15.md` extended to 48 laws (FL.XLVII Direct; FL.XLVIII Adjacent ★; 13 / 11 / 24) + `traceability-grid.svg` and `_gen_traceability_grid.py`.
- `tool-map-matrix/`: **The Tool Map Matrix** (15 blockages × 22 tools from Exp 6 and Vol 5 Part VI; exposes that the idol row had no protocol) and **A34 The Throne Question** (a Part VI entry in the A25 format; repentance not warfare; Companion II; an ask).
- `docs/`: Part 3 dated and the Register row corrected (both queued for mirror); search index regenerated twice.
- `_docx_tools/`: the three small scripts the Word copies were built with (see §5).

## 3. Disciplines to keep

- **Mirror only on John's explicit word.** The five standing-divergence files in the CCA repos get targeted edits. `week-06-brave.md` is CRLF.
- **Light rule seam (not yet adopted, but used all session):** clocks, rooms, prose refinements, new trails = tell; anchors, new laws, safeguarding, coverings, the rule itself, new practice on real people = ask.
- **Baton:** John edits a Word file and says "closed" → diff against the repo Markdown with `pandoc -t plain --wrap=none`, keep his deletions exactly, tidy only residue, report. His app-downloaded copies save with no-dash filenames and may be intermediate saves; compare text before deleting anything.
- **One Word file per deliverable.** IJH Council material lives in `2026 Meetings/Council/`; FotH pilot deliverables in `Churches and Ministries/CCA/FotH Pilot/`.
- **Commit messages via `git commit -F file`** — the harness's Bash tool turns stdin into a FIFO on any `<` in the command text, and the co-author trailer contains one.

## 4. FotH side, since the 09-04 handoff

- Week 1 (2 Sept) did not run; two family interviews found child care and the parent-present hour, not the curriculum. John is weighing an evening series at CCA, an evening at his home under Living Hope, or a fully teen-led 22-week evening series, possibly every other week. Nothing in plans, deck, site, or print has changed.
- New in FotH dev `_implementation-notes/`: `covering-briefing/` (the one-sitting **Church Authority briefing**), `host-profile/` (the **Host Profile**: seven host-owned lines, CCA filled in, a Living Hope sketch — the answer to "does a new sponsor need a new repo?" is no), `spiritual-direction-card/` (**Spiritual Direction, in Protestant Words**, v2 with John's edit).
- Follow-ups held for John's ruling: the host-profile sweep (handbook §3/§6 and lesson-plan footers → "the host"; move the page to `docs/shared/`); renaming the repo to the plain edition name when the CCA chapter closes (site is `fellowshipoftheheart.org`, so readers never see the repo name).

## 5. Tooling that survived, and how the Word copies are built

Pandoc is at `C:\Users\jgtit\AppData\Local\Pandoc\pandoc.exe` (not on PATH). No LibreOffice, no poppler. The chain: `pandoc file.md --from markdown --to docx -o file.docx` (use `--from markdown`, not gfm, when image `{width=..}` attributes are used; `--resource-path=.` for images) → optional `python _docx_tools/tighten_onepager.py file.docx` (one-page density) or `landscape_tables.py` (wide grids) → verify by exporting to PDF through Word COM (`_docx_tools/export-pdf.ps1`, edit the paths at the top) and rendering pages with `pymupdf` (installed this session) → `Read` the PNGs.

## 6. Still John's

The meeting itself and its rulings; the theory-of-action sentence; the re-launch shape and the covering approach (the two briefings and the card are the instruments); whether the traceability study and the Tool Map Matrix get promoted and where they live; a second pass on the matrix to verify the A-list protocols' when-NOT sections; the laws-curriculum brainstorm (nine shapes, held); adult repo gates 18c/19/20; the papers.

Standing nag: **reboot the Dell.**
