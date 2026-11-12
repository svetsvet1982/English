import re,sys
p=sys.argv[1]; L=open(p,encoding='utf-8').read().split('\n')
for i,l in enumerate(L):
    m=re.match(r"^(\d{3})\. ([A-Z]+): (.*)",l)
    if m and len(m.group(3).split())<=8:
        print(m.group(1),m.group(2),'|',m.group(3),'|',L[i+1].strip())
