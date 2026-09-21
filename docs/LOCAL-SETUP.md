# Setting up a local session (Windows)

What went wrong on 2026-09-21, so it doesn't repeat:

| What happened | Consequence |
| --- | --- |
| The folder was not a git repo, and git was not installed | No clone, no push, **no way to publish** — Meta fetches the video from a URL, and the URL comes from pushing to this repo |
| The working files live only on `claude/wedding-timeline-reel-adcqej`; `main` holds just the website | A default clone looks empty — no CLAUDE.md, no reels |
| CLAUDE.md was recreated from scratch by the new session | Two diverging copies of the standing rules |

Composio was fine. **Git was the linchpin**, and it is the one thing that
cannot be worked around: without a push there is no public URL, and without
a public URL nothing can be posted.

## Before the first session

**1. Install Git for Windows** — <https://git-scm.com/download/win>

Take the defaults. It brings Git Bash (every script here is bash) and Git
Credential Manager, which handles the GitHub login on first push.

**2. Install ffmpeg and Python**

In PowerShell:

```powershell
winget install Gyan.FFmpeg
winget install Python.Python.3.12
```

Then, in a **new** terminal so PATH is picked up:

```bash
pip install pillow
```

Pillow is what the card generators use. ffprobe comes with ffmpeg.

**3. Clone the repo — NOT inside OneDrive**

```bash
cd /c/
mkdir -p dev && cd dev
git clone https://github.com/eventplannerai123/eventplannersai
cd eventplannersai
git checkout claude/wedding-timeline-reel-adcqej
```

**Do not work in `OneDrive\Desktop\...`.** OneDrive syncs while ffmpeg
writes, locks files mid-render, and uploads every intermediate frame and
10-30 MB export. `C:\dev\` or any unsynced folder is fine.

**4. Check it before starting work**

```bash
bash scripts/check-setup.sh
```

It verifies the branch, the tools, and that CLAUDE.md is the committed one.

## Starting the session

In the Claude Code desktop app, **before sending the first message**, set
Environment to **Local** and pick `C:\dev\eventplannersai`. Those controls
are fixed once the first message is sent — a running session cannot be
converted, which is why today's could not be switched.

Confirm with `pwd` in the first message:

- Local: `/c/dev/eventplannersai`
- Still cloud: `/home/user/eventplannersai`

## The one rule that keeps the rules intact

**Never let a session write CLAUDE.md from scratch.** It is committed; if
it appears missing, the checkout is on the wrong branch. Fix the branch,
don't recreate the file. The same goes for `docs/POSTING.md`.

## What local actually buys

Full recordings read off disk — no ~26s upload ceiling, no split clips, no
frame-matched seams, no jump cuts covering a missing middle. That is the
whole benefit. Everything else is equal, and posting still needs a push.

## Known rough edge

`reels/*/build/render.sh` carries absolute paths from the cloud scratchpad.
They are a record of what produced each cut, not portable scripts — expect
to repoint the input paths when reusing one.
