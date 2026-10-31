"""대본 마크다운을 부별 PDF와 전체 합본 PDF로 만든다.

사용법: python3 tools/make_pdf.py
"""
import html
import re
from pathlib import Path

import markdown
import json
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent / "the_first_year"
OUT = ROOT / "PDF"
PARTS = ["1부", "2부", "3부", "4부"]
TURN = re.compile(r"^(\d{3})\. ([A-Z][A-Z .'&-]*): (.*)$")
TRANS = re.compile(r"^    (.*)$")

CSS = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body { font-family: 'WenQuanYi Zen Hei', sans-serif; font-size: 10.5pt;
       line-height: 1.5; color: #222; }
h1 { font-size: 20pt; margin: 0 0 4pt; color: #7a4a00; }
h2 { font-size: 14pt; margin: 14pt 0 6pt; border-bottom: 1px solid #ccc; }
blockquote { background: #f6f3ec; border-left: 4px solid #c9a227; margin: 8pt 0;
             padding: 6pt 10pt; font-size: 9.5pt; }
blockquote ul { margin: 2pt 0; padding-left: 14pt; }
.ep { page-break-before: always; }
.ep:first-of-type { page-break-before: auto; }
.turn { margin: 0 0 6pt; page-break-inside: avoid; }
.en { padding-left: 26pt; text-indent: -26pt; }
.num { color: #999; font-size: 8.5pt; display: inline-block; width: 22pt; text-indent: 0; }
.spk { font-weight: bold; color: #1f4e79; }
.ko { color: #555; font-size: 9.5pt; padding-left: 26pt; }
.cover { text-align: center; padding-top: 220pt; page-break-after: always; }
.cover h1 { font-size: 32pt; }
.cover p { font-size: 13pt; color: #666; }
.toc { page-break-after: always; }
.toc li { margin: 2pt 0; }
li { margin: 2pt 0; }
"""


def ep_key(p):
    return int(p.name.split("화")[0])


def render_episode(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    out, buf = [], []

    def flush():
        # python-markdown은 목록 앞에 빈 줄이 있어야 목록으로 인식한다
        for j in range(len(buf) - 1, 0, -1):
            cur, prev = buf[j], buf[j - 1]
            if cur.startswith("> - ") and prev.startswith("> ") and not prev.startswith("> - "):
                buf.insert(j, ">")
        if buf:
            out.append(markdown.markdown("\n".join(buf)))
            buf.clear()

    i = 0
    while i < len(lines):
        m = TURN.match(lines[i])
        if m:
            flush()
            num, spk, text = m.groups()
            ko = ""
            if i + 1 < len(lines) and TRANS.match(lines[i + 1]):
                ko = TRANS.match(lines[i + 1]).group(1)
                i += 1
            out.append(
                f'<div class="turn"><div class="en"><span class="num">{num}</span>'
                f'<span class="spk">{html.escape(spk)}:</span> {html.escape(text)}</div>'
                f'<div class="ko">{html.escape(ko)}</div></div>'
            )
        else:
            buf.append(lines[i])
        i += 1
    flush()
    return '<section class="ep">' + "\n".join(out) + "</section>"


def title_of(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            return line[3:]
    return path.stem


def build_html(parts, title):
    toc, body = [], []
    for part in parts:
        eps = sorted((ROOT / "대본" / part).glob("*.md"), key=ep_key)
        toc.append(f"<h2>{part}</h2><ol>")
        for ep in eps:
            toc.append(f"<li>{html.escape(title_of(ep))}</li>")
            body.append(render_episode(ep))
        toc.append("</ol>")
    sub = " · ".join(parts) if len(parts) > 1 else parts[0]
    return (
        f"<!doctype html><html lang='ko'><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
        f"<div class='cover'><h1>THE FIRST YEAR</h1><p>{sub}</p><p>영어 대화문 시리즈</p></div>"
        f"<div class='toc'><h1>목차</h1>{''.join(toc)}</div>"
        + "".join(body)
        + "</body></html>"
    )


NODE = """
const { chromium } = require('playwright');
const jobs = JSON.parse(process.argv[1]);
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const [src, dst] of jobs) {
    await page.goto('file://' + src, { waitUntil: 'load' });
    await page.pdf({
      path: dst, format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: "<div style='font-size:8pt;width:100%;text-align:center;color:#999'><span class='pageNumber'></span></div>",
      margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
    });
    console.log('wrote', dst);
  }
  await browser.close();
})();
"""


def main():
    OUT.mkdir(exist_ok=True)
    jobs = [([p], f"The_First_Year_{p}") for p in PARTS]
    jobs.append((PARTS, "The_First_Year_전체"))
    with tempfile.TemporaryDirectory() as tmp:
        pairs = []
        for parts, name in jobs:
            src = Path(tmp) / f"{name}.html"
            src.write_text(build_html(parts, name), encoding="utf-8")
            pairs.append([str(src), str(OUT / f"{name}.pdf")])
        subprocess.run(["node", "-e", NODE, json.dumps(pairs)], check=True)


if __name__ == "__main__":
    main()
