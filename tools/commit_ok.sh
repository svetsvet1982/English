#!/bin/bash
# Stage only episode files that pass tools/check.py, then commit and push.
cd "$(dirname "$0")/.." || exit 1
git config core.quotepath false
find 대본 -name '*.md' -print0 | xargs -0 -n1 python3 tools/check.py 2>/dev/null | grep ': OK' | sed 's/: OK.*$//' | tr '\n' '\0' | xargs -0 -r git add
git diff --cached --quiet && { echo "nothing passing to commit"; exit 0; }
git commit -qm "${1:-Update episodes}

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01MXuWsD1EKu9NdxrMhKF3jY"
git push -q origin claude/affectionate-carson-2o31dj 2>&1 | tail -2
git log --oneline -1
