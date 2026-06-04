# Vol 1 Plain-Language Sweep — Continuation Note (for a fresh session)

**Purpose.** Finish de-jargoning the rest of IJH Volume 1 so every chapter reads at a level a
**scripturally competent 15–16-year-old** can follow — *without changing any theology* and
*without altering any Scripture quote*. **37 chapters are done: all of List B (the moderate tier),
the 5 from the prior peer-review session, the List-A corporate/communal cluster FL.XXIX–XXXIV, AND
the List-A substrate cluster FL.XXXV–XXXVIII (all 2026-06-04).** List B + FL.XXIX–XXXIV are dev+prod
in sync (corporate cluster mirrored to prod `f24a131`); the **substrate cluster FL.XXXV–XXXVIII is on
dev, awaiting John's review before the prod mirror.** What remains in List A: the **miracle-cluster
FL.XL–XLV (6 chapters)**. Then **List C (Explorations + supplementals + framing)**. This note is
self-contained: a new session can start from here with no ramp-up. **NEXT UP: the miracle-cluster
FL.XL–XLV** (narrative-heavy, lots of interleaved Gospel quotes — watch the lead-in sentences).

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

### A. Densest (substrate/operational-heavy) — **THE NEXT SESSION'S WORK**
*Orientation: these split into three clusters. (1) **Substrate/soul laws** FL.XXXV–XXXVIII (Trust,
Eschatological Glory, Worship Alignment, Soul-Restoration) — heaviest on "substrate / operational /
the participant." (2) **Miracle-cluster** FL.XL–XLV (Abiding-Fruitfulness, Defilement-Cleansing,
Kingdom-Confrontation Authority, Cross-Boundary Faith-Access, Sign-as-Revelation, Voice-of-Christ-
Reaches-into-Death) — narrative-heavy, lots of interleaved Gospel quotes; watch the lead-in
sentences. (3) **Corporate/communal laws** FL.XXIX–XXXIV (Corporate Emotional Integration, Communal
Soul-Care, Corporate Scriptural Reception, Communal Worship Heart-Alignment, Community Polity-
Structure, Marriage Covenant Architecture) — same "operational / P3-or-P4 / GV" register as the
List B community laws (FL.XVIII/XX/XXV/XXVI/XXVII), so those finished chapters are the best
templates to imitate. Expect the recurring four-point "Why This Is a Foundational Law" block and a
`***Mirror***` + `***Certainty***` tail in most. Do a handful per session; mirror per John's review.*
- [x] FL.XXXV Trust-Substrate ✓ 2026-06-04 (dev `8896da9`)
- [x] FL.XXXVI Eschatological Glory ✓ 2026-06-04 (dev `0d50be3`)
- [x] FL.XXXVII Worship Alignment ✓ 2026-06-04 (dev `a5d564d`)
- [x] FL.XXXVIII Soul-Restoration ✓ 2026-06-04 (dev `7eaf2d8`)
- [ ] FL.XL Abiding-Fruitfulness
- [ ] FL.XLI Defilement-Cleansing Reversal
- [ ] FL.XLII Kingdom-Confrontation Authority
- [ ] FL.XLIII Cross-Boundary Faith-Access
- [ ] FL.XLIV Sign-as-Revelation
- [ ] FL.XLV Voice-of-Christ-Reaches-into-Death
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

**↑ List B COMPLETE (all 22 moderate chapters swept). Remaining: List A (the 16 densest) + List C (Explorations/supplementals).**

### C. Explorations / supplementals / framing
- [ ] Taxonomy Key (Structural vs Operational Law jargon)
- [ ] Exploration 1 — How to Get Faith
- [ ] Exploration 2 — My Spirit, Heart, Soul, and Body
- [ ] Supplemental — The Three Desires (review flagged as weakest; check tier language too)
- [ ] Exploration 3 — Faith, Hope, and Love
- [ ] Exploration 4 — Wisdom, Knowledge, Understanding, Discernment
- [ ] Exploration 5 — The Gateway Condition (Fear of the Lord)
- [ ] Exploration 6 — The Obedience Channel
- [ ] Exploration 7 — Spiritual Authority (the "force multiplier / circuit / transformer / voltage" language)
- [ ] Spiritual Force, Energy, and Power (the "stock / inflow / outflow / reinforcing feedback loop / field equations" systems-dynamics jargon)
- [ ] Connecting the Dots (check)
- [ ] Opening Miracle Frame — Einstein/C.S. Lewis paragraphs + "Connections" footnote ("metaphysical presupposition," "bandwidth," "Spirit Stage")
- [ ] (skip) index.md, periodic-table-see-volume-5.md, A Word to My Kids, read-me-first.md

### D. Separately tracked (NOT part of the language sweep)
- [ ] **Vol 5 Periodic Table tier sync** — match FL.XXVIII (→ Reasonably Inferred) and FL.XXXIX
      (→ candidate) to the Vol 1 tier drops. Vol 5 not yet touched.

---

## How to start the new session (List A)

**Paste this as the first message:**

> *Continue the Vol 1 plain-language sweep per
> `_implementation-notes/peer-review-vol1/plain-language-sweep-continuation.md`. List B is done and
> mirrored, and the List-A corporate/communal cluster **FL.XXIX–FL.XXXIV is done on dev** (awaiting
> John's review before the prod mirror). Pick up the rest of **List A**: the substrate laws
> **FL.XXXV–XXXVIII** (Trust-Substrate, Eschatological Glory, Worship Alignment, Soul-Restoration —
> heaviest on "substrate/operational"), then the miracle-cluster **FL.XL–XLV** (narrative-heavy,
> lots of interleaved Gospel quotes — watch the lead-in sentences). Do a few per turn, one commit
> per chapter to dev, jargon-grep-verify each, and mirror a batch to prod when I say so.*

Workflow each turn: `Read` chapter → `Edit` prose paragraph-by-paragraph (verses verbatim) →
jargon-grep-verify → commit to dev → push. Mirror to prod only after John reviews on the dev site
([https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/)).
Update the STATUS line and check the boxes here as you go. After List A, List C remains
(Explorations + supplementals + framing).
