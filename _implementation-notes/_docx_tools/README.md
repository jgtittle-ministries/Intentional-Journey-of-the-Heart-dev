# Word-copy tooling (2026-09-05)

pandoc lives at C:\Users\jgtit\AppData\Local\Pandoc\pandoc.exe (not on PATH).
Build: pandoc file.md --from markdown --to docx -o file.docx  (add --resource-path=. when the page has images).
tighten_onepager.py file.docx  -> 10pt body, narrow margins, for one-page handouts.
landscape_tables.py file.docx  -> Letter landscape, 8pt table text, for wide grids.
export-pdf.ps1  -> exports draft.docx to draft.pdf through Word COM; edit the $dir path at the top, then render pages with pymupdf and Read the PNGs.
No LibreOffice or poppler on this machine; python-docx and pymupdf are installed.
