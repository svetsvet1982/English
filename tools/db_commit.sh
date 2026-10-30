#!/bin/bash
# DEEP BACKGROUND: stage episode files that pass the 150-turn check plus the continuity memo, then commit and push.
cd "$(dirname "$0")/.." || exit 1
git config core.quotepath false
find DEEP_BACKGROUND/대본 -name '*.md' -print0 | xargs -0 -n1 python3 tools/check.py --turns 150 2>/dev/null | grep ': OK' | sed 's/: OK.*$//' | tr '\n' '\0' | xargs -0 -r git add
git add DEEP_BACKGROUND/연속성_메모.md DEEP_BACKGROUND/시리즈_바이블.md tools/db_commit.sh 2>/dev/null
git diff --cached --quiet && { echo "nothing passing to commit"; exit 0; }
git commit -qm "${1:-Add DEEP BACKGROUND episode}

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01CehbhUTyWKYbFsdtPRecQf"
for i in 1 2 3 4; do git push -q origin claude/keen-allen-fpsmp3 2>&1 && break; sleep $((2**i)); done
git log --oneline -1
