# The three-a-week test — decision rule

**Written 2026-09-30, before any data from the test exists.** That is the
point of it: the rule is fixed while nobody has a stake in the answer, so on
Oct 14 the number gets read rather than argued with.

Nothing in this file is a prediction. It is only what counts as which result.

## The rule

**Metric.** Instagram Insights **weekly accounts reached**, the 7-day figure
Instagram reports. Not the sum of individual post reach.

**Baseline: 201** — the week to Sun 28 Sep (79, 38, 28, 19, 16, 13, 8).

**Weeks measured:** Thu 1 – Wed 7 Oct, and Thu 8 – Wed 14 Oct.

| Result | Decision |
| --- | --- |
| Both weeks beat 201 | Keep three a week. |
| Neither week beats 201 | Back to daily. Three a week is not the answer and the constraint is something else. |
| One of the two beats it | Hold three a week and run two more weeks. Do not decide on a split. |

That is the whole rule. Read the number, find the row, do what it says.

## Why 201 and not 371

The week before the baseline week averaged 53 a post, so roughly **371**.
Both numbers are real, and the plan does not say which one "improved" means.
They are not equivalent tests:

- Three posts beating **201** need about **67 reach each**. Demanding — the
  best post of the last fortnight got 79 — but reachable.
- Three posts beating **371** need about **124 each**. **No post in the
  series has ever done that.**

So 371 is not a test, it is a guarantee of failure. 201 is the honest bar, and
it is already a hard one. Recorded here so the softer-looking number is not
quietly swapped in later either.

## The number cannot be pulled from here (established 2026-10-12)

**Only Sahiba can read it, in the Instagram app.** Tried on Oct 12, a day
before the second week closes:

- `INSTAGRAM_GET_USER_INSIGHTS` accepts `period` of **`day` or `lifetime`
  only**. Meta removed the `week` and `days_28` periods from the Insights API,
  so there is no weekly reach endpoint left to call.
- Daily reach **can** be fetched, but summing seven days of it is the same
  error as summing seven posts, in a different shape: an account that saw
  something on Monday and again on Thursday is counted twice. See the trap
  below — it applies to days exactly as it applies to posts.

So the deduplicated figure exists only in Insights in the app. Ask her for it
rather than reconstructing it, and do not accept a summed number from any
source as a substitute.

**The metric is called "Viewers" in the app (confirmed from her screen,
2026-10-12).** There is no "accounts reached" label any more. Instagram's
current Insights has three tabs — Overview, Content, Audience — and the
deduplicated figure sits on **Overview**, below the headline tiles, under the
heading **"Views by content type"**, as **Viewers**. The Content tab carries the
same metric per post, as a "Viewers" sort chip next to "Views".

Reference point from that screen: **681 viewers for Sep 12 – Oct 11**, against
3,221 views over the same 30 days. Views run roughly 4.7x viewers on this
account, which is the scale of the double-counting the baseline problem below is
about.

So: ask her for **Viewers**, on the Overview tab, for the date range wanted.

**Views is not reach, and the app now leads with views.** On 2026-10-12 the
first number that came back was "220 views". Instagram's 2024 Insights redesign
made **Views** the headline metric, so it is the number the dashboard shows
first and the easy one to read off. It counts plays, including the same person
twice. **Accounts reached counts each account once**, and that is the metric
this test is written on — the baseline of 201 is a reach figure, so comparing
220 views against it would be comparing two different things and would read as
a pass when it might not be one.

Ask for **accounts reached** by name, and if a number arrives without a label,
ask which metric it is before writing it down.

**Where she finds it:** Instagram app → her profile → **Professional dashboard**
→ **Accounts reached** → change the date range to the week in question. Both
weeks are inside Insights' 90-day retention, so Thu 1 – Wed 7 is still
readable.

## The baseline is itself a summed number (found 2026-10-12)

**This is a flaw in the rule above, found before any October number was read,
and it has to be fixed or the test is biased.**

The baseline is given as "201 — the week to Sun 28 Sep (79, 38, 28, 19, 16, 13,
8)". Those seven numbers add to exactly 201. They are the **per-post reach** of
that week's seven posts, taken from the same source as CLAUDE.md's "reach fell
every day of the week to Sep 28". So **201 is a sum of per-post reach**, which
is precisely what the section below says must never be compared against a
deduplicated weekly figure.

Comparing October's deduplicated weekly reach against 201 is biased **against**
October: the same account seeing two posts counts twice in 201 and once in the
October figure. The test would under-report October and could fail a cadence
that actually worked.

**The fix, which follows this file's own stated metric rather than overriding
it:** read **accounts reached for the baseline week in Insights too**, and
compare deduplicated to deduplicated on both sides. Sun 28 Sep is inside the
90-day retention window, so the figure is still readable.

Until that number exists, **201 is not the bar** — it is a different unit. The
decision on Wed 14 Oct uses the Insights figure for the baseline week, whatever
it turns out to be, against the Insights figures for the two October weeks.

Recorded now, with no October number in hand, so this is a correction to the
instrument and not a reaction to a result.

## The trap that would void the comparison

Instagram's weekly reach counts **each account once**, however many posts that
person saw. Adding up seven posts' individual reach gives a different, larger
number, because the same followers are counted repeatedly.

Compare a summed number against a deduplicated one and the result is noise.
**Use the Insights weekly figure on both sides.**

Note which way this cuts: fewer posts means less overlap between them, so the
deduplicated weekly figure should fall by *less* than the post count does.
Going from 7 posts to 3 does not imply 57% less weekly reach.

## What this test cannot tell you, however it lands

Reach was already falling before the cadence changed — 79 down to 8 across the
baseline week. So if it recovers, "posting less helped" and "the slide ended
on its own" cannot be separated. Six data points will not fix that.

This is not a reason to abandon the test. It is a reason not to over-read the
result in either direction, and a reason not to protect the test by holding
back other changes: the attribution is already lost, so the cost of running
something else alongside it is close to zero.

## Two things to record but not decide on

Neither of these changes the rule above. They are for understanding *why* the
number moved.

**Engagement rate per post** (interactions ÷ reach). The plan's theory is that
low engagement causes suppression, which causes lower reach. If that theory is
right, engagement rate moves *first* and reach follows. A flat reach with a
rising engagement rate is the mechanism working but not yet compounded — which
would otherwise read as failure.

**TikTok as a rough control.** Same content, same cuts, cadence unchanged. If
Instagram recovers while TikTok stays flat, that is weak evidence for the
cadence change. If both rise together, it was the content or the week. Not a
true control — different platform, different algorithm — but it is free.

## The thing the plan itself calls most likely to matter

Zero comments across more than forty-five posts. The plan names manual
engagement — substantive comments on other planners' accounts — as "the thing
most likely to matter", and then places it outside the plan.

It is the only lever never tried. Running it during these two weeks muddies
attribution, but per the section above, attribution is already unavailable.
Recorded here so that trade-off is a decision rather than an oversight.
