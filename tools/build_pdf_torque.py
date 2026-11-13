"""Build one PDF per TORQUE part (12 parts x 12 episodes x 150 turns).

Usage: python3 tools/build_pdf_torque.py [part numbers...]   (default: every part)
Reuses the episode renderer from tools/build_pdf.py; output goes to TORQUE/pdf/.
"""
import pathlib, re, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_pdf import CSS, inline, ep_key, render_episode  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "TORQUE" / "대본"
OUT = ROOT / "TORQUE" / "pdf"

PART_TITLES = {
    1: ("Spin-Up", "시동", "2024.11–2025.1", "전기자전거"),
    2: ("Home Front", "가전", "2025.2–4", "세탁기·에어컨"),
    3: ("Motor City", "모터 시티", "2025.5–7", "자동차"),
    4: ("Crossroads", "갈림길", "2025.8–10", "한국 합작·EV·소송"),
    5: ("Red Tape", "레드 테이프", "2025.11–2026.1", "군용 드론"),
    6: ("Field", "들판", "2026.2–4", "농기계"),
    7: ("Comfort Zone", "안락 지대", "2026.5–7", "히트펌프·냉난방"),
    8: ("Every Watt", "1와트", "2026.8–10", "데이터센터"),
    9: ("Copycat", "카피캣", "2026.11–2027.1", "전동공구"),
    10: ("Pulse", "맥박", "2027.2–4", "의료기기"),
    11: ("Hands", "손", "2027.5–7", "로봇·워싱턴"),
    12: ("Torque", "토크", "2027.8–10", "선박·글로벌"),
}


def build_part(n, tmp):
    en, ko, period, market = PART_TITLES[n]
    files = sorted((SCRIPTS / f"{n}부").glob("*화_*.md"), key=ep_key)
    toc, eps = [], []
    for f in files:
        title, h = render_episode(f)
        toc.append(f"<li><span>{ep_key(f)}화</span>{inline(title)}</li>")
        eps.append(h)
    doc = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover"><div class="series">TORQUE</div><h1>{n}부</h1><div class="sub">{en} ({ko})</div>
<div class="meta">{period} · {market}<br>오하이오 데이턴 모터 공장 영어 대화문 · {len(files)}화 · 화당 150턴 · 영한 대역</div></div>
<div class="toc"><h2>차례</h2><ol>{''.join(toc)}</ol></div>
{''.join(eps)}</body></html>"""
    src = pathlib.Path(tmp) / f"torque{n}.html"
    src.write_text(doc, encoding="utf-8")
    name = re.sub(r"[^A-Za-z0-9]+", "_", en).strip("_")
    return src, OUT / f"TORQUE_{n:02d}부_{name}.pdf"


def main():
    parts = [int(a) for a in sys.argv[1:]] or sorted(PART_TITLES)
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for n in parts:
            src, dst = build_part(n, tmp)
            subprocess.run(["node", str(ROOT / "tools" / "render_pdf.js"), str(src), str(dst), "TORQUE"], check=True)
            print(dst)


if __name__ == "__main__":
    main()
