# Session handoff — START HERE (2026-06-11)

Self-contained pickup. Everything below is **shipped to dev + prod and in sync** unless marked otherwise. This session ran a long arc across **two projects** (IJH + FotH). Nothing is mid-flight.

## Repo states (all clean, in sync)
| Repo | Path | HEAD |
|---|---|---|
| **IJH dev** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` | `86f67ca` |
| **IJH prod** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` | `068c727` |
| **FotH dev** | `C:\Users\jgtit\claude\_work\fellowship-of-the-heart-pilot-at-cca-dev` | `0fd36de` |
| **FotH prod** | `C:\Users\jgtit\claude\_work\fellowship-of-the-heart-pilot-at-cca` | `9dae8d0` |

IJH dev↔prod in sync except the intentional `docs/index.md` DEV banner (dev carries extra notes commits). FotH dev↔prod in sync except **`docs/start-here.md`** (one line — dev links the IJH **-dev** site, prod links IJH prod) and `docs/index.md` (DEV banner). Both use the **static warm reader** (manifest.js + search-index), not MkDocs.

---

## ✅ What shipped this session (three arcs)

### Arc 1 — IJH "big-guard": FL.XXXIX + FL.XIX core-text de-mechanize (dev `4967441` → prod `9338695`)
Aligned the registry `core_text` (+ FL.XXXIX Master Index prose) to the already-settled chapters so no surface reads as a God-obligating technique. FL.XXXIX: dropped "return-mechanism that exceeds proportional scaling"/"conditioned on the surrender" → Christ's free sovereign doing + John 12:24 cruciform + Mark 12 widow's-mite + prosperity-fence. FL.XIX: dropped "increased magnitude where conditions are properly observed" → same KIND of anointing, double-portion = inheritance (Deut 21:17), Spirit not bound to means (Acts 10:44–46). Stripped the obsolete `confidence_rationale` flags. Tier/link/anchor audits clean. **This closed the last item from the 2026-06-09 queue.**

### Arc 2 — IJH Vol 2: eight-author peer review + implementation through Tier A
**The review** (multi-agent workflow, 8 authors: Keller/Stott/Fee/Willard + Foster/Eldredge/Prince/**Lewis**) → artifact `_implementation-notes/peer-review-vol2/peer-review-vol2-eight-authors.md` (+ `.docx`), committed dev `1d53ff0`/`8b8067a` (dev-only, NOT mirrored; diagnostic). 8 authors · 70 presses → 26 concerns · 19 verified. Headline: commend-with-revisions; two gating pastoral-safety faults.
**Implemented + mirrored** (each its own dev→prod cycle, byte-identical):
- **#1** clinical-referral "limits of safe" guard — pointer pass (the guard already exists in FC + FotH; surfaced at point of use). dev `c10f0e8`/prod `8867ced`.
- **#4** 2C victim-agency guard (mirrors V1 FL.V). dev `5b1a3d7`/prod `bc89b8e`.
- **#2** sovereignty / Dark-Night off-ramp (the last gate) + softened "Not gradually, but suddenly"; closed **#7** and **#18** for free. dev `e3dfd5b`/prod `ebe69f2`. **Then consolidated** the repeated sovereignty-of-timing language to one canonical "standing word" hub in Exp 2 (spokes trimmed to point to it). dev `f4b55ec`/prod `61c6a1a`. **Re-use that hub for any future sovereignty/timing mention.**
- **Tier A cheap wins** — #11 (2A falling-away→Keeper), #22 (0B dry-season), #14 (Four Connects standing-vs-deepening), #5 (6B/6A interior reconciliation→FL.V), #17 (intro "simply true"), #9 (Prince biconditional broken, fruit-of-Spirit primary), Exp 9 tier word (Speculative→65%/RI), Tool Map footer 6A→6, Dave Smith dangling-link deleted, "Followship"→"Fellowship". dev `c473ece`+`d733623` → prod `068c727`.

**IJH Vol 2 — STILL OPEN (awaiting John):** the **Tool Map rewrite (#3)**; the **deferred Exp 4/Exp 6 registry `core_text`** updates (ride with #6/#3); Tier B softenings **#6** (Ps 66:18), **#8** (Sower-mapping certainty/authority), **#10** (2A man-centric), **#13** (one authority line in 2B), **#15** (proof-texts), **#16** (taxonomy split), **#19** (generational bondage), **#20** (Bilgere import), **#21** (session-liturgy lineage); residual **#12** Container pause/decline/exit clause; the **4 judgment calls** (deliverance grammar; taxonomy relocation #16; 2A man-centric repair-now-vs-later #10; sudden-vs-gradual — largely met by #2).

### Arc 3 — FotH: eight-author peer review + implementation through Tier A + Tier B
**The review** (same 8-author engine + a safety-architecture scan + child-safeguarding + IJH-fidelity lenses; first run failed on 2 agents missing StructuredOutput → hardened prompt + resumed) → artifact `…fellowship-…-dev/_implementation-notes/peer-review-foth/peer-review-foth-eight-authors.md` (+ `.docx`), committed dev `62cd6fe` (dev-only). 8 authors · 64 presses → 26 concerns · 19 verified. Headline: warmly commend, substantial revisions **before more minors enter**; FotH's safety architecture is "unusually mature."
**Implemented + mirrored:**
- **Tier A child-safeguarding** (A1 participant safety footer ×5 files; A2/A3 forgiveness≠reconciliation in anger-knot + household; A4 confession discern-harm-from-grievance; A9 garden solo-return stop-and-tell) → dev `9867188`/prod `e825ef6`.
- **Tier A theology/fidelity** (A5 atoning ground; A6 canon-closure; A7 fear-knot de-absolutize; A8 anti-verdict; A10 warfare named/ministry-vs-watchfulness; A11 union-with-Christ framing; A13 redemptive-generational; start-here 38→46 Laws) → dev `057fb58`+`6718893`/prod `3c14b7c`.
- **Tier B draftable** (B1 inline crisis SSOT terminal in GD §6; B3 per-room competency floor + junior depth-floor [VERIFIED HIGH]; B5 external-correction at GO Wk8 landing; B6 taxonomy out of participant targets) → dev `77bd32d`/prod `ca62c9f`.
- **B2 + B4 SCAFFOLDED** with `[fill in]` placeholders (the launch gates only John/JD can finish) → dev `0fd36de`/prod `9dae8d0`.

**FotH — STILL OPEN:** Tier C judgment calls (deliverance grammar, justice stream, etc.); the deferred Tier A micro-polish (H8.2/GO-Wk8 canon one-liners, body-sent-beyond "sent means opposed", shadow-mission gift-not-fixed, shame belovedness reorder, A12).

---

## ⚠ STANDING OPERATIONAL TO-DOS (John / JD — launch-blockers, now written into the FotH handbooks as checkboxes)
1. **The A1 "Your Cohort Companion: ____" blank** (printable) must be filled with a real name + number before any participant materials are printed for a cohort.
2. **B2 (GS Handbook §6 launch checklist):** named on-call backup · populated Cat 1–5 referral numbers (Warrenton-local) · every Companion trained + signed CCA child-protection policy · **Virginia mandatory-reporting review closed** · Lead Companion + CCA head-of-school signatures.
3. **B4 (inviting-others Section 3 gate):** the **Virginia legal review** for a teen leading other minors + institutional confirmation on file · two-adult covering present-in-room.

When the B2/B4 facts exist, drop them into the `[fill in]` placeholders — minutes of work.

---

## Conventions / gotchas (don't re-derive)
- **FotH mirror is NOT like IJH's.** Procedure: baseline-check prod vs dev pre-edit (EOL-normalized); **copy the matching docs files** dev→prod; **`docs/start-here.md` is divergent** (prod keeps its IJH-prod URL) — apply edits to it *in place*, never copy; then **`cd prod && node tools/build-manifest.mjs && node tools/build-search-index.mjs`** (prod rebuilds its own search-index); commit "Mirror … from dev"; push. Verify staged blobs == dev blobs via `git rev-parse`.
- **IJH** uses `_gen_search_index.js` at `_work/` (`node _work/_gen_search_index.js "<abs repo>"`) + the `_implementation-notes/_link_audit.py` / `_anchor_audit.py` / `_tier_audit.py`. FotH uses `tools/build-manifest.mjs` + `tools/build-search-index.mjs`.
- Both repos: `autocrlf=true`, blobs stored **LF**; working tree CRLF. "Byte-identical" = committed-blob SHA, not working-tree.
- **Peer-review agents' line/section refs are sometimes imprecise** (this session: an Appendix-D citation, FotH Section 9 / Appendix E / GO §5). Grep to verify before editing; place fixes at the real home.
- **Divine pronouns** capitalized in book prose, lowercase in scripture quotes — check the referent. FotH papers follow the same rule.
- Mirror only on John's explicit "mirror". Review artifacts are diagnostic — nothing edited into a volume until John picks the finding.
- John uses the Claude desktop app; ELI5 git/CLI. JD (Epithetical / vertidog@gmail.com) is John's son, the governance/legal/cron teammate — B2/B4 legal review is his lane.
