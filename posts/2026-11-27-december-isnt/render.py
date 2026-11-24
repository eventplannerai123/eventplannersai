"""Assemble the Fri 27 Nov planner-feelings Reel for Instagram and Facebook.

One text image held 9.00s with music and no voiceover, as the November plan
specifies for this format; TikTok takes the same image as a photo post.

**ITS BED IS ITS OWN GENERATION**, checked on the md5 against all three of
this week's others — her Nov 10 rule about two posts sharing their opening
bars, applied across the week rather than just the day. Fingerpicked nylon
guitar with a soft pad and a light tambourine: warm and moving forward
rather than a slow pad, which is her Nov 10 instruction about energy.

Instrumental, checked the two ways that do not need ears: the spectrogram
shows regular plucked transients and none of the formant movement a sung
vowel makes, and Scribe transcribed it to an empty string.

The energy profile settles the trim: -14.7 to -17.3 dB across all 30
seconds, flat end to end with no intro build and no ring-out, so the cut
starts at 0.0 with a 0.8s fade in and 1.2s out.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "december-isnt.jpg")
BED = os.path.join(HERE, "build", "music", "bed-9s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 9.0
BED_DB = 1.2                   # swept: +0.0 measured -15.2, this lands -14.0


def render():
    assert os.path.exists(IMG), IMG
    assert 7.0 <= HOLD <= 10.0, f"{HOLD}s is outside the format's 7-10s"
    out = os.path.join(HERE, "december-isnt-instagram.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y",
                    "-loop", "1", "-t", f"{HOLD:.3f}", "-i", IMG, "-i", BED,
                    "-filter_complex",
                    f"[0:v]scale={W}:{H},fps={FPS},setsar=1[v];"
                    f"[1:a]volume={BED_DB}dB,alimiter=limit=0.891:level=0[a]",
                    "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", out], check=True)
    print(f"{HOLD:.2f}s hold, bed {BED_DB:+.1f} dB -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    render()
