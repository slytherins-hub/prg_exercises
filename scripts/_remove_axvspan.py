"""One-shot script: remove the 3.6 axvspan demo section from the notebook generator."""
import re, pathlib

p = pathlib.Path("scripts/create_cv09_notebooks.py")
text = p.read_text(encoding="utf-8")

# Pattern: the md() cell starting "## 3.6 Segmentace signálu" and the code() cell after it
# ending just before the md() cell that starts with "\n---\n\n## 📝 ÚKOL:"
pattern = re.compile(
    r'    md\("""\\\n## 3\.6 Segmentace sign.+?"""\),\n\n    code\("""\\\nfazes.+?"""\),\n\n(?=    md\("""\\\n---)',
    re.DOTALL
)

new_text, n = pattern.subn("", text)
if n == 0:
    print("NO MATCH – nothing changed")
else:
    p.write_text(new_text, encoding="utf-8")
    print(f"Removed {n} occurrence(s). Lines now: {new_text.count(chr(10))}")
