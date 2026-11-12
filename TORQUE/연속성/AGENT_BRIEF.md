# TORQUE — 집필 에이전트 작업 지시서 (Writer brief)

You are writing one Part (12 episodes) of TORQUE, an English-learning dialogue series for Korean B1+–C1 learners. Repo root: `/home/user/English`. Work only inside `TORQUE/`.

## Read first (in this order)
1. `TORQUE/시리즈_바이블.md` — the whole bible. Especially: section 1 (format rules), 2 (stage), 3 (characters, catchphrases, Korean speech styles), 4 (real-event timeline), 5 (arc), your Part's section in 6 (episode loglines, scene/turn ranges, key expressions), 7 (long-running threads), 9 (continuity notes from Part 1).
2. Style references — read fully: `TORQUE/대본/1부/1화_What_Spins_Today.md`, `TORQUE/대본/1부/8화_Poached.md`, `TORQUE/대본/1부/12화_Inauguration_Day.md`. Match their voice, header format, and footer sections exactly.
3. Any files already in `TORQUE/연속성/` for earlier Parts (`{N}부.md`) — continuity notes written by other writers. Earlier Parts may still be in progress; read what exists.

## Output
- Write episodes to `TORQUE/대본/{N}부/{E}화_{English_Title}.md` (spaces → `_`), E = 1..12, in order. Write each episode fully before starting the next.
- Header block, `## 대본`, then footer sections `## 핵심 표현 정리 (낭독하지 않음)` (10–15 items with turn numbers), `## 현안 메모 (낭독하지 않음)` (2–3 bullets on the real US issue), `## 다음 화 예고 (낭독하지 않음)`. Episode 12 also gets `## {N}부 정리 (낭독하지 않음)`.
- Exactly 150 turns, numbered 001–150: `NNN. SPEAKER: English line` then next line 4-space indent + Korean name + `: ` + natural Korean translation. Speaker labels are uppercase (e.g. SAM, WEN, GLORIA, EARL, TYLER, ERIN, LILY, STAN, VICTORIA, MINJUN). No narration or stage directions anywhere in the script — scene changes are implied by dialogue only. 3–5 scenes per episode.
- Turn length mix target: short (≤8 words) 25–30%, medium (9–15) 30–35%, longer (16–25) 20–25%, long (26–40) 15–20%. **Nothing over 45 words.** Long turns carry explanations, persuasion, memories; keep it natural spoken American English. Use the "In plain English?" device to explain jargon once or twice per episode.
- Korean translations: natural spoken Korean, consistent per-character speech style from bible section 3 (Gloria 직설 반말 "얘", Wen 건조한 존댓말, Earl 투박한 반말, Tyler 군대식 해요체, Stan 노인 반말, etc.).

## Check every episode
`python3 tools/check.py --turns=150 <file>` must print OK. Then aim for short ≤30%. Helpers:
- `python3 tools/torque_shorts.py <file>` lists short turns.
- `python3 tools/torque_apply.py <file> <dictfile>` replaces whole turns; dictfile is a Python dict literal `{'NNN': ("English", "Korean"), ...}` (put dict files in your own temp dir, not in the repo). Re-run check after.

## Story rules
- Follow your Part's loglines, dates and turn ranges in the bible; you may adjust small details if something is illogical, but record every change in your continuity file.
- Real events are background, delivered through news/TV/phone alerts/conversation; the companies and people are fictional. **Never name real politicians** ("the President", "the administration", "Washington", "Commerce", "the Chinese government"). Keep it politically balanced — employees hold different views; policies help some and hurt others.
- Facts: the bible's section 4 lists real events. For items marked ★ or anything after mid-2026, you may do a quick WebSearch to confirm what actually happened; if still unsure, keep the reference general rather than inventing specifics.
- Keep motifs alive: morning huddle "What spins today?", "Let's see if it spins.", Old Betsy, Gloria's runway board, STAN76 (meaning revealed only in 7부 10화: Stan was hired at GM in 1976), Earl's "Metal don't lie.", Lou's Diner and Donna, Wright brothers line.
- At most 3 new minor characters per episode. Reuse names already established; avoid reusing a name for a different person.

## Continuity file
Create/keep updating `TORQUE/연속성/{N}부.md` (Korean): every fact you fix that later Parts need — money amounts, dates, contract terms, new characters (name, role, speech style), who knows what, open threads, and any deviations from the bible.

## Do NOT
- Do not run any git commands (no add/commit/push). The coordinator commits.
- Do not edit `시리즈_바이블.md`, other Parts' files, or `tools/check.py`.

## When done
Reply with a short report: the 12 titles, check results (short % per episode), deviations from the bible, and the key continuity facts the next Part's writer must know.
