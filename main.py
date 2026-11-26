import os

LINE = "fix: it works now. don't ask how. don't touch it. don't look at it. just merge before sunrise."

LIMIT = 139
if len(LINE) != 94 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 94 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# Lowercase, no scope, no body — exactly how it was typed at 3am.
