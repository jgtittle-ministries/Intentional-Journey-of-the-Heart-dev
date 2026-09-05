# Governance for a Quiet Season

*A draft for the Council — 6 September 2026*

**Status: draft for discussion. Nothing in it is in force until the Council has heard it and John has signed it.**

---

## Why this draft exists

Part 1 of Volume 6 was written for a project with many hands: outside contributors, contested claims, a Council that votes, a technical maintainer, a pipeline that checks every proposal. It was drafted in April 2026 and revised in June. It was never signed and never ratified; its signature line is still blank. The project it describes has not arrived.

What has arrived is this. Since the repository was created in April, every change has been made by John, with JD as technical maintainer and an AI assistant doing the mechanical work. No outside proposal has been received. No issue has been opened by anyone outside the project. Repository traffic is a trickle. The claim registry has never been reviewed by the Council; every `last_council_review` field is still null. The schema and contributor guide drafted for the June meeting never moved to the repository root, and the contributor guide that is there still calls itself a placeholder.

None of that is failure. It is the actual shape of the work in this season: one man thinking carefully, writing, and correcting, with a small fellowship around him. The governance should describe that honestly rather than describe a legislature that has never convened. A rule that is written but not followed teaches everyone who reads it that the project does not do what it says.

This draft therefore proposes a light rule for the quiet season, keeps what still carries weight, shelves what does not, and names the trigger that would bring the heavier rule back.

---

## 1. Who decides

During John's active tenure, John is the steward and editor of the work. He decides what changes. Part 1 already said this in the language of a founder's veto; it is simply true in practice, and this rule says it plainly.

The Council is John's counsel and covering, not a legislature. Its first job, in Part 2's words, is its own formation; its second is stewardship of the work. In this season the stewardship takes one concrete form: once a month, at its regular meeting, the Council hears what John has changed and what he intends to change, and it blesses, questions, or asks him to wait.

For the Council's word to mean anything, *wait* has to be real. When the Council asks John to wait, he waits, and the reason is written down. This is the Rule of Life's own line: we do not use votes to end disagreements that have not yet been prayed through. The same applies to blessings; a change the Council has not prayed through is not yet blessed.

---

## 2. Three kinds of change, three kinds of ask

Part 1's three confidence tiers are kept, because the distinction they draw is real. What changes is what each tier requires. Voting thresholds and comment periods are replaced by three verbs.

**Tell.** Working claims (Part 1's Tier 2), prose refinement, cross-references, new research trails, corrections of fact or citation, readability, site mechanics. John makes the change, mirrors it to the published site when it is ready, and reports it at the next meeting. Most of a year's work lives here.

**Ask.** Anything that changes what the work claims at its foundations: the four axioms and the other anchor claims (Tier 1); adding, removing, or re-tiering a Foundational Law; revising a preserved minority position or closing an open question; anything touching safeguarding; and any change to this rule itself. John brings these to the Council before they are published. The development repository may carry the draft; the published site waits for the Council's blessing. If the Council is divided, the change waits and the division is recorded.

**Wait.** Frontier claims (Tier 3: the force equation, the conservation laws, and the rest held below 65%). These do not move on argument; they move on evidence. When evidence exists, the change becomes an Ask. Part 1's research-program track was the right instinct here, and the Research Register is where that work is already tracked.

When a change is hard to classify, it is an Ask.

---

## 3. Traceability: the repository is the record

The project has had a complete audit trail from its first day. Every change is a commit with a written reason. The development repository holds work in progress; the published repository holds what has been released; nothing reaches the published site except by a deliberate mirror on John's word. That is the change-control system. It does not need a second one layered on top of it.

Two things are added, both small.

**The Council Log.** One file in Volume 6, one entry per meeting, a paragraph or two: the date, who was present, what was told, what was asked and how it was answered, what was held, and any dissent by name. Newest entry first. It is public. This is the *outcomes public* layer of Part 2's Benedictine principle, and it is the only new record this rule creates.

**The monthly changes note.** Before each meeting, John (or the assistant, from the commit history) prepares a short note in three lists: told, asking, waiting. It is the agenda for the governance portion of the meeting, and once the meeting has happened it becomes the Council Log entry.

---

## 4. What is kept from Part 1, and why

- **The four-factor test and disconfirmability.** These remain the standard any substantive change must meet. They are John's own thinking discipline of twenty years. The Council may ask of any Ask: which scriptures, whose experience, does it cohere, what does tradition say, and what would show it wrong. They stop being template sections to police and become questions the Council asks aloud.
- **Preserved dissent.** When a claim is revised, the prior position is kept with its argument, not deleted. When the Council declines a change someone cared about, the argument is kept in the Log. This is a content discipline, it costs nothing in a quiet season, and it is what makes this a living tradition rather than a series of overwrites.
- **The Scripture-Grounding Standard.** Unchanged.
- **The Research Register.** Unchanged, and in active use.
- **The claim registry, re-described.** The four registry files remain as the index of claims, tiers, and dependencies, and the tier audit keeps the chapters, the Master Law Index, the Periodic Table, and the registry in agreement. The registry is no longer described as the object the Council ratifies claim by claim, and the `last_council_review` field is retired. It is a map the Council may consult, kept in step with the prose, which remains canonical.
- **The license.** CC BY 4.0 for the corpus and the Developer Certificate of Origin for contributions. Unchanged.
- **Part 2 entire.** The Council as a Fellowship of the Heart, the meeting rhythm, the handling of disagreement, the Rule of Life. Nothing in this draft alters Part 2. This draft is an attempt to obey it.
- **The Succession Letter, which is the one thing that stays heavy.** A work carried by one person is most exposed exactly where Part 1 was most careful, and here the project is at its own rule: the letter names David R. Smith as Theological Successor and John David Tittle as Literary Executor, and John signs it at this meeting, dated 6 September 2026, with Council members as witnesses. Alternates stay blank until he names them. JD, who already serves as the project's technical maintainer, holds that work within the Literary Executor's administrative custody, so no separate co-maintainer role needs inventing.

---

## 5. What is shelved, and the trigger for bringing it back

Shelved: the five-seat Council with denominational caps and staggered terms; Recognized Contributor status and Council elections; the seven-day, fourteen-day, and thirty-day periods; quorum and the two-thirds supermajority; the no-confidence mechanism; automated downstream-impact reports and CI validation of the registry; the annual calibration cycle and calibration report; Zenodo, Hypothesis, the fiscal sponsor, and incorporation; the pull-request review workflow on GitHub.

None of it is deleted. Part 1 stays in Volume 6 under a short new preface, as the governance model held in reserve for a larger season.

**The trigger.** If in any twelve months the project receives three or more substantive outside proposals, or a second regular editor joins the work, or the Council itself asks, the Council revisits this rule and may restore any part of Part 1. Until then the light rule stands.

---

## 6. Outside contributions in the meantime

Anyone may open an issue on the repository or write to John. A serious proposal is welcome and will be brought to the Council as an Ask at the next meeting, with the proposer told when that is. The Proposal Template remains available as a courtesy for anyone who wants to be thorough; it is not a gate. The one-page CONTRIBUTING file is rewritten to say exactly this.

---

## 7. The question this rule does not answer

Part 2 says the Council is under a spiritual authority that has yet to be identified and must be clarified before initiation. No procedure in this draft answers that, and no procedure could. It remains the one governance question that matters more than anything above, and it belongs on the Council's agenda ahead of this draft.

---

## 8. What adopting this would change in the repository

For the Council's information. None of it happens until John says so.

1. The root `GOVERNANCE.md` becomes this rule. It currently says the project is in pre-Council operation and points readers to a superseded Word document.
2. The root `CONTRIBUTING.md` placeholder becomes a one-page version of §6.
3. Part 1 receives a short preface naming it as the model held in reserve, and the Volume 6 index describes it that way.
4. A Council Log file is created in Volume 6, with this meeting as its first entry.
5. The `last_council_review` fields are removed from the registry files.
6. The GitHub pull-request review workflow is disabled.
7. Part 3, now dated 6 September 2026, is mirrored to the published site once signed and witnessed; alternates are added if John names them.

---

*Prepared for the Council meeting of 6 September 2026. Draft, not in force.*
