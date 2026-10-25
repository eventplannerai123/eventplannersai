# 2026-10-24 — Vendor deposit tracker, redone with a file

**Status: built as far as it can be. Blocked on her screen recording.**

Sat 24 Oct's second Instagram post. Replaces the Sep 3 prompt, which typed every
dollar amount and date into the chat — her note of Oct 19: no planner does that.
The Oct 15 rebuild stays up; this is a new video, not an edit of it.

## What is ready

| | |
| --- | --- |
| Voiceover, Instagram | `build/vo/instagram-vo.mp3` — 28.79s, 84 words, verbatim from the guide's Sat 24 block |
| Voiceover, TikTok | `build/vo/tiktok-vo.mp3` — 30.12s, 88 words, written here for the command-style hook |
| Caption | `build/caption.txt` — the guide's text with "Prompt below" dropped (retired Oct 12) and the prompt under its own `AI Prompt:` label |
| Scripts | `build/voiceover-script.txt` |

Both generated with ElevenLabs, voice **Vanessa - Beach Girl**
(`8DzKSPdgEQPaK5vKG0Rs`), model `eleven_multilingual_v2`. Two takes each; the
first was kept in both cases. Neither script depends on the footage, which is
why they were made before the recording exists — the standing instruction from
2026-09-24.

Loudness is **not** normalised yet. The explicit-gain + `alimiter(level=0)`
stage runs at render time against the finished mix, as on Oct 23, because
`loudnorm`'s two-pass stalls well short of −14 LUFS on Vanessa's crest factor.

## What is blocked

Her screen recording. Drive `October 24`
(`10qrEO6jeYhA7ehE3yMkd2wZOx1ylNlgA`) holds the payment sheet and the two
industry-truth JPEGs and nothing else — checked 2026-10-25 with
`mcp__Google_Drive__search_files` on `parentId`, which is the listing that
actually honours its filter.

## The demo

`Vendor Payments — March Wedding`, Google Sheet id
`1JiQVyhx72BvWMDZPTn99_KQGmOZ980oR8d8VbEwePKQ`, built Oct 19. Wedding **Sat 13
March 2027**, 160 guests, ten vendors. The point of the file is that its due
dates mix fixed dates with ones tied to the wedding date:

| Vendor | Next payment | Due |
| --- | --- | --- |
| Transportation | $1,350 balance | **Nov 1 2026** — the next one |
| Venue | $6,000 (2nd of 3) | Nov 13 2026 |
| Officiant | $500 balance | Dec 1 2026 |
| Rentals | $2,175 balance | Feb 26 2027 |
| Photography | $3,800 balance | Feb 27 2027 |
| Florist | $3,100 balance | Mar 1 2027 |
| Catering | $17,150 balance | 14 days before the wedding — **and the total moves with the final headcount** |
| Hair and makeup | $2,140 balance | Morning of the wedding |
| Band | $4,500 balance | Day of the wedding, cashier's check only |
| Stationery | paid in full | — |

Answer sanity check, from the guide: **$74,940 contracted, $28,225 paid,
$46,715 still owed.** Nine vendors still owe something; transportation is next.

## Prompt she pastes (sheet uploaded first)

> Here's the vendor payment sheet for a March 13 wedding. Today is October 24.
> List every payment still owed in date order, working out the real date for
> anything tied to the wedding date. Flag anything due in the next 30 days,
> total what's been paid and what's still owed, and tell me which balances
> could still change.

## Plan for the cut

30–45s, two cuts, TikTok first. Per the guide's format line: open on the
finished list with the Nov 1 payment highlighted, then the file upload and the
prompt, then the answer zoomed to about 85% width. Screen-in-shot rule applies.

- Hook overlay, 0:00–0:02 — "Nine vendors still owed money. The first balance is due in 8 days."
- Takeaway overlay, last 3s — "Upload the file. Don't retype it."
- Highlights via `tools/cardkit.py` `fit_highlight`, never typed coordinates.
- Crop computed from the source, not pasted; check `stream_side_data=rotation` first.
- Ad-check the **exported** mp4's bottom ~300px through to the final frame.
  Eight advertisers seen so far and the list keeps growing, so look for anything
  new rather than a known logo.
