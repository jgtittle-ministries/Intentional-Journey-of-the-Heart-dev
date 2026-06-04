# Vol 1 Plain-Language Sweep — Continuation Note (for a fresh session)

**Purpose.** Finish de-jargoning the rest of IJH Volume 1 so every chapter reads at a level a
**scripturally competent 15–16-year-old** can follow — *without changing any theology* and
*without altering any Scripture quote*. **LISTS A, B, AND C ARE ALL COMPLETE AND DEV + PROD IN SYNC — the entire Vol 1
plain-language sweep is DONE.** Lists A + B (38 law-chapters) mirrored earlier (corporate
cluster → prod `f24a131`; substrate → prod `e3735d6`; miracle → prod `9ae2de1`). **List C (all 14
Explorations + supplementals + framing chapters) swept on dev 2026-06-04 (`ea9b4c9` → `9266015`) and
MIRRORED TO PROD `0a297c2`** (byte-identical SHA-256, diff balanced 175/175, all Scripture verified
verbatim). The ONLY remaining item in the whole effort is the **separately-tracked Vol 5 Periodic
Table tier sync (section D)** — which is NOT part of the language sweep. This note is self-contained.

Working repo (dev): `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev`
Folder: `docs/volume-1-laws-of-the-spirit/`
Related: session memory `project_ijh_vol1_four_tradition_peer_review.md`; the peer-review artifact in this same `_implementation-notes/peer-review-vol1/` folder.

---

## The standing rules (non-negotiable)

1. **Plain enough for a 15–16-year-old.** Short sentences, concrete images, few abstract nouns.
2. **Never change a Scripture quote.** Rewrite only the *prose around* the quotes. (Method below
   guarantees this.)
3. **Preserve all theology**, including the peer-review fixes already applied. This is a
   *readability* pass only — no doctrine changes.
4. **Divine pronouns capitalized** (He/Him/His for Father/Jesus/Spirit) in any new prose. Scripture
   quotes keep their translation's orthography as-is.
5. **Drop the catalog tags from prose** (the verbose "Operates at Period 4, Group II, horizontal
   expression…" tails, and inline "P3/GV" etc.). The Period/Group placement still lives in the
   preamble catalog and the Vol 5 table, so nothing is lost. (John approved this.)
6. **dev → review → prod.** Commit each chapter to the `-dev` repo, push, then mirror to the prod
   repo (`…\Intentional-Journey-of-the-Heart`) in a batch with a `Mirror … from dev` commit. The
   `LF will be replaced by CRLF` git warning is benign — ignore it.

---

## The method that works (PROVEN across all 22 List-B chapters — use this)

**Use the `Edit` tool, paragraph by paragraph.** This was the actual workflow for the whole List B
session and it is the recommended one. Why it's safe: the files have **mixed curly + straight
quotes/apostrophes** (the prose has curly `'` in "David's", curly `"…"` in embedded quotes), and the
Edit tool matches **byte-exact** — so a mismatch *fails loudly and changes nothing*. There is
**zero risk of silently corrupting a Scripture quote**: if you reproduce a verse fragment wrong in
`old_string`, the edit just doesn't apply, and you fix it. (The old PowerShell `Splice` helper below
still works as a fallback, but you don't need it.)

Per-chapter loop:
1. `Read` the whole chapter once.
2. Walk it top to bottom. For each **prose** paragraph, do one `Edit` (old_string = the exact
   paragraph, new_string = the plain rewrite). **Leave every Scripture quote block untouched.**
3. **Interleaved Scripture-Ground paragraphs** (shaped `Citation: "verse" commentary`, very common in
   List A) have TWO editable spans: the **lead-in** before the quote *and* the **commentary** after
   it. Edit both, and keep the verse fragment **byte-identical** (copy it through unchanged, curly
   quotes and all). **Gotcha:** it's easy to edit the after-quote commentary and forget the lead-in
   sentence — the grep in step 4 catches these.
4. **Verify with a jargon-grep** (Grep tool, `output_mode: content`) over the finished file, e.g.
   pattern: `\boperational\b|P\d/G[IVX]+|Period \d|the participant|substrate|articulation|the present law|trajectory|constitutive|<any Greek/Latin you glossed>`.
   It should return **no matches** — except the standard nav-button tier label at the very bottom
   (`Operational Law of Wide Consent`, capital O), which is correct and stays. Fix anything else it
   finds, then move on.
5. One commit per chapter:
   `Vol 1 FL.XX: plain-language sweep (de-jargon for a 15-16-year-old reader)` +
   `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Push to dev.

**Mirroring to prod** (after John reviews a batch on the dev site): copy the swept files dev→prod
with PowerShell `Copy-Item -Force`, then **diff-verify before committing**: `git diff --stat` in the
prod repo should show **equal insertions and deletions** per file (paragraph swaps), and
`git diff | grep -E "^[+-]\*?["“]"` should be **empty** (proves no Scripture verse lines changed).
Commit with `Mirror Vol 1 plain-language sweep from dev (FL.…)`, push. Then update this note's STATUS
line with the prod hash.

```powershell
# Fallback only — the Edit tool is preferred. Anchored splice on quote-free first/last words:
function Splice($raw, $a, $bIncl, $new, $tag) {
  $s = $raw.IndexOf($a); $e = $raw.IndexOf($bIncl)
  if ($s -lt 0) { throw "$tag start" }; if ($e -lt 0) { throw "$tag end" }
  $e = $e + $bIncl.Length; if ($e -le $s) { throw "$tag span" }
  return $raw.Substring(0, $s) + $new + $raw.Substring($e)
}
```

**Budget reality:** List A chapters are LONG (often 20+ paragraph-edits each: a framing block, 6–8
interleaved Scripture-Ground paragraphs, a multi-paragraph Mechanism section, a four-point "Why This
Is a Foundational Law" section, a Proposed Law, a Mirror, and a Certainty line). Plan on a handful
per session. The PowerShell working dir is `C:\Users\jgtit\claude` (NOT the repo) — use absolute
paths or `git -C "<repo>"`.

---

## The voice (target register)

Before → after examples from the completed sweeps:
- "the enthroned Objects transmit through the implicit-learning channel" → "a child soaks up what
  her family treasures the same way she picks up its language or accent."
- "the nesting's intactness is an operational condition for the transmission mechanisms" →
  "(nested circles) each circle holds the smaller ones inside it; break a bigger circle and the work
  gets harder in the ones it held."
- "the disproportionate-multiplication regime conditioned on the surrender into Christ's operational
  possession" → "Christ multiplies, freely; the surrender is simply the empty hands that let Him."
- "double portion = magnitude" → "a son asking for the inheritance, not an apprentice asking for a
  bigger battery."

### Jargon → plain glossary (recurring terms)
- "substrate / substrate condition" → "the underlying thing / what holds it up / the soil it grows in"
- "operational / operates / operational dynamic" → usually delete, or "how it works / works"
- "the participant" → "a person / you / she"
- "transmission / transmits" → "passing down / handed on"
- "the [Jacobean/Pauline/Markan] articulation" → "James says / Paul says / Mark tells it"
- "idol-ward face / the law's idol-ward face" → "the dark side of this law"
- "enthrone / enthroned Object" → "put at the center / what the heart treasures most"
- "Period 0 / Group V / P#/G# / Operator tag C+P / Layer is Substrate / directionality tag (V/H/B)"
  → **drop from prose**
- "scale-invariant" → "works at every scale / at every size, from one person to a whole community"
- "bidirectional" → "runs both ways"
- "kind-specificity / positioned readiness / enabling-condition" → plain paraphrase per context
- Keep: the bold **Proposed Law** statement, the **Certainty** tier line, Scripture refs, and the
  chapter's section headings. Translate their *prose*, keep their *structure*.

### Additions learned in the List B session (2026-06-03) — these recur heavily in List A
- **"operational"** is the #1 offender in the dense chapters (operational form/condition/output/
  mechanism/scope/realism/precision, "operationally important," etc.). Usually **delete** it or
  recast as "how it works / in practice / what it produces."
- **Gloss foreign-language terms, don't just drop them.** List A has Greek/Latin/Hebrew (e.g.
  *thlipsis/hypomonē/dokimē/elpis*, *obduratio*, *gnomic will*, *hebel*, *semper reformanda*,
  *ressourcement*, *concupiscentia*). Give the plain English meaning inline; keep at most a
  recognizable term where it genuinely helps, with its meaning right there.
- **"the participant / the pursuer / the practitioner"** → "a person / you / she / the rescuer," etc.
- **"trajectory"** → "path / where it's headed / the slide." **"the dynamic"** → "this / the pattern."
- **"calcify/calcification"** (it's a law NAME — keep the title) → in prose, "harden," and gloss
  "calcifies" on first use ("like soft tissue turning to bone").
- **"metastasize"** (FL.XVIII) → "spread / poison."  **"structured cessation"** (FL.XXIII) →
  "deliberately stopping."  **"embedded practice / substance"** (FL.XXVII) → "built-in practice /
  the content / the heart of it."
- **The "four inclusion criteria" block** (recurs verbatim in the dense chapters under "Why This Is
  a Foundational Law"): render as "meets all four tests for inclusion," then "the backing from many
  writers… / every mainstream Christian tradition accepts it… / clearly runs in one direction… /
  works as a principle…"
- **Mirror heading:** relabel `***Mirror (statement form):***` → `***Mirror (stated form):***`, and
  open with "The dark, idol-ward face of … is …".
- **Catalog tags to strip from prose** (expanded list): `P#/G#`, `P3/GV`, `Period 0/3/4`,
  `Group I/II/IV/V/VI`, `tag V/B`, **`Band 1`**, "scale-invariant" framing sentences, and the stray
  `****,****` bold-marker artifacts (seen in FL.III/FL.VII). All Period/Group data still lives in the
  Vol 5 table, so nothing is lost.
- **Per-chapter diff size** ran ~8–26 changed lines (insertions == deletions). If a prod-mirror diff
  shows unequal counts or any `+/-` on a verse line, STOP — something touched a quote.

---

## STATUS — what's done

**Fully swept (27):** FL.XVII, FL.XIX, FL.XXIV, FL.XXVIII, FL.XXXIX (dev `5dbfcdf`,`62ca920`,
`e2aa374`,`46e3afc`,`6ad4033`; mirrored to prod `f25f022`); **FL.II, FL.III, FL.IV, FL.VI,
FL.VII, FL.VIII** (2026-06-03, dev `254d322`,`61cdab3`,`aec2efb`,`9550d2b`,`c7d537f`,
`adc5988` — **mirrored to prod `ba6815c`**); **FL.X, FL.XI, FL.XII, FL.XIII, FL.XIV**
(2026-06-03, dev `0361669`,`db22715`,`c94e045`,`d964e5b`,`34f2ff2` — **mirrored to prod
`e278780`**); **plus FL.XV, FL.XVI, FL.XVIII, FL.XX, FL.XXI** (2026-06-03, dev `88ac44b`,
`9af80f9`,`e53c089`,`bbac6b8`,`8fa7a31` — **mirrored to prod `e84baab`**); **plus FL.XXII, FL.XXIII,
FL.XXV, FL.XXVI, FL.XXVII, FL.XLVI** (2026-06-03, dev `370d83a`,`7f50044`,`ad18cb5`,`f076aef`,
`c56dde8`,`186e472` — **mirrored to prod `9f7b117`**).

**→ List A corporate/communal cluster (FL.XXIX, XXX, XXXI, XXXII, XXXIII, XXXIV) COMPLETE — dev +
prod IN SYNC 2026-06-04** (dev `4374ddf`,`81a9792`,`c1fda04`,`ce8c8df`,`ee645bd`,`c9ce11e` + dev
polish `+ punctuation tidy`; **mirrored to prod `f24a131`**). Mirror was byte-identical (6/6 SHA256
match), diff was 169 ins / 169 del balanced, and every Scripture wording verified present verbatim.
Notes from this batch: bidirectional Mirrors relabeled
`***Mirror (both directions at once):***` (matching swept FL.XVIII); statement-form Mirrors relabeled
`***Mirror (stated form):***` opening "The dark, idol-ward face of …"; **"Band 2"/"Band 3" labels
stripped** (like "Band 1") while the substantive principle-vs-specific-form distinction was kept in
plain words (FL.XXXIII polity-form left to traditions; FL.XXXIV marriage form scripturally specified
— this contrast preserved); Greek/Hebrew/Latin glossed inline (*barē*/*phortion*, *koinōnia*,
*episkopos*/*diakonos*/*presbyteros*, *dabaq*, *anam cara*, "the worship working on the soul" for
*leitourgia*); the jargon section heading "The Broader Dyadic-Pair-Bond Architectural Territory" →
"Other Close Two-Person Bonds (Beyond Marriage)"; every inline P#/G# tag dropped; "the catalog" kept
as the live term for the law table. All six jargon-grep-verified clean.

**→ List B (the entire moderate tier, 22 chapters) is COMPLETE; dev + prod in sync as of
2026-06-03.** Across the session: Greek/Latin/Hebrew glossed to plain English; the heavy
"operational / substance / the participant / trajectory" register stripped; `****,****` bold
artifacts cleaned (FL.III/VII); "metastasis" plain-rendered (FL.XVIII); every chapter
jargon-grep-verified; every prod mirror diff-verified (Scripture untouched). The four prod-mirror
commits this session: `ba6815c`, `e278780`, `e84baab`, `9f7b117`.

**Already largely plain from the peer-review edits (light pass or skip):** FL.I (rewritten in #2),
FL.V (gospel-order edit), FL.IX (Generosity edit), Opening Miracle Frame (#1 — but its Einstein/
C.S. Lewis paragraphs + the "Connections" footnote still have jargon → light sweep), Kingdom-Now
framing chapter (mostly readable), Exploration 8 (#8 — mostly plain now), "A Word to My Kids"
(already warm — skip), preamble catalog one-liners (fine as-is).

---

## REMAINING — the sweep checklist (grouped by density)

### A. Densest (substrate/operational-heavy) — **✓ COMPLETE 2026-06-04 (dev + prod in sync)**
*All 16 done and mirrored to prod in three verified batches: corporate/communal FL.XXIX–XXXIV →
prod `f24a131`; substrate FL.XXXV–XXXVIII → prod `e3735d6`; miracle-cluster FL.XL–XLV → prod
`9ae2de1`. Lessons that recurred (apply these in List C too where relevant): strip the catalog
scaffolding hard — Operator-tag codes (C / C+P / C+T), "Period N / Group N cell," "candidate pass /
matured catalog," version IDs (`v5_6_0_17`), and the "V/H/B/I tag" taxonomy paragraph — while keeping
the substantive point each carried (e.g. "this is Christ's own work, we only receive it" for the
Christ-operated miracle laws). For the Christ-operated laws the Mirror isn't a God-ward/idol-ward
pair, so I used a plain descriptive label like `***Mirror (Christ's work — the failure is refusing
it):***`. Removed one stale process-divider line in FL.XLV ("End of the canonical Foundational
Laws…") since FL.XLVI follows it. Greek/Hebrew/Latin glossed inline throughout (sēmeia, ego eimi,
talitha cumi [kept — preserved Scripture], ex opere operato, res et sacramentum, unio mystica,
Nachfolge, simul justus et peccator); "parousia" → "Christ's return."*
- [x] FL.XXXV Trust-Substrate ✓ 2026-06-04 (dev `8896da9`)
- [x] FL.XXXVI Eschatological Glory ✓ 2026-06-04 (dev `0d50be3`)
- [x] FL.XXXVII Worship Alignment ✓ 2026-06-04 (dev `a5d564d`)
- [x] FL.XXXVIII Soul-Restoration ✓ 2026-06-04 (dev `7eaf2d8`)
- [x] FL.XL Abiding-Fruitfulness ✓ 2026-06-04
- [x] FL.XLI Defilement-Cleansing Reversal ✓ 2026-06-04
- [x] FL.XLII Kingdom-Confrontation Authority ✓ 2026-06-04
- [x] FL.XLIII Cross-Boundary Faith-Access ✓ 2026-06-04
- [x] FL.XLIV Sign-as-Revelation ✓ 2026-06-04
- [x] FL.XLV Voice-of-Christ-Reaches-into-Death ✓ 2026-06-04
- [x] FL.XXIX Corporate Emotional Integration ✓ 2026-06-04 (dev `4374ddf`)
- [x] FL.XXX Communal Soul-Care for the Wounded ✓ 2026-06-04 (dev `81a9792`)
- [x] FL.XXXI Corporate Scriptural Reception ✓ 2026-06-04 (dev `c1fda04`)
- [x] FL.XXXII Communal Worship Heart-Alignment ✓ 2026-06-04 (dev `ce8c8df`)
- [x] FL.XXXIII Community Polity-Structure ✓ 2026-06-04 (dev `ee645bd`)
- [x] FL.XXXIV Marriage Covenant Architecture ✓ 2026-06-04 (dev `c9ce11e`)

### B. Moderate (individual + community laws not yet touched)
- [x] FL.II Confession-Restoration ✓ 2026-06-03
- [x] FL.III Heart-Throne ✓ 2026-06-03
- [x] FL.IV Humility-Exaltation ✓ 2026-06-03
- [x] FL.VI Hear-and-Obey ✓ 2026-06-03
- [x] FL.VII Drawing-Near Reciprocity ✓ 2026-06-03
- [x] FL.VIII Desire-for-God ✓ 2026-06-03
- [x] FL.X Ask-Seek-Knock ✓ 2026-06-03
- [x] FL.XI Renewal-of-Mind ✓ 2026-06-03
- [x] FL.XII Honor-Authority Flourishing ✓ 2026-06-03
- [x] FL.XIII Pure-Heart Vision ✓ 2026-06-03
- [x] FL.XIV Vanity-of-Substitutes ✓ 2026-06-03
- [x] FL.XV Hardening ✓ 2026-06-03
- [x] FL.XVI Bondage ✓ 2026-06-03
- [x] FL.XVIII Bitter-Root Community ✓ 2026-06-03
- [x] FL.XX Gathered-Body Discernment ✓ 2026-06-03
- [x] FL.XXI Household Formation ✓ 2026-06-03
- [x] FL.XXII Endurance-Hope ✓ 2026-06-03
- [x] FL.XXIII Sabbath Rest ✓ 2026-06-03
- [x] FL.XXV Restoration-of-the-Erring ✓ 2026-06-03
- [x] FL.XXVI Doctrinal Calcification ✓ 2026-06-03
- [x] FL.XXVII Thick Practice Transmission ✓ 2026-06-03
- [x] FL.XLVI Communal Truth-Telling ✓ 2026-06-03 (was already the warmest prose — light pass)

**↑ List B COMPLETE (22 moderate chapters) and List A COMPLETE (16 densest), all dev + prod in sync.**

**↑↑ List C COMPLETE (all 14 essays/supplementals/framing chapters), dev + prod IN SYNC as of
2026-06-04 (dev `ea9b4c9` → `9266015`; prod mirror `0a297c2`, balanced 175/175, Scripture verbatim).
The WHOLE Vol 1 plain-language sweep is now FINISHED — the only remaining task is the
separately-tracked Vol 5 tier sync (section D), which is not part of the language sweep.**

### C. Explorations / supplementals / framing — **✓ COMPLETE 2026-06-04 (all 14; dev + prod IN SYNC — prod mirror `0a297c2`)**
*All 14 swept and pushed to dev in 14 per-chapter commits (`ea9b4c9` → `9266015`, pushed `f3d82cb..9266015`). Each was jargon-grep-verified and diff-verified (balanced ins==del, no Scripture line altered; embedded inline verse fragments confirmed verbatim where present). Lessons specific to List C: these are essays, so the work was different from A/B — no catalog tags to strip, but a **physics-and-systems metaphor family** instead. The right move on the author's deliberate analogies (electrical "ground reference" in Exp 5; circuit/transformer in Exp 7; stock/feedback-loop and the f×g×h equation in Spiritual Force) was to **keep the analogy and the substance but gloss the technical terms inline** so a teen can follow — NOT to delete them (they're John's own teaching voice, and the Spiritual Force chapter is literally about building toward equations). "Force multiplier" kept as a recognizable idiom. Two scholarly "Open Trails" tradition-notes in Connecting the Dots left as reference apparatus. Renamed a few jargon section-headings to plain ones (e.g. "The Feedback Loop"→"The Loop That Feeds Itself"; "The Time Delay Factor"→"The Time Delay"; "The Discovery That Changes the Equations"→"...the Picture"; "The Developing Dynamics"→"Starting to Put Numbers on It").*
*Orientation — READ THIS, List C is different from A/B.* These are **essays / teaching chapters, not
law-entries** — so they do **NOT** have the "Why This Is a Foundational Law" four-criteria block, the
`***Mirror***`, or the `***Certainty***` tail. No Operator/Period/Group catalog tags to strip either
(those live only in the law chapters). The jargon here is a **different family**: physics-and-systems
metaphors (voltage/circuit/transformer; stock/inflow/feedback-loop/field-equations), philosophy-speak
(Einstein/C.S. Lewis, "metaphysical presupposition," "bandwidth"), and taxonomy abstraction
("Structural vs Operational Law"). Same standing rules apply (15–16-yr-old reading level; verses
byte-identical; divine pronouns capitalized; "the catalog" stays). Workflow identical: Read → Edit
paragraph-by-paragraph → grep-verify (tune the grep to the physics/systems terms below) → commit per
chapter to dev → push → mirror a batch on John's word. Files live in the same
`docs/volume-1-laws-of-the-spirit/` folder.
- [x] Taxonomy Key — `taxonomy-key-how-this-volume-classifies-its.md` ✓ 2026-06-04 (dev `ea9b4c9`) — kept the P/G/direction reference key intact (the chapter's whole purpose), plained the explanatory prose around it
- [x] Exploration 1 — How to Get Faith — `exploration-01-how-to-get-faith.md` ✓ 2026-06-04 (dev `3184cfc`)
- [x] Exploration 2 — My Spirit, Heart, Soul, and Body — `exploration-02-my-spirit-heart-soul-and.md` ✓ 2026-06-04 (dev `9770dce`) — glossed dichotomist/trichotomist + "forensic"; capitalized two stray lowercase divine pronouns in prose; embedded 1 Thess 5:23 quote verified verbatim
- [x] Supplemental — The Three Desires — `supplemental-three-desires.md` ✓ 2026-06-04 (dev `8bb04fb`) — readability pass only (didn't re-argue the chapter)
- [x] Exploration 3 — Faith, Hope, and Love — `exploration-03-relationship-of-faith-hope-and.md` ✓ 2026-06-04 (dev `eac0b9e`) — inline 1 John 4:18 fragment verified
- [x] Exploration 4 — Wisdom, Knowledge, Understanding, Discernment — `exploration-04-wisdom-knowledge-understanding-and-discernment.md` ✓ 2026-06-04 (dev `ce4a545`)
- [x] Exploration 5 — The Gateway Condition (Fear of the Lord) — `exploration-05-gateway-condition.md` ✓ 2026-06-04 (dev `cd05ba7`) — kept the author's electrical "ground reference" analogy but glossed voltage/ground for a teen
- [x] Exploration 6 — The Obedience Channel — `exploration-06-obedience-channel.md` ✓ 2026-06-04 (dev `bd48275`) — "signal/noise/gain/systems" recast plainly; kept the C.S. Lewis paragraph
- [x] Exploration 7 — Spiritual Authority — `exploration-07-spiritual-authority.md` ✓ 2026-06-04 (dev `ccdebef`) — kept "force multiplier" (recognizable idiom + chapter's name, now glossed); made the circuit/transformer/voltage image plain ("broken wire" vs "good wire built for the job")
- [x] Spiritual Force, Energy, and Power — `spiritual-force-energy-and-power.md` ✓ 2026-06-04 (dev `657693d`) — densest of List C: "stock"→"reservoir", "inflow/outflow"→"fills/drains", glossed Maxwell/field-equations/conservation/heuristic; KEPT the f×g×h equation but explained "multiply not add" plainly; cleaned a stray `**` artifact; 7 embedded verse fragments all verified verbatim
- [x] Connecting the Dots — `connecting-the-dots-how-the-eight-explorations.md` ✓ 2026-06-04 (dev `ed25514`) — light; **the three tradition trail-notes (Wesleyan-Holiness / Global Pentecostal / Sacramental) were intentionally LEFT as scholarly "Open Trails / Further reading" pointer material** (annotated bibliography for a researcher carrying the work forward — same treatment bibliography got in Lists A/B). Only the two candidate-law trail bullets (Trust-Direction, Seek-First) had their antecedent/consequent/allusive/propositional jargon plained.
- [x] Supplemental — Held Tensions & Shadow Pairs — `supplemental-held-tensions-and-shadow-pairs.md` ✓ 2026-06-04 (dev `6a47a97`) — competing-values "pole/deformation/register/orthogonal" plained; BSCP draft quote + all 3 cross-links verified verbatim
- [x] Opening Miracle Frame — `opening-miracle-frame.md` ✓ 2026-06-04 (dev `146b288`) — Newtonian/Einstein/"projection of a general framework"/"anomalous" recast as plain "smaller picture / bigger picture"; footnote "metaphysical presupposition"/"bandwidth" plained
- [x] "What We Are Being Formed For" Kingdom-Now framing — `what-we-are-being-formed-for-the.md` ✓ 2026-06-04 (dev `9266015`) — light; "operational/corpus/proof-text/claim registry/epistemic/propositional/directionality/provenance/axioms" plained or glossed; this chapter is very quote-dense — all inline ESV quotes verified byte-identical on every changed line
- [ ] (skip) `index.md`, `periodic-table-see-volume-5.md`, `word-to-my-kids-at-the-end.md`, `read-me-first.md`, `foundational-laws-thirty-eight-operational-laws-of-wide.md` (preamble one-liners, fine as-is)

### D. Separately tracked (NOT part of the language sweep)
- [x] **Vol 5 Periodic Table tier sync** — ✓ DONE 2026-06-04 (dev `292cd96` → prod mirror `e42b91d`).
      Matched FL.XXVIII (→ **Reasonably Inferred**, still a Foundational law — only the certainty
      dropped) and FL.XXXIX (→ **Candidate, Reasonably Inferred**, matching Vol 1's "Reasonably
      Inferred (Candidate Law)"). 4 surgical label edits in `periodic-table-of-spiritual-laws-a-summing.md`
      (2 table cells + 2 per-entry headers); Band/Operator/structural-completeness prose left intact
      because FL.XXVIII stays Foundational and the P0/GV completeness claim never counted FL.XXXIX.
      Mirror verified SHA-256 byte-identical, diff 4/4 balanced. Confirmed the note's two-law scope was
      exactly right: in Vol 1, ONLY FL.XXVIII and FL.XXXIX sit at Reasonably Inferred; FL.XL–XLVI are
      all Clearly Taught, so their certainty already matched Vol 5.

      **✓ BROADER "38-vs-46" FRAMING RECONCILIATION — DONE & DEV+PROD IN SYNC 2026-06-04 (dev `af070fa`
      → prod mirror `e9bab0e`, SHA-256 byte-identical, diff 24/24).** Reconciled the whole Vol 5 catalog framing to Vol 1's
      "38 Foundational Laws of wide consent (FL.I–XXXVIII) + 8 candidate laws under community review
      (FL.XXXIX–XLVI)." 24 balanced label/prose edits: (1) every count statement (intro line 17,
      snapshot line 19/67, legend provenance line 83, layer line 93, conclusion 1004/1008/994) now reads
      "38 Foundational + 8 candidates" (55-law total unchanged: 38+8+8 spec+1 anomaly); (2) all 8
      per-entry headers FL.XXXIX–XLVI now `(Candidate)`, and their table cells carry a `Candidate` marker;
      (3) "admitted" reframed to "added as candidates / surfaced," and FL.XLI's body no longer self-calls
      "admitted Foundational Law"; (4) structural-completeness prose preserved where still true (P3 + P4
      stay "complete at the Foundational tier" — every Group keeps a genuine FL.I–XXXVIII entry) and
      recast where a candidate does the work (P0/GI positive-substrate gap + P5/GI now credited to the
      FL.XL / FL.XLV candidates; P3/GV "densest cell" recast as 3 Foundational + the FL.XLVI candidate).
      Resolves the 38-vs-45/46 discrepancy the four-tradition peer review noted
      (see [[project_ijh_vol1_four_tradition_peer_review]]). **DONE — dev + prod in sync; nothing left.**

---

## How to start the new session (List C — the last list)

**Paste this as the first message:**

> *Continue the Vol 1 plain-language sweep per
> `_implementation-notes/peer-review-vol1/plain-language-sweep-continuation.md`. **List B and all of
> List A are done and dev+prod in sync — only List C (Explorations + supplementals + framing)
> remains.** Heads-up: List C chapters are essays, NOT law-entries, so there's no four-criteria /
> Mirror / Certainty structure and no catalog tags — the jargon is physics-and-systems metaphors
> instead (voltage/circuit in Exploration 7; stock/inflow/feedback-loop/field-equations in Spiritual
> Force, Energy, and Power; Einstein/C.S. Lewis in the Opening Miracle Frame). Start with the
> Taxonomy Key and Exploration 1, or go straight at the heaviest (Spiritual Force/Energy/Power and
> Exploration 7). Do a few per turn, one commit per chapter to dev, grep-verify each (verses
> byte-identical), and mirror a batch to prod when I say so.*

Workflow each turn (unchanged from List A/B): `Read` chapter → `Edit` prose paragraph-by-paragraph
(verses verbatim) → grep-verify (point the grep at the physics/systems terms, not the catalog terms)
→ commit per chapter to dev → push. **Prod-mirror discipline** (proven across all 3 List-A batches):
`Copy-Item -Force` dev→prod, then verify (1) SHA-256 byte-identical dev vs prod, (2) `git diff --stat`
balanced ins≈del, (3) a Python check that every ≥40-char double-quoted span in HEAD survives verbatim
in the swept file — only then commit `Mirror … from dev` and push. Mirror only after John reviews on
the dev site
([https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/)),
or when he says "mirror and continue." Update the STATUS line + check the boxes here as you go.
**After List C, the whole Vol 1 sweep is finished** — only the separately-tracked Vol 5 tier sync
(section D) would remain.
