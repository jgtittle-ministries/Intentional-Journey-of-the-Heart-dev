> [!CAUTION]
> # YOU ARE LOOKING AT THE DEV ENVIRONMENT
>
> This is the **`-dev` repository** — a development preview of *Intentional Journey of the Heart*.
> Changes here are **not yet final**, may be incomplete, and may change without notice.
>
> **Production (live) repository:** [Intentional-Journey-of-the-Heart](https://github.com/jgtittle-ministries/Intentional-Journey-of-the-Heart)
> **Production (live) site:** [intentionaljourneyoftheheart.org](https://intentionaljourneyoftheheart.org/)

---

# Intentional Journey of the Heart — DEV PREVIEW

*Notes to My Kids (and Grandkids): On My Personal Exploration of the Laws of God's Love*

**By John G. Tittle**

📖 **Read the DEV preview site:** **[jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/)**

[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

---

## About

A multi-volume theological exploration of the laws and relationships that govern
spiritual life — what the world of the Spirit looks like when you map it the way
the natural sciences map the physical world.

This repository is the **development preview** of the project. The canonical
working home — including final published content — is the [production
repository](https://github.com/jgtittle-ministries/Intentional-Journey-of-the-Heart).
The preview site is served by GitHub Pages straight from this repository: a
static reader at the repository root renders the Markdown under `docs/` in the
browser. Nothing reaches the production repository except by a deliberate
mirror on the author's word. The only visible differences from production are
the `Repo` link in the site header and the notice at the top of this file.

## Repository Layout

- `docs/` — the Markdown of the volumes; the canonical text
- `source-documents/` — the original Word documents, kept for provenance
  only; they have diverged from `docs/` and are not edited
- `index.html`, the volume pages (`Volume 1.html` through
  `Volume 6 Governance.html`), and `reader.html` — the reading site, static
  HTML served by GitHub Pages
- `reader.js`, `app.js`, `manifest.js`, `search-index.js` — the reader's
  machinery: the Markdown renderer, the page logic, the chapter list, and the
  generated search index (regenerate it after editing `docs/`)
- `vol1-claims.yml` through `vol4-claims.yml` — the claim registry, an index
  of claims, tiers, and dependencies kept in step with the prose
- `GOVERNANCE.md` — the governance rule in force, *Governance for a Quiet
  Season*, adopted by the Council of Stewards on 6 September 2026
- `CONTRIBUTING.md` — how to contribute, on one page
- `_implementation-notes/` — working notes, drafts, audits, and Council
  packets; never published to the site

## Governance

This project is governed by a light rule for a quiet season, set out in
[`GOVERNANCE.md`](GOVERNANCE.md) and adopted by the Council of Stewards on
6 September 2026. **Volume 6: Governance** of the work holds the Council
paper, the Succession Letter, the Council Log, and, held in reserve, the
fuller governance model of Part 1. See [`CONTRIBUTING.md`](CONTRIBUTING.md)
to contribute.

## License

This work is licensed under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
You are free to share and adapt this material for any purpose, including
commercially, provided appropriate credit is given.

Contributions are accepted under the
[Developer Certificate of Origin](https://developercertificate.org/).
