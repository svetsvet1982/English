import re,sys,ast
p=sys.argv[1]; new=ast.literal_eval(open(sys.argv[2],encoding='utf-8').read())
L=open(p,encoding='utf-8').read().split('\n'); done=set()
for i,l in enumerate(L):
    m=re.match(r"^(\d{3})\. ([A-Z ]+): ",l)
    if m and m.group(1) in new:
        en,ko=new[m.group(1)]
        L[i]=f"{m.group(1)}. {m.group(2)}: {en}"
        name=L[i+1].strip().split(':')[0]
        L[i+1]=f"    {name}: {ko}"; done.add(m.group(1))
open(p,'w',encoding='utf-8').write('\n'.join(L))
print('applied',len(done),'missing',set(new)-done)
