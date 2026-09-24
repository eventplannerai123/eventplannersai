# Posting runbook — Instagram and Facebook

Exact steps for publishing a finished Reel. CLAUDE.md carries the rules;
this file carries the mechanics. If they disagree, the author's guide wins,
then CLAUDE.md, then this.

## Prerequisite: the Composio MCP server

Posting happens through **Composio**, not through any Meta SDK or raw HTTP
call. If the session has no `mcp__Composio__*` tools, it cannot post, and
no amount of instruction changes that — connect Composio first.

Check with a tool search for `COMPOSIO_MULTI_EXECUTE_TOOL`. Every call
below goes through that executor with the listed `tool_slug`.

Connected accounts:

| Platform | Composio account | Target id |
| --- | --- | --- |
| Instagram | `instagram_newing-redate` | `ig_user_id` `28308094898830663` |
| Facebook | `facebook_radius-iguana` | `page_id` `1233196746554445` ("The Event Planners AI") |

TikTok cannot be published publicly through Composio, and Instagram Trial
Reels use an in-app toggle. Both are hand-uploaded by the author.

## Step 0 — approval

**Do not start until the author has said something that clearly means go**
("go ahead", "publish", "post it"). "Looks good" is feedback on the cut,
not permission. There is no technical gate; this step is the only one.

## Step 1 — publish the file to a public URL

Meta fetches the video from a URL rather than accepting an upload, so the
cut must be in the repo and pushed first.

```
https://raw.githubusercontent.com/eventplannerai123/eventplannersai/main/reels/<YYYY-MM-DD-slug>/<file>.mp4
```

Work happens on `main` (since 2026-09-21), so that is the branch in the
URL. Posts published before that date use
`claude/wedding-timeline-reel-adcqej` in their URLs and still fetch from
it — **that branch must not be deleted**, or nine live posts lose their
video. It is identical to `main` and needs no maintenance.

Two things break a live post, neither of them branch-related: moving or
renaming a file after it has been posted, and force-pushing the branch the
URL points at. Don't do either.

Confirm it resolves before using it:

```bash
curl -sSI "$URL" | grep -E '^HTTP|content-length'
```

Renaming or moving that file later breaks the live post. Leave it alone.

## Step 2 — build the caption

Layout, in this order, with blank lines between:

```
<caption body, ending in the CTA>

AI Prompt: "<that day's prompt, verbatim>"

#tag #tag #tag #tag
```

- Hashtags carry a **literal `#`**. The Composio field docs suggest URL
  encoding; that is wrong and publishes `%23tag`.
- **Never write the label "Hashtags:"** — it pastes through into the live
  caption.
- Comment-to-unlock keywords are retired. Prompt pieces close on **"The
  full prompt is in the caption below."** **"link in bio" is not in use** —
  it is only for downloadable files, and only once the bio links to a hub
  page that holds them, which it does not yet. (This file said "link in
  bio" from 2026-09-20 until 2026-09-24; CLAUDE.md is the authority and
  says otherwise.)

Write the caption to a file and keep its md5 — Step 5 compares against it.

## Step 3 — Instagram container

```json
{ "tool_slug": "INSTAGRAM_POST_IG_USER_MEDIA",
  "account": "instagram_newing-redate",
  "arguments": {
    "ig_user_id": "28308094898830663",
    "media_type": "REELS",
    "share_to_feed": true,
    "video_url": "<raw URL from Step 1>",
    "caption": "<caption from Step 2>" } }
```

Returns a container id. Containers are **single use** — if publishing
errors, build a new one rather than retrying with the same id.

## Step 4 — Instagram publish

```json
{ "tool_slug": "INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH",
  "account": "instagram_newing-redate",
  "arguments": {
    "ig_user_id": "28308094898830663",
    "creation_id": "<container id>",
    "max_wait_seconds": 45 } }
```

**Keep `max_wait_seconds` under 60.** On 2026-09-18 a value of 300 exceeded
the MCP client timeout, the call appeared to fail, and both posts had in
fact succeeded server-side. Typical container processing is ~19s.

## Step 5 — Facebook

A separate call, never batched with Instagram, so the outcome is
unambiguous:

```json
{ "tool_slug": "FACEBOOK_CREATE_VIDEO_POST",
  "account": "facebook_radius-iguana",
  "arguments": {
    "page_id": "1233196746554445",
    "file_url": "<same raw URL>",
    "description": "<same caption>" } }
```

**Never blind-retry this one.** It has no duplicate protection. If the
result is ambiguous, read state first (Step 6) and decide from what is
actually live.

## Step 6 — read both posts back

Required by the standing brief: compare each live caption to the approved
text character for character.

```json
{ "tool_slug": "INSTAGRAM_GET_IG_MEDIA",
  "arguments": { "ig_media_id": "<published id>",
                 "fields": "id,caption,permalink,media_type,timestamp" } }
```

```json
{ "tool_slug": "FACEBOOK_GET_PAGE_POSTS",
  "arguments": { "page_id": "1233196746554445", "limit": 3 } }
```

Write the returned caption to a file and `cmp` it against the approved one
rather than eyeballing it. Em dashes and curly quotes are exactly what a
visual check misses.

Two things that look like failures and are not:

- **Facebook usually has not surfaced on the first read-back.** It is still
  processing. Re-read; do not re-post.
- **`FACEBOOK_CREATE_VIDEO_POST` returns a reel id, not a post id.** Seen
  2026-09-23: it returned `1761765678094827`, and `FACEBOOK_GET_POST` refused
  both `<page_id>_1761765678094827` ("object does not exist") and the bare id
  ("must be in full format pageId_postId"). Neither is a failure to post —
  that number is the reel id from the permalink. Read the post back through
  `FACEBOOK_GET_PAGE_POSTS` and take the `id` from the feed entry
  (`1233196746554445_122111214693449533` that day). On 2026-09-22 the
  composite form happened to work, so do not rely on it.
- **Duplicate checks go against the page feed** (`FACEBOOK_GET_PAGE_POSTS`),
  **not** `FACEBOOK_GET_PAGE_VIDEOS`. The video listing can carry entries the
  feed does not — seen 2026-09-20, where a second video-library object for
  the Sep 19 reel looked like a duplicate post and was not.

## Step 7 — record it

Update the day's `reels/<date>-<slug>/README.md` with both permalinks and
the caption-verification result, then commit and push.
