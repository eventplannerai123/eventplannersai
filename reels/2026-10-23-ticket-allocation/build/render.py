#!/usr/bin/env python3
"""Fri 23 Oct — ticket allocation. Two cuts, built from her 56.7s recording.

  * SOURCE is 1206x2622 at 60fps, the usual iPhone capture, so the standard
    crop applies: crop=1206:2144:0:478 drops the status bar and the red dot and
    leaves the ChatGPT input bar at the bottom where the platform UI covers it.
    Recomputed from this file's own width rather than pasted: 2144 = 1206/0.5625.
  * THE RECORDING RUNS PAST THE ANSWER. From about 43s she leaves ChatGPT and
    the capture carries her home screen, her app grid and then this very
    conversation. None of that goes near an export.
  * AN EIGHTH ADVERTISER. A TicketSpice in-app ad ("Sell More Tickets Online",
    "#1 Ticketing Software") slides into the bottom of frame between 38.0s and
    38.5s and stays. The first build ran the email beat to 39.18 and carried it
    plainly legible on the last frame. EVERY BEAT NOW ENDS BY 37.60, and the
    export is re-checked visually on its final frames rather than by a colour
    test, which the Sep 21 note shows can pass a faded logo.
  * THE PROMPT BEAT IS ONLY 2.6s OF SOURCE. At 2.7s she taps the attachment and
    the screen goes to a blank "Loading" for about 0.7s before the demand sheet
    renders. The first build ran to 3.4 and put that blank frame on screen. The
    2.6s is stretched to fill its slot instead, which on a near-static prompt
    screen is invisible.
  * IT OPENS ON THE FINISHED ALLOCATION TABLE, which is the brief's own
    instruction ("not the prompt being sent"), so time-to-payoff is zero.
    THE PROMPT IS NOT CUT, though — video rule 2 — it is the second beat, and
    that frame also carries the attached demand sheet, so one beat does both.
  * BEAT BOUNDARIES SIT IN THE VOICEOVER'S OWN GAPS, measured with
    silencedetect rather than guessed. Instagram speech runs 0-5.68,
    6.29-12.65, 13.16-19.88; the cuts land at 6.20, 9.60 and 15.00.
  * THE TIKTOK VOICEOVER IS SPED 5%. It generated at 20.85s against a 15-20s
    target; at atempo=1.05 it is 19.86s. Pitch is preserved.
  * ENDS ON THE OUTPUT — the drafted email — not an end card. The takeaway
    overlay sits over it.
  * LOUDNESS IS EXPLICIT GAIN PLUS A LIMITER, not loudnorm. Two things went
    wrong before this landed, both only visible by measuring the export:
      - The first build had NO loudness stage at all and shipped at -22.3
        LUFS. The voiceover is the only audio, so the export simply measures
        whatever ElevenLabs handed over, and nothing in the render complains.
      - The two-pass loudnorm that replaced it stalled at -16.0, with true
        peak at -4.19 — 2.7 dB of headroom it declined to use, so this is not
        the documented TP-ceiling stall. linear=true applies one fixed gain and
        undershot.
    So the gain is applied directly: -22.32 LUFS to the house -14 is +8.32 dB,
    which would put the true peak at +3.18, and alimiter catches it. level=0 or
    the limiter renormalises back to full scale and it clips at 0.0 dBFS
    however low the limit is set. MEASURE THE EXPORT, every time.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.dirname(HERE)
SRC = os.environ.get("SRC", "/tmp/claude-0/-home-user-eventplannersai/"
                     "4079a8b4-9eb7-5c73-8b20-b79d77bad268/scratchpad/src-1023/rec.mp4")
CARDS = os.path.join(HERE, "cards")

W, H, FPS = 1080, 1920, 30
SRC_W, SRC_H = 1206, 2622
CROP_H = int(SRC_W / 0.5625)          # 2144
CROP_Y = 478                          # status bar and the red recording dot
assert CROP_Y + CROP_H <= SRC_H
CROP = f"crop={SRC_W}:{CROP_H}:0:{CROP_Y},scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS}"

LAST_CLEAN = 37.60   # the TicketSpice ad arrives between 38.0 and 38.5

# (label, source in, source out, slot duration). A slot longer than the source
# span stretches that beat; equal means 1.0x.
PLANS = {
    "instagram": {
        "vo": os.path.join(REEL, "voiceover", "instagram.mp3"),
        "atempo": None,
        "total": 19.88,
        "gain": 9.40,   # measured: VO -22.32 LUFS; +8.32 lands at -15.0 once alimiter works, so +1.08 more
        "hook": "hook-instagram.png",
        "take_in": 15.80,             # takeaway overlay, in
        "beats": [
            ("allocation", 19.00, 25.20, 6.20),   # 0.00-6.20   2,000/2,000, the bars, the summary
            ("prompt",      0.00,  2.60, 3.30),   # 6.20-9.50   the prompt and the attached sheet
            ("waitlist",   27.20, 32.70, 5.50),   # 9.50-15.00  the ranked waitlist
            ("email",      32.72, 37.60, 4.88),   # 15.00-19.88 the drafted email
        ],
    },
    "tiktok": {
        "vo": os.path.join(REEL, "voiceover", "tiktok.mp3"),
        "atempo": 1.05,
        "total": 19.86,
        "gain": 9.45,   # same correction on the atempo-adjusted TikTok voiceover
        "hook": "hook-tiktok.png",
        "take_in": 15.60,
        "beats": [
            ("allocation", 19.00, 24.10, 5.10),   # 0.00-5.10
            ("prompt",      0.00,  2.60, 3.39),   # 5.10-8.49
            ("waitlist",   26.20, 31.21, 5.01),   # 8.49-13.50
            ("email",      31.21, 37.57, 6.36),   # 13.50-19.86
        ],
    },
}
def build(name, plan):
    out = os.path.join(REEL, f"ticket-allocation-{name}.mp4")
    inputs, chain, parts = [], "", []
    t = 0.0
    for i, (label, a, b, slot) in enumerate(plan["beats"]):
        assert b <= LAST_CLEAN, f"{label} ends at {b}, into the TicketSpice ad"
        span = b - a
        rate = span / slot                 # <1 slows the beat to fill its slot
        assert 0.70 <= rate <= 1.001, f"{label}: {rate:.2f}x is too far from real time"
        inputs += ["-ss", f"{a:.3f}", "-t", f"{span:.3f}", "-i", SRC]
        chain += (f"[{i}:v]{CROP},setpts=PTS/{rate:.6f},"
                  f"trim=duration={slot:.3f},setpts=PTS-STARTPTS[b{i}];")
        parts.append(f"[b{i}]")
        t += slot
    assert abs(t - plan["total"]) < 0.05, f"{name}: beats sum to {t:.2f}, VO is {plan['total']}"

    n = len(plan["beats"])
    chain += "".join(parts) + f"concat=n={n}:v=1:a=0[body];"

    inputs += ["-framerate", str(FPS), "-loop", "1", "-t", f"{plan['total']:.3f}",
               "-i", os.path.join(CARDS, plan["hook"])]
    inputs += ["-framerate", str(FPS), "-loop", "1", "-t", f"{plan['total']:.3f}",
               "-i", os.path.join(CARDS, "takeaway.png")]
    inputs += ["-i", plan["vo"]]

    chain += (f"[body][{n}:v]overlay=0:0:eof_action=repeat:repeatlast=1"
              f":enable='between(t,0,2)'[v1];")
    chain += (f"[v1][{n+1}:v]overlay=0:0:eof_action=repeat:repeatlast=1"
              f":enable='between(t,{plan['take_in']},{plan['total']})'"
              f",format=yuv420p[v];")

    tempo = f"atempo={plan['atempo']}," if plan["atempo"] else ""
    lvl = f"volume={plan['gain']}dB,alimiter=limit=-1.0dB:level=0"
    chain += (f"[{n+2}:a]{tempo}{lvl},aformat=sample_fmts=fltp:sample_rates=48000:"
              f"channel_layouts=stereo,apad,atrim=0:{plan['total']:.3f},"
              f"asetpts=PTS-STARTPTS[a]")

    cmd = (["ffmpeg", "-nostdin", "-v", "error", "-y"] + inputs +
           ["-filter_complex", chain, "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
            "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-r", str(FPS),
            "-t", f"{plan['total']:.3f}",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out])
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    print("built", out)


if __name__ == "__main__":
    # TikTok first, per the Round 6 rule.
    for name in ("tiktok", "instagram"):
        build(name, PLANS[name])
