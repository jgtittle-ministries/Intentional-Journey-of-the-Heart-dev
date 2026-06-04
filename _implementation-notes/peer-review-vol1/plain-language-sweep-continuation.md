# Vol 1 Plain-Language Sweep — Continuation Note (for a fresh session)

**Purpose.** Finish de-jargoning the rest of IJH Volume 1 so every chapter reads at a level a
**scripturally competent 15–16-year-old** can follow — *without changing any theology* and
*without altering any Scripture quote*. Five chapters are done; ~40 sections remain. This note is
self-contained: a new session can start from here with no ramp-up.

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

## The method that works (anchored PowerShell splices)

These files use **straight apostrophes/quotes** (not curly), so full-paragraph string anchors match
reliably. Replace only prose paragraphs; leave Scripture quote blocks untouched.

```powershell
function Splice($raw, $a, $bIncl, $new, $tag) {
  $s = $raw.IndexOf($a); $e = $raw.IndexOf($bIncl)
  if ($s -lt 0) { throw "$tag start" }; if ($e -lt 0) { throw "$tag end" }
  $e = $e + $bIncl.Length; if ($e -le $s) { throw "$tag span" }
  return $raw.Substring(0, $s) + $new + $raw.Substring($e)
}
```
- For each jargon paragraph, `Splice` from its first words to its last words with the new plain
  text. Because start/end are *inside* the paragraph, the surrounding `\n\n` blank lines are
  preserved (this avoids the paragraph-merge bug — do **not** anchor across blank lines, and don't
  use a "keep-then-resume" splice unless you re-add the `\n\n` yourself).
- For a scripture-citation paragraph shaped `Citation: "quote" commentary`, splice only the
  **commentary** (anchor its first words → its last words); the quote stays verbatim.
- Write with `[System.IO.File]::WriteAllText($f, $raw, (New-Object System.Text.UTF8Encoding($false)))`.
- **Verify** after each file: a `[regex]::Matches($raw, 'jargon|terms|here')` count that should be 0,
  then `Read` the whole file to confirm the quotes are intact and the prose flows.
- Commit one chapter per commit; message like:
  `Vol 1 FL.XX: plain-language sweep (de-jargon for a 15-16-year-old reader)` +
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

**Budget reality:** a dense chapter (read + apply + verify) is a real chunk of context. Plan on
roughly **4–6 dense chapters per session** before quality/error-risk climbs. Likely 2–3 sessions
total for what remains.

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

---

## STATUS — what's done

**Fully swept (21):** FL.XVII, FL.XIX, FL.XXIV, FL.XXVIII, FL.XXXIX (dev `5dbfcdf`,`62ca920`,
`e2aa374`,`46e3afc`,`6ad4033`; mirrored to prod `f25f022`); **FL.II, FL.III, FL.IV, FL.VI,
FL.VII, FL.VIII** (2026-06-03, dev `254d322`,`61cdab3`,`aec2efb`,`9550d2b`,`c7d537f`,
`adc5988` — **mirrored to prod `ba6815c`**); **FL.X, FL.XI, FL.XII, FL.XIII, FL.XIV**
(2026-06-03, dev `0361669`,`db22715`,`c94e045`,`d964e5b`,`34f2ff2` — **mirrored to prod
`e278780`**); **plus FL.XV, FL.XVI, FL.XVIII, FL.XX, FL.XXI** (2026-06-03, dev `88ac44b`,
`9af80f9`,`e53c089`,`bbac6b8`,`8fa7a31` — **mirrored to prod `e84baab`**); **plus FL.XXII, FL.XXIII,
FL.XXV, FL.XXVI, FL.XXVII, FL.XLVI** (2026-06-03, dev `370d83a`,`7f50044`,`ad18cb5`,`f076aef`,
`c56dde8`,`186e472` — pushed to dev, **prod mirror pending John's review**). **List B (the entire
moderate tier) is now COMPLETE.** Greek/Latin/Hebrew glossed throughout; the heavy "operational/
substance/the participant/trajectory" register stripped; every chapter jargon-grep-verified after
editing; catalog tags (P#/G#, Band 1, scale-invariant, etc.) dropped from all prose.
Catalog tags dropped throughout; `****,****` artifacts cleaned in FL.III/FL.VII; Latin/Greek/Hebrew
terms glossed to plain English in FL.XIV/XV/XVI; medical "metastasis" register plain-rendered in
FL.XVIII; the dense community/generational chapters (FL.XX gathered-body, FL.XXI household)
de-jargoned but kept theologically intact.

**Already largely plain from the peer-review edits (light pass or skip):** FL.I (rewritten in #2),
FL.V (gospel-order edit), FL.IX (Generosity edit), Opening Miracle Frame (#1 — but its Einstein/
C.S. Lewis paragraphs + the "Connections" footnote still have jargon → light sweep), Kingdom-Now
framing chapter (mostly readable), Exploration 8 (#8 — mostly plain now), "A Word to My Kids"
(already warm — skip), preamble catalog one-liners (fine as-is).

---

## REMAINING — the sweep checklist (grouped by density)

### A. Densest (substrate/operational-heavy — handle like FL.XXVIII; ~1–2 per session)
- [ ] FL.XXXV Trust-Substrate
- [ ] FL.XXXVI Eschatological Glory
- [ ] FL.XXXVII Worship Alignment
- [ ] FL.XXXVIII Soul-Restoration
- [ ] FL.XL Abiding-Fruitfulness
- [ ] FL.XLI Defilement-Cleansing Reversal
- [ ] FL.XLII Kingdom-Confrontation Authority
- [ ] FL.XLIII Cross-Boundary Faith-Access
- [ ] FL.XLIV Sign-as-Revelation
- [ ] FL.XLV Voice-of-Christ-Reaches-into-Death
- [ ] FL.XXIX Corporate Emotional Integration
- [ ] FL.XXX Communal Soul-Care for the Wounded
- [ ] FL.XXXI Corporate Scriptural Reception
- [ ] FL.XXXII Communal Worship Heart-Alignment
- [ ] FL.XXXIII Community Polity-Structure
- [ ] FL.XXXIV Marriage Covenant Architecture

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

## How to start the new session

Suggested first message: *"Continue the Vol 1 plain-language sweep per
`_implementation-notes/peer-review-vol1/plain-language-sweep-continuation.md`. Start with FL.II–FL.IV,
show me each before pushing."* — then work down list B (moderate) or A (dense) a few at a time,
pushing to dev per chapter and mirroring to prod in a batch when John has reviewed.
