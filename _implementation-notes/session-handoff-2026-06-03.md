# Session Handoff — 2026-06-03

## TL;DR
Two big things this session: (1) **completed the IJH source-folder mining sweep** (every enumerated OneDrive source folder now assessed), and (2) ran a **methodology-lineage pass** crediting John's transformation-engineering / consulting toolkit (AIM, Zenger/Frontline, SERVQUAL, Gallup Q12) across IJH and BSCP. Also did a substantial **FotH Going-Out repair** (a from-scratch Design-B handbook) and a full **FotH `.docx` source reconciliation**. Everything is shipped to prod; all repos in sync.

## Repo states (all in sync as of handoff)
| Repo | dev | prod |
|---|---|---|
| IJH | `3ce345d` | `87be479` |
| BSCP | `5c9236f` | `419d56e` |
| FotH | `56aa042` | `484d464` |
| IJH preview | — | stale by design (`4110ed1`) — do NOT mirror unasked |

Local clones all under `C:/Users/jgtit/claude/_work/`. Conventions: IJH/FotH/preview = **static warm reader** (markdown fetched at runtime; regen `node _work/_gen_search_index.js "<repo>"` after content edits; reader.html is a TARGETED edit dev→prod, only the topnav "Repo" link differs). BSCP = **Material for MkDocs + GitHub Actions** (push triggers build; no index step; `mkdocs.yml` is targeted-edit only). Commit trailer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

## What shipped this session (all on prod)
1. **IJH Outlines folder** → **Vol 6 Genesis correction**: the name "Intentional Journey of the Heart" was in active use as a named workshop (Jul 2008) + constituted initiative (Jul 2009), correcting the published "name first appears in Aug-2011 'Rest of the 94%'" claim. (catalog-history.md)
2. **Heart Work on Beliefs folder** → **Powlison** Vol 5 Part II entry (Seeing With New Eyes / X-Ray Questions; the frame/pattern/response grid behind V2.Exp0 + Part VI).
3. **Fellowship of the Heart** work:
   - Verified the FotH "Inviting Others vs Going Out" two-springs divergence → **rewrote `going-out/handbook.md` as a from-scratch Design-B (body-sent) handbook** matching the 12 sessions; **aligned `going-out/index.md`**; recorded the resolution in `going-out/CHANGELOG.md`. Design-A content remains correctly in `inviting-others-handbook.md`.
   - **B17 (PIES) §5.1(c)** co-gender clearing enrichment (from the Womens-events "Clearing Model for Women": log-removal-vs-connection why-framing + co-gender facilitation guidance).
4. **Calling Retreat folder** → **Barkalow** Vol 5 Part II formative-lineage entry (It's Your Call / The Noble Heart; calling lineage, Eldredge-adjacent).
5. **Band of Brothers and Sisters → Weapons Master v4** → **Founder's Genesis** provenance paragraph naming the "Weapons Master" as the precursor to the **Formation Companion** (+ the WM "basics"/1 Tim 3 fed to the FC's open character-prerequisites section via the Tittle Part II FC summary).
6. **AIM / IMA** (org-change methodology) → IJH Vol 5 **Part I "Conner, Daryl R."** entry (cite-not-reproduce; Conner tradition vs IMA's AIM kept distinct) **+ BSCP** "borrowed-from" list.
7. **Zenger / Frontline Leadership / AchieveGlobal** (leadership development) → IJH Vol 5 **Part I "Zenger & Folkman"** entry (thin footprint, hedged; tied to Leader Level taxonomy / Companion development).
8. **SERVQUAL** (customer-satisfaction measurement) → **BSCP** (borrowed-from list + Ch 2 Surveys note). Off-domain for IJH.
9. **Gallup Q12** (employee engagement) → **BSCP** (borrowed-from list + Ch 2 Surveys note). Off-domain for IJH.

## Sweep status — COMPLETE
All enumerated IJH source folders assessed (see [[project_ijh_source_folder_mining]] memory for the full per-folder table). The pattern held: most folders were already-captured provenance, third-party (cite-only), or personal; ~1 genuine pickup each. **No queued folders remain.** Notable no-pickup confirmations: Churches and Ministries (the ASC/2007 Tittle-Smith "Relational Discipleship" Field Manual is the operational taproot — already captured across Vols 2/5/6); Archive and Reference (12.7 GB of `.au` teaching-tape audio + already-captured/third-party docs).

## FotH source-of-truth + reconciliation (important for future FotH work)
- The canonical FotH `.docx` source folder (`Documents/Fellowship of the Heart/Current Doc for FotH`) is **GONE** (Documents reorg). The **sole surviving Word sources** are now `Documents/Intentional Journey of the Heart/Fellowship of the Heart/` (a `_SOURCE_OF_TRUTH.md` marker sits at its root). **Do NOT delete that folder.**
- `_work/foth_deploy.py` `SRC_ROOT` was repointed there + JOBS remapped (`python foth_deploy.py --check` = 47/47 resolve). `regen_foth_sources.py` regenerated all drifted `.docx` from the live `.md` (md→pypandoc→docx, images/HR stripped, `format='markdown-smart' --wrap=none`; originals backed up to `_Archive/pre-reconcile-2026-06-03/`). The Design-B GO handbook + the new Interrogating Reality card got fresh `.docx`. **Sources now match the live site** (6 files differ only by cosmetic markdown serialization — list numbering / inline-code backticks — not prose).

## Open / parked items (John's call; none urgent)
- **John Trentham** Vol 5 entry — Powlison's protocol-partner ("Powlison & Trentham discernment protocols" in the TA paper), still uncatalogued. Would need citation built/verified (no source doc in the folders).
- **TrueFaced** (Thrall/McNicol/Lynch) Part II entry — parked from the Convene mining; recommended but never committed.
- **"Measuring Spiritual Maturity v1–3"** drafts (FotH research subfolder) — un-drilled; likely drafts of the published MSM Hearing-God Paper.
- **Gartner balanced-scorecard research** (2000–01, in the BSCP folder) — a legit early-BSC influence; available as a next BSCP acknowledgment (John surfaced "Gartner" re Q12 but it's a separate thread).
- FotH CHANGELOG still references the (now-resolved) Design conflict as history — already updated to mark RESOLVED; fine.

## Key recipes / gotchas (reuse)
- **Formative-lineage entry pattern** (used for Barkalow, Conner/AIM, Zenger): model on the **Blackaby** entry — "not cited by name in IJH, but… I acknowledge this connection… both builds on and goes further." Name real convergences; re-ground secular mechanism in the Spirit's work per the V2.Exp0 Tool Import Discipline. **IP-sensitive sources (AIM, Q12, Avatar) = cite-not-reproduce.**
- **Methodology lineage destinations:** measurement/org-change/leadership methods from John's consulting career → **BSCP** (the transformation-engineering home) and/or **IJH** where there's a genuine community/formation connection (org-change → community replication; leadership-dev → Leader Level taxonomy). Pure customer/employee measurement (SERVQUAL, Q12) = **BSCP only** (off-domain for IJH).
- **Extraction:** `.doc/.docx` via Word COM (PowerShell); `.pdf` via pypdf; `.au` = audio (not minable); `md→docx` via pypandoc (`markdown-smart`, `--wrap=none`). Cache at `_work/_convene_extract/IJH_Outlines/`.
- **IJH index char-cap quirk** (not a bug): the big Part I/II files exceed the 24,000-char index cap, so entries near the END (Powlison, Zenger) leave `search-index.js` unchanged (render fine, just not full-text searchable); entries near the top (Barkalow, Conner) do change it.
- **Bibliography placement:** Part I = scholarly/empirical/secular; Part II = formation/theological. Alphabetical-ish by surname.
- **Mirror discipline:** content `.md` = byte-copy dev→prod + verify SHA256 + regen index (IJH) / Actions build (BSCP), commit `"Mirror … from dev"`. BSCP generalizes away from CSC + named clients/individuals.
