# Session handoff — START HERE (2026-06-08)

Clean, self-contained pickup. **Resume focus for the next session: the "granddaddy voice" loop + the open peer-review concerns** (John explicitly asked to restart that work after pausing the simplification cycle). The searchability + simplification cycles are DONE — see the summary near the bottom.

## Repo state (in sync)
- **IJH dev** `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` — HEAD **`b24a469`**
- **IJH prod** `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` — HEAD **`9938ac8`**
- **dev ↔ prod docs in sync** — the ONLY difference is `docs/index.md` (prod clean; dev carries the `!!! danger "YOU ARE VIEWING THE DEV PREVIEW SITE"` banner). **Never mirror `docs/index.md`.** dev also carries extra `_implementation-notes/` notes (not mirrored by design).
- Static **"warm reader"** (index.html / app.js / manifest.js / search-index.js) — **NOT MkDocs**. Live dev: https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/

---

## ⭐ RESUME 1 — the "granddaddy voice" loop
John dictates a warm, first-person observation tied to a specific FL chapter (speech-to-text in chat); the assistant returns a **four-part contract**, John picks, then it's implemented close-of-chapter → pushed to dev → John says **"mirror"** → byte-identical mirror to prod.

**The four-part contract (return for each dictation):**
1. **Echo** — restate in 1–2 lines so transcription slips get caught (catches this series: "Carrie Job"→**Kari Jobe**, "effective taxonomy"→**Affective Taxonomy**, "Taro"→Truro, Elijah→Elisha).
2. **Draft** — two intensities (**tighter** + **fuller**) in the granddaddy voice.
3. **Placement verdict** — default **close-of-chapter** (after the *Certainty* note, before the next-FL nav button).
4. **Consistency check** — duplicate/contradict the chapter or corpus? fits John's settled conclusions (de-mechanize, no prosperity drift, the tiers)? Flag honestly — especially **overlap with already-shipped testimonies** (the recurring "dark valley → turn to Him" refrain; the daughter's grief at FL.XXIX/XXX; Truro at FL.XXVII).

**Voice spec:** warm, first-person, ONE concrete memory/confession. Lead **"A word from your Granddaddy."** Divine pronouns capitalized (He/Him/His) in new prose; scripture quotes keep translation orthography. Ends pointing to Christ/grace. Plain enough for a 15–16-yr-old.

**Standing preferences (carry these):**
- John usually picks **tighter** (chose *fuller* a few times: FL.XXII, XXXIV, XXXVI, XXXVII).
- **No FL.→FL. cross-links inside testimonies** unless he asks (he asked once, FL.XXXIII → hyperlink to V1.Exp7).
- **Add a scripture ref only when he asks / when it's load-bearing** (added Phil. 2:10–11 at FL.XXXVI; John 3:3 + 4:24 at FL.XXXVII; kept others ref-free).
- Wife = **Carolyn** = "your grandmother"; kids = "your mom and your uncle." Daughter who passed (FL.XXIX) left **unnamed**.
- **"mirror" is the explicit gate** — never mirror until he says it.

**⭐ 15 FL chapters still WITHOUT a granddaddy testimony** (candidates — `grep -L "A word from your Granddaddy" foundational-law-*.md`):
FL.**VIII** Desire-for-God · **IX** Generosity-Provision · **XIV** Vanity-of-Substitutes · **XV** Hardening · **XVI** Bondage · **XVIII** Bitter-Root Community · **XIX** Spirit-Anointing-Transmission · **XXVIII** Generational Nested Structure · **XXXIX** Surrender-Multiplication · **XLI** Defilement-Cleansing · **XLII** Kingdom-Confrontation · **XLIII** Cross-Boundary Faith-Access · **XLIV** Sign-as-Revelation · **XLV** Voice-of-Christ-into-Death · **XLVI** Communal Truth-Telling.
(All other FL.I–XLVI already carry one. Sequence is John's call — he jumps around.)

**To resume a chapter:** read the FL.md; surface any still-open peer-review item touching it (below); note why it fits him; invite his dictation; run the contract.

---

## ⭐ RESUME 2 — open peer-review concerns (some pair with a granddaddy testimony)
Punch-lists live in `_implementation-notes/peer-review-vol1/` (four-traditions; foster-eldredge-prince) and `_implementation-notes/peer-review-formation-docs/`. **DONE this session: reification cluster XXIX/XXXI/XXXII (#6), FL.XXX never-healed guard, FL.XXXV gift/cross guard (#15/#9), FL.XXXVI Person-of-Christ + judgment (Stott).** Still open:
- **FL.XLI (Defilement-Cleansing)** — insert *faith as the instrument of baptismal cleansing* so the law doesn't imply baptismal regeneration; distinguish sign from thing signified (companion to the FL.XXVII fix already shipped). **Pairs well with a granddaddy testimony.**
- **FL.XXXIX (Surrender-Multiplication)** — *both panels:* lower certainty tier to **Reasonably Inferred**; de-mechanize the "conditioned-on-the-surrender / operational conditions" wording so it can't read as a technique that obligates God; add the cruciform counterweight (John 12:24; the widow's mite, Mark 12). **Contentious — John deferred it once; the "big guard."**
- **FL.XXVIII (Generational Nested Structure)** — most pastorally-hazardous line ("compromised nesting is structurally separated from the divine architecture"): affirm God is the immediate restorer (Ps. 68:5–6; Eph. 1:5; adoption) — never a barrier to grace. (three-stream #5 / four-tradition #29.)
- **FL.XII (Honor-Authority)** — split the certainty tier: keep "Clearly Taught" for the parental command (Exod. 20:12; Eph. 6:2), downgrade the civil/ecclesial generalization; re-embed Rom. 13 in its frame (Daniel, the midwives, Acts 5:29).
- **FL.V (Reciprocal Forgiveness)** — reword "forgiveness extended is the condition for forgiveness received" to avoid the works-righteousness wire; distinguish forgiveness (unilateral) from reconciliation (bilateral).
- **Three-stream smaller items:** #3 deliverance/2 Cor 4:4 in **FL.XVI**; #4 FL.XLII↔FL.XVI link; #6 Deut. 28 covenant transition in **FL.VI**; #7 **FL.XIX** softening; #8 confession-of-mouth (Rom. 10:9–10) in Exp1/**FL.II**; #10 importunate prayer in **FL.X**.
- **Three Desires supplemental** — downgrade from "structural law"/Newton analogy to "pastoral typology"; strengthen imago-Dei grounding; add a feminine-heart section.
- **Formation-Docs FC finding (pending John's go):** promote the embedded "V2.Exp0B Contemplative Substrate" — ALREADY DONE this session (it's a real Vol 2 chapter now). [[project_ijh_formation_docs_peer_review]] is 5/5 complete.

---

## Mechanics (the mirror + build loop)
**Per chapter:** edit the FL.md → regen dev search-index → commit + push dev → on **"mirror"**: `cp` dev file → prod, regen prod index, commit ("Mirror from dev: …"), push.
- **Regen index:** `node C:\Users\jgtit\claude\_work\_gen_search_index.js "<ABSOLUTE repo path>"` (reads manifest.js).
- **Verify a mirror with SHA, not raw `diff`** (prod working-tree CRLF flashes false deltas): `sha256sum dev/file prod/file` should match; a testimony adds exactly **+2** lines.
- **Sync check:** `diff -rq prod/docs dev/docs | grep -v "Only in"` → only `index.md`.
- **Search cap is now 200,000** (raised from 24,000 this session) — every chapter is fully searchable; `_gen_search_index.js` reports `0 capped`. The 24K prose target is now a *quality* discipline only.
- **Length tool:** `node C:\Users\jgtit\claude\_work\_analyze_chapter_lengths.js "<repo>" [threshold]` lists chapters over `threshold` (default 24000) in manifest order with exact processed lengths.

---

## ✅ DONE THIS SESSION (2026-06-08) — do not redo
1. **Granddaddy testimonies + peer-review guards:** FL.XXX (+never-healed guard), XXXI, XXXII, XXXIII, XXXIV, XXXV (+gift/cross guard), XXXVI (+Person/judgment guard), XXXVII, XXXVIII, XL — all shipped + mirrored. **Reification cluster (XXIX/XXXI/XXXII) closed.**
2. **Search cap raised 24K→200K** so Group-B reference docs (Periodic Table, bibliographies, Master Index, Vol 4/6 docs) are fully searchable (capped 22→0; index ~2.05→2.44 MB / ~780 KB gzipped; lazy-loaded on first search → no page-load cost). Generator `_gen_search_index.js` change is live for all future regens.
3. **Simplification quality pass — 9 of the longest laws tightened ~5–9% each** (cut repetition + long block-quotes per the audience guide; testimonies + prior fixes preserved): FL.XXVII (21.8K→19.7K), XXXIII (21.0→19.3), XX (18.4→16.9), XXIII (18.3→16.6), XXI (17.8→16.5), XXVI (17.3→16.4), XVIII (16.2→15.1), XXII (16.1→15.1), XVII (15.3→14.6). **Paused at diminishing returns** (remaining chapters ~14K ≈ corpus norm). Over-cap prose FL.XXXIV/XXXVI/XXXVIII also tightened earlier in the session. **Vol 2 Exp0B (+3.5K) and Exp7 Hearing (+7.2K) were never trimmed** — still long, but fully searchable via the raised cap; optional future quality trims.

**Audience guide for any future trims (John, 2026-06-08):** the reader is a **scripturally literate 15–16-yr-old who can look things up** → short phrases that *point to* the passage are fine; trim long block-quotes to load-bearing lines + ref, condense verse-by-verse lists, de-duplicate restated theses; preserve doctrine, references, cross-refs, and testimonies.

---

## Conventions reference (don't re-derive)
- Divine pronouns capitalized in book prose; lowercase only inside scripture quotes. [[convention_divine_pronoun_capitalization]]
- dev-first → review → "mirror" to prod; never whole-file-copy config files. [[reference_ijh_dev_prod_mirror_workflow]]
- **Preview repo intentionally stale** — do not mirror there unasked.
- John uses the Claude desktop app; explain git/CLI in plain English (ELI5). [[user_ijh_author_new_to_git]]
- Chat links must use markdown `[text](URL)` syntax. [[feedback_chat_links_use_markdown_syntax]]
- Avoid doctrinal debates; prioritize the pastoral core for the dry/desolate believer. [[feedback_avoid_doctrinal_debates_prioritize_pastoral]]
- Prior handoff with deeper history: `session-handoff-2026-06-07-START-HERE.md`.
