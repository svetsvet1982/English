"""Check The Corner House episode files.

Format (기획서 기준): the 대본 section has exactly 120 speaker turns written as
`SPEAKER: line` (no turn numbers). Stage directions are lines in square brackets
and are not counted. The 한글 해석 section repeats the 120 turns in the same order
as `이름: 번역`. Also warns about single sentences longer than 20 words
(기본 원칙: 한 호흡 15단어 이내, 긴 설명은 나눠서).
"""
import re
import sys
import pathlib

KO = {
    "TOMMY": "토미", "GINA": "지나", "MARCUS": "마커스", "MARISOL": "마리솔",
    "EDDIE": "에디", "JESSE": "제시", "MRS. ESPOSITO": "에스포지토 부인",
    "DIEGO": "디에고", "TASHA": "타샤", "TESS": "테스", "ARTURO": "아르투로",
    "CARMEN": "카르멘", "PRIYA": "프리야", "SAM": "샘", "DR. LEVINE": "레빈 박사",
    "WHITLOCK": "휘틀록", "MS. CHEN": "첸", "MS. BROOKS": "브룩스", "LUCA": "루카", "KYLE": "카일", "OFFICER RIVERA": "리베라 경관", "KEISHA": "키샤", "DAVID": "데이비드", "MALIK": "말릭", "MICHAEL": "마이클", "KAYLA": "케일라", "AHMED": "아메드", "CALLER": "전화 속 목소리", "ZOE": "조이", "RAY": "레이", "HÉCTOR": "엑토르", "LUIS": "루이스",
}

bad = 0
for p in sys.argv[1:]:
    text = pathlib.Path(p).read_text(encoding="utf-8")
    try:
        script = text.split("## 대본", 1)[1].split("\n---", 1)[0]
        korean = text.split("## 한글 해석", 1)[1]
    except IndexError:
        print(f"{p}: missing '## 대본' or '## 한글 해석' section"); bad += 1; continue
    en = re.findall(r"^([A-ZÀ-Ý][A-ZÀ-Ý .'&-]*[A-ZÀ-Ý.]): (\S.*)$", script, re.M)
    ko = re.findall(r"^([가-힣][가-힣 .]*): (\S.*)$", korean, re.M)
    issues = []
    if len(en) != 120: issues.append(f"{len(en)} English turns (need 120)")
    if len(ko) != 120: issues.append(f"{len(ko)} Korean turns (need 120)")
    for i, ((s, _), (k, _)) in enumerate(zip(en, ko), 1):
        if s in KO and KO[s] != k:
            issues.append(f"turn {i}: {s} vs {k} (order mismatch)"); break
    long_ = []
    for s, line in en:
        for sent in re.split(r"(?<=[.!?])\s+", line):
            if len(sent.split()) > 20: long_.append(sent[:50])
    if long_: issues.append(f"{len(long_)} sentence(s) over 20 words, e.g. '{long_[0]}…'")
    if issues:
        print(f"{p}: " + "; ".join(issues)); bad += 1
    else:
        print(f"{p}: OK (120 turns, translation aligned)")
sys.exit(1 if bad else 0)
