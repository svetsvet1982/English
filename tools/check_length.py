"""Turn/sentence length check by level for The Corner House.
Targets (English script only):
  1부 A2-B1 : avg turn >= 9w,  avg sentence >= 4.5w, fragments(<=3w) <= 40%, max sentence 20w
  2-3부 B1-B2: avg turn >= 12w, avg sentence >= 5.5w, fragments <= 35%, max sentence 25w, >=8% turns 20w+
  4-5부 B2-C1: avg turn >= 15w, avg sentence >= 6.5w, fragments <= 30%, max sentence 30w, >=18% turns 20w+
"""
import re,sys,statistics as st
rx=re.compile(r"^([A-ZÀ-Ý][A-ZÀ-Ý .'&-]*[A-ZÀ-Ý.]): (\S.*)$",re.M)
T={1:(4.5,.40,20,0,9),2:(5.5,.35,25,.08,12),3:(5.5,.35,25,.08,12),4:(6.5,.30,30,.18,15),5:(6.5,.30,30,.18,15)}
ok=True
for p in sys.argv[1:]:
    part=int(re.search(r"/(\d)부/",p).group(1))
    t=open(p,encoding="utf-8").read().split("## 대본",1)[1].split("\n---",1)[0]
    turns=[m.group(2) for m in rx.finditer(t)]
    sents=[s for x in turns for s in re.split(r'(?<=[.!?])["”]?\s+',x) if s.strip()]
    sl=[len(s.split()) for s in sents]
    avg=st.mean(sl); frag=sum(n<=3 for n in sl)/len(sl); mx=max(sl)
    long_t=sum(len(x.split())>=20 for x in turns)/len(turns)
    a,f,m,l,tw=T[part]
    bad=[]
    at=st.mean(len(x.split()) for x in turns)
    if at<tw: bad.append(f"avg turn {at:.1f}<{tw}")
    if avg<a: bad.append(f"avg sentence {avg:.1f}<{a}")
    if frag>f: bad.append(f"fragments {frag*100:.0f}%>{f*100:.0f}%")
    if mx>m: bad.append(f"longest sentence {mx}w>{m}")
    if long_t<l: bad.append(f"20w+ turns {long_t*100:.0f}%<{l*100:.0f}%")
    print(f"{p.split('/')[-1]}: avg sent {avg:.1f}w, frag {frag*100:.0f}%, turn {st.mean(len(x.split()) for x in turns):.1f}w, 20w+ {long_t*100:.0f}% -> {'OK' if not bad else 'NEEDS WORK: '+'; '.join(bad)}")
    ok &= not bad
sys.exit(0 if ok else 1)
