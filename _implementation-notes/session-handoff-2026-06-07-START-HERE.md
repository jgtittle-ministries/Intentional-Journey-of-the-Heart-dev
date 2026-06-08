# Session handoff — START HERE (2026-06-07)

Clean, self-contained pickup for the next session. Everything below is **done + mirrored to prod** unless explicitly marked open/deferred.

## Repo state (in sync)
- **IJH dev** `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` — HEAD **`6de2058`**
- **IJH prod** `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` — HEAD **`163def9`**
- **dev ↔ prod docs are in sync** — the ONLY difference is `docs/index.md` (prod is clean; dev carries the intentional `!!! danger "YOU ARE VIEWING THE DEV PREVIEW SITE"` banner). **Never mirror `docs/index.md`.** dev also carries extra `_implementation-notes/` notes that are not mirrored by design.
- IJH dev+prod are the **static "warm reader"** (index.html / reader.js / manifest.js / search-index.js) — **NOT MkDocs** (no mkdocs.yml). Live site: https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/

---

## ⭐ LIVE THREAD — the "granddaddy voice" loop (RESUME HERE)
John dictates a warm, first-person personal observation tied to a specific FL chapter (speech-to-text in chat); the assistant returns a **four-part contract**, John picks, then it's implemented close-of-chapter → pushed to dev → John says **"mirror"** → byte-identical mirror to prod.

**The four-part contract (return this for each dictation):**
1. **Echo** — restate in 1–2 lines so transcription slips get caught (this session caught "Taro"→**Truro**; earlier sessions caught Elijah→Elisha).
2. **Draft** — two intensities (**tighter** + **fuller**), in the granddaddy voice.
3. **Placement verdict** — quote the anchor lines; default is **close-of-chapter** (after the *Certainty* note, before the next-FL nav button).
4. **Consistency check** — does it duplicate/contradict the chapter or corpus; does it fit John's established conclusions (de-mechanize, no prosperity drift, the tiers); flag honestly.

**Voice spec:** warm, first-person, ONE concrete memory/confession. Lead **"A word from your Granddaddy."** (personal aside) or **"A word on…/A candid word on…"** (scope/terminology note). **Divine pronouns capitalized** (He/Him/His for Father/Jesus/Spirit) in new prose; **scripture quotes preserve translation orthography** (e.g., Rom. 12:19 "Vengeance is mine" kept ESV-lowercase). Ends pointing to Christ/grace, not to himself. Plain enough for a 15–16-yr-old.

**Standing preferences observed this session (carry these):**
- John usually picks **tighter** (chose *fuller* once, FL.XXII).
- **No cross-links** inside the testimonies — standing preference; do not add FL.→FL. links unless he asks.
- **Add a scripture ref only when he asks / when it's the load-bearing quote** (he asked for Rom. 12:19 at FL.XXII; Mark 10:21–22 and Job 2:13 were kept by default).
- He refers to his wife as **"your grandmother"** (wife = **Carolyn**); kids = **"your mom and your uncle"** (FL.XVII). At **FL.XXIX** his **daughter who passed is left UNNAMED with no relation stated** — he was offered the chance to name her and didn't this session; revisit only if he raises it.
- **"mirror" is the explicit gate.** Don't mirror until he says it.

**Granddaddy testimonies DONE this session (all close-of-chapter, dev→prod mirrored):**
- **FL.XXI** Household-Formation — "handed faith down to my kids late; anyone can start when they turn to Christ; ripple to a thousand generations." (+ carried the **#2 split**, below.)
- **FL.XXII** Endurance-Hope — "three roots of suffering, a scriptural response for each" (my sin→repent; another's sin→forgive, Rom. 12:19; no human cause/the enemy→Eph. 6; never a passive target). *(fuller)*
- **FL.XXIII** Sabbath Rest — the vision of rushing down the stairs past Jesus in the easy chair by the fire; rest as a whole-life posture.
- **FL.XXIV** Confession-in-Community — saying it out loud to a trusted person makes it *real*; "run, don't walk."
- **FL.XXV** Restoration-of-the-Erring — pursuit vs. the other's will; Jesus loved the rich young man and let him walk (Mark 10:21–22); keep the door open.
- **FL.XXVI** Doctrinal-Calcification — complete certainty closes you down (a 1.0 prior can't update); Israel's Judges cycle; *pain* is what reliably breaks calcification (org-change parallel).
- **FL.XXVII** Thick-Practice Transmission — Truro Episcopal liturgy, Rite 2 ×3, J.K.A. Smith's *Desiring the Kingdom*; "liturgy without the Spirit is dull, filled with the Spirit gives life." (+ carried the **ex-opere-operato fix**, below.)
- **FL.XXIX** Corporate-Emotional-Integration — grief after his daughter passed; the ones who **sat with him in the pain** (not fix/fade it) truly helped; Job's friends right for 7 days' silence (Job 2:13) then erred; "go sit with them — don't fix it." Lands on Christ weeping (John 11).
- **FL.XXX** Communal Soul-Care for the Wounded — he prayed with/sat beside many never healed this side of heaven; the deeper battle is trusting He is good/hears/cares and that the one taken Home is healed completely; "I am the one who prays, and He is the Healer." *(tighter)* **+ carried the four-tradition #6 fix:** built the **never-healed pastoral guard** into the Proposed Law (two faithful endpoints — "until she is able to carry it again, **or, when the wound does not heal this side of heaven, all the way home**"), so the recovery telos no longer reads the never-healed as a failure-state. dev `80d5bbd`+`805dfb8` → prod mirror `c7f33d9`.
- **FL.XXXI** Corporate Scriptural Reception — corporate listening seen in two of his own practices, **PROAPT** (Pray/Read/Observe/Apply/Pray/Tell; V2.Exp7) and **Heart Bible Study** (A28, slow/imagery-based); "you hear how God spoke to a brother or sister in that verse and it opens the verse for you — but only done in the Spirit, not a room trading opinions, but one body hearing the one Word together." *(tighter)* dev `9678320` → prod mirror `f85d403`. **Truro kept OUT** (FL.XXVII + V2.Exp7 already use it). **Reification one-liner DEFERRED to the cluster pass** (see OPEN/DEFERRED).
- **FL.XXXII** Communal Worship Heart-Alignment — corporate worship sets him in heaven's throne room (*Revelation Song*, Kari Jobe leading); at the Father's feet before he meant to be, hands raised; the same song alone doesn't do it; the gathered church is caught up into the worship that never stops around His throne. *(fuller)* dev `ff00b32` → prod mirror `3e1dd0a`. Lands on Rev. 4–5 (the chapter's own proof text).
- **FL.XXXIII** Community Polity Structure — from decades of org experience: structure either lifts people up or strangles innovation; you can't opt out, so the real question is whether it builds God's kingdom or feeds the leaders' power. Spiritual authority as **force multiplier** (**first testimony with an inline hyperlink → V1.Exp7 Spiritual Authority**). Lived budget-accountability test from church-home-hunting: "whose authority are you under?" — a warm "the Lord Jesus Christ" isn't the test; "does anyone challenge your budget?" is (structural descriptor + "for example, many non-denominational churches"). *(tighter)* dev `6ad2e0e` → prod mirror `332a0de`. No open peer-review item touched it. Stays form-neutral (matches avoid-tradition-debates).
- **FL.XXXIV** Marriage Covenant Architecture — **major personal disclosure** (John approved publishing): he and Carolyn married without Christ, **both already divorced once**; coming to Christ changed everything; the **"keep no back door open"** teaching they took to heart. The Physician's word to the marriage-wounded: even in separation/divorce Christ will meet you, the pain itself can draw you to Him; turn to Him whatever the cause/outcome, He's working it for your good (Rom. 8:28 echo, no citation per his rule). *(tighter)* dev `538bcb6` → prod mirror `48df322`. **Carries the FL.XXXIV portion of four-tradition #6** (the "clinical handling / Physician-not-cataloguer" flag) — doctrine untouched, tone transformed. NOTE: FL.XXXIV is index-capped, so the testimony is past the search cap (search-index.js unchanged; chapter-only commit, +2 lines).
- **FL.XXXV** Trust-Substrate — **+ carried a double-flagged gospel-grounding guard** (four-tradition #15 Keller/Willard + three-stream #9 Foster): trust risked becoming "the subtlest work" ("am I trusting hard enough?"). Three guards added — Level 1 (cross as supreme proof, Rom. 5:8/8:32), Level 3 (trust is God's gift, Eph. 2:8; paths grow the gift, don't manufacture it), Proposed Law clause (trust is God's own gift, resting on the cross, never a work). Testimony: faith/believe = trust (Greek *pistis/pisteuō*), not head-agreement — he reads Scripture swapping "trust" for "faith/believe"; "Believe in Jesus" = "Trust Jesus," lean on/depend on Him. *(tighter; Greek gloss kept)* dev `76c2b47`+`368144a` → prod mirror `f10d667`. **Begins the FL.XXXV–XLV block** (plain-language register already swept 2026-06-04; this was the separate gospel-grounding item).
- **FL.XXXVI** Eschatological Glory — **+ carried the four-tradition medium item (Stott emphasis):** Level 1 re-centers the hope on the **Person of the returning Christ** (Phil. 3:20; 2 Tim. 4:8, "await/long for Him"); Level 2 adds a **one-line sober obverse** — glory for those who are Christ's, judgment for those apart from Him (2 Pet. 3:7; Rev. 20:11–15), the gospel's mission-urgency. Testimony: the older he gets and the more his heart aches at suffering, the more he longs for Christ's return; that urgency is **part of why he wrote this book** ("I won't always be here to say these things"); every knee will bow (**Phil. 2:10–11**, citation added). *(fuller)* dev `631d176`+`2aba1bd` → prod mirror `c95d38f`.
- **FL.XXXVII** Worship Alignment ("you become like what you worship") — **no guard** (reviewers called it the strongest chapter in the volume). Testimony: the shaping is grounded in seeing *in the Spirit* who God is and His love (born again to see the kingdom, John 3:3; worship in spirit and truth, John 4:24) — not a polished worship set or band, but the deep turning of the heart, the **Affective Taxonomy's progressive internalization**, into **oneness with Christ until no other option is even interesting anymore** (reinforces the reviewers' #1: union with Christ over "alignment"). *(fuller; John 3:3 + 4:24 cited; AT named, no link)* dev `b97a94b` → prod mirror `fec2833`.
- **FL.XXXVIII** Soul-Restoration — **no guard** (register sweep already done; nothing else open). Testimony: "I leak"; the **thorns of the Sower** (the cares/worries of life) poke holes in his soul unnoticed until something stops him and he sees he's **running on his own fumes**; the **promotion he jumped at without asking God or Carolyn** that became a disaster; a merciful God who **draws and restores even through our mistakes when we repent and turn back** ("the forehead-slap and turn back once again"). *(fuller; no citation)* dev `6de2058` → prod mirror `163def9`. Index-capped chapter → testimony past search cap, chapter-only commit (+2).
- **✅ Reification cluster (FL.XXIX/XXXI/XXXII) — four-tradition #6 CLOSED.** Joint one-liner pass: each shared soul/mind/heart definition now names the **one Holy Spirit (1 Cor. 12:13)** + **the person of Christ** as binder, never a group over-soul. FL.XXIX light touch (wove 1 Cor. 12:13 into the existing "Christ's body" line); XXXI (Spirit indwelling + mind of Christ, 1 Cor. 2:16) + XXXII (Spirit poured in, 1 Cor. 12:13/Rom. 5:5 + Christ dwelling among) got the explicit "never a corporate substance set over them" foreclosure. dev `5f5f295` → prod mirror `58f6f68`.

**FL.I–VI** were done in earlier sessions (obs #7–#12). **FL.XXVIII was skipped** this session per John. **Sequence is John's call** — he's been jumping around (next he may continue FL.XXX, or go back to FL.VII, or anywhere).

**How to resume a chapter:** read the FL.md; surface any still-open peer-review item touching it (see the punch-lists in `_implementation-notes/peer-review-vol1/`); note what it is + why it fits him; invite his dictation; run the contract.

---

## Mechanics (the mirror + build loop)
**Per granddaddy chapter:** Edit the FL.md (close-of-chapter, before the nav button) → regen dev search-index → commit + push dev → on "mirror": `cp` dev file → prod, regen prod search-index, commit ("Mirror from dev: …"), push.
- **Regen search index:** `node C:\Users\jgtit\claude\_work\_gen_search_index.js "<ABSOLUTE repo path>"` (needs the absolute path; reads manifest.js). Adding chapter prose changes the index, so regen every time.
- **Verify a mirror with git, not raw `diff`:** prod working-tree files can carry mixed CRLF, so a raw `diff` flashes FALSE deltas on untouched paragraphs. Use `git show --stat HEAD` / the commit diff (git normalizes) — each testimony should be exactly `+2` lines (aside + blank).
- **Sync check:** `diff -rq prod/docs dev/docs | grep -v "Only in"` should show **only `index.md`**.

---

## Formation-Document peer-review series — COMPLETE (5/5), diagnostic
Artifacts (`.md` + `.docx`) in `_implementation-notes/peer-review-formation-docs/` (TA, HFT, SST, MSFIG, FC — 7-author panels; HFT had +Lewis). Purpose: surface IJH-volume changes. Built the .docx with `node _work/_docxbuild/md-to-docx.js <in.md> <out.docx>` (flatten markdown links to plain text in a temp copy first — the converter renders `[text](url)` literally). PDFs extracted via pypdf to `_work/_docxbuild/<doc>-extracted.txt`.
- **TA** → no IJH change. **HFT** → 2 doc findings (Sower mis-attribution; phantom HFMT/roster) — already implemented + mirrored.
- **SST** → ontological-vs-functional trichotomy seam. Implemented dev `3a5c431` → prod `341ef94` (Vol 5 intro `!!! note` guard + "function, not substance"; SST added to the integration-not-replacement list; Vol 1 taxonomy-key Group-axis functional anchor; V1.Exp2 Connections half-line). Then the **pending HFT-review front-matter batch** (HFT desc→framework/PROAPT, MSFIG Sower re-attribution, phantom HFMT→MSF, roster, reading-plan) was mirrored to prod `2c5cde1`.
- **MSFIG** → the named small-group taxonomy ("Social Fellowship→…→Sent as Body") isn't in the Compressed-Edition PDF → attributed as the project's naming (option b) + credited MSFIG as *originating* the held-stages reading. dev `21b0541` → prod `efbc51e`. (Confirmed MSFIG IS the real Sower-mapping home.)
- **FC** → **promoted the embedded "Exploration 0B — The Contemplative Substrate" into a real Vol 2 chapter** `docs/volume-2-knowing-to-doing/exploration-0b-contemplative-substrate.md` (4 practices: fixed-hour prayer, lectio, silent waiting, vigilantia cordis; new "Foundational Practice" type), wired into manifest.js (nav + prev/next) + Vol 2 index TOC + taxonomy-key pointer; reconciled naming to "Exploration 0B" (zero) and fixed the sibling "Exploration 0" stray "O". dev `2f06cd4` → prod `2d79577`; then **hyperlinked its 22 cross-refs** dev `d8841ad` → prod `cc4c01b`. Closes Foster's standing contemplative-practice gap. (FC review noted FL.XLI as a still-open companion item — see below.)

See memory notes [[project_ijh_formation_docs_peer_review]] and [[project_ijh_vol1_four_tradition_peer_review]] for full detail.

---

## OPEN / DEFERRED items (for when John wants them)
- **FL.XLI (Defilement-Cleansing)** — three-stream/four-tradition companion to the FL.XXVII fix: insert *faith as the instrument of baptismal cleansing* so the law doesn't imply baptismal regeneration; distinguish sign from thing signified, irenic to higher-sacramental traditions. (The FL.XXVII half is DONE.)
- ~~**FL.XXIX / XXXI / XXXII reification cluster**~~ **— DONE 2026-06-07** (dev `5f5f295` → prod `58f6f68`). Each definition now names the Holy Spirit (1 Cor. 12:13) + person of Christ as binder, not a group over-soul. **Four-tradition #6 CLOSED.**
- **FL.XXVIII** (Generational Nested Structure) — skipped this session; three-stream #5 suggests adding the cross restoring the broken nesting (Eph. 2:13–22; adoption Eph. 1:5).
- **FL.VII** — still pending from the original FL.I–VI spine-walk.
- **Other still-open three-stream punch-list items** (`_implementation-notes/peer-review-vol1/peer-review-vol1-foster-eldredge-prince.md`): #3 deliverance in FL.XVI; #4 FL.XLII↔FL.XVI link; #6 Deut. 28 covenant transition in FL.VI; #7 FL.XIX softening; #8 confession-of-mouth (Rom. 10:9–10) in Exp1/FL.II; #9 "the force is the Spirit Himself" governing sentence; #10 importunate prayer in FL.X. (#1 FL.XVII curse-breaking and #2 Generational-Transmission split are DONE.)

---

## Conventions reference (don't re-derive)
- Divine pronouns capitalized in book prose; lowercase only inside scripture quotes. [[convention_divine_pronoun_capitalization]]
- dev-first → review → "mirror" to prod; never whole-file-copy config files; targeted edits/diff-first. [[reference_ijh_dev_prod_mirror_workflow]]
- **Preview repo intentionally stale** — do not mirror there unasked.
- John uses the Claude desktop app; explain git/CLI in plain English (ELI5). [[user_ijh_author_new_to_git]]
- Chat links must use markdown `[text](URL)` syntax. [[feedback_chat_links_use_markdown_syntax]]
