"""Check episode files (add --strict for the sentence-quality rules: <=15% short turns, <=12% fragment sentences of <=3 words, mean sentence >=9 words): numbered turns 001-N (N=120 by default; `--turns 120-150` allows a range), each followed by a Korean translation line.
Also prints the turn-length mix (words per English line) and flags episodes outside the target mix:
short <=8 ~25%, medium 9-15 ~35%, longer 16-25 ~25%, long 26-40 ~15%, nothing over 45."""
import re, sys, pathlib
args = sys.argv[1:]
lo_t = hi_t = 120
strict = "--strict" in args
args = [a for a in args if a != "--strict"]
if args and args[0] == "--turns":
    lo_t, hi_t = (int(x) for x in (args[1].split("-") + args[1].split("-"))[:2]); args = args[2:]
bad = 0
for p in args:
    lines = pathlib.Path(p).read_text(encoding="utf-8").splitlines()
    nums, words, sents = [], [], []
    for i, l in enumerate(lines):
        m = re.match(r"^(\d{3})\. [A-Z][A-Z .'&-]*: (\S.*)", l)
        if m:
            nums.append(int(m.group(1))); words.append(len(m.group(2).split()))
            sents += [len(x.split()) for x in re.split(r"(?<=[.!?…])\s+", m.group(2)) if x.strip()]
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not re.match(r"^    \S", nxt) or not re.search(r"[가-힣]", nxt):
                print(f"{p}: turn {m.group(1)} missing Korean line"); bad += 1
    if nums != list(range(1, len(nums) + 1)) or not lo_t <= len(nums) <= hi_t:
        print(f"{p}: turns {len(nums)}, expected 001-{lo_t}..{hi_t} in order"); bad += 1
        continue
    pct = lambda lo, hi: round(100 * sum(lo <= w <= hi for w in words) / len(words))
    mix = (pct(0, 8), pct(9, 15), pct(16, 25), pct(26, 45))
    over = sum(w > 45 for w in words)
    issues = []
    if mix[2] + mix[3] < 30: issues.append("too few long turns (16+ words should be ~40%)")
    if mix[3] < 8: issues.append("too few 26+ word turns (~15%)")
    if mix[0] < (5 if strict else 15): issues.append("too few short turns")
    if over: issues.append(f"{over} turn(s) over 45 words")
    frag = round(100 * sum(x <= 3 for x in sents) / len(sents))
    mean_s = round(sum(sents) / len(sents), 1)
    if strict:
        if mix[0] > 15: issues.append(f"too many short turns ({mix[0]}% <=8 words, max 15%)")
        if frag > 12: issues.append(f"too many fragment sentences ({frag}% <=3 words, max 12%)")
        if mean_s < 9: issues.append(f"sentences too short (mean {mean_s} words, min 9)")
    stat = f"short {mix[0]}% / medium {mix[1]}% / longer {mix[2]}% / long {mix[3]}% / sent {mean_s}w, frag {frag}%"
    if issues:
        print(f"{p}: LENGTH MIX — {stat} — " + "; ".join(issues)); bad += 1
    else:
        print(f"{p}: OK ({stat})")
sys.exit(1 if bad else 0)
