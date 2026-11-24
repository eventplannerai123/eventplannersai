"""Sun 29 Nov demo file — "Annual Client Summit — 2026 Actuals".

The sheet Sahiba opens on screen before pasting the Sun 29 prompt. Eleven
lines of last year's actuals with a Notes column, and the whole point of the
piece lives in two of those notes: the venue and the caterer have **already
quoted 2027**, so a flat 3% uplift is wrong on the two biggest lines.

**EVERY TOTAL IS RECOMPUTED HERE AND ASSERTED AGAINST THE GUIDE'S FIGURE.**
A demo whose arithmetic does not hold ruins the Reel it exists for, and this
one is load-bearing twice over: the overlay says $107,800 and the voiceover
says the right answer is $113,180 against a flat-3% $111,034. All three are
derived below, not typed.

Fictional company, no real vendors, no venue name — the standing rule, and
this file goes on screen in a public Reel.
"""

ROWS = [
    ("Venue rental",            18000, "2027 rate confirmed in contract: $19,500"),
    ("Catering",                35500, "Caterer's 2027 menu letter: $151 a person"),
    ("Bar",                      9800, ""),
    ("AV and production",       14200, ""),
    ("Event staff and security", 6400, ""),
    ("Guest shuttles",           4300, ""),
    ("Décor and florals",        7600, ""),
    ("Photo and video",          3900, ""),
    ("Printing and signage",     1850, ""),
    ("Guest gifts",              5000, ""),
    ("Event insurance",          1250, ""),
]

GUESTS = 250
PER_HEAD_2026 = 142
PER_HEAD_2027 = 151
VENUE_2027 = 19500
UPLIFT = 0.03


def check():
    total = sum(r[1] for r in ROWS)
    assert len(ROWS) == 11, len(ROWS)
    assert total == 107800, f"the eleven lines come to {total}, not 107800"
    assert PER_HEAD_2026 * GUESTS == 35500, "catering is not $142 x 250"
    assert ROWS[1][1] == PER_HEAD_2026 * GUESTS

    # Both notes have to be there, or the piece has no twist.
    noted = [r[0] for r in ROWS if r[2]]
    assert noted == ["Venue rental", "Catering"], noted

    # A flat uplift on everything — the wrong answer, and the number the
    # voiceover contrasts against.
    flat = round(sum(r[1] * (1 + UPLIFT) for r in ROWS))
    assert flat == 111034, f"flat 3% gives {flat}, not 111034"

    # The right answer: the two quoted lines at their quotes, 3% on the nine.
    catering_2027 = PER_HEAD_2027 * GUESTS
    assert catering_2027 == 37750, catering_2027
    rest = [r for r in ROWS if not r[2]]
    assert len(rest) == 9, len(rest)
    real = VENUE_2027 + catering_2027 + sum(round(r[1] * (1 + UPLIFT)) for r in rest)
    assert real == 113180, f"the quoted-rate budget gives {real}, not 113180"
    assert real - flat == 2146, real - flat

    # No real company, venue or vendor anywhere on the sheet.
    text = " ".join(f"{a} {c}" for a, _, c in ROWS).lower()
    for banned in ("llc", "inc.", "ltd", "hotel", "hilton", "marriott"):
        assert banned not in text, f"the sheet names {banned!r}"

    print(f"checks pass: 11 lines totalling ${total:,}, catering "
          f"${PER_HEAD_2026} x {GUESTS}, flat 3% ${flat:,}, "
          f"with the two quotes ${real:,} (+${real - flat:,})")
    return total


def values():
    """The grid as it goes into the Sheet."""
    out = [["Annual Client Summit — 2026 Actuals", "", ""],
           ["250 guests", "", ""],
           ["", "", ""],
           ["Line", "2026 actual", "Notes"]]
    for name, amount, note in ROWS:
        out.append([name, amount, note])
    out.append(["Total", sum(r[1] for r in ROWS), ""])
    return out


if __name__ == "__main__":
    check()
    for row in values():
        print(row)
