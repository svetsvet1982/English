"""Replace whole turns (English line + Korean line) in an episode file.

Usage: python3 tools/oath_rewrite.py EPISODE.md EDITS.txt
EDITS.txt has one turn per line:  NNN|new English line|새 한국어 번역
The speaker labels (English and Korean) are kept from the episode file; only the
spoken text changes. Blank lines and lines starting with # are ignored.
"""
import re, sys, pathlib

ep, edits = map(pathlib.Path, sys.argv[1:3])
lines = ep.read_text(encoding="utf-8").splitlines()
index = {}
for i, l in enumerate(lines):
    m = re.match(r"^(\d{3})\. ([A-Z][A-Z .'&-]*): ", l)
    if m:
        index[m.group(1)] = i
done = 0
for raw in edits.read_text(encoding="utf-8").splitlines():
    if not raw.strip() or raw.startswith("#"):
        continue
    num, en, ko = (x.strip() for x in raw.split("|", 2))
    i = index[num]
    speaker = re.match(r"^\d{3}\. ([A-Z][A-Z .'&-]*): ", lines[i]).group(1)
    ko_line = lines[i + 1]
    ko_name = re.match(r"^    ([^:]{1,25}):", ko_line)
    lines[i] = f"{num}. {speaker}: {en}"
    lines[i + 1] = f"    {ko_name.group(1)}: {ko}" if ko_name else f"    {ko}"
    done += 1
ep.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"{ep.name}: replaced {done} turns")
