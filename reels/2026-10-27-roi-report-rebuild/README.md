# 2026-10-27 — Rebuild 1: the Sep 1 post-event ROI report

Tue 27 Oct's 6:30pm Instagram Reel. The first of the four rebuilds by number,
the last to actually get built, because its master went missing for a week.

## The hook

Approved by Sahiba on 2026-10-16 ("2 is good"):

> **If you didn't define success before the event, you can't prove it after.**

It replaces *"A $85,000 corporate summit just wrapped, and leadership wants
proof it was worth it."* The brief's own diagnosis: that opening is a
hypothetical, which breaks the true-moment rule, and "proof it was worth it" is
abstract for a first line. The new one is her own sentence, from her answer to
the rebuild question.

**NO EMPLOYER, anywhere.** Her answer named one and she asked in the same breath
for it kept out — of the piece, the caption and the overlay.

## Where the master came from, after two dead ends

| Source | What it is | Verdict |
| --- | --- | --- |
| This repo | — | The Sep 1 piece predates it |
| Drive `October 27` | the packing list only | Not there |
| Instagram's own CDN | **720x1280**, 19.5s, 871 kbps | **Rejected** |
| **Her upload, 2026-10-26** | **1206x2144, 60fps, 19.5s, 4.76 MB** | **Used** |

The CDN route does work — `INSTAGRAM_GET_IG_USER_MEDIA` for the `media_url`,
then `GOOGLEDRIVE_UPLOAD_FROM_URL` to pull it server-side past the egress
block — and the file it returns is in `October 27` as
`2026-09-01-roi-report-INSTAGRAM-CDN-720.mp4`. It is two-thirds the resolution
and a second-generation encode, and this piece is a **screen recording**, so an
upscale would soften every letter in it. A rebuild exists to measure whether a
new hook moves skip rate; a softer picture moves watch time on its own and
ruins the only number the experiment is for.

**The URL announces the resolution before you download it.** Its `vencode_tag`
reads `xpv_progressive.INSTAGRAM.CLIPS.C3.720`. Read that and skip the fetch.

**Her file is better than the posted version, not worse.** 1206x2144 is the
native crop of the screen recording — one step before the export that went out
— and it is the exact 0.5625 ratio, so 1080x1920 comes out of it by a clean
downscale. 60fps halves to 30 without resampling.

## The edit

| | |
| --- | --- |
| Splice | **3.03s**, inside the master's own 2.864–3.204 silence, so the opening sentence is replaced whole rather than cut mid-word |
| Opening frame | **t=10.00s** — the cost-breakdown table, with the $85,000 total and the $567 cost per attendee on screen. The rebuild rules say open on the finished result, not the typing |
| Opening length | VO + 0.30s |
| Card | cy=560, where the original's sat, so the one visible change is the words |
| Everything after 3.03s | the original edit, rescaled to 1080x1920 and 30fps and nothing else |

**The opening frame is frozen, and the first build got that wrong.** It fed
`-ss 10 -i SRC` straight into `tpad`, which does not freeze anything — it plays
the master from 10.00s, and the body replays that same stretch seconds later.
The viewer would have watched one scroll twice. The frame is now extracted to a
PNG and looped.

## Loudness is matched to the master, not to −14 LUFS

The master runs **−21.45 LUFS** and the body has to stay as it was or the
control is gone, so the new opening line is brought to the master's level
instead of the house target. The Oct 15 rebuild did the same and shipped at
−21.2 against its master's −21.3.

## Two cuts, and the reason is the voice change

The voice changed to Eryn on Oct 25, mid-rebuild. A rebuild replaces only the
opening line, so an Eryn opening on a Vanessa body means the voice changes three
seconds in — audible, and not something the experiment is testing.

- `roi-report-rebuild-eryn.mp4` — her standing instruction, which named this
  piece explicitly.
- **`roi-report-rebuild-vanessa.mp4` — the one that ships.** One voice
  throughout, matching the body.

**She picked Vanessa on 2026-10-26: "make the whole thing vanessa its too
noticable".** She heard the switch straight away, which settles the general
rule as well: a rebuild keeps the voice of the piece it rebuilds, and Eryn is
for anything built fresh. Nothing else differs between the two files.

## Caption

`build/caption.txt`. Per the rebuild rules it is the original caption with its
first line swapped for the new hook, and `#theeventplannerai` — a dead handle —
replaced by `#aiforeventplanners`. The prompt block and the closing question are
untouched.

## Filed and handed over, 2026-10-27 morning

| | |
| --- | --- |
| Drive `October 27` | `2026-10-27-roi-report-rebuild-instagram.mp4`, id `10XQPOIa9RshM81xaZ_Eo7jjaozB1zWk7`, 8,255,494 bytes — `parents` checked against the folder id, not trusted from the reply |
| TikTok | handed to her at 6:55am Eastern with the caption pasted into the message |
| Instagram + Facebook | 6:30pm Eastern from here, on her Sun 25 approval |

**The TikTok file is the same file, and that is the honest answer rather than
the tidy one.** Her Tue 27 block asks for "CC's TikTok cut of the ROI rebuild
with the same caption". The last two rebuilds each got a genuinely separate
TikTok cut — Rebuild 4 spliced the Sep 26 piece's own **TikTok master** at
3.78s against the Instagram master's 3.70s — because those masters were in the
repo. **The Sep 1 TikTok master is not, anywhere this session can reach**: not
in the repo, not in Drive `October 27`, and Instagram's CDN only serves the
Instagram cut. So there is nothing to splice a TikTok variant out of.

That matters more here than it would elsewhere, because CLAUDE.md records that
the Sep 1 piece's two cuts are "paced differently in the middle, not just at the
hook". A TikTok cut built from the Instagram master would therefore not be the
Sep 1 TikTok edit with a new hook — it would be the Instagram edit. Handing over
the Instagram-derived file is the same thing with one less pretence, and the
Oct 19 girls-at-the-door piece already set that precedent: one file, same
caption, both platforms.

**She was not asked for the TikTok master.** She is on a plane until Wed 28, the
piece ships tonight either way, and the rule is to look first and only ask when
the answer changes something. If she wants the TikTok edit rebuilt properly
later, the master is the one thing needed.

**Duplicate check before the hand-over**: the last 10 TikToks are nothing but
Oct 16–25 pieces, newest the Sun 25 second-column post. No ROI piece among them,
so the file is safe to upload. TikTok also had no post on Mon 26.
