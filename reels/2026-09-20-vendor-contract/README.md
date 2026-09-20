# Vendor contract review reel — 2026-09-20

Comment-to-unlock keyword: **REVIEW**, per the guide's assignment list.

Status: **awaiting approval.** Built and QC'd, not posted.

TikTok is not posted from here; that cut is uploaded by hand per the guide.

## The page-count correction

The brief's hook, caption and voiceover all said the contract was **twelve
pages**. It is **five** (`pdfinfo` reports 5; the document's own footers read
"1 of 3 / 2 of 3 / 3 of 3"). Nothing in it gives twelve.

This was not a cosmetic slip. **ChatGPT states the length out loud in the
footage** — "I read the **entire 5-page contract**, including the service
tables and the terms on pages 4-5" — and that line is on screen during the
reveal. A "twelve pages" hook would have been contradicted by the video
underneath it.

The author chose to drop the number rather than correct it, so:

- Hook, Instagram: "This is a real vendor contract. Most people never read
  past page one." "Page one" is kept deliberately - the hook rule wants a
  concrete detail, and removing the page count takes away the only one the
  original line had.
- Hook, TikTok: "Stop signing vendor contracts you haven't read past page
  one."
- Caption: first sentence becomes "This is a real vendor contract."
- **Voiceover re-recorded** in the same Vanessa - Beach Girl voice
  (`8DzKSPdgEQPaK5vKG0Rs`) via the ElevenLabs connector, script unchanged
  except for the removed clause. Kept as `build/voiceover-corrected.mp3`.
  The original upload, which says "all 12 pages of it", is unused.

## Accuracy check (requested in the brief)

The brief asked for confirmation that the flagged issues are genuinely
valid before this ships. The contract was read in full from the PDF, then
every issue ChatGPT flagged on screen was checked back against the
document. **All nine hold up, and several are quoted verbatim.**

| # | Flagged on screen | Verified against the contract |
| --- | --- | --- |
| 1 | Cancellation clause extremely one-sided | Exact. Deposit non-refundable; cancel inside 90 days, owe full payment; and the quoted "Party A is liable for 50% of the full payment" is verbatim |
| 2 | No protection if the vendor cancels or fails to perform | Correct *absence* - there is no vendor-side cancellation, refund, substitute-vendor or nonperformance clause anywhere in the document |
| 3 | "Finalization" undermines what you are buying | Verbatim from the FINALIZATION clause |
| 4 | "Product Match" gives the vendor too much discretion | PRODUCT MATCH: "Party A will do its best to find the best matching alternative" |
| 5 | Conflict-of-interest clause far too broad | Verbatim, including "penalties as high as full payment" |
| 6 | Property damage liability essentially unlimited | Contract says damage "caused by sober or inebriated individuals" |
| 7 | Stolen-property clause broader still | Verbatim: "Any items found to be missing or stolen during or at the termination of the event will be the responsibility of party B" |
| 8 | "Tax TBD" conflicts with the stated total | Matches the totals block exactly - Subtotal $21,435, Discount $1,660, Discount price $18,805, Travel/setup/breakdown Included, Tax TBD, Total price $18,805 |
| 9 | Travel/setup/breakdown says "Included" without defining what | "TRAVEL, SET UP & BREAKDOWN Included", undefined |

**No fabrications.** The sharpest observation on screen is also correct and
carefully hedged: on the 50%-refund sentence it says "Party A is the
vendor. It may be a drafting error that was intended to say Party B, but
you should not assume that." That is exactly right, and it does not
overclaim.

It also frames itself as "a contract-review/negotiation analysis rather
than legal advice," which is worth having on screen for this topic.

Issues in the contract it did **not** flag: the vendor owning all event
photos and video, the New York City forum clause, unbounded hotel
accommodation, the bounced-check clause making the client liable for the
entire contract, and the vendor disclaiming liability for its own preferred
vendors. Not errors - the nine it caught are the substantive ones - but
noted since the brief asked about misses too.

## Cuts

Both 1080x1920 (ratio exactly 0.5625), 30 fps, H.264 high, CRF 19,
voiceover normalised to -14 LUFS (measured -13.97, TP -1.47).

| File | Platform | Duration | Ramp | Time to payoff | Opening line |
| --- | --- | --- | --- | --- | --- |
| `contract-instagram.mp4` | Instagram, Facebook | 16.20s | 3.0x | 3.98s | "This is a real vendor contract. Most people never read past page one." |
| `contract-tiktok.mp4` | TikTok (manual post) | 16.50s | 2.8x | 4.26s | "Stop signing vendor contracts you haven't read past page one." |

End card on both: "Save this before your next contract signing."

## Source handling

Two clips from a 52-second original, cut by the author: A is 15.75s, B is
12.19s. Both 1206x2622 at 60 fps, and confirmed distinct (the Sep 16
duplicate-upload check).

Clip A's structure, from a 10 fps frame-difference scan:

| Span | What it is |
| --- | --- |
| 0.00-1.40 | prompt in the box, contract attached, keyboard up |
| 1.40-2.10 | send tap, keyboard dismisses |
| 2.10-3.55 | message settles |
| 3.55-7.25 | **frozen** - the generating wait, frame deltas ~0.02 |
| 7.25-10.55 | answer streaming in |
| 10.55-15.75 | scrolling the answer |

### Representative slice

Flagging this per the timing rules. The real generating phase is 3.7
seconds of a completely static screen followed by streaming text. Segment 2
runs A 2.20-10.55 at 3.0x, which is the whole span rather than a slice -
at 3.0x it already compresses to 2.78s, inside the 2.5-3s beat, so no
material had to be dropped.

### The A/B join

A and B do **not** overlap - frame-matching B's opening against all of A
returns a best MAD of 21.8, i.e. no shared frame, so the author's two
slices come from different parts of the 52s original with a gap between.
The join is therefore a jump cut, placed past item 2 so it advances rather
than repeating. It happens to land well: A's last visible line is "If Party
A cancels, becomes unable to perform, or materially fails to provide the..."
and B picks up at "refund of amounts paid for services not provided" - the
continuation of that same sentence.

Ad check: 19 frames sampled across both raw clips at 1.5s intervals; no
in-app ads.

## Silent tail

The corrected voiceover is 8.78s against a 16.20s cut, leaving 7.4s. That
is by far the longest tail of the series, and it is deliberate: the author
chose to hold the reveal rather than cut under the 16-second floor. The
whole stretch is the flagged-issues list **scrolling at normal speed**, not
a freeze - a moving, readable reveal, which is what the "save this" end
card is asking for.
