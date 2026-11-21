"""Build PDFs for THE QUIET LEDGER: one per part plus a combined full-series PDF.

Usage: python3 tools/build_ql_pdf.py
Output: The_Quiet_Ledger/pdf/. Reuses the episode renderer from build_pdf.py.
"""
import pathlib, subprocess, tempfile
from build_pdf import CSS, ep_key, inline, render_episode

ROOT = pathlib.Path(__file__).resolve().parent.parent
SERIES = ROOT / "The_Quiet_Ledger"
SCRIPTS, OUT = SERIES / "대본", SERIES / "pdf"
LABEL = "THE QUIET LEDGER"
PARTS = {1: "Dark Money (검은돈)", 2: "The Old Firm (옛 회사)",
         3: "Southie (사우디)", 4: "The Quiet Ledger (조용한 장부)"}
CSS_QL = CSS.replace("#8a6d3b", "#2f4f4f")


def part_html(n):
    files = sorted((SCRIPTS / f"{n}부").glob("*화_*.md"), key=ep_key)
    toc, eps, turns = [], [], 0
    for f in files:
        title, h = render_episode(f)
        turns += h.count('class="turn"')
        toc.append(f"<li><span>{ep_key(f)}화</span>{inline(title)}</li>")
        eps.append(h)
    cover = (f'<div class="cover"><div class="series">{LABEL}</div><h1>{n}부</h1>'
             f'<div class="sub">{PARTS[n]}</div><div class="meta">워싱턴 D.C. 첩보 스릴러 영어 대화문 · '
             f'{len(files)}화 · {turns:,}턴 · 영한 대역</div></div>')
    return cover + f'<div class="toc"><h2>차례</h2><ol>{"".join(toc)}</ol></div>' + "".join(eps)


def write(tmp, name, body, dst):
    src = pathlib.Path(tmp) / name
    src.write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS_QL}</style>'
                   f'</head><body>{body}</body></html>', encoding="utf-8")
    subprocess.run(["node", str(ROOT / "tools" / "render_pdf.js"), str(src), str(dst), LABEL], check=True)
    print(dst)


def main():
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        bodies = {n: part_html(n) for n in PARTS}
        for n, body in bodies.items():
            write(tmp, f"p{n}.html", body,
                  OUT / f"THE_QUIET_LEDGER_{n}부_{PARTS[n].split(' (')[0].replace(' ', '_')}.pdf")
        title = (f'<div class="cover"><div class="series">{LABEL}</div><h1>전체</h1>'
                 f'<div class="sub">1부–4부 · 48화</div><div class="meta">워싱턴 D.C. 첩보 스릴러 영어 대화문 · 영한 대역</div></div>')
        write(tmp, "all.html", title + "".join(bodies.values()), OUT / "THE_QUIET_LEDGER_전체_1-4부.pdf")


if __name__ == "__main__":
    main()
