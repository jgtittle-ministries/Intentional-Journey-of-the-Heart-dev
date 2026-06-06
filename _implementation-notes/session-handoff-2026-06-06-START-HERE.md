# Session Handoff — START HERE (morning of 2026-06-06)

**Read this first — it's self-contained.** Yesterday's full detail/history is in
[`session-handoff-2026-06-05.md`](session-handoff-2026-06-05.md); this is the clean pickup.

## Repos & state (everything committed, mirrored, in sync)
- **dev** `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` — content HEAD **`84e6246`** (working tree clean except one pre-existing untracked `.docx` in `_implementation-notes/peer-review-vol1/`; dev also carries extra notes commits).
- **prod** `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` — HEAD **`eea9f55`**, clean.
- **dev+prod docs are byte-identical** on every content file, except the intentional standing divergence: dev `docs/index.md` carries the "DEV PREVIEW" banner (do not mirror that). 
- **Mirror discipline:** edit dev → push → John reviews on the [dev site](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/) → on John's word "mirror", apply identical edits to prod → verify **SHA-256 byte-identical** + balanced diff → commit "Mirror … from dev". Preview repo intentionally stale.

## ⭐ LIVE THREAD — the "granddaddy voice" walk through the Vol 1 spine
John is going **chapter by chapter** through Vol 1's Foundational Laws, dictating warm first-person
asides ("A word from your Granddaddy.") that get placed as the chapter's **closing testimony**.
**Done + ALL mirrored to prod (obs #7–#12):**
- **FL.I** — tithing → what we were really sowing was hearing-and-obeying (the harvest is this work).
- **FL.II** — the fear of confessing to others is unfounded (they're too taken with their own sin to condemn).
- **FL.III** — achievement is still the idol on his throne (his most personal; still active).
- **FL.IV** — but offer the work to the Lord and it becomes *flow* → "I feel His pleasure" = what exaltation means (redemptive other half of III; + Vol 5 *Flow*/Csikszentmihalyi bib entry).
- **FL.V** — depth of forgiveness: poison-you-drink; forgiveness ≠ trust (abused-wife safeguard — trust is earned by proven behavior); the God-allowed offense → Joseph's "what is He up to?"
- **FL.VI** — backbone of Vol 2/FotH; the hard lesson: obey is my job, He's the Healer, the outcome can look different (carried the cruciform/non-payoff peer-review fix experientially; + Payne Part-II bib cite).

**NEXT: FL.VII (Drawing-Near Reciprocity).** Before John dictates, surface any still-open peer-review
items touching FL.VII as context (read the live chapter first — some "open" items were already fixed).

## The loop (per chapter)
1. John names/starts a chapter → **first surface open peer-review items touching THAT chapter** (read the live file; verify done-vs-open — the four-tradition pass landed *most* but not all).
2. John dictates his thoughts → return the **4-part contract**: Echo (catch transcription slips, esp. names) / Draft ×2 intensities / Placement verdict / Consistency check.
3. On his pick (intensity + placement) → implement as **close-of-chapter testimony** (before the next-law button) → push dev.
4. John reviews on dev → says **"mirror"** → byte-identical mirror to prod.

## Conventions to carry
- Lead: **"A word from your Granddaddy."** (capital-G Granddaddy). Ends God-ward.
- **Divine pronouns capitalized** in the book (He/Him/His for Father/Jesus/Spirit). NOTE the Hearing-God *papers* are lowercase — book is caps.
- **Match each file's punctuation**: FL law-chapter *prose* = straight apostrophes/quotes (Scripture blocks stay curly); Vol 3 files + Vol 5 bibliography = curly. Grep `’` count before editing.
- **No tradition-vs-tradition doctrinal debates** — deliver the plain-Scripture pastoral core ([[feedback_avoid_doctrinal_debates_prioritize_pastoral]]). John prizes pastoral support, esp. the dry/desolate believer.
- **Cite sources John names** in the Vol 5 bibliography (Part I = scholarly/secular alphabetical; Part II = formation/theology authors). Check if already present before adding (e.g., Payne was already in Part II).
- GET-before-PUT / diff-before-commit; John is new to git → ELI5; he uses the **Claude desktop app** (no terminal status line — [[user_runs_claude_desktop_app]]).

## Small pending option
- John's wife is **Carolyn** (per read-me-first). FL.I (on prod) still says "your grandmother and I" — offer to swap to **Carolyn**; use Carolyn in future asides.

## Still-open Vol-1 peer-review buckets (picked up per-chapter as John reaches them)
Warfare at the law level (deceiver/2 Cor 4:4 in FL.XV; a warfare law in the spine; Gal 3:13 up from the
Vol 3 basement); FL.IX prosperity-firewall at the table/one-sentence-law level; FL.VIII Jer 17:9 "An
Objection"; FL.XIX keep-vs-downgrade fork; soften Exp 7 "force multiplier" + add Luke 10:20; Foster's
contemplative-stillness law (Ps 46:10); Foster's "These Are Not Levers"/trail-map note at the catalog
front door. (FL.XVI Deliverer + the dry-season guard + the Vol 3 apologia were done this session.)
