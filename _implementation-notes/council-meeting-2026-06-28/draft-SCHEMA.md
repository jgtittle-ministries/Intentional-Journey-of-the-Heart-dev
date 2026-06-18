> **DRAFT for Council ratification — 2026-06-28.** This is the first-substantive-vote
> artifact named in Volume 6 Part 1 §13.1. On ratification it moves to the **repository
> root** as `SCHEMA.md`. Until ratified it is a working draft, not the authoritative schema.
> Drafted "from the implicit specification in the registry files" (Part 1 §13.1) — i.e., the
> header conventions in `vol1-claims.yml`–`vol4-claims.yml` plus Volume 6 Part 1 §2–§3.

# SCHEMA.md — The IJH Claim-Registry Schema

This document defines the schema for the *Intentional Journey of the Heart* claim registry — the four YAML files (`vol1-claims.yml` through `vol4-claims.yml`) that are the project's authoritative, machine-readable record of what it claims and at what confidence. It is the reference both a human contributor and the CI validator check an entry against.

**Governance status.** Per Part 1 §3, the schema definition *itself* is governed under the same **two-thirds supermajority** rule as the constitution. Changing this document — adding a field, adding a claim `type`, changing an enumeration — is a governance-amendment-level act, not an editorial one. **CI validation should reject any claim entry that does not conform to the current schema**, so that schema drift cannot accumulate silently as contributors add entries in idiosyncratic formats.

**`schema_version` at time of this draft:** `0.3`.

---

## 1. File layout

| File | Volume | Notes |
|---|---|---|
| `vol1-claims.yml` | Vol 1 — Foundation | Axioms, Explorations, the Foundational Laws, the Periodic-Table structural metadata |
| `vol2-claims.yml` | Vol 2 — Therapeutic | Operationalization of Vol 1 |
| `vol3-claims.yml` | Vol 3 — Quantitative | The force/field material; lowest-confidence tier lives here |
| `vol4-claims.yml` | Vol 4 — Testing | Methodology, hypotheses, protocols, open trails, and an `instruments` section |

Volume 5 is a bibliography and reference volume; it carries **no** claim registry. Volume 6 (governance) is prose, not a registry. The four `.yml` files live at the **repository root**.

## 2. File-level keys

Each registry file opens with:

| Key | Required | Meaning |
|---|---|---|
| `project` | yes | Always `IJH`. |
| `volume` | yes | Integer `1`–`4`. |
| `schema_version` | yes | The schema revision this file conforms to (e.g., `0.3`). |
| `founder` | yes | `John G. Tittle`. |
| `last_council_review` | yes | Date of the last Council confirmation, or `null` while founder-stewarded. **The registry walk-through (Part 1 §13.2) is the act of moving this from `null` to a date.** |
| `source_document(s)` | yes | The originating `.docx` / chapters, for **provenance only** (see `CONTRIBUTING.md` — the Markdown under `docs/` is canonical, not the source `.docx`). |
| `volume_notes` | optional | Free-text scope notes (Vol 4 uses this). |
| `claims` | yes | The list of claim entries (§3–§6). |
| `instruments` | Vol 4 only | Measurement tools held as reference material **outside** the claim list — instruments are not propositions the Council votes on (Part 1 §3). |

A leading comment block documenting the file's conventions and a **schema change log** is expected at the top of each file (see §9).

## 3. Claim entry — universal fields

Every entry in `claims` carries these unless noted:

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique ID. Pattern: `V{volume}.{type}{number}` for axioms / explorations / supplementals / minorities (e.g., `V1.Ax1`, `V1.Exp8`, `V1.Sup1`, `V1.Exp3.Mn1`); `FL.{Roman numeral}` for Foundational Laws (e.g., `FL.XLI`). |
| `type` | yes | The claim's kind — controlled but extensible vocabulary (§7). |
| `title` | yes | Short human-readable name. |
| `core_text` | yes | The canonical statement of the claim (YAML block scalar). This is the text the Council votes on. |
| `status` | yes | `core` \| `minority` \| `open` (§7). |
| `confidence` | yes\* | Integer 0–100 (§7), or `null` for claims whose confidence **inherits** from an upstream claim (Vol 4 uses `confidence_inherited_from`). |
| `confidence_rationale` | recommended | Why the claim sits at its confidence. |
| `scripture_refs` | yes (claims of the world) | List of scripture citations (`Book Chapter:Verse`). |
| `external_sources` | optional | Non-scripture sources (authors, works). |
| `traditions_supporting` | recommended | Subset of `{Reformed, Evangelical, Charismatic, Mystical, ...}`. |
| `traditions_dissenting` | optional | Same vocabulary; empty list if none. |
| `upstream_dependencies` | yes | List of claim IDs this claim depends on. Validated as a **DAG** (no cycles). |
| `downstream_dependents` | yes | List of claim IDs that depend on this one (may use `V{n}.All`). |
| `open_questions` | optional | Unresolved sub-questions preserved as first-class content (§7). |
| `flip_conditions` | recommended | What evidence or argument would move/overturn the claim — the disconfirmability discipline. |
| `notes` | optional | Working annotations. |

\* Either `confidence` or `confidence_inherited_from` must be present for a claim of the world; methodology/instrument entries may carry neither.

## 4. Foundational-Law structural metadata (Periodic-Table extension)

Vol 1 Foundational Laws (and a few structural claims) carry additional fields that place each law in the Vol 5 Periodic Table and name its mechanism. These are **not** required on non-FL entries.

| Field | Values |
|---|---|
| `pt_period` | `P0`–`P5` — Periodic-Table period (structural-articulation anchor). |
| `pt_group` | `GI`–`GVI` — Periodic-Table group (operational dimension; tracks the SST five-dimension axis). |
| `directionality` | `V` (Vertical, person↔God) \| `H` (Horizontal, person↔person) \| `B` (both) \| `I` (intra-personal). |
| `band` | `1` (multi-author scriptural footing) \| `2` (principle + scripturally-specified pathway) \| `3` (principle + tradition-arbitrated form) \| `null`. |
| `mirror_type` | `statement` \| `constitutive` \| `constitutive_bidirectional` \| `christological_condition` \| `orientation_neutral`. |
| `mirror_text` | The idol-ward / failure-mode face of the law, when named. |
| `operator` | `P` (participant) \| `S+P` (Spirit through participant) \| `C` (Christ; participant receives) \| `C+P` \| `T+P` \| `C+T`. |
| `layer` | `substrate` (continuous condition) \| `operation` (discrete cause-and-effect event). |
| `scale_range` | NT-breakpoint scope, from `{1, 2, 3, 12, 70, 120, ~500, city, diaspora, generation, eschatological}` — single value or `"N – N"` range. |
| `gateway` | `true` when the entry is a designated structural-threshold Gateway. |

A companion discipline applies corpus-wide (Part 1 §8): every claim using a physical analogy should be tagged **`illustrative`** or **`load_bearing_proposed`**. Converting an analogy from illustrative to load-bearing is a two-thirds-supermajority vote — it is effectively a claim that a piece of physics also holds for spiritual dynamics, and must not happen by drift.

## 5. Dissent and Council-action fields

| Field | Used on | Meaning |
|---|---|---|
| `parent_claim` | minority / dissent entries | The canonical claim this dissents from (e.g., `V1.Exp3.Mn1` → `parent_claim: V1.Exp3`). |
| `minority_positions` | canonical entries | List of the minority IDs attached to this claim. |
| `council_reply` | minority / flagged entries | The Council's recorded response to a preserved dissent. |
| `council_flag` | any | Marks an entry for Council attention. |
| `author_note` | any | The founder's / author's note on the entry. |
| `formerly_canonical` | revised entries | Tag on a prior canonical version demoted to minority when a claim is revised — the argument is **preserved, never deleted** (Part 1 §7). Downstream claims citing the old version are auto-flagged for review. |
| `confidence_inherited_from` | Vol 4 | The upstream claim a testable hypothesis inherits its confidence from (the upward-calibration link, Part 1 §9). |

## 6. Vol 4 type extensions and `instruments`

Vol 4 is methodology, not claims-about-the-world, so the schema added five `type` values for it — `methodological_principle`, `testable_hypothesis`, `research_question`, `protocol`, `open_trail` — and a separate top-level **`instruments`** section for measurement tools (held outside `claims` because instruments are not propositions to vote on). This is the worked precedent for the extension rule in §7.

## 7. Controlled vocabularies

**`status`** — exactly one of: `core` (canonical), `minority` (a preserved competing position), `open` (an entry holding an unresolved question). Minorities and open questions are **first-class content, not footnotes**, and are tracked separately (Part 1 §7).

**`type`** — an **open but governed** vocabulary. A proposed new type requires explicit Council ratification at two-thirds supermajority, and the proponent must show **no existing type fits** — not merely that a new one is more convenient (Part 1 §3). Current families (the registry files are authoritative for the full list):
- *Claims of the world (Vol 1–3):* `axiom`, `opening_exploration`, `structural_law`, `operational_law`, `foundational_law`, `diagnostic_law`, `developmental_law`, `dynamic_law`, `kinematic_law`, `eschatological_law`, `gateway_law`, `modeling_law`, `tool_application_law`, `governing_premise`, `structural_and_operational_law`, `quantitative`, `qualitative`, `qualitative_visual`, `analytical_equation`, `conservation_hypothesis`, `mixed`.
- *Dissent & inquiry:* `minority_dissent`, `open_question`.
- *Methodology (Vol 4):* `methodological_principle`, `testable_hypothesis`, `research_question`, `protocol`, `open_trail`.

**`confidence`** — integer 0–100, mapping to the **qualitative certainty tier**:

| Certainty tier | Range | Default |
|---|---|---|
| Clearly Taught | 85–95 | 85 |
| Reasonably Inferred | 65–80 | 75 |
| Speculative | 30–55 | 40 |
| Axiom (working-axiom tier) | 90 | 90 |

This certainty axis aligns with the **governance tier** that sets review procedure (Part 1 §5): **Tier 1 Anchor** (≥ 85, revisions are governance-level, two-thirds), **Tier 2 Working** (65–80, consent-based refinement — the corpus's normal rhythm), **Tier 3 Frontier** (< 65, the research-program track — *moves only when evidence accumulates, not when a well-argued proposal arrives*). The tiers govern **pace, not importance**.

## 8. Validation rules (for CI)

A conforming registry satisfies:
1. Every `id` is unique across its file and well-formed for its type.
2. Every ID in `upstream_dependencies` / `downstream_dependents` / `minority_positions` / `parent_claim` resolves to a real entry, and the dependency graph is a **DAG** (no cycles).
3. `status`, `type`, and every enumerated field hold a value from its controlled vocabulary; an unknown `type` is rejected until ratified (§7).
4. Each claim of the world has either `confidence` (0–100) or `confidence_inherited_from`.
5. A revised canonical claim retains its prior version as a `formerly_canonical` minority; nothing is overwritten in place.
6. Foundational-Law certainty tier agrees across all four places it is stated — the chapter, the Master Law Index, the Periodic Table, and `vol1-claims.yml` (the `_tier_audit.py` check named in `CONTRIBUTING.md`).

## 9. `schema_version` and the change log

`schema_version` is bumped whenever the schema changes, and each file carries a `# Schema change log:` comment block recording what changed and why. Current history (from the registry headers):

- **`v0.3` (2026-05-26)** — added `layer`, `operator`, `scale_range`; extended `mirror_type` with `christological_condition` (the Alternative-E structural revision).
- **`v0.2` (2026-05-23)** — added `pt_period`, `pt_group`, `directionality`, `band`, `mirror_type`, `mirror_text`, `gateway` (the matured-catalog Periodic-Table metadata); added the 38 Foundational Laws.
- **`v0.1`** — initial demonstration encoding.

---

*Ratifying this document fixes `schema_version 0.3` as the Council-authoritative schema. Subsequent changes follow the two-thirds-supermajority amendment path (§3 / Part 1 §6).*
