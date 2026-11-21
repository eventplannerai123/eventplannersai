"""Assemble the Mon 23 Nov planner list Reel for Instagram and Facebook.

The November plan's planner-list-Reel format: one image held 8-10 seconds as
a Reel with music on Instagram and Facebook, and the same image as a photo
post on TikTok. Nine seconds is the middle of that range and gives five boxes
time to be read.

**IT IS A REEL AND NOT A PHOTO, AND THE NUMBERS SAY WHY.** On Mon 9 the photo
version of a 12:30pm slot reached 15; the two posted as Reels reached 146 and
130. So after posting, check the profile shows it as a Reel.

THE BED IS ITS OWN GENERATION: warm electric piano and a brushed shaker over
a walking upright bass. Monday's other post, the 6:30pm RSVP redo, carries a
voiceover and no bed, so there is nothing for it to clash with — but it is a
fresh generation regardless, because on Nov 11 two of that day's Reels went
out on one track and she heard it immediately.

**Light and upbeat rather than soft, which is a judgement call between two of
her instructions.** The format line written on Nov 18 says "soft music"; her
Nov 10 instruction, after hearing the first two beds, was "moving forward
lets to more upbeat instrumentals". The Nov 18 wording reads as carried over
from the planner-feelings spec rather than a fresh decision about this
format, so this one has movement without being busy. Worth her ear on it.

Instrumental, checked the same two ways as every bed: a spectrogram read for
the formant movement a sung vowel makes — even texture end to end, regular
transients, nothing sweeping — and Scribe, which returned an empty string.
The generation's own settings say "Instrumental: False" either way, so they
are not the check.

The energy profile also settles the trim: -12.2 to -14.5 dB across all 25
seconds with no ring-out, so the cut starts at 0.0. That is what the Thu 26
bed failed and had to be regenerated for. 0.8s fade in, 1.2s fade out, and
**+0.0 dB** into the limiter for -14.0 LUFS: this one came out of the model
already there.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "hills.jpg")
BED = os.path.join(HERE, "build", "music", "bed-9s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 9.0


def render():
    assert os.path.exists(IMG), IMG
    assert 8.0 <= HOLD <= 10.0, f"{HOLD}s is outside the format's 8-10s"
    out = os.path.join(HERE, "hills-instagram.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y",
                    "-loop", "1", "-t", f"{HOLD:.3f}", "-i", IMG, "-i", BED,
                    "-filter_complex", f"[0:v]scale={W}:{H},fps={FPS},setsar=1[v]",
                    "-map", "[v]", "-map", "1:a",
                    "-c:v", "libx264", "-profile:v", "high", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", out], check=True)
    print(f"{HOLD:.2f}s hold -> {os.path.basename(out)}")
    return out


if __name__ == "__main__":
    render()
