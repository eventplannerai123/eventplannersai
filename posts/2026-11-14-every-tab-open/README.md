# Sat 14 Nov — "Every tab open on my laptop at 2am before load-in"

Planner-life post 2 of 4 (content bank 34). Instagram and Facebook get the
still held 8 seconds under a generated instrumental; TikTok gets the same image
as a photo post, by her hand, with the caption pasted into the message.

| | |
| --- | --- |
| Instagram / Facebook | `every-tab-open-instagram.mp4`, 1080x1920, 8.00s |
| TikTok | `slides/every-tab-open.jpg`, the same frame |
| Caption | identical on all three, `build/caption.txt` |

## A row of tabs is a column on a 9:16 frame

The guide asks for "one image styled as a row of browser tabs". Eight tabs
side by side across 1080px gives each one about 120px, which fits no tab title
at all, so rendering the brief literally would have produced eight unreadable
slivers.

What a reader recognises as *my tabs* is the tab shape, the favicon dot and the
close cross — so they are stacked inside a browser window, and the shape does
the work a horizontal strip does on a laptop. Each tab came out 107px tall at
34px type.

**The last tab is the active one, and that is the whole AI tie.** Seven tabs are
the job; one is doing the boring part. ChatGPT is the only tab in full white
with the purple accent bar.

## The list is the guide's default, not hers

Her Sat 14 YOU line asks for her real 6 to 8 tabs by Thu 12 and says CC uses
the list below if she does not send them. She has not, so this is the default.

Swapping it is one edit to `TABS` — the layout fits whatever it is given and
asserts 6 to 8 of them. **Ask again before Friday evening**, because that is
when the file goes to her for the 9am TikTok.

## Nothing named

A real 2am tab bar would carry the venue, the client and the event in three
different titles. None of them is here: "Floor plan — v4", not the room's name;
"quick question" — Inbox (1)", not who sent it.

## The bed

Upbeat, per her Nov 10 instruction, and deliberately **not Friday's**: electric
piano and a bouncing synth bass with a hi-hat and handclap pulse, against
Friday's guitar and marimba. Two Reels a day apart on the same track would read
as one piece of stock music, which is exactly what she caught on Wed 11.

Instrumental proved rather than assumed — the spectrogram is regular hi-hat
transients over harmonic low bands with no vocal formant movement, and Scribe
returned an empty string. Its own settings said "Instrumental: False", which is
why the settings are not the check.

**It needed +0.2 dB, not +12.** This generation came out far hotter than the
others — +2.0 dB measured -12.6 LUFS, where Friday's needed +3.4 to reach -14.
The sweep ran +2.0 down to -1.8 and back in to +0.2, which measured **-14.0
LUFS, -1.1 dBTP** on the finished export. The lesson is the standing one: sweep
and measure, never carry a gain figure over from the last piece.

**Both raw beds came out 618,514 bytes**, which looked like Drive having served
a cached copy of Friday's. It had not — the md5s differ. Two 25.03s mp3s at the
same constant bitrate are simply the same size, and the checksum is what
settles it.

## Checks

- 6 to 8 tabs asserted; the active tab asserted to be the last one.
- No "prompt", "link in bio", "Gumroad" or "Comment" in the image text or the
  caption.
- Tab height asserted at 60px minimum so the titles stay readable; it came out
  at 107px.
- Brand system is the guide's: lavender #CECBF6, deep purple #3C3489, Poppins,
  EP + star wordmark drawn as a polygon because Poppins has no U+2726 glyph.
- TikTok safe zones: the title starts at y=250, clear of the top 12% (230), and
  the wordmark sits above the bottom 25%.
- Export probed at 1080x1920, 8.00s, 30fps, and measured at -14.0 LUFS.
