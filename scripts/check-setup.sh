#!/usr/bin/env bash
# Verify a working session has everything it needs. Safe to re-run.
fail=0
ok(){ printf '  ok    %s\n' "$1"; }
bad(){ printf '  FAIL  %s\n' "$1"; fail=1; }

echo "Tools"
for t in git ffmpeg ffprobe python3; do
  command -v "$t" >/dev/null 2>&1 && ok "$t $(command -v $t)" || bad "$t not on PATH"
done
python3 -c "import PIL" 2>/dev/null && ok "python pillow" || bad "pillow missing (pip install pillow)"

echo "Repo"
if git rev-parse --git-dir >/dev/null 2>&1; then
  ok "git repo"
  b=$(git rev-parse --abbrev-ref HEAD)
  [ "$b" = "claude/wedding-timeline-reel-adcqej" ] \
    && ok "on branch $b" \
    || bad "on branch '$b' - expected claude/wedding-timeline-reel-adcqej (main has no reels or CLAUDE.md)"
else
  bad "not a git repo - clone it, do not work in a loose folder"
fi

echo "Rules"
for f in CLAUDE.md docs/POSTING.md; do
  if [ -f "$f" ]; then
    git ls-files --error-unmatch "$f" >/dev/null 2>&1 \
      && ok "$f (committed)" \
      || bad "$f exists but is UNTRACKED - it was recreated, not checked out. Fix the branch instead."
  else
    bad "$f missing - wrong branch"
  fi
done

echo "Location"
case "$(pwd)" in
  *OneDrive*) bad "working inside OneDrive - it locks files mid-render. Move to C:\\dev\\" ;;
  *) ok "not inside OneDrive" ;;
esac

echo
[ $fail -eq 0 ] && echo "All checks passed." || echo "Some checks failed - fix before working."
exit $fail
