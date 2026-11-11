"""Assemble the Fri 13 Nov planner-feelings Reel for Instagram and Facebook.

The Nov 8 format rule turns this 12:30pm slot into a Reel: the same still held
7-10 seconds under music on Instagram and Facebook, and a photo post on
TikTok. Eight seconds is the middle of that range and about as long as the
three paragraphs take to read.

THE BED IS THE FIRST UPBEAT ONE. Her instruction on Nov 10, after hearing the
Wed 11 pair: "moving forward lets to more upbeat instrumentals". Those two
were deliberately soft, because the guide's format line says "soft
royalty-free music" and the brief was to sit behind text; she heard them and
wanted more energy, and her words govern. This one is plucked acoustic guitar
and marimba over electric piano with a light shaker pulse, major key, steady —
brighter and with movement, but still even enough not to fight the reading.

ONE BED PER POST PER DAY. Friday's other piece is the venue-email Reel, which
carries an Eryn voiceover and no music at all, so there is nothing to clash
with — but the rule stands either way after Wed 11, when both Reels went out
of here on one track and she spotted it: "are they both the same?"

A Reel posted from this session cannot use Instagram's licensed audio library,
so whatever is in the mp4 is what goes out. Instrumental, checked the same two
ways as the earlier beds: a spectrogram read for the formant movement a sung
vowel makes, and Scribe, which transcribes an instrumental to an empty string.
The generation's own settings are not the check — they can report
"Instrumental: False" even when the prompt asked for none.

Nothing moves in the frame. A push on typeset text softens the glyphs for no
gain, and there is one image.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "slides", "plan-your-own-party.jpg")
BED = os.path.join(HERE, "build", "music", "bed-8s.wav")

W, H, FPS = 1080, 1920, 30
HOLD = 8.0


def render():
    assert os.path.exists(IMG), IMG
    out = os.path.join(HERE, "plan-your-own-party-instagram.mp4")
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
