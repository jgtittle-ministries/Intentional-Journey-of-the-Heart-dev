# Session Handoff — 2026-07-08 · START HERE

**Read this first in a new session.** This was the biggest single session in the program's history: the Formation-Docs assumptions-review series CLOSED (12 of 12), a whole new book was planned, written, peer-reviewed, published, and renamed — **"A Church Prepared for Revival — A Pilot Proposed" (CPR)** — the long-parked "Drift and the Source" paper was bench-passed and published into IJH Vol 3, and the three-book ecosystem was cross-linked dev AND prod. The authoritative per-project state lives in the memory files; this handoff is the map.

## 1. Repo state (verified at handoff)

| Repo | Dev | Prod | Notes |
|---|---|---|---|
| IJH | `78d4479` + this handoff | mirrored same-day | in sync; JD pushes here — fetch first |
| FotH | current | mirrored same-day | home page carries the CPR welcome |
| **CPR (NEW)** | `jgtittle-ministries/a-church-prepared-for-revival-a-pilot-proposed-dev` | `…-proposed` (no -dev) | **repos RENAMED 2026-07-08** from `a-church-in-revival-…`; old Pages URLs 404 (no redirect) |

CPR Pages: dev + prod both live under the new slug. Local clones renamed to match; `.claude/launch.json` preview config `church-in-revival-dev` points at the renamed dev folder (port 8931).

## 2. The assumptions-review series — CLOSED (12/12)

FC (Doc 11) and MSF (Doc 12) completed this session; docx deliverables in `_work\_docxbuild\` (`FC/MSF Foundational-Assumptions Peer Review v1.docx`). **Hear-and-obey: twelve for twelve, zero qualifications** — upgraded LOAD-BEARING (Krathwohl) and PROTECTIVE (Langberg). The series close-out + final open ledger live in the MSF verification §5 (also summarized in memory `project_ijh_formation_docs_assumptions_review`). Headlines: FC = formator's-formation ANSWERED (interior) + the canon-of-descent 6-voice convergence; MSF = "the instrument's relationship to power is undesigned" (5-seat convergence) + the Deutsche Christen test + Baxter's "measure nothing you will not weep over." Archive of the 12 review folders: offered, never requested.

## 3. CPR — the new book (memory: `project_church_in_revival_pilot`)

- 23 pages / ~61k words on the FotH reader engine; four movements answering *Do you want a revival? / What might it take to prepare the soil?* + Reference.
- **The four parked drafts SHIPPED here** as standalone pastoral chapters (seven-letters, dryness/differential = write-the-signs landed, drift, generations) — John: "glad to let those four chapters sit in CPR"; no IJH versions planned.
- **"Who Watches the Shepherds?"** (Mvt III 05) — John's demand; the canon-of-descent published: oversight, member's channel, graduated response/removal, hand above the senior leadership, civil-authorities-first.
- Reviews: summarized in Reference; **full insights chapter lives dev-only in `_on-request/` — NEVER mirror**; both Reference pages say "available from the author on request." The written-in-voice framing (exercises in perspective, NOT endorsements) is a publication-ethics requirement — never weaken it.
- Phase 4 benches fixed 36 items; Phase 5 caught + fixed the in-book link bug — **CONVENTION: in-content cross-links are plain relative .md paths; `reader.html#docs/…` double-wraps and breaks** (the renderer resolves against the current file and wraps .md links itself).
- Mirror transform (dev→prod): banner variants → "A proposal in progress — offered for prayer and honest discussion"; envLabel ''; SITE.repo; prod README preserved; `_on-request/` excluded. Handle BOTH banner variants (dryness chapter has "…, not yet a program.").

## 4. "Drift and the Source" — PUBLISHED (the awaiting-verdict draft resolved)

Lives at IJH Vol 3 `docs/volume-3-quantitative-framework/drift-and-the-source-one-law-at-three-scales.md`, between the revival-record chapter and Open Trails, mirrored to prod after a **direct two-bench pass (40 fixes)** — see the dev commit `6b61320` message for the full fix list. Header points pastoral readers to CPR; CPR's five Going-deeper paragraphs name it. IJH manifest is HAND-threaded (VOLUME_CHAPTERS + PATH_TO_INFO prev/next); search index via `node ../_gen_search_index.js "$(pwd -W)"` (needs absolute path). The four research syntheses + Wesley-1786 addition stay dev-only in `_implementation-notes/` as the scholarly base.

## 5. Engine fix (all three readers)

`history.scrollRestoration = 'manual'` added at the top of reader.js's first IIFE in CPR, FotH, and IJH (dev+prod): hashchange→reload navigation was landing readers at the bottom of the next chapter. Preview-tool gotchas learned: it caches computed styles per element (use fresh probe elements), drops viewport emulation on reload, and preview_screenshot times out on these readers.

## 6. Standing state (unchanged this session)

JSFSC foundation resubmitted, awaiting Porter — companions + paper-4 deferred until his decision. FotH FC1 gated on CCA + VA legal review (note: CPR's "Who Watches the Shepherds?" pre-drafts much of what that review will demand). Council: NOT config-controlling CPR, but wants impact/feedback — the prod link is ready to share (John hasn't yet). Granddaddy voice dormant. Source-folder mining resumes at `IJH Outlines`. Meta-law program P1.1 done. Vol 3 spiritual-time companion chapter still unwritten (research done) — its revival-record chapter IS live.

## 7. Immediate pickup options

1. **Council share** of CPR for impact/feedback (John's move; link: https://jgtittle-ministries.github.io/a-church-prepared-for-revival-a-pilot-proposed/).
2. **CPR content revisions** as John reads/gets feedback — dev first, mirror on his word, transform per §3.
3. **Archive the 12 review folders** under `_implementation-notes/peer-review-*/` if John asks.
4. **JSFSC** wakes when Porter rules.
5. Nothing moves without John's word; JD pushes to dev — fetch/rebase first.
