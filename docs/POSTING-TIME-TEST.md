# Morning vs evening — pre-registration

**Written 2026-10-15, before any data.** She asked for it run properly, and the
two tests before this one were not: the length test and the cadence test both
decided what counted as a result after seeing the numbers, and both ended up
unreadable. This file fixes the rules first. Read it on **Fri 13 Nov** rather
than re-deciding then.

All times Eastern.

## The question

Does the day's main Instagram post reach more accounts at **10:00am** or at
**6:30pm**?

## Design

- **28 days, Fri 16 Oct – Thu 12 Nov.** 14 mornings, 14 evenings.
- The arm for each day is **fixed in the table below, written in advance**.
  Nothing is reassigned once the run starts, whatever a day's numbers look
  like.
- **Every weekday carries exactly 2 mornings and 2 evenings**, so the arm is
  not confounded with day of week. Reach varies more by weekday than by hour
  on most accounts, and an unbalanced draw would have buried the effect. The
  first random draw gave 16/12 with all four Mondays in the morning arm and was
  discarded for that reason.

### What counts

- **The day's main Instagram post only.**
- Metric: **reach** (unique accounts), per post, read from the API at least 7
  days after posting so late reach is counted.

### What is excluded, and why — decided now, not later

- **Second posts of the day.** The evening slot would be perfectly confounded
  with being the second post of the day: anything posted at 6:30pm after a
  10am post is competing with it for the same small audience, so a difference
  could never be attributed to the hour. This is why the test is not run as
  same-day pairs, which would otherwise have been the stronger design.
- **Trial Reels.** A trial's distribution is deliberately different — non-
  followers only — so it is not measuring the same thing.
- **Nothing else.** In particular, **no dropping outliers after the fact.** Two
  posts since Sep 15 reached 159 and 85 against a median of 27, and the
  temptation to call those "not representative" is exactly how the earlier
  tests went wrong. The geometric mean below already damps them.

## The decision rule

Compare the **geometric mean of reach** in each arm.

| Evening ÷ morning | Verdict |
| --- | --- |
| **≥ 1.35** | Evening wins. Move the default posting time to 6:30pm. |
| **≤ 0.74** | Morning wins. Keep 10am, and stop asking. |
| **between** | **No detectable difference. Keep mornings.** |

**Why 1.35 and not something tighter.** Her log-reach standard deviation over
the last month is 0.53 — reach is wildly variable on an account this size. At
14 posts per arm that spread can only distinguish a ratio of about **1.37**.
Asking for anything finer would be reading noise.

| Posts per arm | Smallest difference it can actually detect |
| --- | --- |
| 7 | 1.55x (+55%) |
| 10 | 1.45x (+45%) |
| 14 | **1.37x (+37%)** |

**So say plainly what a null result means**: "no effect large enough for this
account to see", not "time of day does not matter". A real 15% effect exists or
does not, and this test cannot tell you either way. That is worth knowing
before it runs, not after.

## The schedule

| Day | Arm | Post at |
| --- | --- | --- |
| Fri 16 Oct | **PM** | 6:30pm |
| Sat 17 Oct | **PM** | 6:30pm |
| Sun 18 Oct | **AM** | 10:00am |
| Mon 19 Oct | **PM** | 6:30pm |
| Tue 20 Oct | **AM** | 10:00am |
| Wed 21 Oct | **AM** | 10:00am |
| Thu 22 Oct | **PM** | 6:30pm |
| Fri 23 Oct | **AM** | 10:00am |
| Sat 24 Oct | **PM** | 6:30pm |
| Sun 25 Oct | **PM** | 6:30pm |
| Mon 26 Oct | **AM** | 10:00am |
| Tue 27 Oct | **PM** | 6:30pm |
| Wed 28 Oct | **AM** | 10:00am |
| Thu 29 Oct | **PM** | 6:30pm |
| Fri 30 Oct | **AM** | 10:00am |
| Sat 31 Oct | **AM** | 10:00am |
| Sun 01 Nov | **PM** | 6:30pm |
| Mon 02 Nov | **AM** | 10:00am |
| Tue 03 Nov | **PM** | 6:30pm |
| Wed 04 Nov | **PM** | 6:30pm |
| Thu 05 Nov | **AM** | 10:00am |
| Fri 06 Nov | **PM** | 6:30pm |
| Sat 07 Nov | **AM** | 10:00am |
| Sun 08 Nov | **AM** | 10:00am |
| Mon 09 Nov | **PM** | 6:30pm |
| Tue 10 Nov | **AM** | 10:00am |
| Wed 11 Nov | **PM** | 6:30pm |
| Thu 12 Nov | **AM** | 10:00am |

**Clocks change Sun 1 Nov.** Eastern goes from UTC−4 to UTC−5, so from that day
6:30pm is 23:30 UTC rather than 22:30, and 10:00am is 15:00 rather than 14:00.
Any scheduled task set before 1 Nov and firing after it is an hour wrong.

## What could still spoil it

Worth writing down now so it is not discovered as a surprise:

- **Approval timing.** Posts run from here after she approves. If approval
  arrives after the slot, the post misses its assigned time. A day posted
  outside its slot by more than an hour is recorded as **void** and excluded —
  but the void count is reported, because if half the run voids, the result is
  not a result.
- **Reach is still falling.** The trend hits both arms roughly equally because
  the arms alternate throughout, which is the main thing the weekday-balanced
  design buys. It does not fix the variance.
- **Content quality varies more than the hour does**, and is not controlled.
  With 14 per arm it should average out; with fewer it would not.

## Read on Fri 13 Nov

Pull reach for every main post 16 Oct – 12 Nov, label by the table above, drop
voids and trials, take the geometric mean of each arm, apply the table. Record
the result here — including the void count and both arm sizes — and update the
guide's default posting time only if the rule says so.
