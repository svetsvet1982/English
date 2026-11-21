"""Style stats for TORQUE episodes: choppy turns (only short fragments) and tiny turns.
Usage: python3 tools/torque_style.py [-v] files...   (-v lists flagged turns)"""
import re, sys
VERBOSE = '-v' in sys.argv
files = [a for a in sys.argv[1:] if a != '-v']
def sents(t):
    t = re.sub(r'\b(Mr|Mrs|Ms|Dr|St|a\.m|p\.m|U\.S)\.', r'\1', t)
    return [s for s in re.split(r'(?<=[.!?])\s+|\s+—\s+|—', t) if s.strip()]
tot = {'turns':0,'choppy':0,'tiny':0}
for p in files:
    L = open(p, encoding='utf-8').read().split('\n')
    n = ch = ti = 0; sl = []; flagged = []
    for l in L:
        m = re.match(r"^(\d{3})\. [A-Z][A-Z .'&-]*: (.*)", l)
        if not m: continue
        n += 1; t = m.group(2); ss = sents(t); lens = [len(s.split()) for s in ss]; sl += lens
        w = len(t.split())
        if len(ss) >= 2 and max(lens) <= 5: ch += 1; flagged.append(('CHOPPY', m.group(1), t))
        elif len(ss) >= 3 and sum(x <= 4 for x in lens) >= len(ss) - 1: ch += 1; flagged.append(('CHOPPY', m.group(1), t))
        elif w <= 3: ti += 1; flagged.append(('TINY', m.group(1), t))
    avg = sum(sl) / len(sl)
    ok = ch <= 12 and ti <= 7 and avg >= 8.5
    print(f"{p.split('대본/')[-1]}: {'STYLE OK' if ok else 'STYLE FIX'} — choppy {ch} ({100*ch//n}%, max 12) tiny {ti} ({100*ti//n}%, max 7) avg-sentence {avg:.1f}w (min 8.5)")
    tot['turns'] += n; tot['choppy'] += ch; tot['tiny'] += ti
    if VERBOSE:
        for k, num, t in flagged: print(' ', k, num, t)
if len(files) > 1:
    print(f"TOTAL turns {tot['turns']} choppy {tot['choppy']} ({100*tot['choppy']/tot['turns']:.1f}%) tiny {tot['tiny']} ({100*tot['tiny']/tot['turns']:.1f}%)")
