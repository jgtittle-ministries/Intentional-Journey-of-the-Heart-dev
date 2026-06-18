# Session handoff — START HERE (2026-06-18)

Self-contained pickup. Everything below is shipped and verified. Supersedes the 2026-06-17 START-HERE handoff. *(Note: this session's commits/artifacts are stamped 2026-06-17; the system clock rolled to 06-18 — same body of work, no discrepancy in content.)*

## Repo state
| Repo | Path | HEAD |
|---|---|---|
| **IJH dev** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart-dev` | `15dcffa` |
| **IJH prod** | `C:\Users\jgtit\claude\_work\Intentional-Journey-of-the-Heart` | `8d01617` |

**dev and prod are in sync on all published content** (docs/, manifest.js, the *.html, search-index.js). Dev carries *additional dev-only working artifacts* under `_implementation-notes/` (peer-review folders, the panel registry, brainstorm notes, this handoff) — those are **never mirrored**. Rollback tag `v5.7.2-baseline` stands in both repos.

Standing facts (don't re-derive): static "warm reader" (index.html/reader.js/**manifest.js** nav-list + prev/next chain/search-index.js), NOT MkDocs; regen index with `node _work/_gen_search_index.js "<ABS repo path>"`; **divine pronouns Capitalized in the books**, lowercase in the academic Formation Documents; ESV verbatim; plain (15–16-yr-old) register; John uses the **desktop app** and is **new to git** (ELI5, offer to run commands, don't hand him CLI). Mirror procedure + HTML-edit-in-place gotcha: [[reference_ijh_dev_prod_mirror_workflow]], [[reference_ijh_logo_and_html_mirror_gotcha]]. md→docx: `node _work/_docxbuild/md-to-docx.js <in.md> <out.docx>` (it can hit an EBUSY lock if the docx is open in Word — ask John to close it).

## §1 What this session did (all shipped + mirrored unless noted)
1. **Vol 1–3 peer review** (McGrath / Peterson / Polkinghorne) — 4 findings live on both repos (H1 surface the TFT-Challenged critique + reframe F_s as a schema; H2 "If You Come Weary" slow-door front chapter; M1 guard-before-the-taxonomy-levels; M3 passage→law hermeneutical note). **M2 (divine-action trail) DECLINED — recoverable via `git cherry-pick c9b8e8c`.** [[project_ijh_vol1_3_peer_review]]
2. **Formation Companion** — added *"Other Possible Development Paths Held Open for Future Contributors"* (names streams beyond the four traditions, **no assessment**, gated by the Powlison/Trentham test + an experienced contributor; parallels the held-open spiritual-warfare + women's-side frontiers) + a matching Vol 6 Research Register trail. The three FC article drafts matched (JSFSC→v3 docx, CEJ→v2 docx education-framed, merged md). [[reference_ijh_edits_formation_companion]]
3. **NEW Vol 3 companion chapter — "The Engine Beneath the Force: Spiritual Energy, Time, and Inertia"** (after Exp 9): inertia (`aₛ=Fₛ/mₛ`, dual valence)/kairos-time/energy (G as open-system source)/the work-integral (widow's mite)/revival-as-activation-cascade/friction γ/gift-of-faith-as-localized-barrier-drop/temperature/congregation phase-map; **Schwarz *God's Energy* energeia grounding** (energy = NT word, not borrowed physics); 2 self-contained SVG figures (`images/energy-landscape.svg`, `images/congregation-phases.svg`). [[project_ijh_engine_chapter]]
4. **Law-expansion stress-test** of the Engine exercise → **0 new Foundational Laws** (field-roles/instruments + re-descriptions; catalog holds at 47). Artifact md+docx in `_implementation-notes/`.
5. **Peer-Review Panel Registry v1** — Council instrument for the **first Council meeting, 2026-06-28** (`_implementation-notes/peer-review-panel-registry/`, md + docx). 24-persona bench, 7 reviews on record, target→panel empanelment guide, shared method. [[reference_ijh_peer_review_panel_registry]]
6. **Engine chapter peer-reviewed by the quantitative nine-author panel** (registry's first live run) → full punch-list **implemented + mirrored** (H1 guards soul→congregation; H2 gift-of-faith repaired; M1 boundary→ordinal + symbols policed; M2 temperature fixed; M3 believer's responsive part; M4/M5 energeia + commensurability; 5 lows). Review artifact marked **RESOLVED** with a finding→commit table.
7. **Authorial-intent clarification (important):** the project is John's **testimony to his kids/grandkids — NOT an apologetic.** Adversarial panel **declined** and removed from the registry. Panels/guards serve **fidelity, pastoral safety, clarity**, not argument. [[feedback_project_is_testimony_not_apologetic]]

## §2 Open items / next tasks
- **Granddaddy note for the Engine chapter** — the chapter's ONE remaining content gap. John dictates it; drop it into the open spot at the chapter's end and run the small dev→prod follow-up. (Granddaddy notes are **John's own — never fabricate.**)
- **LANGBERG-2 — the FC safeguarding architecture** (informed consent + right to stop; conduct rules barring dual/exploitative relationships; a complaints body; grievance/removal process; witness/debrief for solo high-intensity work). Reserved for the Council / Character-Prerequisites pass; carried into the 2026-06-28 meeting.
- **Council first meeting 2026-06-28** — the Panel Registry docx is ready for review; Stewards to nominate reviewers for the named gaps (woman theologian, Orthodox/patristic, Roman Catholic sacramental, majority-world, analytic philosophy, OT/hermeneutics). The adversarial panel is *not* on the table (set aside).
- **M2 divine-action trail** — declined; do NOT re-add unless John asks (cherry-pick `c9b8e8c` if he changes his mind).

## §3 How to work here (the standing posture)
dev-first; **mirror ONLY on John's explicit "mirror."** One change at a time, show him in chat, pause for his OK. Working artifacts live in `_implementation-notes/` (dev-only). And hold the frame from §1.7: this is a grandfather handing down what he has seen — keep it **true, safe, and clear**, not armored for debate. See [[reference_ijh_dev_prod_mirror_workflow]], [[reference_ijh_version_baseline]], [[user_ijh_author_new_to_git]], [[user_runs_claude_desktop_app]], [[convention_divine_pronoun_capitalization]].
