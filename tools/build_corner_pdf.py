import subprocess, glob, os, re, html
root="/home/user/English/대본_The_Corner_House"
out="/home/user/English/PDF"; os.makedirs(out, exist_ok=True)
css="""

body { font-family: 'WenQuanYi Zen Hei', sans-serif; font-size: 10.5pt; line-height: 1.55; color:#111; }
h1 { font-size: 20pt; margin: 0 0 4pt; } h2 { font-size: 14pt; border-bottom: 1px solid #999; padding-bottom:3pt; margin-top:16pt;}
h3 { font-size: 12pt; }
blockquote { background:#f4f4f4; border-left:4px solid #888; margin:8pt 0; padding:6pt 10pt; font-size:9.5pt; }
.ep { page-break-before: always; }
p { margin: 3pt 0; }
.cover { text-align:center; padding-top: 200pt; } .cover h1 { font-size: 34pt; } .cover p { font-size: 13pt; }
.toc { page-break-before: always; } .toc li { margin: 1pt 0; font-size: 10pt; }
code { font-family: inherit; }
"""
def ep_html(path):
    md=open(path,encoding="utf-8").read()
    # keep line breaks for script/translation lines
    md=re.sub(r"(?m)^(> \*\*.*\*\*)\n> -", r"\1\n>\n> -", md)
    md=re.sub(r"(?m)^([^\n#>\-|\[].*\S)$", r"\1  ", md)
    return subprocess.run(["pandoc","-f","markdown","-t","html"],input=md,capture_output=True,text=True).stdout
def build(files, title, subtitle, name):
    toc="".join(f"<li>{html.escape(os.path.basename(f)[:-3].replace('_',' '))}</li>" for f in files)
    body=f"<div class='cover'><h1>{title}</h1><p>{subtitle}</p></div><div class='toc'><h2>목차</h2><ol>{toc}</ol></div>"
    body+="".join(f"<div class='ep'>{ep_html(f)}</div>" for f in files)
    h=f"<!doctype html><html lang='ko'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
    hp=f"{name}.html"; open(hp,"w",encoding="utf-8").write(h)
    return hp, f"{out}/{name}.pdf"
jobs=[]
allf=[]
for i in range(1,6):
    fs=sorted(glob.glob(f"{root}/{i}부/*.md")); allf+=fs
    jobs.append(build(fs,"THE CORNER HOUSE",f"{i}부 · {len(fs)}화 대본 (영어 대본 + 한글 해석)",f"The_Corner_House_{i}부"))
jobs.append(build(allf,"THE CORNER HOUSE","전체 90화 대본 (영어 대본 + 한글 해석)","The_Corner_House_전체_90화"))
open("jobs.txt","w").write("\n".join(f"{a}\t{b}" for a,b in jobs))
