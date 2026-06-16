# Session handoff — START HERE (2026-06-16)

Self-contained pickup. **Task: continue working the remaining proposed hear-and-obey laws, ONE AT A TIME, using the exact rhythm of the 2026-06-16 session (§3 below).** Everything from that session is shipped to dev + prod and in sync.

## Repo state
| Repo | Path | HEAD |
|---|---|---|
| **IJH dev** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` | `cf2aa95` (+ this handoff commit) |
| **IJH prod** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` | `531f4dc` — **in sync** |

- **Rollback point:** annotated git tag **`v5.7.2-baseline`** exists in BOTH repos (dev `64eee70` / prod `46b9458`) — the clean state *before* the new-laws arc. To undo everything: `git reset --hard v5.7.2-baseline` in a repo. John is new to git — offer to run it; don't hand him commands. See [[reference_ijh_version_baseline]].
- **Catalog now = 47 Foundational Laws (38 wide-consent + 9 newer, FL.XXXIX–XLVII)** within edition **v5.7.2**. (FL.XLVII Word's-Efficacy was added as content; the edition stamp was NOT bumped — bumping to 5.7.3 to mark the new law is John's call if he wants it.)
- Standing IJH facts (don't re-derive): it's the static "warm reader" (index.html/reader.js/manifest.js/search-index.js), NOT MkDocs; dev→prod mirror only on John's explicit "mirror"; plain-language register (15–16-yr-old readable); **divine pronouns capitalized in the books** (lowercase only in the academic papers); ESV quotes verbatim. See [[reference_ijh_dev_repo]], [[reference_ijh_dev_prod_mirror_workflow]], [[convention_divine_pronoun_capitalization]].

## §1 What the 2026-06-16 session did (context)
Ran a traceability analysis (which laws/explorations trace to the "hear and obey God" core — see [[reference_ijh_traceability_hear_and_obey]]), then generated hear-and-obey candidate laws and worked the top five **one at a time**. Result: **1 minted, 4 absorbed as enrichment** — the catalog already held most of it. Full arc + per-commit detail in [[project_ijh_new_laws_hearobey_arc]]. The five:
- **Word's-Efficacy → minted as FL.XLVII** (new Vol 1 chapter + Periodic Table P0/GIV + full reconciliation to 47 laws).
- **Indwelling-Word → enrichment** of V2.Exp7 (affective-taxonomy internalization).
- **Reception-Posture → enrichment** (Isa 66:2 → V1.Exp5; James 1:21 → V2.Exp1).
- **Stillness-Before-God → enrichment** of V2.Exp0B Silent Waiting (Isa 30:15 + Hab 2:1).
- **Doer-Becomes-Knower → enrichment** of V1.Exp6 (Ps 25:14 / 119:100 / Hos 6:3 + 2 Tim 3:7).

## §2 The remaining proposed laws — WORK THESE NEXT (one at a time)
From the expansion analysis (`_implementation-notes/IJH_Law_Expansion_HearAndObey_Line_v1.docx`, full drafts in `IJH_HearAndObey_New_Laws_Drafts_v1.docx`). Expect the same pattern: **most will fold; few (if any) will mint.** Suggested order = the 3 "hold" finalists first, then the 4 demoted.

**A — "Hold" finalists (strongest remaining):**
1. **Spirit-Illumination Law** (Direct). *The Spirit's inward illumination is the condition under which the natural person can receive/understand the things of God.* 1 Cor 2:12-14; John 16:13; 1 John 2:27; Eph 1:17-18. Operator **S+P**, cell P0/GI. Note: its operator is no longer a blocker (S+P is an existing tag); the only open question is the inclusion edge-case — it describes what **God** does, not a human cause→effect. Genuine MINT candidate (the divine side of reception) OR fold into V1.Exp1 / V2.Exp7's doctrinal frame. Examine where it best fits.
2. **Trained-Discernment Law** (Adjacent). *Discernment trained by sustained practice → distinguishing God's voice and will from counterfeits.* Heb 5:14; 1 Thess 5:21; 1 John 4:1; Phil 1:9-10. Note: overlaps **V2.Exp7a Discernment-of-Voices** and the **V1.Exp4 Wisdom Cluster** — likely fold; decide the Foundational-vs-Exploration relation.
3. **Wholehearted-Seeking Law** (Direct). *Seeking God with the whole, undivided heart → finding Him; divided/half-hearted → not found.* Jer 29:13; Deut 4:29; 2 Chron 15:2; Heb 11:6. Note: overlaps **FL.VII Drawing-Near Reciprocity** — decide whether wholeheartedness is a distinct law or the condition-clause already inside FL.VII (likely fold/enrich FL.VII).

**B — "Noted but not recommended" (demoted; expect already-covered):**
4. **Acknowledging-Christ Law** (Adjacent). Acknowledging Christ before others ↔ He acknowledges you before the Father; denying ↔ denied. Matt 10:32-33; Luke 12:8-9; Rom 10:9-10; 2 Tim 2:12. Note: reciprocity-family; the confession-of-the-mouth half (Rom 10:9-10) is **already added** to V1.Exp1 this arc — likely already-covered.
5. **Quick-to-Hear Law** (Adjacent). Quick to hear, slow to speak → understanding; answering before hearing → folly. Jas 1:19; Prov 18:13; Eccl 5:1-2. Note: substantially absorbed by the new Stillness + Reception-Posture enrichments — likely already-covered.
6. **Faithful-in-Little Law** (Adjacent/Less). Faithful use of what God entrusts → entrusted with more. Luke 16:10; Matt 25:21,29; Luke 19:17. Note: stewardship-increase; overlaps V1.Exp6 Obedience Channel + FL.XXXIX — likely fold/Less.
7. **Word-Hidden-in-Heart Law** (Direct). God's word stored in the heart → guarded from sin, steadied walk. Ps 119:11; Ps 37:31; Deut 6:6; Col 3:16. Note: folds into the Indwelling-Word material now in V2.Exp7 — likely already-covered.

(If John wants entirely new candidate lines beyond hear-and-obey, the `anthropic-skills:ijh-law-catalog-expansion` skill generates high-bar candidates + stress-tests the table.)

## §3 THE RHYTHM TO FOLLOW (this is the method John liked)
For each candidate, **one at a time**, do NOT batch:
1. **Examine where it best fits.** Read the candidate's claim + verses, then GREP the corpus for those verses / the mechanism to map overlaps (which existing FL / Exploration already holds it). Read the most-likely host chapter(s).
2. **Recommend fold-or-mint, with reasons,** and let John decide (he refines — e.g., he folded Indwelling-Word, distributed Reception-Posture). Honor the high inclusion bar: don't mint what the structure already carries.
3. **Implement on John's go, dev-first, ONE commit per law.** Plain register, divine pronouns capitalized, ESV verbatim. Push to dev; do NOT mirror per-law.
4. **HOLD the catalog count** ("47 Foundational Laws / 9 newer") until the whole set is finished — same as last time — so the count pass happens once at the end.
5. After all remaining laws are decided: do the **end-of-set reconciliation** (§4) + **mirror** (§5) on John's explicit "mirror."

## §4 If a law IS minted (newer-tier), the surfaces to touch
A new Foundational Law would be **FL.XLVIII** (next numeral; confirm with John). Match the newer-tier chapter format (intro · ## The Scriptural Ground · ## The Mechanism · ## Why This Is a Foundational Law · **Proposed Law (…newer / still-being-tested)** · ***Mirror:*** · ***Certainty:*** · closing nav button; NO separate "Shadow Pair" section). Then:
- **manifest.js** — nav-list entry + prev/next chain (insert as the new last FL, before exploration-01; repoint the prior last-FL's `next` and the new law carries the "Return to the Periodic Table" closing button).
- **Volume 1.html** — add a card + bump the section-head `<span class="count">`.
- **docs/volume-1-laws-of-the-spirit/index.md** — add the entry line.
- **Periodic Table** (`docs/volume-5-references/periodic-table-of-spiritual-laws-a-summing.md`) — add to the Slim-Format grid cell + a reference-list entry (ordered by Period/Group).
- **Count language (the end-of-set pass), in ALL of:** the Periodic Table (many spots: intro counts, slim header, provenance prefixes, "X Foundational Laws split", the P0-completeness + Open-Questions text), the **Vol 1 framing chapter** `foundational-laws-thirty-eight-operational-laws-of-wide.md` (title + "forty-seven" + the "Nine/Ten Newer Laws" heading + add the law's one-line entry), `index.md` ("The Forty-… Laws"), the **Master Law Index** `docs/volume-3-quantitative-framework/appendix-master-law-index.md`, the **Vol 6 catalog history** `docs/volume-6-governance/appendix-catalog-history.md`, **Volume 1.html** (badge + subtitle + overview card), **index.html** (Volume 1 description).
- **Regenerate search-index:** `node _work/_gen_search_index.js "<ABS repo path>"`.
- **GOTCHA:** a blind "forty-seven→forty-eight" sweep will corrupt the **FL.XLVI chapter's ordinal self-reference** ("forty-sixth law") and any "forty-seventh"/"FL.XLVII" that is a substring of the next numeral — do the count tokens carefully (the safe non-range tokens can be scripted; range tokens like `FL.XXXIX–XLVII` and any "Nth law" ordinals must be hand-checked). Verify with a `-o` grep sweep + a search-index regen-then-grep (the regen catches body-text stragglers a truncated grep misses). The reusable bump scripts from this session are in `_work/_docxbuild/bump_version_5_7_2.py` (version stamps) and `bump_count_47.py` (count tokens) — adapt, don't rerun blind.

## §5 Mirror procedure (on John's explicit "mirror")
1. `git -C PROD fetch origin`; confirm prod clean + not behind (JD may have pushed — if so, reconcile first).
2. Baseline-check: prod HEAD blob == dev's pre-arc blob for each changed file (catches divergence). 
3. Copy changed `docs/**/*.md` + `manifest.js` dev→prod. **HTML (`index.html`, `Volume N.html`) — edit in place, NEVER cp** (per-repo "Repo" link / envLabel divergence). Regen **prod's own** search-index.
4. Verify each changed `docs/*.md` staged blob == dev HEAD blob (0 mismatches) before committing.
5. Commit `Mirror … from dev (<sha>)`; push. (No new tag needed; `v5.7.2-baseline` stays the rollback point.)
6. CRLF warnings on commit are normal (Windows line-ending bookkeeping); verify via `git show --stat`/blob compare, not raw `diff`.

## §6 Artifacts (committed to dev `_implementation-notes/`)
- `IJH_Law_Expansion_HearAndObey_Line_v1.docx` — the candidate set + stress-test + recommendations (source for §2).
- `IJH_HearAndObey_New_Laws_Drafts_v1.docx` — full chapter-style drafts of the original five (format reference for any mint).
- `fl-traceability-to-hear-and-obey-2026-06-15.md` (+ `.docx`) — the traceability analysis the candidates came from.

Superseded prior handoffs remain in `_implementation-notes/`.
