"""Check Spanish episode files (PLUS ULTRA): 120-150 consecutive numbered turns starting at 001,
each followed by a Korean translation line. Also prints the turn-length mix (words per Spanish line):
tiny <=3 words at most 3%, short <=8 at most 12%, medium 9-15 ~35%, longer 16-25 ~33%,
long 26-40 ~20%, nothing over 45."""
import re, sys, pathlib
UP = "A-ZÁÉÍÓÚÑÜ"
TURN = re.compile(rf"^(\d{{3}})\. [{UP}][{UP} .'&-]*: (\S.*)")
bad = 0
for p in sys.argv[1:]:
    lines = pathlib.Path(p).read_text(encoding="utf-8").splitlines()
    nums, words = [], []
    for i, l in enumerate(lines):
        m = TURN.match(l)
        if m:
            nums.append(int(m.group(1))); words.append(len(m.group(2).split()))
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not re.match(r"^    \S", nxt) or not re.search(r"[가-힣]", nxt):
                print(f"{p}: turn {m.group(1)} missing Korean line"); bad += 1
    if nums != list(range(1, len(nums) + 1)) or not 120 <= len(nums) <= 150:
        print(f"{p}: turns {len(nums)}, expected consecutive 001-120..150"); bad += 1
        continue
    pct = lambda lo, hi: round(100 * sum(lo <= w <= hi for w in words) / len(words))
    mix = (pct(0, 8), pct(9, 15), pct(16, 25), pct(26, 45))
    tiny = pct(0, 3)
    over = sum(w > 45 for w in words)
    issues = []
    if tiny > 3: issues.append(f"too many 1-3 word turns ({tiny}%, max 3%)")
    if mix[0] > 12: issues.append(f"too many short turns <=8 words ({mix[0]}%, max 12%)")
    if mix[1] < 25: issues.append("too few medium turns (9-15 words, ~35%)")
    if mix[2] + mix[3] < 40: issues.append("too few long turns (16+ words should be ~50%)")
    if mix[3] < 12: issues.append("too few 26+ word turns (~20%)")
    if over: issues.append(f"{over} turn(s) over 45 words")
    stat = f"{len(nums)} turns — tiny {tiny}% / short {mix[0]}% / medium {mix[1]}% / longer {mix[2]}% / long {mix[3]}%"
    if issues:
        print(f"{p}: LENGTH MIX — {stat} — " + "; ".join(issues)); bad += 1
    else:
        print(f"{p}: OK ({stat})")
sys.exit(1 if bad else 0)
