"""Check episode files: exactly N numbered turns (default 120; pass --turns=150 for TORQUE), each followed by a Korean translation line.
Also prints the turn-length mix (words per English line) and flags episodes outside the target mix:
short <=8 ~25%, medium 9-15 ~35%, longer 16-25 ~25%, long 26-40 ~15%, nothing over 45."""
import re, sys, pathlib
bad = 0
args = sys.argv[1:]
N = 120
for a in [a for a in args if a.startswith("--turns=")]:
    N = int(a.split("=")[1]); args.remove(a)
for p in args:
    lines = pathlib.Path(p).read_text(encoding="utf-8").splitlines()
    nums, words = [], []
    for i, l in enumerate(lines):
        m = re.match(r"^(\d{3})\. [A-Z][A-Z .'&-]*: (\S.*)", l)
        if m:
            nums.append(int(m.group(1))); words.append(len(m.group(2).split()))
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not re.match(r"^    \S", nxt) or not re.search(r"[가-힣]", nxt):
                print(f"{p}: turn {m.group(1)} missing Korean line"); bad += 1
    if nums != list(range(1, N + 1)):
        print(f"{p}: turns {len(nums)}, expected 001-{N:03d} in order"); bad += 1
        continue
    pct = lambda lo, hi: round(100 * sum(lo <= w <= hi for w in words) / len(words))
    mix = (pct(0, 8), pct(9, 15), pct(16, 25), pct(26, 45))
    over = sum(w > 45 for w in words)
    issues = []
    if mix[2] + mix[3] < 30: issues.append("too few long turns (16+ words should be ~40%)")
    if mix[3] < 8: issues.append("too few 26+ word turns (~15%)")
    if mix[0] < 15: issues.append("too few short turns (~25%)")
    if over: issues.append(f"{over} turn(s) over 45 words")
    stat = f"short {mix[0]}% / medium {mix[1]}% / longer {mix[2]}% / long {mix[3]}%"
    if issues:
        print(f"{p}: LENGTH MIX — {stat} — " + "; ".join(issues)); bad += 1
    else:
        print(f"{p}: OK ({stat})")
sys.exit(1 if bad else 0)
