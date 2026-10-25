"""Build one PDF per part from the episode markdown files.

Usage: python3 tools/build_pdf.py [part numbers...]   (default: every part folder)
Writes HTML to a temp dir and renders with Playwright Chromium via tools/render_pdf.js.
"""
import html, pathlib, re, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "대본"
OUT = ROOT / "pdf"

PART_TITLES = {
    1: "Bleeding (출혈)", 2: "Fresh Faces (새 얼굴)", 3: "The Money (돈)",
    4: "Comeback (반격)", 5: "Legacy (유산)", 6: "Two Cities (두 도시)",
}

CSS = """
@page { size: A4; margin: 18mm 17mm 20mm 17mm; }
body { font-family: 'NanumBarunGothic', 'NanumGothic', sans-serif; font-size: 10.2pt; line-height: 1.45; color: #1d1d1f; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; text-align: center; page-break-after: always; }
.cover .series { font-size: 13pt; letter-spacing: .35em; color: #8a6d3b; }
.cover h1 { font-family: 'NanumMyeongjo', serif; font-size: 40pt; margin: 8mm 0 4mm; }
.cover .sub { font-size: 14pt; color: #555; }
.cover .meta { margin-top: 18mm; font-size: 10pt; color: #777; }
.toc { page-break-after: always; }
.toc h2 { font-family: 'NanumMyeongjo', serif; font-size: 18pt; border-bottom: 2px solid #8a6d3b; padding-bottom: 2mm; }
.toc ol { padding-left: 0; list-style: none; }
.toc li { padding: 1.6mm 0; border-bottom: 1px dotted #ccc; font-size: 11pt; }
.toc li span { color: #8a6d3b; display: inline-block; width: 13mm; }
.ep { page-break-before: always; }
.ep-head .kicker { color: #8a6d3b; font-size: 9.5pt; letter-spacing: .2em; }
.ep-head h2 { font-family: 'NanumMyeongjo', serif; font-size: 21pt; margin: 1mm 0 4mm; }
.info { background: #f6f3ec; border-left: 3px solid #8a6d3b; padding: 3mm 4mm; font-size: 8.8pt; color: #444; margin-bottom: 5mm; }
.info div { margin: .6mm 0; }
.turn { display: grid; grid-template-columns: 9mm 1fr; column-gap: 2mm; margin: 0 0 2.3mm; page-break-inside: avoid; }
.num { color: #aaa; font-size: 8pt; padding-top: .6mm; }
.en { font-size: 10.6pt; }
.en b { color: #8a6d3b; font-size: 8.8pt; letter-spacing: .04em; margin-right: 1.2mm; }
.ko { color: #666; font-size: 9pt; }
h3 { font-family: 'NanumMyeongjo', serif; font-size: 12.5pt; border-bottom: 1px solid #ddd; padding-bottom: 1mm; margin: 7mm 0 2mm; page-break-after: avoid; }
ul.notes { padding-left: 4.5mm; font-size: 9.2pt; }
ul.notes li { margin: 1mm 0; }
ul.notes b { color: #1d1d1f; }
"""


def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r"\1", t)
    return t


def ep_key(p):
    return int(re.match(r"(\d+)화", p.name).group(1))


def render_episode(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    out, title, kicker, info, section = [], "", "", [], None
    notes = {}
    i = 0
    while i < len(lines):
        l = lines[i]
        m = re.match(r"^(\d{3})\. ([A-Z][A-Z .'&-]*): (.*)$", l)
        if l.startswith("# "):
            kicker = l[2:].strip()
        elif l.startswith("## ") and not title:
            title = l[3:].strip()
        elif l.startswith("## "):
            section = l[3:].strip()
            notes[section] = []
        elif l.startswith("> - "):
            info.append(l[4:])
        elif m:
            ko = lines[i + 1].strip() if i + 1 < len(lines) else ""
            ko = re.sub(r"^[^:]{1,25}:\s*", "", ko)
            out.append(
                f'<div class="turn"><div class="num">{m.group(1)}</div><div>'
                f'<div class="en"><b>{inline(m.group(2))}</b>{inline(m.group(3))}</div>'
                f'<div class="ko">{inline(ko)}</div></div></div>')
            i += 1
        elif section and section != "대본" and l.startswith("- "):
            notes[section].append(l[2:])
        elif section and section != "대본" and l.startswith("  ") and notes.get(section):
            notes[section][-1] += " " + l.strip()
        i += 1
    body = [f'<section class="ep"><div class="ep-head"><div class="kicker">{inline(kicker)}</div>'
            f'<h2>{inline(title)}</h2></div>']
    if info:
        body.append('<div class="info">' + "".join(f"<div>{inline(x)}</div>" for x in info) + "</div>")
    body += out
    for sec, items in notes.items():
        if sec == "대본" or not items:
            continue
        name = re.sub(r"\s*\(.*?\)\s*$", "", sec)
        body.append(f"<h3>{inline(name)}</h3><ul class=\"notes\">" +
                    "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
    body.append("</section>")
    return title, "\n".join(body)


def build_part(n, tmp):
    files = sorted((SCRIPTS / f"{n}부").glob("*화_*.md"), key=ep_key)
    toc, eps = [], []
    for f in files:
        title, h = render_episode(f)
        toc.append(f"<li><span>{ep_key(f)}화</span>{inline(title)}</li>")
        eps.append(h)
    doc = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover"><div class="series">THE BOOK</div><h1>{n}부</h1><div class="sub">{PART_TITLES.get(n, "")}</div>
<div class="meta">뉴욕 모델 에이전시 영어 대화문 · {len(files)}화 · 화당 120턴 · 영한 대역</div></div>
<div class="toc"><h2>차례</h2><ol>{''.join(toc)}</ol></div>
{''.join(eps)}</body></html>"""
    src = pathlib.Path(tmp) / f"part{n}.html"
    src.write_text(doc, encoding="utf-8")
    return src, OUT / f"THE_BOOK_{n}부_{PART_TITLES[n].split(' (')[0].replace(' ', '_')}.pdf"


def main():
    parts = [int(a) for a in sys.argv[1:]] or sorted(
        int(p.name[:-1]) for p in SCRIPTS.iterdir() if p.is_dir() and p.name.endswith("부"))
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for n in parts:
            src, dst = build_part(n, tmp)
            subprocess.run(["node", str(ROOT / "tools" / "render_pdf.js"), str(src), str(dst)], check=True)
            print(dst)


if __name__ == "__main__":
    main()
