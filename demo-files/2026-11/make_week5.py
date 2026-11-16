"""Staffing Plan — Fall Product Launch, for the Wed 18 Nov slide Reel.

The Wed 18 CLAUDE CODE line: build it in Reels > November > November 18,
fictional company and names only, "check the six role counts add to 40 and
that Hospitality has two leads and no captain".

**THE WHOLE PIECE TURNS ON ONE DEFECT IN THE FILE**: five roles have exactly
one named captain, and Hospitality and VIPs has two people marked "lead" and
no captain at all. Slide 5 is the AI flagging it. So the defect is built in
deliberately and asserted here — if a later edit gave Hospitality a captain,
the Reel would be making a claim the file does not support.

Everything is invented: Lumenfield is not a real company and every number is
a 555 line.

Writes two tabs as lists of rows; `make_sheet.py` beside it pushes them into
the Google Sheet. Run `python3 make_week5.py` to see the checks pass.
"""

ROLES = [
    # (role, radio channel, captain, how many people)
    ("Registration",          2, "Dana Ruiz",    8),
    ("Room and ushers",       3, "Marcus Lee",  10),
    ("Speaker ready room",    4, "Priya Shah",   4),
    ("Food and beverage",     5, "Tom Becker",   6),
    ("AV liaison",            6, "Lena Ortiz",   4),
    ("Hospitality and VIPs",  7, None,           8),   # two leads, no captain
]

HOSPITALITY_LEADS = ["Sam Okafor", "Jo Martin"]

FIRST = ["Aisha", "Ben", "Cora", "Dev", "Elena", "Felix", "Gia", "Hugo",
         "Imani", "Jonah", "Kira", "Luca", "Maya", "Noor", "Omar", "Pia",
         "Quinn", "Rafa", "Sena", "Theo", "Uma", "Vik", "Wren", "Yusuf",
         "Zara", "Ada", "Bo", "Cleo", "Dara", "Eli", "Faye", "Gus"]
LAST = ["Alvarez", "Brennan", "Castellano", "Dunbar", "Eriksen", "Fontaine",
        "Gallagher", "Haddad", "Ibarra", "Jensen", "Kowalski", "Lindqvist",
        "Moreau", "Nakamura", "Oyelaran", "Petrov", "Quintero", "Rossi",
        "Sandoval", "Tanaka", "Ueda", "Vasquez", "Whitfield", "Xiao",
        "Yildiz", "Zografos", "Ashworth", "Bellweather", "Carrow", "Delacroix",
        "Everly", "Fairholm"]

SHIFTS = {
    "Registration":         "4:00pm - 9:30pm",
    "Room and ushers":      "4:30pm - 9:30pm",
    "Speaker ready room":   "3:30pm - 8:30pm",
    "Food and beverage":    "3:00pm - 10:00pm",
    "AV liaison":           "2:00pm - 10:30pm",
    "Hospitality and VIPs": "5:00pm - 9:30pm",
}

STAFF_HEADER = ["Name", "Role", "Captain / lead", "Shift", "Radio channel",
                "Mobile"]

ESCALATIONS = [
    ("Registration", "Dana Ruiz", 2, [
        "A guest is not on the list and says they were invited.",
        "Someone asks to collect a badge for a colleague.",
        "A walk-up wants to register at the door.",
    ]),
    ("Room and ushers", "Marcus Lee", 3, [
        "An attendee is irate or will not take a seat.",
        "A row or section has to be held and guests are already in it.",
        "The room is at capacity and people are still arriving.",
    ]),
    ("Speaker ready room", "Priya Shah", 4, [
        "A speaker has not checked in 30 minutes before their slot.",
        "A speaker wants to change their slides after the cut-off.",
        "A speaker asks for a change to the running order.",
    ]),
    ("Food and beverage", "Tom Becker", 5, [
        "A station is running empty before its service time ends.",
        "A guest reports an allergy that is not on the dietary list.",
        "A guest asks for the bar after last call.",
    ]),
    ("AV liaison", "Lena Ortiz", 6, [
        "A microphone fails during a live session.",
        "The slides will not advance or the wrong deck is loaded.",
        "A speaker asks to add a video or live audio on the day.",
    ]),
    ("Hospitality and VIPs", None, 7, [
        "A VIP arrives earlier or later than the arrival plan.",
        "A VIP asks for a change to their seat or their table.",
        "A VIP brings a guest who is not on the list.",
    ]),
]

ESC_HEADER = ["Role", "Captain", "Radio channel", "Situation that goes to the captain"]


def _name_pool():
    """32 first names x 32 surnames, walked so no pair repeats.

    THE FIRST VERSION HUNG. It took FIRST[i % 32] with LAST[(7i + 3) % 32],
    and because 7 and 32 are coprime that pair cycles after 32 values — while
    40 staff minus 5 captains and 2 leads needs 33 distinct generated names.
    The 33rd request looped forever looking for a combination that could not
    exist. Walking both indices independently gives 1,024.
    """
    for k in range(len(FIRST) * len(LAST)):
        yield f"{FIRST[k % len(FIRST)]} {LAST[(k // len(FIRST) + k) % len(LAST)]}"


def build_staff():
    rows = []
    used = set()
    pool = _name_pool()
    for role, channel, captain, count in ROLES:
        names = []
        if captain:
            names.append((captain, "Captain"))
        elif role == "Hospitality and VIPs":
            names += [(n, "Lead") for n in HOSPITALITY_LEADS]
        while len(names) < count:
            n = next(pool)
            if n in used or any(n == x for x, _ in names):
                continue
            used.add(n)
            names.append((n, ""))
        for n, mark in names:
            used.add(n)
            rows.append([n, role, mark, SHIFTS[role], channel,
                         f"(212) 555-0{200 + len(rows):03d}"])
    return rows


def build_escalations():
    rows = []
    for role, captain, channel, situations in ESCALATIONS:
        # Blank, not "NOT NAMED": the gap has to be DERIVED from the Staff
        # tab, where Hospitality shows two Leads and no Captain. Writing
        # "NOT NAMED" here would hand the answer over, and the Reel would be
        # showing AI read a label rather than spot a problem.
        for s in situations:
            rows.append([role, captain or "", channel, s])
    return rows


def check(staff, esc):
    counts = {}
    for r in staff:
        counts[r[1]] = counts.get(r[1], 0) + 1
    for role, _, _, want in ROLES:
        assert counts[role] == want, f"{role}: {counts[role]} rows, guide says {want}"
    assert sum(counts.values()) == 40, f"{sum(counts.values())} staff, guide says 40"
    assert len(staff) == 40

    caps = {}
    for r in staff:
        if r[2] == "Captain":
            caps.setdefault(r[1], []).append(r[0])
    leads = {}
    for r in staff:
        if r[2] == "Lead":
            leads.setdefault(r[1], []).append(r[0])

    for role, _, captain, _ in ROLES:
        if captain:
            assert caps.get(role) == [captain], f"{role} captain is {caps.get(role)}"
            assert role not in leads, f"{role} has leads as well as a captain"
    # The defect the Reel is about, asserted rather than hoped for.
    assert "Hospitality and VIPs" not in caps, "Hospitality must have NO captain"
    assert leads["Hospitality and VIPs"] == HOSPITALITY_LEADS, \
        "Hospitality must have exactly the two named leads"
    assert len(leads) == 1, "only Hospitality carries leads"

    names = [r[0] for r in staff]
    assert len(set(names)) == 40, "duplicate staff names"
    mobiles = [r[5] for r in staff]
    assert len(set(mobiles)) == 40, "duplicate mobile numbers"
    assert all(m.startswith("(212) 555-") for m in mobiles), "555 numbers only"

    assert len(esc) == 18, f"{len(esc)} escalation rows, want 3 per role over 6 roles"
    assert not any("NOT NAMED" in str(c) for r in esc for c in r), \
        "the Hospitality gap must be derivable, not labelled"
    assert all(r[1] == "" for r in esc if r[0] == "Hospitality and VIPs")
    per = {}
    for r in esc:
        per[r[0]] = per.get(r[0], 0) + 1
    assert all(v == 3 for v in per.values()), per
    assert set(per) == {r[0] for r in ROLES}

    print(f"checks pass: {len(staff)} staff in {len(counts)} roles "
          f"({'+'.join(str(counts[r[0]]) for r in ROLES)} = 40), "
          f"5 captains, Hospitality 2 leads and no captain, "
          f"{len(esc)} escalation rows")


if __name__ == "__main__":
    s = build_staff()
    e = build_escalations()
    check(s, e)
