import docx
import re
from pathlib import Path

DOCX_PATH = Path(r"c:/Users/zhenx/Desktop/my_first_bank_project/ai规划.docx")
OUT_PATH = Path(r"c:/Users/zhenx/Desktop/my_first_bank_project/three_year_plan.md")

if not DOCX_PATH.exists():
    print(f"ERROR: {DOCX_PATH} not found")
    raise SystemExit(1)

doc = docx.Document(str(DOCX_PATH))
lines = []
for p in doc.paragraphs:
    text = p.text.strip()
    if not text:
        continue
    style = ''
    try:
        style = p.style.name
    except Exception:
        style = ''
    if style and style.startswith('Heading'):
        m = re.search(r"Heading\s*(\d+)", style)
        if m:
            level = int(m.group(1))
            level = min(max(level,1),6)
            lines.append('#'*level + ' ' + text)
        else:
            lines.append('## ' + text)
    else:
        lines.append(text)

OUT_PATH.write_text('\n\n'.join(lines), encoding='utf-8')
print(f"WROTE: {OUT_PATH}")
