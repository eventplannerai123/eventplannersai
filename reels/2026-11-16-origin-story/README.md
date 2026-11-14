# Mon 16 Nov — the origin story: 3,500 name tags, coded by guest type

Reel, 6:30pm Instagram and Facebook; TikTok at 9am from the file she posts
herself. Content bank 11, her origin story — the first time AI saved her real
time, so it is a personal piece rather than a demo.

## What the answer did

She recorded it on Sat 14. The answer took **1m 27s** and came back complete:

| | |
| --- | --- |
| Original registrations | 3,500 |
| Duplicate registrations removed | 112 |
| Final registrations | 3,388 |
| Organisation names standardised | 35 variations corrected (96 spellings of 61 names) |
| Missing guest-type codes | 0 |
| Codes | DEL 2,540 · SPO 510 · SPK 96 · STF 162 · VIP 80 |

Every figure matches the file the demo generator built and asserted, so the
piece is making a true claim on screen. It also wrote an Excel workbook and a
CSV with four worksheets including an audit trail, which the brief did not
ask for.

**She uploaded the export as a 53-page PDF, not the Google Sheet.** It cost
about a minute of "Extracting text from registration PDF" and "Inspecting and
Repairing Truncated PDF Records" — the whole middle of a 127-second
recording — and it still came back right. Worth knowing before Tue 17's BEO
redo, which is a PDF by design.

## The twist, and it is hers

Confirmed 2026-11-14. The answer codes every row by the guest type the
attendee **picked at registration**, and a badge has to say what someone is
doing **on site**: a sponsor who is also speaking needs SPK, not SPO. Anyone
with two roles is still a check by hand. The last voiceover line, the end
card and the caption's second paragraph are built on that, which is what the
brief asks for.

## Build

- **It opens on the payoff, not the prompt**, because the Mon 16 brief says
  "open on the finished, coded list, not the upload". That inverts the Oct 5
  rule 2 for this piece only, and a day's brief overrides. The prompt is the
  second beat and the whole of it is in the caption, so nothing is hidden —
  and the 6-second ceiling is satisfied at frame one.
- **The whole prompt is in the sent bubble, not the input box** — the
  opposite of Fri 13. By the time she sends it the box has scrolled to the
  back half, so b1 comes from the loading phase.
- One highlight, on b2, fitted with `cardkit.fit_highlight` from a seed y and
  **baked into the frame**: every beat carries a 4% push, so an overlay added
  after the concat would drift off the line.
- Cards are opaque. Both land on dense black text and show through at 243.
- Eryn, `eleven_v4`, 19.44s from 59 words — 3.03 w/s, in line with the 3.1
  planning figure. Raw came out at **-24.6 LUFS**, and the sweep landed at
  **+14.0 dB** into `alimiter=limit=0.841:level=0` for -14.0 LUFS on the
  finished export. Never carry a gain figure over.
- `elevenlabsusercontent.com` is egress-blocked here, so the mp3 was routed
  through Drive and the staging copy trashed afterwards.
- No music bed: a piece with a voiceover does not take one.
- No BUDGET line. The brief says so, and the Nov 3 soft mention covers Thu 5,
  Mon 9, Tue 10 and Tue 17 only.

Exports: 1080x1920, 30fps, H.264 high, CRF 19, +faststart, AAC 192k/48kHz,
19.44s both cuts, -14.0 LUFS measured on each. Hook and end card verified on
the exported frames, not just in the preview.

## Approved, filed and scheduled

She approved it on Sat 14 ("approved"), two days early, the same day she
recorded it.

- Drive `November 16` (`1mij0zABAvcy7QT7Ronw3cglG8nmG93wo`) — both cuts,
  uploaded from **commit-pinned** raw URLs with each returned `size` checked
  against the local file.
- Instagram and Facebook at **6:30pm Monday**, one-shot task
  `trig_0124njsgPQjeVY9se4eLnMey` (23:30 UTC).
- TikTok handed over the moment she approved, per her Oct 30 rule, after a
  clear last-10 duplicate check.
