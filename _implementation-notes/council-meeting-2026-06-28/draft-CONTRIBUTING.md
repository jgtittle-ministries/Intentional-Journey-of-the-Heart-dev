> **DRAFT for Council ratification — 2026-06-28.** One of the contributor documents named in
> Volume 6 Part 1 §13.3. On ratification this **replaces the placeholder `CONTRIBUTING.md`** at
> the repository root. Kept deliberately short by design (Part 1 §4): a one-page guide that gets
> read beats a ten-page policy that does not.

# Contributing to the Intentional Journey of the Heart

Welcome. This guide is the first thing a new contributor reads. It sets the **voice** of the project and the **mechanics** of contribution. The full procedures live in Volume 6 (Governance); this is the door, not the whole house.

## Voice of the project

This is a contemplative project, not a software-paced one. Contribution is welcomed in that spirit:

- **Correction without contempt.** Disagreement is surfaced as engagement *with* the work, not dismissal *of* it.
- **Preservation of dissent rather than erasure.** Minority positions and open questions are first-class content. When a canonical claim is revised, the prior version is **preserved as a minority position, not deleted**.
- **Pace matters.** Most Council work happens in prayer and discernment, upstream of any vote. Votes are rare and are not used to end a disagreement that has not yet been prayed through.

## What the project is, structurally

The content is organized as a structured **claim registry** — the four files `vol1-claims.yml` through `vol4-claims.yml` at the repository root. Every claim has an ID, a confidence rating, scripture references, upstream/downstream dependencies, and — where applicable — preserved minority positions and open questions. The schema is documented in **`SCHEMA.md`**.

**Source of truth.** The published Markdown under `docs/` is the **canonical** source for the volumes' prose. Each chapter's `source:` front-matter names the originating `.docx` for **provenance only** — those documents are historical and have since diverged as the volumes were edited in place. **Never regenerate a chapter from its `source:` document**; doing so would silently discard later edits (testimonies, doctrinal guards, cross-references). Edit the Markdown directly, and keep the dev and prod repositories in sync via the mirror workflow.

## How contribution works

1. **Identify the target claim by ID** (e.g., `V2.Exp6`). Copy **`PROPOSAL_TEMPLATE.md`** and fill **every** section.
2. **Submit.** Submission opens a **14-day open comment period** visible to all Recognized Contributors, and triggers an **automated downstream-impact report** — the list of every claim whose `upstream_dependencies` includes your target. You are responsible for engaging each one; the tooling makes sure none are missed. *No contributor can revise a claim without confronting its downstream consequences.*
3. **Council decision (after day 14)** — one of four: **accept and merge**; **accept as a preserved minority**; **reject, with written reasons preserved**; or **escalate** to the dissent-resolution protocol.

Every proposal must clear three disciplines, all enforced by the template:

- **The four-factor derivation** — (a) independent scriptural lines, (b) experiential corroboration, (c) conceptual coherence with adjacent claims, (d) consistency with the Christian traditions. **A proposal that leaves any factor blank is returned for strengthening, not reviewed.**
- **Downstream-impact acknowledgment** — for each affected claim, say whether you strengthen, weaken, invalidate, or leave it untouched.
- **Disconfirmability** — name concretely what would count as evidence *against* your proposal. A proposal whose author cannot say what would disconfirm it is not accepted as canonical (it may be preserved as an open question).

## What different claims require (confidence tiers)

The review procedure depends on the claim's tier (Volume 6 Part 1 §5–§6):

- **Tier 1 — Anchor (confidence ≥ 85%).** The structural backbone (the axioms, Fear of the Lord, Sin Blockage, Heart Soil, and so on). Revisions are **governance-level**: Council consent, two-thirds supermajority, optional 30-day extended comment.
- **Tier 2 — Working (65–80%).** The majority of the corpus, and where normal contribution happens. **Consent-based approval**: passes when no Council member objects within 14 days and a quorum of four is engaged.
- **Tier 3 — Frontier (< 65%).** The force/conservation material and preserved open questions. **Not eligible for routine approval** — they require the **research-program track**: a Council sponsor and a minimum six-month active-testing window. Frontier claims move when *evidence* accumulates, not when a well-argued proposal arrives.

Trivial work (typo and citation fixes) runs on **lazy consensus** — seven days of silence equals approval.

## Becoming a Recognized Contributor

Anyone may submit a proposal. A contributor who has had **at least three substantive contributions accepted, across at least two volumes, over eighteen months** becomes a **Recognized Contributor** — named in the project masthead, and (once the founder's veto sunsets) a voter in Council elections. Every body is answerable to another: Council members to Recognized Contributors via a no-confidence mechanism; the founder to the Council via the sunset clause.

## Consistency checks (run after edits)

A doctrinal fix often lands in a chapter but not in its summaries or the registry. Three quick checks in `_implementation-notes/` catch that drift — run the relevant one after content changes:

- **`_link_audit.py`** — orphan files, manifest-vs-disk, broken `.md`/PDF/image links.
- **`_anchor_audit.py`** — every `#fragment` link resolves to a real heading.
- **`_tier_audit.py`** — each Foundational Law's certainty tier agrees across the **chapter**, the **Master Law Index**, the **Periodic Table**, and `vol1-claims.yml`. Run after any tier or doctrinal change.

Always re-run the search-index generator after editing `docs/`.

## License and contributor agreement

This work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). By submitting a contribution you agree it is licensed under the same terms. Contributions are accepted under the [Developer Certificate of Origin](https://developercertificate.org/) — a lightweight `Signed-off-by:` sign-off affirming you have the right to submit the material.

## Contact

For now, contact is through GitHub issues and discussion on this repository. The formal Council and contributor process opens on the timeline in Volume 6 §13.

---

*For the complete procedures, see Volume 6 (Governance) Parts 1–3, `SCHEMA.md`, and `PROPOSAL_TEMPLATE.md`.*
