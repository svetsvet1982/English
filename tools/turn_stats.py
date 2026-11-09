import re,glob,sys,statistics as st
rx=re.compile(r"^([A-ZÀ-Ý][A-ZÀ-Ý .'&-]*[A-ZÀ-Ý.]): (\S.*)$",re.M)
def stats(p):
    t=open(p,encoding="utf-8").read().split("## 대본",1)[1].split("\n---",1)[0]
    turns=[m.group(2) for m in rx.finditer(t)]
    w=[len(x.split()) for x in turns]
    sents=[s for x in turns for s in re.split(r"(?<=[.!?])\s+",x) if s.strip()]
    sl=[len(s.split()) for s in sents]
    frag=sum(1 for n in sl if n<=3)/len(sl)
    return st.mean(w), sum(1 for n in w if n>=20)/len(w), st.mean(sl), frag
for part in range(1,6):
    rows=[(p,*stats(p)) for p in sorted(glob.glob(f"대본_The_Corner_House/{part}부/*.md"))]
    print(f"{part}부 avg turn {st.mean(r[1] for r in rows):.1f}w | turns>=20w {st.mean(r[2] for r in rows)*100:.0f}% | avg sent {st.mean(r[3] for r in rows):.1f}w | fragments(<=3w) {st.mean(r[4] for r in rows)*100:.0f}%")
    if "-v" in sys.argv:
        for r in rows: print(f"   {r[0].split('/')[-1][:30]:30} {r[1]:5.1f} {r[3]:5.1f} {r[4]*100:4.0f}%")
