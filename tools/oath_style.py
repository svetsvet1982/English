"""Sentence-level style check for THE OATH episodes (complements tools/check.py).

Usage: python3 tools/oath_style.py [-v] FILE...
Flags episodes whose dialogue is too choppy: too many fragment sentences
("Senator. Pennsylvania. Not crying.") or too many very short turns.
-v lists the offending turn numbers so they can be rewritten.

Targets per episode:
  avg words per sentence  >= 8.0
  sentences of <=3 words  <= 15% of all sentences
  fragment-heavy turns    <= 5%   (>=2 sentences of <=3 words making up half or more of the turn)
  short turns (<=8 words) 10-18%
"""
import re, sys, pathlib

TURN = re.compile(r"^(\d{3})\. [A-Z][A-Z .'&-]*: (\S.*)")


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])[\"”']?\s+", text) if s.strip()]


def analyze(path):
    turns = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        m = TURN.match(line)
        if m:
            turns.append((m.group(1), m.group(2)))
    sw, frag_turns, short_turns = [], [], []
    for num, text in turns:
        lens = [len(s.split()) for s in sentences(text)]
        sw += lens
        tiny = sum(1 for x in lens if x <= 3)
        if tiny >= 2 and tiny * 2 >= len(lens):
            frag_turns.append(num)
        if len(text.split()) <= 8:
            short_turns.append(num)
    n = len(turns) or 1
    stats = {
        "avg_sentence": sum(sw) / max(len(sw), 1),
        "tiny_sentences": 100 * sum(1 for x in sw if x <= 3) / max(len(sw), 1),
        "fragment_turns": 100 * len(frag_turns) / n,
        "short_turns": 100 * len(short_turns) / n,
    }
    issues = []
    if stats["avg_sentence"] < 8.0: issues.append("sentences too short on average")
    if stats["tiny_sentences"] > 15: issues.append("too many <=3-word sentences")
    if stats["fragment_turns"] > 5: issues.append("too many fragment-chain turns")
    if not 10 <= stats["short_turns"] <= 18: issues.append("short-turn share outside 10-18%")
    return stats, issues, frag_turns, short_turns


def main():
    args = sys.argv[1:]
    verbose = "-v" in args
    args = [a for a in args if a != "-v"]
    bad = 0
    for p in args:
        s, issues, frag, short = analyze(p)
        line = (f"avg sentence {s['avg_sentence']:.1f} words / tiny sentences {s['tiny_sentences']:.0f}% / "
                f"fragment turns {s['fragment_turns']:.0f}% / short turns {s['short_turns']:.0f}%")
        if issues:
            bad += 1
            print(f"{p}: STYLE — {line} — " + "; ".join(issues))
        else:
            print(f"{p}: STYLE OK ({line})")
        if verbose:
            print("  fragment-chain turns:", " ".join(frag) or "-")
            print("  short turns (<=8 words):", " ".join(short) or "-")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
