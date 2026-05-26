# IJH Cross-Volume Readability and Consistency Audit (v1)

**Triggering observation.** Across the session that closed Phases 1–4 of the periodic-table-restructure arc, the catalog accumulated substantial new structural machinery: seven new Foundational Laws (FL.XXXIX–XLV); the Substrate Layer articulation; the Operator tag (six values: P / S+P / C / C+P / T+P / C+T); the Christological-condition Mirror form (a fourth Mirror form); the scale-range attribute across NT breakpoints; per-entry attribute lines on every PT entry; two new "What the Shape Reveals" sub-sections (Substrate-Revealing Operations; Functional Specialization Across Volumes); the Vol 6 catalog history's seventh major architectural decision. The accumulation is operationally appropriate — each move was earned by a real structural finding — but it raises a question that the audit needs to answer: **can a first-time reader still find their way in?**

**Audit scope.** Cross-volume read for consistency and readability. Identify what overwhelms a new reader, what is internally inconsistent across volumes, and where the matured-catalog vocabulary has spread without scaffolding.

**Audit posture.** Conservative. The catalog's analytical depth is the point; the audit's job is not to remove the depth but to layer the reader's access to it.

---

## Top findings

### Finding A — The HOW TO READ block in the Vol 5 PT chapter was overwhelming

**Issue.** Before the audit pass, the HOW TO READ block stacked eight attribute classes equally: directionality, confidence, speculative marker, band, layer, scale-range, operator, mirror field, plus provenance prefixes and other markers. A first-time reader had to learn the full vocabulary before reading the table.

**Fix applied (this audit).** Tiered the HOW TO READ block into two sub-sections: *Essential metadata* (read first — directionality, confidence, speculative marker, band, provenance prefixes, other markers, reference list pointer) and *Matured-catalog metadata* (second-pass reading — layer, scale-range, operator, mirror field with the four forms). The matured-catalog metadata is explicitly framed as additive — the essential metadata is sufficient to locate and read any entry at a working level.

**Status: closed.**

### Finding B — No first-time-reader scaffolding at chapter entry

**Issue.** The Vol 5 PT chapter opens directly into the consolidated reference's structural argument. A first-time reader hit the deep end immediately. The chapter assumes familiarity with Vol 1 FL articulation, the catalog's expansion arc, and the matured-catalog vocabulary.

**Fix applied (this audit).** Added a "Reader's Path" tip callout at the top of the Vol 5 PT chapter naming three reading tiers (Essential 15–20 min; Second-pass; Deep-dive) and explicitly framing the matured-catalog metadata as additive rather than required.

**Status: closed.**

### Finding C — The Slim Format table cells are bloated, especially P0/GI

**Issue.** The P0/GI cell now holds five entries, each with parenthetical attribute notes (Band, Operator). The cell line is approximately 5 entries × 60 characters average = ~300 characters wide, which renders poorly on narrow screens and creates a wall of text in the row. Other cells (P0/GVI at 4 entries; P0/GV at 4 entries) have the same problem to a lesser degree.

**Fix recommended for Phase 5+.** Consider one of:
- (a) Remove the parenthetical attribute notes from the Slim Format cells (Band, Operator, etc. live in the reference list and on each entry's attribute line; the Slim Format doesn't need to carry them too).
- (b) Switch the dense cells to a list format within the cell rather than a `·`-separated prose run.
- (c) Reduce cell content to just `FL.X Name (V) Confidence` with all other attributes in the reference list only.

**Status: deferred to Phase 5+.** Not applied in this audit because it's a structural format decision that affects readers' expectations of the Slim Format's information density; deserves its own consideration pass.

### Finding D — The matured-catalog terminology has spread without a glossary

**Issue.** Terms introduced or formalized during the periodic-table-restructure arc — "matured-catalog," "Alt E" / "Alternative-E," "Christological-condition Mirror form," "Substrate Layer," "the three phases of the restructure," "ambiguous-cases log" — appear in multiple places (Vol 5 PT chapter, Vol 6 catalog history, the new FL chapters, the per-entry attribute lines) without a single defined-glossary location. A reader encountering "matured-catalog" in one place has to infer its meaning from context.

**Fix recommended for Phase 5+.**
- (a) Add a brief glossary section to the Vol 5 PT chapter's opening, defining the matured-catalog terms in 1–2 sentences each.
- (b) Or: add a footnote/inline-link on first occurrence of each term pointing to a single canonical definition.

**Status: deferred to Phase 5+.**

### Finding E — Per-FL chapter consistency varies

**Issue.** The Foundational Law chapters were written across the catalog's expansion arc and vary substantially in depth, style, and structure:
- The earliest FL chapters (FL.I–XIII original Vol 1) are shorter and more pastoral in voice.
- The middle FL chapters (FL.XIV–XXXIV expansion arc) are denser and more analytical.
- The Phase 1/3 FL chapters (FL.XL, XXXIX, XLI–XLV) are the longest and most attribute-aware, with explicit mentions of Operator, Layer, Mirror form, and inclusion-bar checks in the prose.

A reader who clicks through from FL.I to FL.XLV moves through three distinct chapter genres without warning.

**Fix recommended for Phase 5+.**
- (a) Consider a focused chapter-consistency pass that brings the early FL chapters to a baseline depth (not necessarily the full Phase 3 depth, but enough that the genre shift is gradual).
- (b) Or accept the variation as a feature of the catalog's iterative development and note it in the Vol 1 overview.

**Status: deferred to Phase 5+.**

### Finding F — The "What the Shape Reveals" series has grown to many sub-sections

**Issue.** The Vol 5 PT chapter's "What the Shape of the Table Reveals" section now holds the following sub-sections:
- The Group V Column's Structural Density
- The Endurance-Hope and Suffering-as-Formation Parent-Child Relationship
- The Community-Relational Substrate at P3/GV
- What the Completed Period 4 Row Reveals
- The Body of Christ Master-Frame
- The Period 3 Row's Structural-Completion
- The Group VI Architectural-Framework Across Scales
- Vol 3 Forward-References Review and Resolution
- The Period 0 Row's Proportionality Pattern
- The Threshold/Gateway Pattern
- Cross-Group, Cross-Scale Nearness-or-Distance Articulation
- The Period 0 Row's Substrate-and-Operation Architecture
- Substrate-Revealing Operations (Phase 2 addition)
- The Functional Specialization Across Volumes (Phase 2 addition)

That's 14 sub-sections. Each one names a structural pattern. A reader looking for "the catalog's structural insights" finds a wall of headers.

**Fix recommended for Phase 5+.**
- (a) Add a navigational opening to the "What the Shape of the Table Reveals" section that lists the sub-sections by category (row-completion findings, cross-row patterns, Group-column patterns, matured-catalog insights) so a reader can jump to what they want.
- (b) Or consider consolidating closely-related sub-sections.

**Status: deferred to Phase 5+.**

### Finding G — Dev vs prod differentiation is minimal

**Issue.** The dev preview site has a danger callout at the top of the home page ("YOU ARE VIEWING THE DEV PREVIEW SITE") but the rest of the content is essentially identical to prod. A reader who lands on dev via a direct chapter link may not see the warning. The two sites' identity differences are only in `mkdocs.yml` (site_name, site_description, site_url, repo_url) and the home page callout.

**Fix recommended for Phase 5+ if at all.** This is a low-priority observation — the dev/prod parallelism is intentional (dev is published for John's review before prod mirror) and the warning is in the most-prominent place. Possibly add a small "DEV" badge to the site header on dev so it's visible from any page, not just the home. Probably not worth the work.

**Status: noted, no action recommended.**

### Finding H — The home page provides minimal first-reader navigation

**Issue.** The home page says: "Begin with the Read Me First, then the Introduction, then the volumes in order." That's a fine pointer but doesn't tell a reader what they'll encounter or how to navigate the corpus's substantial breadth.

**Fix recommended for Phase 5+.** Consider a small expansion of the home page:
- A 1–2 sentence summary of what the IJH project is for
- A "Reading Paths" section with 2–3 candidate paths (e.g., "If you want the principles first → start with Vol 1 Read Me First; if you want the analytical instrument → start with the Vol 5 Periodic Table; if you're a Council member → start with Vol 6")

**Status: deferred to Phase 5+.**

### Finding I — Cross-volume references could be more explicit

**Issue.** Some volumes assume cross-volume knowledge without explicit pointers. For example:
- Vol 5 PT chapter assumes Vol 1's FL articulation. There's no "see [section] for the underlying chapter" pointer near each reference list entry.
- Vol 4 testing framework references LotS-* claim codes that are documented in the Vol 6 registry. The reference is to the registry but a reader doesn't know the registry's URL.
- The Functional Specialization Across Volumes sub-section in Vol 5 names what each volume does — that's good — but doesn't have inline links to start-points in each volume.

**Fix recommended for Phase 5+.** Light cross-reference pass: add inline links in the matured-catalog sub-sections that point at specific volume sections.

**Status: deferred to Phase 5+.**

### Finding J — The per-entry attribute lines work, but the format may want refinement

**Issue.** The italic `*Attributes: Layer X · Scale-range Y · Operator Z*` line was added during Phase 4 to every PT entry. It works but is dense — six conceptual values (Layer, Scale-range, Operator) packed into one line. A reader who hasn't read the matured-catalog HOW TO READ section may not know what these mean when encountering them in the reference list.

**Fix recommended for Phase 5+.**
- (a) Consider linking the attribute words to their HOW TO READ definitions on first occurrence per entry (markdown links to anchors within the chapter).
- (b) Or add a brief footnote at the start of the reference list pointing readers to the HOW TO READ block.

**Status: deferred to Phase 5+.**

---

## Findings inventory

| Finding | Status |
|---|---|
| A — HOW TO READ block overwhelming | **Closed (fixed this pass)** |
| B — No first-time-reader scaffolding at chapter entry | **Closed (fixed this pass)** |
| C — Slim Format cells bloated, P0/GI especially | Deferred to Phase 5+ |
| D — Matured-catalog terminology without glossary | Deferred to Phase 5+ |
| E — Per-FL chapter consistency varies | Deferred to Phase 5+ |
| F — "What the Shape Reveals" sub-section count | Deferred to Phase 5+ |
| G — Dev vs prod differentiation minimal | Noted, no action |
| H — Home page first-reader navigation | Deferred to Phase 5+ |
| I — Cross-volume references could be more explicit | Deferred to Phase 5+ |
| J — Per-entry attribute line format | Deferred to Phase 5+ |

## Recommended Phase 5 readability work-stream

When ready to address the deferred findings, suggested sequencing:

1. **Glossary addition** (Finding D) — small change, high leverage; centralizes the matured-catalog vocabulary
2. **Home page expansion** (Finding H) — small change, high leverage for first-time readers
3. **Slim Format format review** (Finding C) — moderate change; affects table density across all six rows
4. **Sub-section navigation** (Finding F) — moderate change; navigational opening at "What the Shape Reveals"
5. **Cross-volume links** (Finding I) — distributed pass; touches many files but each touch is small
6. **Per-FL chapter consistency** (Finding E) — large pass; consider whether to do or accept the variation
7. **Per-entry attribute line format** (Finding J) — distributed; might be folded into the chapter-consistency pass

A focused Phase 5 readability pass covering items 1–5 could land in 1–2 work sessions; items 6–7 are larger commitments deserving their own decision.

## What this audit closed and what remains

**Closed in this pass.** Two of the top three immediate-overwhelm issues for a first-time reader (Findings A and B). After this pass, a first-time reader landing on the Vol 5 PT chapter sees a tip callout naming the reading tiers and finds the HOW TO READ block organized into Essential and Matured-catalog tiers. The most-required information is reachable in 15–20 minutes; the deeper material is available without forcing itself on the reader.

**Remains.** The Slim Format cell density, the missing glossary, the home-page navigation, and the per-FL chapter consistency are real readability issues but each is a deliberate work-stream of its own. They are inventoried here as the Phase 5+ readability backlog.

The catalog is now in a state where the analytical depth is preserved, the matured-catalog framework is fully applied across surfaces, and the front-line first-reader experience has been substantially improved. The deferred items can be addressed when the right time comes — they are real but none is blocking.
