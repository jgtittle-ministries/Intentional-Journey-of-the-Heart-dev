# Process Retrospective — The Mustard Seed Resolution as a Dry Run of the Vol 6 Governance Machinery

*A meta-document. Where the Phase 1–6 files in this folder are the **content** of the Mustard Seed resolution, this file records what the **process** taught us. The Mustard Seed question was the first open question to travel the entire Vol 6 resolution machinery end-to-end, so its run doubled as a live test of the governance model itself — on a genuinely uncertain question rather than a toy one. Written for the next steward picking up the next open question (V3.Exp3.Open2, the differential gift of faith, is the natural successor).*

*Completed 2026-06-02, at the signing/close-out of the Phase 6 proposal. The resolution itself is still in its public comment period (closes 2026-06-15); this retrospective is about the machinery, not the verdict.*

---

## 1. What the run actually exercised — the full path

The reusable end-to-end sequence, in the order it ran. This **is** the resolution playbook; everything below is commentary on it.

1. **Open-question identification** — the question already named in the registry (V1.Exp8's cap; V3.Exp3.Open1 / `V3.Eq.Mustard` as the downstream gate).
2. **Phase 1 — coded corpus.** Systematic coding of ~59 miracle / answered-prayer entries across OT, Gospels, Acts, Epistles. The evidentiary spine.
3. **Phase 2b — adversarial pass.** First attempt to break the emerging reading.
4. **Phase 2c — independent adversarial pass.** A reviewer *blind to the analysis and mandated to overturn it*.
5. **Phase 3–4 — adjudication.** Discriminator tables; weighing the lines of evidence against each other.
6. **Phase 5 — cross-tradition survey.** Does the reading hold across all four streams the project draws on?
7. **Phase 6 — Proposal-Template draft.** The seven-section template filled for the first time, with proposer-only items left as `[John: …]` placeholders rather than fabricated.
8. **Claim-registry enactment** — `vol1`/`vol3` YAML edited with **"effective on close"** semantics (pre-staged, not yet live).
9. **Research Register state move** — Recommended → Underway → an **"Awaiting comments"** callout.
10. **14-day public comment period** + a **scheduled routine** to close it automatically.
11. **Worked-resolution reader chapter** (`docs/volume-6-governance/mustard-seed-worked-resolution.md`) — the reasoning made reader-visible, framed as the template for the next resolution.
12. **Signature + close-out** — proposer signs; "pending signature" language flips to "signed and submitted" across the proposal and the register.

## 2. What held up under load

- **The Frontier / Working tier split — the load-bearing rule.** A persuasive, well-evidenced proposal arrived, and the process still *refused* to re-rate the Frontier-tier V3.Exp3 on argument alone — routing it into the research-program track (Council sponsor + six-month window) while letting the Working-tier V1.Exp8 open-question resolution proceed on the strength of the analysis. The tier distinction is the rule most likely to be bulldozed by a compelling case, and it did not bend. This is the single strongest result of the dry run: the governance model's "Frontier claims move only when evidence accumulates, not when a well-argued proposal arrives" survived first contact with exactly the kind of proposal that would test it.
- **The adversarial pass was not ceremony.** Phase 2c genuinely changed the output — four amendments were folded back in (the omitted faith-magnitude vocabulary engaged head-on in §2/§3a; the κατά datum weighted honestly in §5; the gift-of-faith claim reworded as concession-plus-limit in §4; the persistence/faith partition softened in §1). A disconfirmability step that never changes anything is theater; this one earned its keep, and it is the part of the process most worth protecting against being skipped "because we're confident."
- **Resolve one thing, honestly surface the next.** Rather than folding the gift-of-faith tension away to make the resolution look tidy, it was split out as a new preserved open question (V3.Exp3.Open2). The "nothing is ever deleted" discipline did real work — the process produced *one resolution and one new honest question*, not a clean win.
- **"Effective on close" staging worked.** The registry could represent an *in-flight* resolution — confidence pre-staged at 80 but gated by prose until the comment period closes, the open_question kept formally `open` until then — without prematurely committing the number. The schema turned out to be expressive enough to hold a resolution mid-flight.

## 3. Seams the run exposed — fix or watch before the next one

- **Out-of-repo automation dependency.** The comment-period close leans on a scheduled remote routine (`trig_01TtC1ahUvy8GrzEeUqLSqdj`, fires 2026-06-15) *plus* a manual `search-index.js` regen whose generator lives outside the repo. The close is therefore **not self-contained in the repository.** A future steward reading only the repo could miss the close step entirely. *Mitigation for next time:* record the close mechanism inside the register/proposal, not only in a session handoff, and prefer a close procedure a steward can run from the repo alone.
- **A pre-staged confidence field can read as already-live.** `confidence: 80` is correct, but anyone scanning the YAML field without reading the adjacent `confidence_rationale` prose could take it as the current rating rather than the on-close target. *Mitigation:* consider a lightweight convention for in-flight values (e.g. an explicit `pending_until:` field or a `[effective 2026-06-15]` tag in the value) so the gate is legible at the field level, not only in prose.
- **AI versus human adversarial pass.** Phase 2c's "mandated to overturn" reviewer was an AI pass; the *human* independent reader was made **optional** and explicitly declared non-blocking. That was a reasonable call for this question, but it should be a *conscious* call each time, not a default — the higher the stakes (and the closer a claim sits to Frontier or to pastoral practice), the stronger the case for a human in that seat. *Recommendation:* tie the human-pass requirement to tier, not to convenience.
- **Template placeholders for proposer-only content** (signature, contact, personal witness) were needed and improvised as `[John: …]` markers. Minor, and now an established pattern, but worth baking into the Proposal Template itself so the next proposer sees the slots rather than inventing them.

## 4. Checklist for the next resolution

Distilled from the above — the short version a steward can follow.

- [ ] Name the open question from the registry; identify every downstream claim it gates **and each one's tier** (the tier decides what kind of move is even possible).
- [ ] Build the coded corpus first; let the evidence, not the hoped-for conclusion, set the reading.
- [ ] Run the adversarial pass with a genuine mandate to overturn — and **fold its amendments back in.** If it changed nothing, it was not adversarial enough.
- [ ] Decide the human-independent-reader requirement up front, keyed to the highest tier touched.
- [ ] Fill the Proposal Template; leave proposer-only items as visible placeholders rather than fabricating them.
- [ ] Enact the registry with explicit in-flight semantics; make the "effective on close" gate legible at the field level, not only in prose.
- [ ] Move the Research Register state and open the comment period; **record the close mechanism inside the repo.**
- [ ] Write the worked-resolution chapter so the reasoning is public, not just the verdict.
- [ ] At close: flip the registry, confirm the confidence move, update the register/proposal language, regen `search-index.js` for both repos, mirror dev→prod.

## 5. The deeper point

A governance model whose central discipline is that claims must be **disconfirmable** (V4.M3) owes the same standard to its own machinery. This run was that test: the process for resolving open questions was itself put through a live, non-trivial case and watched for where it would bend. It mostly held — and where it strained (out-of-repo automation, field-level legibility of in-flight values, the human-pass default), the strain is now documented rather than discovered the hard way next time. The resolution's own §5 asks "what would count as evidence against this?"; this retrospective asks the same question of the process that produced it, and keeps the answer where the next steward will find it.
