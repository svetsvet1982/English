# TORQUE — 문체 다듬기 지시서 (Style revision brief)

The user's feedback: too many turns are just lists of words or strings of very short sentences. Your job is to revise ONE Part's 12 episodes so the dialogue reads as connected, natural spoken English with real sentences — without changing the story.

## Measure
`python3 tools/torque_style.py -v <file>` prints `STYLE OK` / `STYLE FIX` and lists flagged turns:
- **CHOPPY** — a turn made only of short fragments ("This page. Operating loan. Six hundred and forty thousand dollars. Seven point four percent.")
- **TINY** — a turn of 1–3 words ("Who makes them?", "Tell me.")

Pass targets per episode: **choppy ≤ 12, tiny ≤ 7, average sentence ≥ 8.5 words**. Every episode must reach `STYLE OK`.

## How to rewrite
- Join fragments into full sentences with connectors and clauses: because, so, which, who, when, while, although, if, until, that's why, the thing is, what I mean is, I don't think…, you'd think…, relative clauses, participle phrases.
- Fold a list into one sentence with a verb: "Men and trucks. It's the same in Ohio." → "It's always men standing around trucks, and honestly, it's the same back in Ohio."
- A tiny reply becomes a real reply that still sounds spoken: "Who makes them?" → "Who makes those motors, and why do you keep buying them if they die every winter?"
- "This page. Operating loan. Six hundred and forty thousand dollars. Seven point four percent." → "This is the operating loan we signed in March, six hundred and forty thousand dollars at seven point four percent."
- Questions in pieces ("What about the government money? The bridge payments?") → one question: "What about the government money, the bridge payments everyone keeps talking about?"
- Keep it spoken American English, B1+–C1, not written prose. Contractions stay. Don't turn everyone into a lecturer; vary length.
- **Keep on purpose** (these may stay short): catchphrases — "What spins today?", "Let's see if it spins.", "Copy that.", "Metal don't lie.", "Runway.", "Noted." — and a few emotional peaks/cliffhangers per episode. That's what the 12-choppy / 7-tiny allowance is for.
- Do not change facts, names, numbers, dates, who says what, plot order, or any line that other episodes quote (e.g. letters, emails, testimony exhibits, Victoria's texts). If a line is a quoted document, leave it.

## Rules
- Same turn count (150), same numbering, same speaker on each turn. Rewrite whole turns only; never merge or delete turns.
- Update the Korean translation of every turn you change: natural spoken Korean, same character speech style as before (Gloria 반말 "얘", Wen 건조한 존댓말, Earl 투박한 반말, Tyler 해요체, Stan 노인 반말…).
- No turn over 45 words. After editing, `python3 tools/check.py --turns=150 <file>` must still print OK (it needs ≥15% turns of 8 words or fewer — keep enough natural short replies).
- Leave the header block and the footer sections alone, except: if a 핵심 표현 entry cites a turn whose wording you changed so the expression disappears, keep the expression in the new wording or update the entry.
- Edit with `python3 tools/torque_apply.py <file> <dictfile>` (dict literal `{'NNN': ("English", "Korean"), ...}`). **Put every dict/temp file only in your own folder** `/tmp/claude-0/-home-user-English/ca7470d4-4515-5e13-b997-8c1bc52fe74b/scratchpad/style_partN/` (N = your Part), names prefixed `sN_`. Other writers work in parallel; never use a shared filename.
- Do not run git. Do not touch other Parts, the bible, or tools.

## Done
For each episode: `STYLE OK` and check `OK`. Reply with a table of before/after numbers (choppy, tiny, avg sentence) per episode and anything you deliberately left short.

## Addendum — avoid mechanical joins (coordinator, after spot checks)
Don't glue fragments with a connector that doesn't fit. Bad: "Don't ask, and the motors die from moisture, dust, and cold, so I replace six…" / "We should go, because Janine's coming at two…". Good: "Don't ask. The motors die every winter from the moisture, dust and cold, so I end up replacing six or seven a year." Use `because` only for a real cause, `so` only for a real result. Two or three real sentences in one turn are fine — the goal is full sentences with verbs and normal clauses, not one long chain. Aim for an average sentence of about 9–13 words; if an episode is above ~14, you've probably over-joined.
