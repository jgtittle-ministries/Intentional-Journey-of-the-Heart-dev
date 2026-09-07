# Contributing

This project is governed by a light rule for a quiet season, [*Governance for a Quiet Season*](GOVERNANCE.md), adopted by the Council of Stewards on 6 September 2026. This page says what that means if you want to contribute. It is deliberately one page.

## How to contribute

Anyone may open an issue on this repository or write to John. A serious proposal is welcome and will be brought to the Council of Stewards as an Ask at its next monthly meeting; you will be told when that is. The [Council Log](docs/volume-6-governance/council-log.md) records, publicly, what was asked and how it was answered, and when the Council declines a change someone cared about, the argument is kept in the Log rather than discarded.

The [Proposal Template](docs/volume-6-governance/proposal-template.md) remains available as a courtesy for anyone who wants to be thorough. It is not a gate. What any substantive change must be able to answer, in the Council's hearing, are the questions the work has always asked of itself: which scriptures, whose experience, does it cohere, what does tradition say, and what would show it wrong.

Three kinds of change are handled three ways. Refinements of prose, cross-references, corrections, and new research trails are made and reported (*tell*). Anything touching the work's foundations, a Foundational Law, a preserved minority position, safeguarding, or the rule itself is brought to the Council before it is published (*ask*). Frontier claims move only on evidence (*wait*). When in doubt, it is an ask.

## What is canonical

The Markdown under `docs/` is the canonical text of the volumes. The `.docx` files under `source-documents/` are provenance only; they have diverged from the published text and are not edited. The four registry files, `vol1-claims.yml` through `vol4-claims.yml`, are an index of claims, tiers, and dependencies, kept in step with the prose; the prose, not the registry, is the record. Nothing reaches the published site except by a deliberate mirror from the working repository on John's word.

## For maintainers

After content changes, run the checks under `_implementation-notes/`: `_link_audit.py` (orphans, manifest-vs-disk, broken links), `_anchor_audit.py` (every `#fragment` resolves to a heading), and `_tier_audit.py` (each Foundational Law's tier agrees across its chapter, the Master Law Index, the Periodic Table, and the registry). Regenerate the search index after editing `docs/`. The reader's machinery at the repository root mirrors to the published repository by targeted edit, never by whole-file copy.

## License

The work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). By contributing you agree your contribution is licensed under the same terms, and you accept the [Developer Certificate of Origin](https://developercertificate.org/): a `Signed-off-by:` line on your commits says you have the right to submit the contribution under that license.

## Contact

GitHub issues on this repository, or John directly. The Council meets on the first Sunday of each month.
