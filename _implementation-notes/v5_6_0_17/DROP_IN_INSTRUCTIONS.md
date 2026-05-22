# IJH Repository Direct Drop-In Files — v5_6_0_14 through v5_6_0_17

This directory contains the twelve destination files that were missing from the previous push. Each file is a complete standalone document ready to drop directly into the repository at its named location.

## Files in This Directory

**Four new FL chapter files** (one per revision):

- `foundational-law-xxxv-the-trust-substrate-law.md` — FL.XXXV (admitted at v5_6_0_14, P0/GII)
- `foundational-law-xxxvi-the-eschatological-glory-law.md` — FL.XXXVI (admitted at v5_6_0_15, P5/GII)
- `foundational-law-xxxvii-the-worship-alignment-law.md` — FL.XXXVII (promoted-and-relocated at v5_6_0_16, P0/GII)
- `foundational-law-xxxviii-the-soul-restoration-law.md` — FL.XXXVIII (admitted at v5_6_0_17, P0/GIII)

**Four full Vol 1 overview files** (cumulative — each version supersedes the prior):

- `foundational-laws-thirty-five-operational-laws-of-wide.md` — Vol 1 at v5_6_0_28
- `foundational-laws-thirty-six-operational-laws-of-wide.md` — Vol 1 at v5_6_0_29
- `foundational-laws-thirty-seven-operational-laws-of-wide.md` — Vol 1 at v5_6_0_30
- `foundational-laws-thirty-eight-operational-laws-of-wide.md` — Vol 1 at v5_6_0_31

**Four PT chapter edit files** (one per revision):

- `pt-chapter-v5614-edits.md` — edits for the v5_6_0_14 revision
- `pt-chapter-v5615-edits.md` — edits for the v5_6_0_15 revision
- `pt-chapter-v5616-edits.md` — edits for the v5_6_0_16 revision
- `pt-chapter-v5617-edits.md` — edits for the v5_6_0_17 revision

## What Claude Code Should Do

Simple: drop all twelve files into the repository as-is. No parsing of BEGIN/END markers required. No instruction interpretation required. Each file's content is exactly what should be in the repository at its named location.

The recommended approach:

1. Copy all 12 files into the repository's root (or matching directory if the existing files like `foundational-law-xxxiv-marriage-covenant-architecture-law.md` and `foundational-laws-thirty-four-operational-laws-of-wide.md` live somewhere specific).
2. Commit. Suggested commit message: `v5_6_0_14 through v5_6_0_17: Add FL.XXXV–XXXVIII chapters, Vol 1 overview updates (Thirty-Five through Thirty-Eight), and PT chapter edits files`
3. Production publish.

Either single combined commit or four sequential commits (one per revision) is fine — the four FL chapter files and the four PT edit files are independent of each other. The Vol 1 overview files are cumulative but only the final one (`foundational-laws-thirty-eight-operational-laws-of-wide.md`) is the canonical Vol 1 at the production state v5_6_0_17. The intermediate Vol 1 versions (thirty-five, thirty-six, thirty-seven) can be committed as historical reference files alongside the previous `foundational-laws-thirty-four-operational-laws-of-wide.md` style.

## Note on PT Chapter Edits

The four `pt-chapter-v56XX-edits.md` files are edit-instruction documents matching the existing pattern (`pt-chapter-v567-edits.md` through `pt-chapter-v5613-edits.md`). They contain instructions for applying targeted edits to `periodic-table-of-spiritual-laws-a-summing.md` (the Vol 5 PT chapter).

The edits should also be applied to `periodic-table-of-spiritual-laws-a-summing.md` to bring the PT chapter to its v5_6_0_17 state. The edits files describe each edit with its anchor (the location to modify) and the replacement content. Each edits file applies cumulatively on top of the prior revision's PT chapter state.

If applying the edits to the master PT chapter file is non-trivial in Claude Code, the edits files themselves serve as the v5_6_0_14 through v5_6_0_17 record and can be added to the repository as-is (matching the existing pattern); the master PT chapter file can be updated in a subsequent dedicated pass.

## Verification After Push

After the drop-in is complete, the repository should contain:

**38 Foundational Law chapter files** (FL.I through FL.XXXVIII):
- The 34 prior FL chapter files (already present)
- The 4 new FL chapter files dropped in at this push

**Vol 1 overview files** at successive titles (the production reader needs only the most-recent file):
- The prior `foundational-laws-thirty-four-operational-laws-of-wide.md` (already present)
- The 4 new Vol 1 overview files dropped in at this push (with `foundational-laws-thirty-eight-operational-laws-of-wide.md` being the canonical Vol 1 at production)

**PT chapter edits files**:
- The prior pt-chapter-v567-edits.md through pt-chapter-v5613-edits.md (already present)
- The 4 new pt-chapter-v5614-edits.md through pt-chapter-v5617-edits.md dropped in at this push

**Master PT chapter file** (`periodic-table-of-spiritual-laws-a-summing.md`):
- The current production state should reflect the v5_6_0_17 edits cumulatively. The four pt-chapter-v56XX-edits.md files document the specific edits; these need to be applied to the master file. (If applying the edits to the master file is deferred to a subsequent pass, the edits files themselves preserve the record of what should be applied.)

Once the twelve drop-in files are in the repository, the v5_6_0_14 through v5_6_0_17 work is complete in the active catalog state.
