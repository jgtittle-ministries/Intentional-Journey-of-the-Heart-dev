# Session Handoff — 2026-09-07 · START HERE

**Read this first in a new session. The LIVE state is in Ghost Memory (call `context()` and `by_tag("nag-every-thread")` first); this file is the repo-side snapshot for John and JD. It covers 5–7 September 2026 and supersedes the 09-05 handoff. The FotH pilot's own handoff (FotH dev `session-handoff-2026-09-04-START-HERE.md`) still stands for the pilot.**

## 0. Heads and queues

| Repo | Dev head | Prod head | Mirror queue |
|---|---|---|---|
| IJH | this handoff's commit, after `feddaaf` | `5829975` | **Empty.** Everything the Council blessed is published. |
| FotH pilot | `e60414b` | `c23b8b8` | Nothing. |

All working trees clean at close. A sibling Claude session fixed the reader's markdown renderer on dev (`faed7d9`); it is mirrored to prod. `.github/workflows/claude-code-review.yml` on dev is renamed `.disabled` under the light rule; `claude.yml` (issue-comment responder) stays.

## 1. The Council meeting, 6 September 2026 — done

Present: Barry Boyle, Dave Smith, John Tittle. The full record is the first entry of the **Council Log**, `docs/volume-6-governance/council-log.md`, live on the site with every packet document linked as the Council saw it (dev permalinks pinned to `9286a6e`, the three reference items at `1cafeaf`; `council-meeting-2026-09-06/packet-sources.md` maps the packet folder to the repository).

- **Approved:** ask 1 (Meta-Law Layer, retroactive); ask 2 (the light rule, now in force); ask 4 (the Succession Letter, signed before the Council, witnesses Boyle and Smith, original with John's estate papers); ask 7 (candidate FL.XLIX admitted to the newer tier; **chapter to be rewritten in John's words before publication**).
- **Held, answer within a month (by the 4 October meeting):** ask 3 (the two foundation inserts; John's "and lived" edit is applied on dev), ask 5 (traceability study → Research Register), ask 6 (A34 The Throne Question).
- **Spiritual authority, stepwise:** Bill Fairback and Ryan Hammond asked (spiritual direction for John; Hammond as authority over a FotH at Living Hope; a covering over IJH as the next ask), answer promised ≈ 20 September; John to ask Andrea Sponsler (CCA head of school) about an evening club at his home; Dave Smith meets Tom Wooten (The Crucible Project) later in October; AJ McGraw open.
- **Open question logged:** Dave Smith asked whether a Meta-Law Layer dimension should be level of complexity.
- **Standing pattern:** first Sunday of each month, face to face, as a Fellowship of the Heart; members submit agenda items through the month. Next: **4 October 2026**.

Name: it is **Fairback** (not Fairbank). The OneDrive packet folder is now `Current Documents/2026 Meetings/Sept Council/` (17 files); expect one folder per meeting.

## 2. What landed, 5–7 September

- **Volume 2 draft:** theory-of-action sentence chosen (in `council-meeting-2026-09-06/draft-foundations-inserts.md`; still a held ask).
- **FL.XLIX candidate note** (`candidate-fl-xlix-household-hearing-law.md`): admit-vs-absorb case against FL.XXI, chapter-ready draft, table stress-test, and Part D (what admission touches). Admitted; **not yet minted** — John rewrites first.
- **The light rule applied (its §8):** root `GOVERNANCE.md` is the adopted rule with its record; `CONTRIBUTING.md` is one page; `last_council_review` removed from the four registry files; READMEs cleaned of MkDocs; PR-review workflow disabled on dev.
- **Volume 6 re-fronted (John's reading, twice):** the front piece is now `docs/volume-6-governance/governance-for-a-quiet-season.md`, titled **"Governance in This Season"** — a plain account of how the work is governed now, eight headings, no revision history. The volume reads: the front piece, Part 2, Part 3, Council Log, working documents, then **Reference** holding **Part 1** (name kept because Volume 4 and the Research Register cite "Vol 6 Part 1"; manifest title "Part 1: Governance Model (in reference)"; three-sentence preface). The landing page `Volume 6 Governance.html` carries the same text as section I; its baked-in Part 1 section is gone; last section retitled Reference.
- **Mirrored to prod in stages:** Part 3 (dated, witnessed) + Register row + Council Log (`d0ef53a`, link fix `ae45c0e`), reader fix (`dadca35`), landing page (`eedcd70`), adoption (`7f3f2ff`, README `beed04d`, `5564787`), re-fronting (`5829975`). Live-verified each time.

## 3. Disciplines to keep (new ones first)

- **Landing pages are hand-written.** The root `Volume N.html` pages bake in content and keep their own chapter lists; `manifest.js` feeds only the reader. After adding any docs page, grep the volume's root HTML and edit it on dev and prod (targeted edit; the Repo link is the standing divergence).
- **Shared checkout, two sessions:** run `git diff` on the exact file before every `git add`; a concurrent session's working-copy changes get swept into your commit otherwise (it happened once this session).
- **Verify deploys with a cache-bypassing fetch** (`fetch(url, {cache:'reload'})` then reload); the browser served stale reader.js and markdown twice.
- **`git show <commit>:file` emits LF; the checkout is CRLF** — compare with `diff --strip-trailing-cr` or blob hashes, not a plain diff.
- **Mirror only on John's explicit word.** Reader machinery by patch of the same hunks, never a whole-file copy. Baton: John edits a Word file and says "closed" → diff with `pandoc -t plain --wrap=none`. One Word file per deliverable, one folder per meeting. Commit messages via `git commit -F file`.

## 4. Still John's

The FL.XLIX chapter in his words; the three held asks (Council answers by 4 October); Part 3 alternates; a private records repository for the signed letter's scan (Part 3 promises "the project's secure repository"); whether Part 1's own body text ("design proposal") gets a softer line (a tell); the FotH re-launch shape and covering (the two briefings and the card are the instruments); the host-profile sweep and repo rename; the matrix when-NOT pass; the laws-curriculum brainstorm (held); his doctorate conversations (Liberty and Kairos; questions in OneDrive `Documents/EdD/`).

## 5. For the next session, in order

1. Expect: the Living Hope answer (≈ 20 September); Dave's October meeting; the October changes note from the commit history (told / asking / waiting) as the agenda, then the second Log entry after 4 October.
2. When John says the FL.XLIX chapter is his: mint it per Part D of the candidate note.
3. Tooling unchanged: pandoc at `C:\Users\jgtit\AppData\Local\Pandoc\pandoc.exe`; search index `cd /c/Users/jgtit/claude/_work && node _gen_search_index.js "C:/Users/jgtit/claude/_work/<repo>"`; local preview via `.claude/launch.json` (`ijh-dev-static` :8747, `ijh-dev-fig` :8761).

Standing nag: **reboot the Dell.**
