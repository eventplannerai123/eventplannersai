# The four-Reel hook rebuild experiment — results

Pulled from the Instagram Graph API on **2026-10-29**, the day the guide's Thu 29
block asked for them. Every figure is `lifetime`, which means it keeps accruing:
a number copied out of here next week will not match.

The design: take a Reel that underperformed, replace **only its first 3 seconds**
with a new hook, keep the rest of the edit byte-identical, and post it as a
regular feed Reel. Four pieces, run Oct 15–27. The metric the experiment names
is **skip rate** — Instagram's own "percentage of views from people who skipped
during the first 3 seconds", which is as close as the API gets to measuring a
hook directly.

## The numbers

| | Original | Rebuild | Skip | Avg watch |
| --- | --- | --- | --- | --- |
| **1** ROI report | Sep 1, 9:52am — 14 views, 11 reach | Tue 27, 6:30pm — **26 views, 19 reach** | 70% → **57.1%** | 5.94s → 3.91s |
| **2** Deposit tracker | Sep 3, 9:08am — 15 views, 15 reach | Wed 15, 9:30am — **39 views, 30 reach** | 84.6% → **71%** | 3.67s → **5.32s** |
| **3** Feedback debrief | Sep 30, 9:02am — 23 views, 17 reach | Fri 17, 11:18am — **37 views, 25 reach** | 63.2% → 82.1% | 5.32s → 4.36s |
| **4** Staffing plan | Sep 26, 9:02am — 24 views, 20 reach | Thu 22, 6:30pm — **195 views, 172 reach** | 80% → 85% | 5.23s → 2.46s |

Media ids, for re-pulling: rebuilds `18003611627798319`, `18212241865362368`,
`18002430083814206`, `18133295842786706`; originals `18146376565557032`,
`18437908249177797`, `18017699552938755`, `17915786724259148`.

## Skip rate went two better and two worse

Views rose on all four, and that is the tempting headline. It is not a result.

**Only Rebuilds 2 and 3 are clean tests.** Both originals and both rebuilds went
out in the morning, so the hook is the only thing that changed. Rebuilds 1 and 4
moved to the 6:30pm slot, which her own Oct 1–25 figures put at 134 average reach
against 29 for daytime — a 4.6x gap, far larger than anything a hook rewrite
would produce. So their view gains cannot be credited to the hook at all, and
Rebuild 4's 195 views are mostly the slot.

Among the two clean ones: **one better, one worse.** That is no signal.

Worth noting separately that skip rate and watch time moved in *opposite*
directions on three of the four. Rebuild 1 cut skip from 70% to 57.1% and still
lost two seconds of average watch; Rebuild 4 added 171 reach and lost nearly
three. A hook that stops the scroll is not the same thing as a piece that holds
someone, and the experiment was only ever built to measure the first.

## So the experiment is inconclusive, and the reason is the calendar

It does not show that rebuilding a hook lowers skip rate. It does not rule it
out either — four pieces, two of them confounded, on an account where a single
post's reach ranges 11 to 221.

The honest account is that the design was **overtaken by the Oct 25 posting-time
rule**. The experiment was written when everything went out in the morning; half
of it then ran in the evening. A fifth rebuild would have to go out in the same
slot as its original to measure anything, and nothing is scheduled.

**Do not re-run this as designed.** If the hook question comes back, the test
has to hold the slot fixed, which now means comparing two evening Reels.

## The originals' numbers in the guide have already moved

Recorded on the day against what the API returns now:

| Post | Guide says | Oct 29 pull |
| --- | --- | --- |
| Sep 1 ROI report | 3.3s average watch | **5.94s** |
| Sep 26 staffing plan | 23 views, 20 reach | **24 views**, 20 reach |
| Sep 30 feedback debrief | 20 views, 16 reach | **23 views, 17 reach** |

None of these changes a decision that was made on them. The point is the habit:
**a lifetime figure written into the guide is a snapshot**, and a selection made
by comparing a fresh pull against a month-old note is comparing two different
things. Re-pull both sides.
