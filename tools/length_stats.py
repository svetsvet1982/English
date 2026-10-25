"""Turn-length mix for episode files: share of short (1-7 words), medium (8-20), long (21-45), extra-long (46+) turns."""
import re, sys, pathlib
for p in sys.argv[1:]:
    counts = [0, 0, 0, 0]
    for l in pathlib.Path(p).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\d{3}\. [A-Z][A-Z .'&-]*: (.*)", l)
        if m:
            n = len(m.group(1).split())
            counts[0 if n <= 7 else 1 if n <= 20 else 2 if n <= 45 else 3] += 1
    total = sum(counts) or 1
    pct = [round(100 * c / total) for c in counts]
    print(f"{p}: short {pct[0]}% / medium {pct[1]}% / long {pct[2]}% / 46+ {counts[3]} turns")
