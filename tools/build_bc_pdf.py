"""Build BACK CHANNEL PDFs: one per part and one per season.

Usage: python3 tools/build_bc_pdf.py [season numbers...]   (default: 1 2 3)
Reuses the episode renderer and styles from build_pdf.py.
"""
import pathlib, subprocess, sys, tempfile
from build_pdf import CSS, ROOT, ep_key, inline, render_episode

SEASONS = {
    1: ("BACK_CHANNEL", "", ["Cold Water (차가운 바다)", "Southern Cross (남십자성)", "Old World (구세계)", "Red Line (레드 라인)"], "2028–2029"),
    2: ("BACK_CHANNEL_S2", "Deepfake Peace", ["Armistice (정전)", "Chokepoint (해협)", "Yellowcake (옐로케이크)", "Chamizal (차미잘)"], "2029–2030"),
    3: ("BACK_CHANNEL_S3", "Window Four", ["Window Four (4번 창구)", "Flight 752 (752편)", "Walk-In (워크인)", "The Caroline Test (캐롤라인 기준)"], "2026–2028 · 프리퀄"),
}


def cover(heading, sub, meta):
    return (f'<div class="cover"><div class="series">BACK CHANNEL</div><h1>{heading}</h1>'
            f'<div class="sub">{sub}</div><div class="meta">{meta}</div></div>')


def part_html(base, n):
    files = sorted((base / "대본" / f"{n}부").glob("*화_*.md"), key=ep_key)
    toc, eps = [], []
    for f in files:
        title, h = render_episode(f)
        toc.append(f"<li><span>{n}부 {ep_key(f)}화</span>{inline(title)}</li>")
        eps.append(h)
    return toc, eps, len(files)


def render(tmp, name, body, dst, label):
    src = pathlib.Path(tmp) / f"{name}.html"
    src.write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}'
                   f'.toc li span{{width:20mm}}</style></head><body>{body}</body></html>', encoding="utf-8")
    subprocess.run(["node", str(ROOT / "tools" / "render_pdf.js"), str(src), str(dst), label], check=True)
    print(dst)


def build_season(s, tmp):
    folder, subtitle, parts, years = SEASONS[s]
    base = ROOT / folder
    out = base / "pdf"
    out.mkdir(exist_ok=True)
    label = f"BACK CHANNEL S{s}"
    season_name = f"시즌 {s}" + (f" — {subtitle}" if subtitle else "")
    all_toc, all_eps, total = [], [], 0
    for n, ptitle in enumerate(parts, 1):
        toc, eps, count = part_html(base, n)
        total += count
        all_toc += toc
        all_eps += eps
        meta = f"{season_name} · {years} · 외교 안보 영어 대화문 · {count}화 · 화당 150턴 · 영한 대역"
        body = (cover(f"{n}부", ptitle, meta) +
                f'<div class="toc"><h2>차례</h2><ol>{"".join(toc)}</ol></div>' + "".join(eps))
        short = ptitle.split(" (")[0].replace(" ", "_")
        render(tmp, f"s{s}p{n}", body, out / f"BACK_CHANNEL_S{s}_{n}부_{short}.pdf", label)
    meta = f"{years} · 외교 안보 영어 대화문 · 4부 {total}화 · 화당 150턴 · 영한 대역"
    body = (cover(f"시즌 {s}", subtitle or "Back Channel", meta) +
            f'<div class="toc"><h2>차례</h2><ol>{"".join(all_toc)}</ol></div>' + "".join(all_eps))
    render(tmp, f"s{s}", body, out / f"BACK_CHANNEL_S{s}_전체.pdf", label)


def main():
    seasons = [int(a) for a in sys.argv[1:]] or [1, 2, 3]
    with tempfile.TemporaryDirectory() as tmp:
        for s in seasons:
            build_season(s, tmp)


if __name__ == "__main__":
    main()
