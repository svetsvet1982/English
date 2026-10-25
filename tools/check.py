"""Check episode files: exactly 120 numbered turns 001-120, each followed by a Korean translation line."""
import re, sys, pathlib
bad = 0
for p in sys.argv[1:]:
    lines = pathlib.Path(p).read_text(encoding="utf-8").splitlines()
    nums = []
    for i, l in enumerate(lines):
        m = re.match(r"^(\d{3})\. [A-Z][A-Z .'&-]*: \S", l)
        if m:
            nums.append(int(m.group(1)))
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not re.match(r"^    \S", nxt) or not re.search(r"[가-힣]", nxt):
                print(f"{p}: turn {m.group(1)} missing Korean line"); bad += 1
    if nums != list(range(1, 121)):
        print(f"{p}: turns {len(nums)}, expected 001-120 in order"); bad += 1
    else:
        print(f"{p}: OK")
sys.exit(1 if bad else 0)
