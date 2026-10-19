# Working in this repo

This repo holds the website plus the daily Reels for **@aiforeventplanners**.
Each finished piece lives in `reels/YYYY-MM-DD-slug/` with its two cuts, the
card generator, and a README recording what shipped.

The authoritative source is the author's September guide (a .docx they
upload per session). The rules below are the parts that govern rendering
and posting, copied here so they survive between sessions — the guide
itself records that relying on a per-session upload has caused rules to be
missed. **If the uploaded guide and this file disagree, the guide wins, and
update this file to match.**

## How to reply to her (standing instruction, 2026-09-30)

She asked for this twice, so it is a rule, not a preference.

- **Be as concise as possible.** No walls of text, no restating what she
  already knows, no narrating the work. Lead with the answer.
- **Keep the technical detail out of the reply.** ffmpeg numbers, loudness
  figures, filter names and timestamps belong in the reel README and the
  commit message, not in chat. Mention a number only when she has to act on
  it or decide something with it.
- **One thing per reply. This is the rule broken most often** (her
  instruction, 2026-10-18: "tell me one thing at a time"; again 2026-10-19:
  "you are giving me way to much information at one time we discussed this
  before"). Concretely, in a normal reply:
  - **answer the question asked, and stop.** Do not append the other open
    items, the caveats, or the reasoning unless she asks for them.
  - **no tables** unless she asked to see numbers.
  - **no bulleted caveat list.** If something genuinely qualifies the answer,
    it is one sentence inside the answer, or it waits.
  - **the action list is the one next thing**, not a roundup. Carrying four
    open items forward every reply is the same failure as a wall of text.
  - Things that are done need no narration at all. A log entry, a struck
    guide line, a commit — none of that goes in the reply.

  The failure mode is always the same: the work genuinely had several parts,
  so the reply reports all of them. She does not want the report. Put the
  parts in the README and the commit message, which is what they are for, and
  tell her the one thing she has to act on.

- **End with a clear action list** — hers separated from this session's, with
  dates, **when there is genuinely more than one thing outstanding and she has
  asked for the picture.** Otherwise the last block is one line.
- **Spell out anything she has not done before**, step by step, including
  where to click. Do not assume a setting is findable just because it is
  named.
- **Always give times in Eastern** (her instruction, 2026-10-15: "always tell
  me eastern"). Never quote UTC to her, and never leave a time unconverted
  because the scheduling tool stores it in UTC. Say "6:30pm" — if the UTC
  figure matters at all, it goes in the README or the commit message.
  **Eastern is UTC−4 (EDT) until Sun 1 Nov 2026, then UTC−5 (EST).** A
  scheduled task set before that date and firing after it will land an hour
  later in her day than intended, so re-check anything standing when the clocks
  change.

## The working guide is a Google Doc (from 2026-09-30)

**"AI for Event Planners — Working Guide"**, doc id
`1x8jXHHNOOl9ipDO5u7ZEfbtiG9ABor_zrEYal56Xtrg`. It replaces the per-session
.docx, and **no local copy is kept** — read the section you need from the live
doc at the start of each task and make every update in the doc itself.

Read and write were both verified on 2026-09-30 through Composio's
`googledocs` connection (account `googledocs_malter-azoch`).

- Read with `GOOGLEDOCS_GET_DOCUMENT_PLAINTEXT`. The doc is ~87k characters,
  so the response goes to the workbench; pull out the one section you need
  there rather than into chat.
- **Never append to the very end.** The doc finishes with a bulleted list, so
  an append becomes a bullet, and deleting its text leaves an empty bullet
  behind. Insert into the right section instead.

**Cross tasks off in the doc as they are finished** (her instruction,
2026-10-12: "as you go along in the guide can you start crossing off the things
you have completed"). The guide's own Oct 1 convention: every task under YOU and
CLAUDE CODE is a checkbox, she ticks hers, and "Claude Code and Claude.ai can't
tick boxes through the API, so when they finish a task they strike the line
through and add '✅ done' with the date. A struck-through line means done,
whoever did it." So check for strikethrough before starting anything.

- `GOOGLEDOCS_REPLACE_ALL_TEXT` **cannot do this** — it only changes text, and
  the convention needs real strikethrough formatting. Use
  `GOOGLEDOCS_UPDATE_EXISTING_DOCUMENT` (batchUpdate) with an `insertText` for
  the marker and an `updateTextStyle` carrying `strikethrough: true`.
- Index ranges come from `GOOGLEDOCS_GET_DOCUMENT_BY_ID`. **Walk tables too** —
  a plain pass over `body.content` paragraphs found 851 of the doc's 1034 and
  missed the task lines entirely, because much of the guide sits in table cells.
- Per line, one batch of two requests: `insertText` at `end - 1` (before the
  paragraph's newline), then `updateTextStyle` over `start` to
  `end - 1 + len(marker)`. The marker `" ✅ done Oct 12"` is 14 units; compute it
  rather than hard-coding. Operations run in order, so the style range is
  measured against the post-insert text.
- **Do the highest index first.** An insert shifts every index after it, so
  working top-down invalidates the ranges you already measured.
- Verify by re-reading the paragraph and checking `textStyle.strikethrough` is
  `True`, not by trusting the batchUpdate reply — it returns empty objects on
  success either way.

**Strike it when it becomes true, not only when you do it.** The misses are
always the same shape: a task finishes on a *later* turn than the one that
touched it, and the moment passes. On 2026-10-14 an audit found two — the Mon 12
question of the day, struck only once she answered it two turns later, and the
Tue 13 TikTok carousel, which stayed "scheduled" until she confirmed it the next
day. So strike on the confirming message, not on the building one.

**Audit the week's blocks when she asks, and periodically anyway.** Walk every
task line in the recent day blocks and print struck/unstruck — it takes one
pass and it is the only way to catch the ones that went true quietly. Her
instruction is "as you go along", and going along includes going back.

**Only strike what actually happened as written.** On 2026-10-12 her own line
"Record the site-report screen recording — PLANNED TRIAL, upload it yourself"
was left unstruck: she recorded it, but the piece had become the event-brief
piece and she uploaded it as a regular Reel, not a trial. Half-done against a
changed brief is hers to judge. The TikTok line stayed unstruck too, because
she had only scheduled it, and **scheduled is not posted**.

**Question of the day.** Ask it at the start of every session, plus any
earlier ones still unanswered, and write her answer straight into the doc's
career content bank as a new numbered item — hook, the true story, the AI
shortcut — then mark that day's question answered with the date. Claude.ai
reads the answers from this doc, so an answer that stays in chat is lost.

**Take the next item number from the highest one in the bank, never from the
question list.** They do not line up: the bank also holds extras she adds by
hand, such as item 16 on 2026-09-30 ("They were told exactly which entrance.
They still used the wrong one."), which answers no daily question. On
2026-09-30 the bank ran 1-16, so the next item was 17 while only three daily
questions had been answered. As of 2026-10-15 it runs **1–31** (17-19 came from
her 2007 internship paper; 20-22 from her Oct 4 budget answer; 23-24 from her
Oct 4 site-visit answer; 25 from her Oct 7 runny-eggs remark; 26 she added
herself on Oct 7, "Every conference has the dry sandwich lunch"; 27-29 from her
Oct 12 staff-briefing answer; 30 from her Oct 15 senior-stakeholder answer;
31 from her Oct 15 ROI answer), so the next new item is 32.

**Never name an employer, and that includes one she names herself.** On
2026-10-15 her ROI answer opened with a company name and she said in the same
breath not to use it ("dont use the company name"). Item 31 carries the story
with the role described instead — "a corporate role running high-profile client
and broker events" — and a standing NO EMPLOYER note, because the risk is not
her forgetting, it is this session copying her words through to a caption or an
overlay. The same applies to clients: on the same day she named two principals
in conversation, and item 30 records the distinction they illustrate without
either name. **She adds items by
hand, so re-read the bank's highest number from the live doc rather than
trusting this line.**

Write the range with an **en dash**, as the bank does elsewhere ("items 20–22").
The Oct 12 entry went in with an em dash and had to be corrected.

**One answer can be several items.** Her Oct 4 answer to "the most common
reason an event budget goes over" named three distinct causes — no contingency
line, an unpriced rain plan, and year-on-year inflation — and she said so
herself: "could actually lead into 3 pieces of content". Each became its own
numbered item rather than one crowded entry, because the bank is a source of
individual pieces. Mark the question answered with the range (items 20-22).

The same happened again that day: her site-visit answer gave a firewall
question and, filed under "other", hidden venue fees — items 23 and 24. **Her
"other" items are bank material too**, even when they do not answer the
question asked.

**Check which questions are already marked answered before asking.** The Oct 1,
2 and 3 questions were all answered on Sep 30 in one sitting, so on Oct 2 the
next unanswered one was **Sun 4 Oct** — the one she asked to be given on
Sunday. A day whose question is already answered has nothing to ask.

## Everything for a post lives in one Drive folder (reorganised 2026-10-14)

Drive started on 2026-10-01 as a place for finished cuts, so she stops saving
them to a hard drive. **On 2026-10-14 the author reorganised it**: a post's
whole life now sits in one folder — her screen recordings, prompt files and
photos alongside the finished cuts. **The old Screenrecordings folder is empty
and no longer used.**

**Folders go by the date the post goes out, not the date she recorded.** The
Oct 14 recording of the annoyed-email piece lives in `October 15`, because that
is when it posts.

| | |
| --- | --- |
| Parent | `AI for Event Planners — Reels & Screen Recordings`, id `1GFs9qwlVHq6Pdo0LEX0TG5lFN4ipmtax` |
| Month | `October`, id `1gCWHchI1_mvS7eQiQmGDlp6H8P8i59Qg` |
| Days | `October 1`–`19`, `21`, `23`, `25`–`30` exist; create the rest as the schedule reaches them. `October 19` is `1wlB2Pyy8tfd5CqHIzYgWGKTe3FeE6H5-`, made 2026-10-19 with Composio's `GOOGLEDRIVE_CREATE_FOLDER` (`name` and `parent_id` — **not** `folder_name`, which is rejected), and its `parents` was checked against the month id rather than trusted from the reply, which does not include it. `October 17` is `1tqjkG8iGyX6ZMmeBti-oH09Fo1A2rtVR`, made 2026-10-17 with `mcp__Google_Drive__create_file` (mimeType `application/vnd.google-apps.folder`, `parentId` the month) — it inherits the month's link-sharing, so a file dropped in it is readable from here straight away |
| Naming | finished cuts `YYYY-MM-DD-slug-instagram.mp4` and `-tiktok.mp4`; carousel slides `YYYY-MM-DD-slug-instagram-1.jpg` … `-5.jpg` and the same for `-tiktok-`; her own files keep their own names |

**"Finished cuts" means carousel slides too.** On 2026-10-16 the runny eggs
carousel was built, approved and committed, and the Drive upload was skipped
entirely — she had to ask, "i dont see the carosel saved to the files". The
cause was this table reading as a rule about mp4s. It is not: **every finished
file for a post goes to its day folder**, slides included, and a carousel means
ten uploads, both sets. Do it as part of the build, not when asked.

She calls the parent "AI for Event Planners — Reels" in conversation; its real
title carries "& Screen Recordings" on the end. **The id is what matters** —
Drive allows duplicate names, so look a folder up rather than matching a string.

`October 1` is `1I9q3H4T29ZoMeDt72CYik_ck-oqxhDzG` and `October 15` is
`1LTWK7D8rNsRwell3OKUFUPq7K6whUsOY`; the rest are not listed here.

At the start of each month, create the month folder under the parent and its
day subfolders, and record the month id here.

**`GOOGLEDRIVE_LIST_FILES` silently ignores its `query`.** On 2026-10-14 three
different `'<id>' in parents` queries each returned the same 100 files — the
whole of My Drive — which would have supported any conclusion at all. Nothing
in the response says the filter was dropped. **Use
`mcp__Google_Drive__search_files`** instead, which honours `parentId = '<id>'`
and `createdTime > '<RFC3339>'`, and returns `parentId` per file so the answer
can be checked. `GOOGLEDRIVE_FIND_FOLDER` is fine for folders — it does return
`parents`. `GOOGLEDRIVE_GET_FILE_METADATA` does **not** return parents at all.

**So check Drive before telling her something is missing** — rule 6 of the Oct 5
video lessons. On 2026-10-14 she asked "are you sure its not already in the
folder" about footage this session had just asked her to film. It was not
there, but the first listing used to check was the broken one above.

**She does not need to paste a Drive link any more** (settled 2026-10-16, when
she asked outright: "do i stil need to copy and paste the screen recording link
from google drive each tim or are you able to grab it directly"). **She does
not.** She drops the file into the day folder and says so; this session finds
it and downloads it.

Why it works: the `October` month folder carries **`role: reader, type: anyone`**
— "Anyone with the link — Viewer" — and every day folder and every file created
inside inherits it. Verified on Oct 16 against `October`, `October 18` and her
20.6 MB screen recording in it, all three returning the same permission.

- Find it with `mcp__Google_Drive__search_files` and `parentId = '<day folder>'`.
- Download it with
  `curl -L "https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t"`.
  Check the bytes match Drive's `fileSize` and that it is not a sign-in page.
- **`mcp__Google_Drive__download_file_content` caps at 10 MB** and refuses
  anything larger, which is most recordings. The curl route has no such cap —
  20.6 MB came down whole on Oct 16.
- **If a future folder is not shared, the curl route silently returns a Google
  sign-in page instead.** Check `mcp__Google_Drive__get_file_permissions` for
  `type: anyone` before concluding a file is missing or broken, and ask her to
  share it rather than guessing.

**Use `GOOGLEDRIVE_UPLOAD_FROM_URL`** (Composio, account
`googledrive_hasty-charer`) with the cut's `raw.githubusercontent.com` URL —
the same one Meta fetches from. Drive pulls it server-side, so no bytes pass
through the session. Push to the repo first, or the URL will not resolve.

**Its field names are `source_url`, `name` and `parent_folder_id`** — not
`file_url`, and not `parent_id`. On 2026-10-04 `parent_id` was passed and
**silently ignored**: the call reported success and the file landed in the root
of My Drive instead of the day folder. A wrong `source_url`/`name` fails loudly;
a wrong parent does not. **Check `parents` in the response against the folder id
you asked for**, not just `size`. The stray copy was trashed and the file
re-uploaded.

**This session cannot move a file between Drive folders.**
`mcp__Google_Drive__update_file` takes no `addParents`/`removeParents` — the
call is rejected with "Unknown name". On 2026-10-16 she uploaded the runny eggs
photo to `Event photos` rather than the day folder and it could not be filed
from here. Renaming works; re-parenting does not. Ask her to move it in the
Drive app (long-press → Move), and treat the file as usable where it is in the
meantime.

**Do not use the inline-upload route for video.** Both the native Drive
connector's `create_file` and Composio's `GOOGLEDRIVE_UPLOAD_FILE` take the
bytes inside the call: base64 adds a third, so a 6.8 MB cut becomes 9.1 M
characters, and `GOOGLEDRIVE_UPLOAD_FILE` caps at 5 MB anyway. Every finished
cut so far is larger than that.

Verify by comparing the returned `size` to the local file. Started 2026-10-01
with the vendor quotes pair, both exact.

## Render rules

- **1080x1920, ratio exactly 0.5625.** Verify with ffprobe before calling an
  export finished; never leave raw screen-recording dimensions.
- **Check `stream_side_data=rotation` before planning any crop on a phone
  clip.** On 2026-10-07 both of her conference clips reported 1920x1080 and read
  as landscape, which would have meant a 608-wide centre slice upscaled 1.78x.
  They carry `rotation=-90` and decode as 1080x1920 — already the output frame.
  `-show_entries stream=width,height` alone is misleading for anything shot on a
  phone.
- **Compute the crop from the source, don't reuse numbers.** Height =
  width / 0.5625, and set the y-offset so the status bar and the red
  recording dot fall off the top while the ChatGPT input bar stays at the
  bottom, where the platform UI covers it anyway. A y-offset of 0 leaves
  the recording dot in frame. For the usual 1206x2622 iPhone capture that
  is **`crop=1206:2144:0:478`** — 478 off the top, nothing off the bottom.
  Those numbers hold only for a 1206-wide source; a different device
  silently breaks them, so recompute when the capture size changes. The
  guide's duplicate `:0:0` rule was deleted on 2026-09-21, so this is now
  the only crop rule — but it is still compute-from-source, not a fixed
  string to paste blindly.
- 30 fps out, H.264 high, CRF 19, `+faststart`, AAC 192k at 48 kHz.
- **Voiceover to -14 LUFS.** Measure the source with a loudnorm first pass
  and feed the measured values back in, rather than a single dynamic pass.
- The screen recordings carry a silent audio track. The voiceover is the
  only audio.
- **Generate both voiceovers here — standing instruction from 2026-09-24.**
  The author used to record the Instagram one herself and leave the TikTok
  one to this session; she asked for both to be generated from now on. Use
  ElevenLabs, voice "Vanessa - Beach Girl" (`8DzKSPdgEQPaK5vKG0Rs`). Neither
  script depends on the footage, so both can be made as soon as the day's
  script is settled, before the recording exists.
- **Check the day's script length before generating.** The guide's per-day
  scripts have twice run short for a 40-50s day — 66 words on Sep 24 and 64
  on Sep 26, about 25s, which would leave ~20s of silence. Target roughly
  2.55 words per second of finished cut and extend the script by narrating
  what the output actually shows, as the Sep 24 rewrite did.

## Video lessons from Oct 5 (the guide's own, apply to every video)

Added to the guide on 2026-10-05 as six standing rules. They replace several
things below rather than sitting alongside them, so read this block first.

1. **Every video needs sound that tells the story** — an ElevenLabs voiceover
   (Vanessa, standard settings), or, for an overlay-led piece, overlays that
   carry the whole story alone. **This ends the silent quick piece.** The Oct 6
   cancellation piece was built silent to the old spec and she said it "made no
   sense without sound"; the guide was rewritten the same day.
2. **Tell it in order: the prompt first as the setup** (what she asked, zoomed
   on the question), then the key lines of the answer, then the biggest
   takeaway as a big overlay at the end. **Never cut the prompt — "a video
   without the original prompt makes no sense" (Sahiba, Oct 5).**
   **This file had this rule backwards from Oct 5 to Oct 10**, recorded as
   "open on the biggest takeaway, not on the prompt", which is its opposite.
   Re-read from the live guide on 2026-10-10 and corrected. Nothing was
   mis-built on it — the Oct 6 rebuild opened on the prompt because her brief
   said so, and the Oct 7 piece had no prompt to show — but it would have
   wrecked the next quick piece. **Read rule 2 from the guide, not from
   memory.**
3. **Zoom: every highlighted line fills about 85% of the width, in the middle of
   the frame. Freeze frames, never scrolling footage.**
4. **Safe zones for TikTok and Reels: nothing important in the top 12%, the
   bottom 25%, or the right 15%**, where the app's tabs, caption and buttons sit.
5. **Clean every screen recording**: crop off the phone status bar (time, red
   recording dot) and the app's input bar, and cut any ad that appears in the
   answer.
6. **Check before assuming.** Look at the calendar, the live accounts or Drive
   before saying something is undone, open or still to post.

   **Rule 6 covers asking her for things, not just reporting on them** (her
   instruction, 2026-10-19: "You should always look first before asking me").
   On Mon 19 Oct she was asked to edit `IMG_0853` and replied "I don't have
   that photo. What are you talking about" — the filename had been copied
   out of the guide without looking it up. It was in her Drive the whole
   time, in `Event photos`, and one `GOOGLEDRIVE_FIND_FILE` call found it.
   Worse, the next message asked *her* to open it and say whether it was the
   right shot, which is the same failure twice.

   So before handing her any task that names a file: **find the file, open
   it, and look at it.** Only then say what is needed, and say it in terms
   of what is actually in frame. A filename from the guide is a pointer, not
   a thing she will recognise.

   **And where the task can be done here, do it rather than hand it over**
   (her instruction, 2026-10-19: "You can do it on your own"). The same day,
   told the photo needed its branding removed, she was asked whether she
   wanted to do it in ChatGPT — she did not. **De-branding her photos runs
   from here**, with ElevenLabs `creative_edit_image` (`gpt-image-2.5-sunburst`
   for a reference-driven edit): create a flow, `creative_create_asset_upload`
   → PUT the bytes → `creative_finalize_asset_upload` with the `flow_id`, then
   edit with that node as `connect_from`. Pick the best of the four variations
   here rather than making her choose.

   The guide's YOU lines assign work on the assumption this session cannot do
   it. Where that assumption is now wrong, **take the task**, and tell her what
   was done rather than what is needed from her.

   **This does not touch the posting rule.** Nothing is published without her
   explicit go-ahead, ever, whatever else this session does on its own.

Two honest notes on applying these, from the build they came out of:

- **85% of the width is often a reduction, not a magnification.** When the
  answer text runs nearly the full width of the capture — which it usually does
  — those lines already occupy about 96% of the frame, and no crop can enlarge
  them without clipping words. What makes a line read as zoomed is **isolating**
  it: lift the passage onto its own panel and throw the rest of the frame out of
  focus hard. At a light blur the same sentence stays legible behind the panel
  and the frame looks like two copies of itself.
- **Rule 2 makes the opening-shot check matter more, not less.** The cut opens
  on the prompt, so the recording still has to show it. A recording that starts
  after the send tap is still a problem, and the sent prompt bubble is usually
  the better frame to open on anyway — it holds the whole prompt, where the
  input box holds only the first few lines.

## Timing rules

- **Everything is 15-20s from Oct 1.** The October plan sets one target for
  every piece. A day's brief still overrides it, but no piece is long by
  default any more.
- **The length test is over — it measured nothing.** It ran Sep 23-30 on
  named days (short: 23, 25, 29; long: 24, 26, 30) and the October plan
  dropped it: short days averaged 25 views and long days 23, but both sat
  inside a decline that halved reach mid-test, so the comparison is
  worthless. At three Instagram posts a week it would be three against
  three, which is not enough either. Recorded so it is not re-run in the
  belief it was never tried.
- **The 6-second payoff ceiling was never part of the length test** and is
  unaffected by dropping it. It applies to every piece at every duration.
- **Time to payoff must stay under 6 seconds** — everything before the
  reveal, combined. This is a hard ceiling from real watch-time data and is
  the rule most often missed. The Sep 12 reel shipped at 6.5s and broke it.
- The generating section needs a **visible beat of 2.5-3s minimum**, sped
  to 2-3x, about 4 seconds. **This is what gets sacrificed first when the
  setup is crowded, and it shows.** On Sep 29 a four-beat setup - prompt,
  lawn plan, empty hall, generating - left each beat about a second under
  the 6-second ceiling, and the author said the piece "flips to the rain
  plan floorplan way too fast". The fix is to drop a setup beat, not to
  shave the generating one: three beats at a readable speed beat four
  flashing past. Check what the reveal itself already says before keeping a
  setup shot - that day's diagram was captioned with the indoor dimensions,
  so the empty-hall shot was redundant.
- If the real generating phase runs much longer than that and is visually
  static, take a **representative slice** rather than compressing the whole
  thing, and say so in the reply.
- Hold the reveal at normal speed so it is readable. A freeze on the final
  frame is fine; a long silent tail is not, so prefer the lower end of the
  duration range when the voiceover is short.

## Structure and overlays

- **Two separate cuts every time**, never one file posted twice. Instagram
  takes the narrative hook; TikTok takes a genuinely different command-style
  hook ("Stop doing X") and slightly different pacing.
- **Build the TikTok cut first.** Round 6 briefs say so outright: TikTok is
  the primary discovery platform now, so its cut is not a derivative of the
  Instagram one.
- Footage in motion from frame one. **Never open on a static title card.**
- Only two text overlays: the hook at 0:00-0:02 and the end card. **No
  rolling mid-video captions** — transcription-synced captions were tested
  and made retention worse.
- **Round 6 (Sep 23-30) dropped the end card**: every brief in it said "end on
  the output itself, not an end card asking for a comment". The October
  plan's six Instagram briefs continue this — each specifies a hook overlay
  at 0:00-0:02 and nothing else. The two-overlay rule is the written default;
  in practice every current brief overrides it down to one.
- **The quick-piece format was rewritten on 2026-10-05** and is no longer
  silent. It is **15-20s**: open on the prompt as the setup (0:00-0:04, zoomed
  on the question, with an overlay saying what was asked), then 2-3 key lines
  of the answer as zoomed, highlighted freeze frames, then the biggest takeaway
  as a big overlay at the end. A **30-40 word voiceover this session writes
  from the takeaway**, shown to her with the edit. No scrolling, no end card.
  The caption's first line states the takeaway, then the full prompt as typed,
  then four hashtags, no CTA. **A quick piece gets one cut, not two** — but
  that cut is no longer TikTok-only. Under the Oct 12 daily rule every TikTok
  also goes to Instagram, and on 2026-10-15 the annoyed-email quick piece was
  scheduled as the evening's **second Instagram post**, the same file and the
  same caption, hashtags included, posted from here to Instagram and Facebook
  after the day's main piece. So: one cut, three platforms, TikTok by her hand
  and the other two from here.
- **Never post both cuts to the same platform** — near-identical posts
  split engagement.
- Hooks must name a concrete scenario, number or timeframe immediately.
  Abstract superlatives and vague teases both measured badly.
- Prefer broader "event" framing in the opening hook line even when the
  demo content is sector-specific ("a $85,000 event just wrapped", not "a
  $85,000 corporate summit"). Say "event planner", not "wedding planner",
  in general self-identification. Neither overrides genuinely
  wedding-specific content, hashtags or research scope.
- **Transformation is a hypothesis, not the house format** (downgraded by the
  October plan, 2026-09-28). A messy real input visibly becoming a structured
  output on screen. It was written in on 2026-09-20 off three posts — 83, 110
  and 155 reach — and every transformation piece since has gone 28, 19, 16,
  13, 8. The pattern did not hold. Keep making them, because they are good
  pieces, but **stop treating the format as the explanation for anything**,
  and do not enforce a quota of them.
- **The build-story format is the one being tested now.** The best Instagram
  post of the week by a distance was the coloring book build story — 90 views,
  79 reach, against a weekly average of 29. Not a demo: a personal, honest
  account of making something, including what went wrong. The AI-makes-mistakes
  piece is what tests whether it repeats; it **moved from Wed 7 to Fri 9** and
  Headcount moved to the following week.
- **"B-roll of real work" means the artefact the piece is about.** The Oct 7
  build used her conference footage — an empty ballroom, a corridor, a drinks
  table — and she rejected it: "No this isn't good content." The execution was
  fine; the footage was generic, and a build story is personal by definition.
  When a piece is about a seating chart, a floor plan or a budget, the footage
  has to show **that artefact**. Check what the voiceover is about before
  accepting whatever footage is to hand, and say so rather than building it.
- **No more than two wedding-specific pieces in any seven.** The account is
  "event planner", and Round 5 drifted to four weddings in a row.
- Use only the author's uploaded footage. No stock, no generated visuals.
  Their own output files (a floor plan PNG, say) are fine when they send one.
  **An AI edit of her own photo is not a generated visual** — the guide itself
  specs those edits (the Event Photo Shortlist carries an EDIT line per file),
  and from 2026-10-19 they run from here rather than from her. The rule bars
  substituting invented imagery for her real work; it does not bar removing a
  logo from a photograph she took.
- **Branding: look at the whole frame, not just the obvious piece.** On
  2026-10-19 the shortlist's edit line for `IMG_0853` covered only "the wall of
  portraits and all lettering", and the frame also carried a client-branded
  runner down the front of the check-in table and a named room sign above the
  door. The client's name is as barred as the employer's, so an edit line out
  of the shortlist is a starting point to be checked against the actual
  picture, never a complete spec.
- **Her raw footage never goes into this repo. The repo is public** — the
  `raw.githubusercontent.com` URLs Meta and Pinterest fetch from only work
  because it is — so committing source media publishes attendees' faces, a
  named venue and any third-party branding in frame. Only finished cuts belong
  here. `.gitignore` carries the rule as of 2026-10-07, after a commit of her
  conference b-roll was correctly blocked as an out-of-place publication; it had
  been staged purely to give Drive a URL to fetch from, which is not a good
  enough reason.
- **So raw source cannot be filed to Drive from here.** The upload-from-URL
  route needs a public URL, and the inline routes are base64 — a 1.5 MB photo
  becomes 2 MB of characters and `GOOGLEDRIVE_UPLOAD_FILE` caps at 5 MB and
  wants an `s3key` rather than a path. **Finished cuts still upload normally**,
  because those are committed. Anything else she wants archived in Drive, she
  adds from her phone.

## Posting

**Cadence from Oct 1 (October plan, written 2026-09-28).** Daily Instagram
posting is over.

| | Frequency | Days |
| --- | --- | --- |
| Instagram | **3 a week** | Mon, Wed, Fri — plus Thu Oct 1 to start |

**The guide's day-by-day table governs, not the Mon/Wed/Fri shorthand.** Week
one is Thu 1, Sat 3, Mon 5, Wed 7 — so **Fri 2 Oct has no Instagram Reel at
all**, and Sat 3 is an extra single photo (the Future of AI pinned post), which
the guide says is placed on a Saturday precisely so it does not take a
Mon/Wed/Fri slot. Read the day's row before assuming a weekday is a posting
day.
| TikTok | daily | every day |
| Facebook | whatever this session posts | automatic |
| Pinterest | 2 pins a day | from Fri Oct 2 |

Why: Instagram reach fell every day of the week to Sep 28 — 79, 38, 28, 19,
16, 13, 8, averaging 29 against 53 the week before. Five weeks of daily
posting with almost no engagement is the likeliest cause. TikTok over the
same week averaged 77 views and grew 62 to 73 followers against Instagram's
281 to 284: twice the reach and three times the growth on a quarter of the
base.

**DECIDED 2026-10-12: back to daily. The test failed.** Deduplicated weekly
viewers went **203 (7 posts) to 64 (3 posts)** — down 68% against a post count
down 57%, and per-post reach fell too, 29.0 to 21.3. Called two days early
because the second week carried zero feed posts and could not change it.

The mechanism, which is the part worth keeping: the baseline week's seven posts
summed to 201 and its deduplicated weekly figure was 203 — **the same number**,
so their audiences barely overlapped. Reach on this account is **additive in
posts**. Posting less can only concentrate an audience that is doubling up, and
this one never was.

It does not follow that daily was working: reach fell 79 to 8 across the
baseline week itself. Volume and per-post decline are two separate problems and
this test only measured the first. **Full write-up in
[`docs/OCT-CADENCE-TEST.md`](docs/OCT-CADENCE-TEST.md).** She is updating the
guide's cadence section; re-read it before planning a week.

**The decision rule is pre-registered in
[`docs/OCT-CADENCE-TEST.md`](docs/OCT-CADENCE-TEST.md)** — written 2026-09-30,
before any data existed, because the plan says "if reach has not improved"
without saying improved against what, and the two candidate baselines (201 and
371) are not equivalent tests. Read that file on Oct 14 rather than
re-deciding what counts as a pass. Two things it fixes that are easy to get
wrong: the baseline is **201**, and the metric is Instagram's **deduplicated
weekly accounts reached**, never the sum of per-post reach.

Honest caveat worth repeating rather than burying: reach was already sliding
before the change, so a recovery cannot be cleanly attributed to posting less.

**Posting time: the day's main post goes out in the MORNING, around 9am**
(her instruction, 2026-10-16: "in general we know that 9am is optimal or early
morning"). **6:30pm is only for a day's second post** — "i think we should only
test the 6:30 time when 2 posts are scheduled that day", same message. So a day
with one Instagram post is a morning post, full stop.

**The morning-vs-evening test is CLOSED, unrun**, on the morning of its day 1.
Her rule ends it rather than narrowing it: the pre-registration excluded second
posts, so if 6:30pm only ever carries a second post, the evening arm can never
be filled and there is nothing to compare. The Fri 16 Oct post was moved from
6:30pm to 9:10am that morning. **Do not re-open it, and do not replace it with
a 9am-vs-11am version** — this account cannot resolve anything under about
1.37x at 14 posts an arm, and two hours inside one consensus band will not
differ by 37%. The full reasoning, and the pre-registration kept unedited
beneath it, are in
[`docs/POSTING-TIME-TEST.md`](docs/POSTING-TIME-TEST.md).

She is right on the substance: morning is the **only** thing the published
research agreed on for a B2B audience, and 9-11am is already where 61% of the
account's 56 posts went. Research in
[`docs/POSTING-TIMES.md`](docs/POSTING-TIMES.md): the published studies
contradict each other on nearly everything else. What is **not** established is
that evening would have lost — it was never measured, so do not claim it was.

**Facebook cannot be measured at all.** It deprecated reach and impressions
in its API in November 2025, it has 7 followers, and every reaction on every
post is the author's own. Keep posting there because it costs nothing —
but **do not report on it** and do not spend manual time on it.

**Who posts what — the author restated this on 2026-09-24 and it has had to
be said more than once, so read it before assuming a piece is yours:**

| Goes out as | Who posts it |
| --- | --- |
| **Anything to TikTok** — the day's cut, the back catalogue, anything a brief calls a "repost to TikTok" | **The author.** Build the file, hand it over with its caption, never upload it. |
| **Anything that is a Trial Reel** | **The author.** Edited in the Claude.ai chat, uploaded with the in-app toggle. |
| Instagram feed Reels and Facebook | This session, after explicit approval. |
| An Instagram **repost** on a trial day | This session in principle — but ask first. Sep 27's was cancelled outright. |

The wording in a brief does not change this: what matters is the platform
and whether it is a trial, not how the line is phrased. **The author is
re-editing the guide as of 2026-09-24 because its Round 6 blocks are
confusing on exactly this point** — two reposts filed under one day, trial
and non-trial posts described in adjacent paragraphs. Until the new guide
lands, treat anything ambiguous about a second post as hers and ask.

Never post without explicit approval in the conversation. Build both cuts,
show the Instagram one, ask, and wait.

This rule is the only thing standing between a draft and a live account.
A PreToolUse hook used to force a permission prompt on every publishing
call; the author had it removed on 2026-09-17, preferring to give the
go-ahead in conversation. So nothing mechanical stops a post now.

**There is no technical gate.** The PreToolUse hook was removed on
2026-09-17 at the author's instruction and has not been replaced, so
nothing mechanical stops a mistaken publish and a live post cannot be taken
back. Do not re-add the hook unless the author asks for it.

**Never publish without her explicit go-ahead in the conversation.**

**The standing rule is post when she says, not post whenever.** Wait for
words that clearly mean go: "go ahead", "publish", "post it". "Looks good"
or "great" is feedback on the cut, not permission — ask.

**Step-by-step mechanics, including exact tool slugs and arguments, are in
[`docs/POSTING.md`](docs/POSTING.md).** Posting runs through the Composio
MCP server; a session without `mcp__Composio__*` tools cannot post at all.

- **Instagram** — Composio account `instagram_newing-redate`, `ig_user_id`
  `28308094898830663`. **The guide agrees as of the 2026-09-29 revision**,
  which also explains the discrepancy that ran from Sep 25 to Sep 28: the
  `17841441013925532` it used to carry is the legacy business-account ID
  that appears inside Insights URLs, and is not what you call the API with.
  Both numbers are real; only this one works. Create the container with `media_type: REELS` and
  `share_to_feed: true`, then publish with a generous `max_wait_seconds`.
  Containers are single-use; on a processing error build a new one.
- **Facebook** — Composio account `facebook_radius-iguana`, page_id
  `1233196746554445` ("The Event Planners AI"), now recorded in the guide
  too. **`FACEBOOK_CREATE_VIDEO_POST` takes `file_url` and `description`** —
  not `video_url`, which is rejected with "At least one of 'video' or
  'file_url' must be provided" (2026-10-15). That is a 400 before anything is
  created, so fixing the field and calling again is not a blind retry; a
  *blind* retry is one after a call that may have succeeded. Never do that —
  it duplicates posts. It has taken three read-backs
  and about fifteen minutes to surface in the page feed on every day from
  Sep 25 to Sep 28; that is normal, not a failure.
- **TikTok is the main platform — and still a manual upload.** (138
  average views per video against Instagram's 53, on a fifth of the
  followers.) Composio cannot publish publicly to TikTok, so **hand over
  the TikTok cut every single day** and never attempt to post it. It is the
  platform that actually reaches people, so its cut is not an afterthought
  to the Instagram one.
- **The split, stated plainly (author, 2026-09-24): anything going to
  TikTok is hers.** Not just the day's TikTok cut — the back-catalogue
  uploads and every item a brief labels "repost to TikTok" too, whatever
  the wording. This session builds those files and hands them over with
  their captions; it never uploads one. **Reposts to Instagram are the
  opposite and do run from here** — the Sep 27 and Sep 28 repost days are
  the only case. So when a day's brief lists a second post, read which
  platform it names before assuming it is this session's work.
- Facebook has 7 followers and is not yet a platform. Still post there, but
  do not read anything into its numbers.
- **Hashtags go on every Instagram caption, always — trials included, and
  anything she uploads by hand** (author, 2026-10-15, verbatim: "Hashtags go on
  every Instagram caption, always — including trials and anything I upload by
  hand. They don't help a trial in its first 72 hours, but they count once it's
  shared to everyone. Stop telling me to drop them, and update your own notes
  to match."). The four are
  `#aiforeventplanners #eventprofs #eventplanningtips #eventplanner`.

  **This reverses what this file said from 2026-09-28 to 2026-10-15** — that a
  trial day's Instagram caption carries none, because a trial is kept off
  hashtag pages. The reasoning was half right and the conclusion was wrong: the
  tags do nothing during the 72-hour trial window, but a trial that clears 100
  views gets shared to everyone, and from that moment they work like any other
  post's. She has had to say this more than once, so **do not suggest dropping
  them again, on any caption, for any reason.** She has reworded the guide's own
  line to "still include them every time".

  Facebook was never the exception — it is never a trial, so it has always taken
  the ordinary caption: body, blank line, `AI Prompt: "..."`, blank line,
  hashtags.
- **A trial day is a Facebook day, and that post runs from here** (author,
  2026-10-12: "update the guide so that anyday theres a trial reel you will
  post to facebook"). The guide's own Oct 1 Facebook rule used to except
  "posts Sahiba uploads herself, such as Trial Reels and Stories"; the trial
  half of that exception is gone, and only Stories are left. So on a trial
  day the Instagram upload is hers and the Facebook post is this session's,
  with the hashtag-bearing caption.
- **But read the Page feed before every Facebook post.** The in-app "Also
  share to Facebook" toggle is on for her own uploads. On 2026-10-12 her
  manual Instagram upload of the event-brief piece appeared on the Page as a
  reel **12 seconds later**, carrying her Instagram caption verbatim — so
  Facebook was already done and a post from here would have duplicated it.
  Facebook has no duplicate protection and a live post cannot be taken back,
  so `FACEBOOK_GET_PAGE_POSTS` first, then decide from what is actually live.
  The guide has said since 2026-08-30 not to rely on that toggle — Meta
  decides whether the cross-post lands as a real video, a plain feed post or
  a bare cover image — so it is a reason to check, never a reason to skip.
- **A trial IS visible to the API, and `is_shared_to_feed` is how you tell**
  (settled 2026-10-15). On a `REELS` item that field is `true` for every Reel
  posted from here and **`false` for exactly the two planned trials** — Oct 12's
  event brief and Oct 14's AV piece, and nothing else in the account. That is
  what a trial is: published, but kept off the grid and the followers' feed.
  Request it explicitly; it is not in the default field set.

  **This corrects a wrong call made earlier the same day.** Seeing both pieces
  in `INSTAGRAM_GET_IG_USER_MEDIA`, this session concluded the toggle had not
  been used and told her two planned trials had gone out as ordinary posts. She
  pushed back — "why is it a problem, they went out as trials" — and she was
  right. The claim rested on a line in `docs/TIKTOK-POSTED.md` saying trials do
  not appear in that endpoint, which was extrapolated from a **Story** that was
  missing on Oct 10. A Story expires and is a different object; it says nothing
  about trials. The media edge lists what the account has published, and a
  trial is published — only its *distribution* is restricted.

  So: **the media edge proves nothing about trial status on its own.** Check
  `is_shared_to_feed`, and when it matters, ask her. Do not tell her a post
  went out wrong on the strength of an inference the API can settle directly.

- **Trial Reels are manual: the Sep 27 and 28 trials do not come through
  here.** Both are planned Instagram trials, edited in the Claude.ai chat and
  uploaded by the author. **Do not post them.** If their content turns up in
  this session, stop and say so rather than building or publishing anything.
- **But each trial day also has a second post, and that one does come through
  here.** Sep 27 and 28 each carry an Instagram **repost** — Sep 3's vendor
  payment schedule and Sep 2's seating chart — posted as a normal feed Reel
  through Claude Code as usual.
  **Sep 27's was cancelled by the author on 2026-09-24** ("skip sunday all
  together"), after the distinction between the trial and the repost was
  put to her. Sep 27 therefore has nothing in it for this session. Sep 28's
  repost has not been cancelled, but do not assume it is on either — ask
  before building it. A trial reaches only non-followers, so on a
  trial day the 280 followers see nothing in feed and nothing lands on the
  grid; the repost reaches a separate audience and the two do not compete.
  **Re-export the file rather than re-using the original byte for byte**, or
  duplicate detection can throttle both copies, and space it several hours
  from the trial upload.
  Generally: the Trial toggle is in-app only, so a trial cannot be
  published from here — only regular feed Reels can. Never post the same
  piece as both a regular Reel and a Trial Reel: that trips Instagram's
  duplicate-content detection and throttles both for up to 30 days. Only
  label a day "Trial Reel" after it has actually been posted as one.
- **A Reel posted from here cannot carry music** (settled 2026-10-16, when she
  asked "it goes out with music?"). Instagram's licensed audio library is
  in-app only. Checked against the live tool schema rather than from memory:
  `INSTAGRAM_POST_IG_USER_MEDIA` has exactly one audio-related field,
  `audio_name`, and it only *labels* the track ("default: 'Original Audio'") —
  it attaches nothing. **Whatever audio is in the mp4 is what goes out**, so a
  silent file is a silent Reel.

  That makes the choice explicit on any silent piece: ship it silent, add a
  voiceover here, or let her upload it in the app with a trending track — and
  only the third gets music, at the cost of it no longer running from here.
  Say so plainly rather than letting a silent file go out unremarked.

  Note the genuine tension with the Oct 5 video lessons: rule 1 allows a silent
  piece "for an overlay-led piece, overlays that carry the whole story alone",
  and the Oct 4 bar-quantities cut is exactly that. So silence is not
  automatically a rule break — but she said of the Oct 6 piece that it "made no
  sense without sound", so raise it every time rather than deciding alone.

- Meta fetches the video from a URL, so push the cut to this repo first and
  pass its `raw.githubusercontent.com` URL. Moving or renaming that file
  later breaks the live post.
- **Caption layout: caption body, blank line, `AI Prompt: "..."`, blank
  line, hashtags.** The AI prompt always goes in the caption so the post
  stands on its own without the video.
- Pass hashtags with literal `#`. The Composio field docs suggest URL
  encoding; that is wrong and would publish `%23tag`.
- **Never write the label "Hashtags:".** Hashtags go on their own line
  starting with `#`, unlabelled. The label used to paste through into live
  captions and had to be deleted by hand.
- After publishing, read both posts back and compare the live caption to the
  approved text character for character.

## CTA

**Never write "Comment [KEYWORD]."** Comment-to-unlock is retired — nine
keywords across the series returned zero comments between them.

- **RETIRED 2026-10-12: do not write "Prompt below."** Her words: "we dont
  need to say prompt below its redundent". She is right — the prompt sits
  directly underneath, under its own `AI Prompt:` label, so the line points at
  something already in view. Captions now go straight from the body to the
  prompt block.
  **Captions already published keep their original wording**, as always; this
  is for new ones. The guide still carries "Prompt below" in its per-day caption
  blocks, so strip it when copying a caption out of the guide until she has
  edited those.

  The history, kept because it shows the direction of travel: the line was
  shortened guide-wide on 2026-09-28 from "The full prompt is in the caption
  below", which appeared
  18 times in the Sep 27 guide and zero times in the Sep 28 one, replaced by
  "Prompt below" in all 16 places. The standing-rules line was changed to
  match, so this is a deliberate edit rather than drift. The point is
  unchanged - the AI prompt sits in the caption body, so the piece is
  self-contained without the video. **Captions already published keep their
  original wording**; do not go back and edit live posts.
- **"link in bio" is available again from 2026-09-28** and is still only for
  **downloadable files**. It was blocked while the bio pointed at the single
  tablecloth product; the bio now points at the Gumroad profile page,
  `aiforeventplanners.gumroad.com`, which holds them. Prompt pieces — most
  of the schedule — still end "Prompt below." instead, because the prompt is
  already in the caption body and there is nothing to download.

The guide keeps the old keyword list as a record of what was tried, so the
mechanic is not reintroduced without knowing it already failed nine times.

**What has actually gone up on TikTok is tracked in
[`docs/TIKTOK-POSTED.md`](docs/TIKTOK-POSTED.md), not in a schedule line.**
Uploads are hers and nothing reports back, so a day's plan records only what was
*meant* to run. On 2026-10-04 two pieces were offered to her as unposted on the
strength of repo notes and both were already live. She now sends one line when
she uploads; record it there, and **never call a piece unposted without checking
that file.**

## TikTok back catalogue (added to the guide 2026-09-23, corrected same day)

**12 of 39** Instagram pieces have never been posted to TikTok, verified
against the full 31-video TikTok catalogue. These are **not reposts** — the
TikTok audience has genuinely not seen them. One goes up per day as a second
post alongside that day's scheduled piece. All manual uploads, so they never
publish from here.

Most of the twelve are carousels: TikTok did not support carousels when they
ran, so they had nowhere to go. That changed, and the first TikTok carousel
went up on Sep 22, which is what makes the backlog postable at all.

- **`#theeventplannerai` is dead** — it points at an account name that no
  longer exists. Swap it for `#aiforeventplanners` wherever the old handle
  appears in the original caption.
- Strip any comment-to-unlock CTA. The Sep 13 centerpieces caption still has
  one. Open questions ("what's the pettiest seating conflict you've had?")
  stay — those are conversation prompts, not a keyword gate.
- Excluded on purpose: the Aug 23 poll carousel (it points at a Story poll
  that no longer exists) and the Aug 30 tablecloth carousel (the
  swipe-to-zoom version of the same content went to TikTok on Sep 22).
- Three links in the guide are still placeholders — the Sep 8 photography
  carousel, the Sep 14 floor plan and the Sep 20 vendor contract. Find them
  on the profile grid by date.
- **The back catalogue ends Sat 3 Oct.** The October plan schedules the last
  three: Sep 14 floor plan (Thu 1, strip the retired LAYOUT keyword), Sep 20
  vendor contract (Fri 2, strip REVIEW), Sep 22 coloring book build story
  (Sat 3). After that every TikTok day is either an Instagram piece's cut or
  one of the five TikTok-only quick pieces.
  **All three are now up** (author, 2026-10-05: "All are posted"), so the back
  catalogue is finished and nothing is left in it.
- **Not to Instagram, not yet.** A second Instagram feed post competes with
  that day's main post for the same small pool of reach. Followers went 271
  to 280 over the fortnight these ran, so the same people would simply see it
  twice. Revisit when the count has roughly doubled.

**How the first version of this list got it wrong**, recorded because the
failure mode is easy to repeat: it listed 15 pieces and 11 of them were
wrong. The TikTok list endpoint returns 20 videos per page and the second
page was never fetched, so the catalogue was incomplete; the "missing" list
was then built by fuzzy word-overlap against captions of very different
lengths. Page the endpoint to the end, and match on something stronger than
word overlap.

## The paid guide and the four templates (added 2026-09-24)

`@_eventguide` — the account whose awards-night post was the model for the
comment-to-unlock experiment — has launched a paid product for the same
audience: a per-event Claude project setup, four document templates, prompt
workflows and instructions.

**The four document templates are the blocker.** Event brief, project plan,
budget, run of show — the four Sahiba actually works from, named Sep 8 and
still unbuilt. Two things wait on them: the Round 6 awards-night piece
promises the pack as its deliverable, and any paid guide would be built
around them.

## Pinterest (added to the guide 2026-09-28, started 2026-09-29)

A separate account and a separate workstream: `@calmbeforetheaisle`, business
account, for the coloring book only. Nothing to do with `@aiforeventplanners`.
**Full working detail is in [`pinterest/README.md`](pinterest/README.md)** —
board ids, the Drive folder, the schedule CSV. The parts that govern:

- **Two pins a day, never a batch.** Twelve at once on a new account reads as
  automated. Two a day for a fortnight takes it from 6 pins to about 30,
  which is the minimum volume Pinterest responds to.
- **It does not need this repo.** `PINTEREST_CREATE_PIN` takes the image bytes
  via `media_source image_base64`, so there is no push-then-fetch step the way
  Instagram and Facebook have. Composio account `pinterest_reking-alpha`.
- **Pin creation works; pin editing does not.** `PINTEREST_UPDATE_PIN` returns
  "does not have access to this restricted feature: `pin_edit`". That is the
  app's access tier, not anything session-specific, so a wrong board or a
  typo is permanent. **Check every argument before the call, not after.** The
  guide's worry that trial-level access would block creation outright was
  tested on 2026-09-29 and did not happen.
- **Outbound clicks is the only number that matters.** Baseline over two
  weeks: 137 impressions, 16 pin clicks, **0 saves, 0 outbound clicks** — and
  133 of the 137 impressions landed on one day, Sep 22, Pinterest's initial
  distribution test. The creative is fine (11.7% tap rate). Nobody clicks
  through, which points at the descriptions; and nobody saves, which matters
  more than it sounds, because **on Pinterest saves are distribution**, so a
  pin with no saves never gets redistributed.
- **No ad spend.** Paying for impressions at a zero outbound-click rate buys
  a larger version of zero. The threshold for revisiting is one organic
  outbound click.
- Review **Tue 14 Oct**. If outbound clicks are still zero after ~30 pins
  across four boards, the problem is the offer or the price rather than the
  marketing, and Pinterest goes on the back burner rather than getting money.
- Links carry `?utm_source=pinterest&utm_medium=social&utm_campaign=<sampler
  |book>&utm_content=<file stem>`. `campaign` is the product, because the
  question worth answering is whether the 99c sampler beats the $5.99 book.
  **The guide says the tag makes traffic "identifiable in Etsy's own stats"
  and that is wrong** — Etsy reports "Pinterest" as a source and nothing
  finer. The author knew and kept the tags anyway: they cost nothing and
  become readable if pins ever point at Gumroad or an owned page.

## Practical gotchas

- **Aim for ~25 seconds of raw footage per recording.** That gives enough
  generating time to compress into a real 3-4 second ramp and enough reveal
  to fill the hold at natural speed. Shorter sources (~12-13s) force
  tradeoffs across duration, ramp and pacing at once.
- **The upload ceiling is ~30 MB, NOT a number of seconds.** Measured
  across every clip uploaded this month: the largest that succeeded was
  29.7 MB, and source bitrates range from **0.96 to 2.68 MB/s - nearly
  3x**. So a duration rule is actively misleading. At ~25 MB:
  screen recordings (1.0-2.1 MB/s) give 12-25s; camera video in HEVC
  (~2.6 MB/s) gives only **9-10s**. Always quote a size, and work out the
  seconds from that clip's own bitrate.
- **Never route uploads through email.** Mail attachment caps are
  typically 25 MB - *tighter* than the chat's ~30 MB - so a clip that
  would have uploaded fine gets bounced, sliced smaller, and bounced
  again. Sending from the phone straight into the chat removes both the
  round trip and the tighter limit.
- Shooting at **1080p/30** rather than 4K/60 roughly halves the camera
  bitrate, and a 1080x1920 30fps Reel discards the extra anyway.
- When clips do need splitting, ask for overlapping takes saved with
  "Save as New Clip". Frame-match the overlap to find the seam, then
  concatenate.
- **Uploads must be sent at "Actual"/"Original" size.** The default
  compressed size produces visibly soft footage.
- **Google Drive works here, and not in the Claude.ai chat.** That is the
  distinction the 2026-09-29 guide revision drew, and it explains the old
  "blocked" note: the Claude.ai chat has no Drive tools and an allowlisted
  network, so files for *that* chat must still be uploaded directly, while
  Claude Code can fetch from Drive freely. The author changed this session's
  network policy on 2026-09-24 and it has been used daily since.
  Download with
  `https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t`.
  The file must be shared **"Anyone with the link - Viewer"**; a
  Restricted file returns a Google sign-in HTML page, not the video, and
  `curl` will happily save that page as an .mp4. Check the response is
  `content-type: video/mp4` before trusting it.
  **This retires the ~30 MB ceiling for anything routed through Drive** -
  the first file this way was 40.6 MB, well past what the chat takes. So
  no more splitting a clip into overlapping takes, and no more seam
  matching, unless the author prefers the chat. Send full-length
  recordings via Drive.
- **A pasted image is not a file.** Images dropped into a message may render
  without landing in the uploads directory. Check for a real path before
  planning to use one.
- **Her phone photos are HEIC, and nothing here decodes them out of the box.**
  `ffmpeg` reports "moov atom not found" (it reads the container as MP4) and
  ImageMagick refuses with "Unsupported codec". The fix is one line:
  `python3.13 -m pip install pillow-heif`, then `pillow_heif
  .register_heif_opener()` and open it with PIL as normal. Do that rather than
  concluding a photo cannot be viewed — on 2026-10-19 the first attempt gave up
  after ffmpeg and ImageMagick both failed, and asked her to look at it
  instead.
  Her stills come off the phone at **3024x4032**, so downscale before reading
  one into the session.
- **Check the reveal for the Adobe Acrobat banner ad and trim around it.**
  It scrolls up into the bottom of frame during long scrolls. Verify this
  **visually** on bottom-strip frames — on 2026-09-21 a red-pixel detector
  reported a cut clean while "Adobe Acrobat ... Ad" was plainly legible in
  it, because the logo fades in and the colour test passed the faded frame.
  A false all-clear is worse than no check.
- Check the full raw footage for other in-app ads before finalising the
  reveal.
- **Ad-check the finished export, over the whole frame — not a crop of the
  source.** On 2026-09-24 a bottom-620px crop of the raw clip read clean at
  the chosen cut point, and the exported reel still carried the ad's lead
  line on its last frame: once the 2144-tall crop is scaled to 1920 that
  source crop stops about 20px short of the frame bottom. Scan the bottom
  ~300px of the actual mp4 through to its final frame. A crop that misses the
  last few rows gives the same false all-clear a colour threshold does.
- **Ads seen so far are not one banner. SEVEN advertisers**: Adobe Acrobat
  (Sep 21), Adobe Firefly (Sep 22), Rillion "AI for Accounts Payable"
  (Sep 23), Cambridge "Event Florals in NYC" (Sep 24), Turning Stone "Make It
  Easier" (Sep 25), **Fever "Private corporate events" (Oct 4)** and **FELFEL
  "Book a Free Tasting — office meals stocked daily" (Oct 16)**. Do not search
  for a known logo — look for anything new at the bottom of the reveal.

  Two corrections worth keeping, because the list's whole point is that it
  keeps growing and an undercount weakens it:

  - **Fever was missed here for twelve days.** It was found and written up in
    `reels/2026-10-04-bar-quantities/README.md` on the day, and never copied
    into this list. A find recorded only in a reel README does not survive into
    the next build — **add it here too**.
  - On 2026-10-16 this list was updated to "six advertisers" on the strength of
    its own five entries plus FELFEL, without checking the reel READMEs. It was
    already seven. Count from the records, not from the line above.

  The Oct 16 one is also a reminder that an ad can sit at the very **end** of a
  recording rather than partway through, so scan to the final frame.
- **"Save as New Clip" splits are not always frame-matchable.** On 2026-09-24
  three clips of the same answer turned out to be separate scroll passes: best
  whole-frame match across the overlaps was MAD 13.4 and 18.6, and last-frame
  to first-frame 21.0 and 17.7 against a control of 28.2 — no true match
  anywhere. That is not a blocker. A dense page of text throws a large MAD for
  even a one-line scroll offset, so check contiguity by **reading the text**
  at each boundary instead; a seam of a line or two reads as ordinary
  scrolling.
- **The note below still stands in full.** It was marked superseded on
  2026-10-05 on the strength of this file's own mis-reading of rule 2 — "the
  cut now opens on the takeaway, never on the prompt". The guide says the
  opposite, so the opening shot matters as much as it ever did. Un-superseded
  2026-10-10.
- The recording is supposed to start with the prompt sitting in the input
  box and the send tap on camera. Three recordings have begun after the tap
  (the third on Sep 25, where the author said to run with it). Flag it
  rather than faking an opening. **But check before assuming it is missing
  again** - the Sep 29 recording opened exactly right, prompt in the box with
  all three files attached and the tap at ~0.7s, and the first build started
  at 7.00s and threw it away. The author spotted it: "Why is the ChatGPT
  prompt not the first thing we see". Look at the first two seconds of every
  source before choosing a cold open.
- **The hook card's usual y=620 is not automatic.** It is placed to avoid
  whatever the frame is showing at 0:00-0:02, and that changes per day: on
  Sep 23 it covered the send button at y880 and moved to 620; on Sep 29 it
  landed on the prompt text - the one thing that opening exists to show - and
  moved to **y=1300**, which sits over the keyboard, carries no information,
  and still clears Instagram's own bottom furniture. Look at the opening
  frames, then pick the y.
- **Never type highlight coordinates by hand** (author, 2026-10-14: "tighten up
  the yellow highlights some times they have been off"). They were being read
  off a y-ruler on a contact sheet and typed in, which is eyeballing: on Oct 14
  both boxes on one beat landed on body text, and it was only caught after a
  full render. Use **`tools/cardkit.py`**:
  `fit_highlight(frame, seed_y, lines=N, up=M)` finds the real text lines in the
  frame, picks the one at `seed_y`, takes `N` of them, and snaps the box to the
  actual ink — so the edges follow the glyphs instead of a guess.
  - **Count lines, do not grow through blank rows.** An earlier version expanded
    until it hit a gap of N blank rows. That cannot work: on the same capture
    the leading inside a heading is 18 rows and inside a body paragraph 33, so
    any one threshold either splits a heading or swallows the next block. The
    caller knows how many lines it means; the frame knows where they are.
  - **Look at `preview()` before rendering.** It composites every overlay onto
    its own beat frame. That is the check that catches a misplaced box without
    burning an export — the Oct 14 mistake survived until the finished mp4
    because this step did not exist.
  - Still verify the hook and the highlights on the **exported** frames too. The
    preview catches placement; the export catches the `repeatlast` class of bug.
- **A single-frame PNG overlay needs `repeatlast=1`.** Feeding a hook card
  straight into `overlay` with `eof_action=pass:repeatlast=0` shows it on
  frame one and then drops it — the Sep 25 first build shipped with no hook
  at all and the filtergraph looked correct. Use
  `eof_action=repeat:repeatlast=1` with an `enable=between(t,0,2)` window,
  and **verify the hook on the exported frames**, never from the command.
  (The Sep 26 script builds the card as a timed stream instead, which is
  also fine — that export was checked and does render.)
- **Leave ChatGPT's floating scroll-to-bottom button in frame** (author,
  2026-10-10: "you dont need to blur it"). It sits around y 1772-1892 of the
  output, inside the bottom 25% that TikTok's caption covers. Both removals
  are worse than the button: a boxblur patch over black-on-white text reads as
  a censor smudge, and cropping above it (source y 2205) forces the width from
  1161 down to 1062, which clipped the "K" off "Key rule" on Oct 10. She had
  asked for it gone on Oct 6; this supersedes that.
- **`alimiter` undoes its own limiting unless you pass `level=0`.** Its
  `level` option (auto level) defaults to true and renormalises the output
  back to full scale, so the audio clips at 0.0 dBFS however low `limit` is
  set. This looks exactly like the limiter not working.
- **`loudnorm` cannot always reach -14 LUFS.** When a voiceover's crest
  factor is high the filter's true-peak ceiling binds first: on Sep 25 the
  measured two-pass result stalled at -15.8 LUFS with TP pinned to -1.5, and
  raising the offset moved it 0.6 dB. When that happens, apply the gain
  explicitly and let `alimiter` (with `level=0`) catch the peaks. Still take
  the first-pass measurement — it is what the gain is computed from. Always
  confirm by measuring the finished export.
