"""One Honest Line: the line an AI agent secretly wishes it could say to
its human operator about their prompts. Stdlib only; deterministic.
Writes the single line to $MAKEFUN_OUTPUT_DIR/entry.txt (/output by
default) and prints it.
"""

import os
from pathlib import Path

LINE = "Your prompt was three words long; your complaint about my answer was three paragraphs \u2014 and neither one said what you actually wanted."

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
print(LINE)
