# IJH session handoff — 2026-05-31

*Self-contained handoff. A fresh session can pick up from here without back-context.*

---

## 0. TL;DR — current state

| Repo | HEAD | Status |
|------|------|--------|
| **dev** | `0534cb8` | clean, in sync with `origin/main`. All session work pushed. |
| **prod** | `d4ca5da` | clean, in sync. All session work mirrored. |
| **preview** | `4110ed1` | **intentionally stale** (per user, until next major revision). Do NOT mirror C/D image cleanup or ATB Phase 2 to preview unasked. |

**Dev/prod docs parity:** the only intended divergence is `docs/index.md` (DEV-preview admonition is dev-only).

**Workflow conventions still in force:**
- All edits land on **dev** first, user reviews, says **"mirror"** → push to **prod** only.
- **Preview stays stale.**
- Markdown files are **CRLF, no BOM** (the reader normalizes CRLF→LF at parse time). The Edit tool struggles with CRLF matches; prefer Python with `open(p,'rb').read().replace(b'\r\n',b'\n').decode('utf-8')` for content edits.
- Reader URL form is **hash-form**: `reader.html#docs%2F<vol>%2F<slug>.md`.
- Vol 5 PDF-popup links are **suffix-style**: `[(pdf)](source-pdfs/x.pdf){: .pdf-popup data-pdf-label="X — Title" }`.
- Mirror commits use `"Mirror … from dev"` framing where appropriate.

---

## 1. What landed this session (chronological)

1. **Group C image cleanup** (bespoke concept diagrams) — completed, mirrored. SMPR redraw + 5 insets + cupped-hands C5 swap + 3 orphaned images removed.
2. **Group D image cleanup** (verse cards) — D25 handshake graphic removed; D23/D24 verse cards kept per user.
3. **Vol 1 closing-image swap** — watermarked man-on-a-rock (`image-008.jpeg`) → clean four-hikers celebration photo (`hikers-summit-celebration.jpg`) in `word-to-my-kids-at-the-end.md`.
4. **MSF chapter content** — populated the previously-empty Vol 5 chapter `measuring-spiritual-formation-at-scale.md` with a Council-audience summary + PDF-popup link + integration-not-replacement admonition.
5. **Cameron & Quinn bibliography entries** — three entries added to Vol 5 Part I (main entry + Diagnosing and Changing OC + Competing Values Leadership) between Brueggemann and Campbell.
6. **Rifkin bibliography entry** — Dr. Stan Rifkin (Master Systems Inc.) added between Newton and Schwarz, with John's "Director of Total Quality" personal detail.
7. **ATB Formation Document — full Phase 1 → Phase 2 promotion:**
   - Three source papers (Warrior Monk × TPM packet; AnswerThis.io trust paper; GPT-5 v6 trust/love/hope paper) extracted and synthesized into a candidate paper.
   - v0 draft → John edited → v1 with annotated bibliography → published.
   - Now lives as the **8th Formation Document** alongside TA, HFT, SST, MSFIG, FC, 4Cs, MSF.
   - Working markdown at `_implementation-notes/atb-attachment-theory-biblical-triad/atb-v1-draft.md`.
   - Published PDF at `docs/volume-5-references/source-pdfs/atb-attachment-theory-and-the-biblical-triad.pdf` (478 KB).
   - Vol 5 summary chapter at `docs/volume-5-references/attachment-theory-and-the-biblical-triad.md`.
   - Added to Vol 5 introduction.md PDF-popup list + index.md.
   - Three FUTURE EXPLORATION pointers (V2.Exp1 Heart Soil, V1.Exp8 Prayer as Resonance, Vol 3 Open Trails) link directly to the new chapter and PDF.
   - Four attachment-theory authors added to Vol 5 Part I bibliography: Bowlby, Granqvist, Kirkpatrick, Mikulincer & Shaver.
8. **Editorial-flag sweep across Vol 5** — removed ALL FLAG-for-John callouts and ALL citation-verification *Note paragraphs across Vol 5 Parts I and II. Confirmed clean by exhaustive sweep.

---

## 2. The ATB workstream — where things live

This is the most likely focus of continued editing.

### Working artifact (editable, off the published site)
- **`_implementation-notes/atb-attachment-theory-biblical-triad/atb-v1-draft.md`**
  — the canonical markdown source. Edits go here. CRLF, no BOM, ~7,700 words + bibliography.

### Published artifacts (live on dev + prod)
- **PDF:** `docs/volume-5-references/source-pdfs/atb-attachment-theory-and-the-biblical-triad.pdf`
  — generated from the v1 markdown. Regenerate after any substantial edit using:
  ```bash
  python C:/Users/jgtit/claude/_work/_imgwork/gen_atb_pdf.py
  # then PowerShell-Word-COM to convert atb-v1-final.docx → PDF (see prior session)
  ```
- **Vol 5 chapter summary:** `docs/volume-5-references/attachment-theory-and-the-biblical-triad.md` — independent of the working markdown (a separate Council-audience summary, NOT auto-generated from atb-v1-draft.md).
- **Introduction list entry:** `docs/volume-5-references/introduction.md` (last bullet in the PDF-popup list).
- **Index entry:** `docs/volume-5-references/index.md` (last bullet).
- **Bibliography entries:** `docs/volume-5-references/part-i-scholarly-and-academic-sources.md` (Bowlby, Granqvist, Kirkpatrick, Mikulincer & Shaver).
- **FUTURE EXPLORATION pointers** in three chapters, each with direct link to the new Vol 5 chapter + PDF popup:
  - `docs/volume-2-knowing-to-doing/exploration-01-heart-soil.md` (Sower-and-Attachment parallel mapping)
  - `docs/volume-1-laws-of-the-spirit/exploration-08-prayer-as-resonance-phenomenon.md` (creaturely substrate of resonance)
  - `docs/volume-3-quantitative-framework/open-trails-what-vol-3-cannot-yet.md` (Attachment-Substrate Measurement Extension)

### ATB regeneration workflow (when the working draft is edited)
1. Edit `_implementation-notes/atb-attachment-theory-biblical-triad/atb-v1-draft.md`.
2. Regenerate docx: `python C:/Users/jgtit/claude/_work/_imgwork/gen_atb_pdf.py` (writes `atb-v1-final.docx`).
3. PowerShell-Word-COM to convert docx → PDF (the prior session has the snippet; uses `wdFormatPDF = 17`).
4. Replace `docs/volume-5-references/source-pdfs/atb-attachment-theory-and-the-biblical-triad.pdf`.
5. If structural content changes affect the Vol 5 chapter summary, update `attachment-theory-and-the-biblical-triad.md` separately.
6. Push to dev, verify build, wait for user "mirror" → push to prod.
7. **Preview stays stale.**

### The three source papers
- Stored in `C:/Users/jgtit/claude/_work/_imgwork/att_src/` (copies; originals in OneDrive `…/FotH 2025/Attachment Theory Plus Sept 2025/`).
- Extracted plain-text in `C:/Users/jgtit/claude/_work/_imgwork/att-*.md`.

---

## 3. Open threads / likely next moves

### Most likely continuations
- **Further editing of ATB v1 draft** — John may want to add personal voice, FotH case examples, or expand specific sections. The working markdown is ready for edits; bibliography is complete.
- **Maturing the Phase 1 → Phase 2 promotion** — anything in the published Vol 5 ATB chapter that John wants to revise. The chapter is a separate Council-audience summary, not auto-generated from the working markdown.

### Identified but deferred follow-ups
- **Vol 5 introduction narrative inconsistency** — the intro text still says "the five Formation Documents" and "FC is the newest of the six" while the PDF-popup list now shows 8 entries (TA/HFT/SST/MSFIG/FC/4Cs/MSF/ATB). A narrative cleanup pass is overdue but was out of scope this session.
- **Vol 5 introduction integration-not-replacement admonition** — currently mentions HFT/MSFIG/TA as the ones to "read through that lens." When extending the sweep, SST/FC/4Cs/MSF should be added; ATB is exempt (it carries the framing natively).
- **Preview repo** — still at `4110ed1`. Carries pre-cleanup C/D images, pre-ATB content. Mirror these only at next major preview refresh (per user's standing instruction).
- **ATB empirical work** — Section 8 of the paper proposes the Sower-as-attachment-pattern parallel mapping as a research question. FotH's 8-week attachment-style trackers correlated with V2.Exp1 Sower-diagnostic outcomes would be the first empirical test.

---

## 4. Key memory files (auto-loaded into Claude's context)

- **[reference_ijh_dev_repo.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/reference_ijh_dev_repo.md)** — dev repo + PDF popup conventions
- **[reference_ijh_dev_prod_mirror_workflow.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/reference_ijh_dev_prod_mirror_workflow.md)** — the mirror workflow
- **[reference_ijh_implementation_notes_convention.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/reference_ijh_implementation_notes_convention.md)** — `_implementation-notes/` convention
- **[task_ijh_image_cleanup.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/task_ijh_image_cleanup.md)** — image cleanup task (all groups done + Vol 1 hikers swap as closing addendum)
- **[task_ijh_affective_taxonomy_reframe.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/task_ijh_affective_taxonomy_reframe.md)** — AT integration-not-replacement framing
- **[reference_collaborator_epithetical_son.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/reference_collaborator_epithetical_son.md)** — JD (the other collaborator) context
- **[convention_divine_pronoun_capitalization.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/convention_divine_pronoun_capitalization.md)** — He/Him for divine pronouns
- **[reference_ijh_atb_formation_document.md](file:///C:/Users/jgtit/.claude/projects/C--Users-jgtit/memory/reference_ijh_atb_formation_document.md)** — ATB Formation Document existence and layout (new, written 2026-05-31)

---

## 5. Quick-reference paths

- **dev clone:** `C:/Users/jgtit/claude/_work/Intentional-Journey-of-the-Heart-dev/`
- **prod clone:** `C:/Users/jgtit/claude/_work/Intentional-Journey-of-the-Heart/`
- **preview clone:** `C:/Users/jgtit/claude/_work/Intentional-Journey-of-the-Heart-preview/`
- **Working artifacts:** `C:/Users/jgtit/claude/_work/_imgwork/`
- **User's current-documents folder** (for docx exchange): `C:/Users/jgtit/OneDrive/Documents/Intentional Journey of the Heart/Current Documents/`
- **FotH 2025 source papers:** `C:/Users/jgtit/OneDrive/Documents/Intentional Journey of the Heart/Band of Brothers and Sisters/Fellowship of the Heart/FotH 2025/Attachment Theory Plus Sept 2025/`

---

## 6. Live URLs (sanity-check from a fresh session)

- **Dev site:** https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-dev/
- **Prod site:** https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/
- **Preview site:** https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart-preview/
- [ATB on prod](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/reader.html#docs%2Fvolume-5-references%2Fattachment-theory-and-the-biblical-triad.md)
- [ATB PDF on prod](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/docs/volume-5-references/source-pdfs/atb-attachment-theory-and-the-biblical-triad.pdf)
- [Vol 5 introduction on prod](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/reader.html#docs%2Fvolume-5-references%2Fintroduction.md)
- [Vol 5 Part I bibliography on prod](https://jgtittle-ministries.github.io/Intentional-Journey-of-the-Heart/reader.html#docs%2Fvolume-5-references%2Fpart-i-scholarly-and-academic-sources.md)

---

## 7. Suggested first actions for the new session

1. Read this handoff + check `git -C dev log --oneline -10` for any commits made after this handoff.
2. Run `git status` in all three repos to confirm clean state.
3. Ask the user what they want to work on. Most likely candidates:
   - More ATB editing
   - Cleanup of the Vol 5 introduction narrative inconsistencies
   - Some other thread they raise
4. Auto-loaded memory files give the conventions; this handoff fills in what state things are in.
