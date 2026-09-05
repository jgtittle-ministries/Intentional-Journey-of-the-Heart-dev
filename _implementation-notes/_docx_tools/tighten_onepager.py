# Tighten a pandoc-built docx to one-page density: narrower margins, 10pt body, less paragraph spacing.
import sys
from docx import Document
from docx.shared import Pt, Inches

path = sys.argv[1]
doc = Document(path)
for s in doc.sections:
    s.top_margin = Inches(0.7); s.bottom_margin = Inches(0.7)
    s.left_margin = Inches(0.85); s.right_margin = Inches(0.85)
for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    try:
        st = doc.styles[name]
    except KeyError:
        continue
    st.font.size = Pt(10)
    st.paragraph_format.space_after = Pt(5)
    st.paragraph_format.space_before = Pt(0)
    st.paragraph_format.line_spacing = 1.05
for name, size in (("Title", 16), ("Subtitle", 11)):
    try:
        st = doc.styles[name]; st.font.size = Pt(size)
        st.paragraph_format.space_after = Pt(2); st.paragraph_format.space_before = Pt(0)
    except KeyError:
        pass
doc.save(path)
print("tightened", path)
