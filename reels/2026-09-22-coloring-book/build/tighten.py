#!/usr/bin/env python3
"""Shorten a voiceover by compressing the gaps between sentences, never the
speech itself, and report where every speech segment lands afterwards."""
import subprocess, re, sys, shlex

def silence_map(path, noise="-32dB", d="0.28"):
    p = subprocess.run(f'ffmpeg -hide_banner -i {shlex.quote(path)} '
                       f'-af "silencedetect=noise={noise}:d={d}" -f null -',
                       shell=True, capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", p.stderr)]
    ends   = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", p.stderr)]
    dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration',
                                '-of','csv=p=0',path],capture_output=True,text=True).stdout)
    return starts, ends, dur

def tighten(src, out, factor, lead=0.25, tail=0.40, floor=0.26):
    starts, ends, dur = silence_map(src)
    # speech segments: 0 -> starts[0], ends[0] -> starts[1], ... ends[-1] -> dur
    segs, gaps = [], []
    prev = 0.0
    for i, s in enumerate(starts):
        if s <= prev:            # leading silence
            prev = ends[i]; continue
        segs.append((prev, s))
        if i < len(ends):
            gaps.append((s, ends[i]))
            prev = ends[i]
    if prev < dur - 0.02:
        segs.append((prev, dur))
    # trailing gap is not a real pause - drop it if the last segment is silence-only
    if gaps and len(gaps) == len(segs):
        gaps = gaps[:-1]
    new_gaps = [max(floor, (e - s) * factor) for s, e in gaps]

    # build the filter: each speech segment, then a shortened slice of its gap
    parts, n = [], 0
    for i, (a, b) in enumerate(segs):
        parts.append(f"[0:a]atrim=start={a:.4f}:end={b:.4f},asetpts=PTS-STARTPTS[p{n}];"); n += 1
        if i < len(new_gaps):
            g0, g1 = gaps[i]; mid = (g0 + g1) / 2.0; half = new_gaps[i] / 2.0
            parts.append(f"[0:a]atrim=start={mid-half:.4f}:end={mid+half:.4f},asetpts=PTS-STARTPTS[p{n}];"); n += 1
    chain = "".join(f"[p{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[j];"
    chain += f"[j]adelay={int(lead*1000)}|{int(lead*1000)},apad=pad_dur={tail}[o]"
    run = f'ffmpeg -y -v error -i {shlex.quote(src)} -filter_complex "{"".join(parts)}{chain}" -map "[o]" -c:a libmp3lame -q:a 2 {shlex.quote(out)}'
    p = subprocess.run(run, shell=True, capture_output=True, text=True)
    if p.returncode: print(p.stderr[-2500:]); sys.exit(1)

    # where each speech segment now starts and ends
    t, table = lead, []
    for i, (a, b) in enumerate(segs):
        table.append((i + 1, round(t, 3), round(t + (b - a), 3)))
        t += (b - a)
        if i < len(new_gaps): t += new_gaps[i]
    total = round(t + tail, 3)
    return table, total

if __name__ == "__main__":
    src, out, factor = sys.argv[1], sys.argv[2], float(sys.argv[3])
    table, total = tighten(src, out, factor)
    print(f"{out}  total {total}s")
    for i, a, b in table: print(f"  s{i:<3} {a:7.3f} - {b:7.3f}")
