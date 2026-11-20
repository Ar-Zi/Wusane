import json
from pathlib import Path


project = Path(__file__).resolve().parent
source = project.parent.parent / "git" / "Kurdish-wordlist"
files = sorted(source.glob("*.txt"))
if not files:
    raise FileNotFoundError(f"No text files found in {source}")

lines = []
for file in files:
    lines.extend(file.read_text(encoding="utf-8-sig").splitlines())

words = [line.strip() for line in lines if line.strip()]
if not words:
    raise ValueError(f"No entries found in {source}")

(project / "wordlist.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
data = json.dumps(words, ensure_ascii=False).replace("<", "\\u003c")
(project / "wordlist.js").write_text(
    f"window.WUSANE_WORDS = {data};\n", encoding="utf-8"
)
