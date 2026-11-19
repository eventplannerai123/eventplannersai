"""Holiday Party RSVP List, for the Mon 23 Nov Reel redo.

The Mon 23 CLAUDE CODE line: build it in Reels > November > November 23,
fictional company and names only, and "check the four meal counts add to 142,
that the 23 dietary notes collapse to 6 restrictions, and that the three
contradictions and six blanks are really there, before Sahiba records".

EVERY COMPANY AND PERSON HERE IS INVENTED. Northline Devices is not a real
company; the party, the departments and all 186 names are made up. That is the
standing rule and it is also what makes the file safe to push to a public repo
for Drive to fetch.

**THREE DEFECTS ARE BUILT IN ON PURPOSE**, because the Reel is about AI
catching them:

  1. 23 guests wrote a dietary note, in 14 different wordings, which collapse
     to six real restrictions — gluten-free 8, nut allergy 5, dairy-free 4,
     shellfish allergy 3, vegan 2, pescatarian 1.
  2. Three of those notes contradict the meal the same person chose: two Beef
     rows reading "vegan" and "pescatarian", and a Chicken row reading
     "vegan - no animal products".
  3. Six plus-ones have a name and no meal choice at all, so the meal column
     totals 142 while 148 people are coming.

Each is asserted here rather than hoped for. A fourth accidental contradiction,
or a seventh restriction creeping in through a new wording, would make the
Reel's own numbers wrong in a way nobody would see by looking at the sheet.

Writes the rows as a list; `make_sheet` pushes them into the Google Sheet.
Run `python3 make_week6.py` to see the checks pass.
"""
import random

COMPANY = "Northline Devices"
INVITED = 180
ATTENDING, DECLINED, NO_REPLY = 142, 31, 7

MEALS = [("Beef", 54), ("Chicken", 48), ("Fish", 22), ("Vegetarian", 18)]

DEPARTMENTS = ["Sales", "Engineering", "Marketing", "Finance", "Operations",
               "People", "Legal", "Customer Success", "Support", "Design"]

# (wording as the guest typed it, how many wrote it, the real restriction)
NOTES = [
    ("no gluten",                   2, "Gluten-free"),
    ("celiac",                      2, "Gluten-free"),
    ("GF please",                   2, "Gluten-free"),
    ("gluten free pls",             2, "Gluten-free"),
    ("nut allergy",                 2, "Nut allergy"),
    ("allergic to nuts",            2, "Nut allergy"),
    ("tree nut allergy - severe",   1, "Nut allergy"),
    ("no dairy",                    2, "Dairy-free"),
    ("lactose intolerant",          2, "Dairy-free"),
    ("shellfish allergy",           2, "Shellfish allergy"),
    ("no shellfish",                1, "Shellfish allergy"),
    ("vegan",                       1, "Vegan"),
    ("vegan - no animal products",  1, "Vegan"),
    ("pescatarian",                 1, "Pescatarian"),
]

WANT_RESTRICTIONS = {"Gluten-free": 8, "Nut allergy": 5, "Dairy-free": 4,
                     "Shellfish allergy": 3, "Vegan": 2, "Pescatarian": 1}

# The notes that cannot sit with the meal the same person chose.
CONTRADICTORY = {"Vegan": {"Beef", "Chicken", "Fish"},
                 "Pescatarian": {"Beef", "Chicken"}}

# Which meal each contradictory note has to sit against, so the day block's
# sentence — two Beef rows and one Chicken row — is true of the file and not
# of whatever the shuffle happened to pick.
CLASH_MEAL = {"vegan": "Beef",
              "pescatarian": "Beef",
              "vegan - no animal products": "Chicken"}

PLUS_ONES = 6

FIRST = ["Aisha", "Ben", "Cora", "Dev", "Elena", "Felix", "Gia", "Hugo",
         "Imani", "Jonah", "Kira", "Luca", "Maya", "Noor", "Omar", "Pia",
         "Quinn", "Rafa", "Sena", "Theo", "Uma", "Vik", "Wren", "Yusuf",
         "Zara", "Ada", "Bo", "Cleo", "Dara", "Eli", "Faye", "Gus", "Hana",
         "Ivo", "Jun", "Kai", "Lena", "Mina", "Nils", "Opal", "Pavel", "Rhea",
         "Sol", "Tove", "Ugo", "Vera", "Wes", "Xan", "Yara", "Zev"]
LAST = ["Alvarez", "Brennan", "Castellano", "Dunbar", "Eriksen", "Fontaine",
        "Gallagher", "Haddad", "Ibarra", "Jensen", "Kowalski", "Lindqvist",
        "Moreau", "Nakamura", "Oyelaran", "Petrov", "Quintero", "Rossi",
        "Sandoval", "Tanaka", "Ueda", "Vasquez", "Whitfield", "Xiao",
        "Yildiz", "Zografos", "Ashworth", "Bellweather", "Carrow", "Delacroix",
        "Everly", "Fairholm", "Garrow", "Halloran", "Ingersoll", "Jarvis"]

HEADER = ["Name", "Department", "RSVP", "Meal choice", "Dietary notes",
          "Plus-one name", "Plus-one meal choice"]


def names(n, rng):
    out, seen = [], set()
    while len(out) < n:
        nm = f"{rng.choice(FIRST)} {rng.choice(LAST)}"
        if nm not in seen:
            seen.add(nm)
            out.append(nm)
    return out


def build():
    rng = random.Random(1123)
    people = names(INVITED + PLUS_ONES, rng)
    guests, plus_one_names = people[:INVITED], people[INVITED:]

    status = (["Attending"] * ATTENDING + ["Declined"] * DECLINED
              + ["No reply"] * NO_REPLY)
    rng.shuffle(status)

    meals = []
    for meal, n in MEALS:
        meals += [meal] * n
    rng.shuffle(meals)

    # Who wrote a note, and what they typed.
    written = []
    for wording, n, restriction in NOTES:
        written += [(wording, restriction)] * n
    rng.shuffle(written)

    attending_idx = [i for i, s in enumerate(status) if s == "Attending"]
    rows = [[g, rng.choice(DEPARTMENTS), s, "", "", "", ""]
            for g, s in zip(guests, status)]

    for slot, i in enumerate(attending_idx):
        rows[i][3] = meals[slot]

    # Place the three contradictions first, on rows whose meal already clashes
    # with the note, then scatter the rest where they do not.
    clashing = [(w, r) for w, r in written if r in CONTRADICTORY]
    plain = [(w, r) for w, r in written if r not in CONTRADICTORY]
    assert len(clashing) == 3, clashing
    assert {w for w, _ in clashing} == set(CLASH_MEAL), clashing

    used = set()
    for wording, restriction in clashing:
        for i in attending_idx:
            if i in used:
                continue
            if rows[i][3] == CLASH_MEAL[wording]:
                rows[i][4] = wording
                used.add(i)
                break
        else:
            raise AssertionError(f"nowhere to put {wording!r}")

    free = [i for i in attending_idx if i not in used]
    rng.shuffle(free)
    for (wording, _), i in zip(plain, free):
        rows[i][4] = wording
        used.add(i)

    # Six plus-ones, each with a name and no meal choice: the caterer's real
    # number is 148, not the 142 in the meal column.
    spare = [i for i in attending_idx if i not in used]
    rng.shuffle(spare)
    for nm, i in zip(plus_one_names, spare[:PLUS_ONES]):
        rows[i][5] = nm

    return rows


def check(rows):
    assert len(rows) == INVITED, len(rows)
    assert len({r[0] for r in rows}) == INVITED, "duplicate guest names"

    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    assert counts == {"Attending": ATTENDING, "Declined": DECLINED,
                      "No reply": NO_REPLY}, counts
    assert sum(counts.values()) == INVITED

    meal = {}
    for r in rows:
        if r[3]:
            meal[r[3]] = meal.get(r[3], 0) + 1
    assert meal == dict(MEALS), meal
    assert sum(meal.values()) == ATTENDING == 142

    # Nobody who declined or never replied carries a meal, a note or a guest.
    for r in rows:
        if r[2] != "Attending":
            assert r[3] == "" and r[4] == "" and r[5] == "", r

    by_wording = {}
    for r in rows:
        if r[4]:
            by_wording[r[4]] = by_wording.get(r[4], 0) + 1
    assert by_wording == {w: n for w, n, _ in NOTES}, by_wording
    assert len(by_wording) == 14, f"{len(by_wording)} wordings, guide says 14"

    bucket = {w: r for w, _, r in NOTES}
    restriction = {}
    for r in rows:
        if r[4]:
            k = bucket[r[4]]
            restriction[k] = restriction.get(k, 0) + 1
    assert restriction == WANT_RESTRICTIONS, restriction
    assert sum(restriction.values()) == 23, sum(restriction.values())
    assert len(restriction) == 6, f"{len(restriction)} restrictions, guide says 6"

    clashes = [r for r in rows
               if r[4] and r[3] in CONTRADICTORY.get(bucket[r[4]], set())]
    assert len(clashes) == 3, [(r[0], r[3], r[4]) for r in clashes]
    assert sorted(r[3] for r in clashes) == ["Beef", "Beef", "Chicken"], clashes

    guests = [r for r in rows if r[5]]
    assert len(guests) == PLUS_ONES, len(guests)
    assert all(r[6] == "" for r in guests), "a plus-one must have no meal"
    assert all(r[2] == "Attending" for r in guests)
    assert len({r[5] for r in guests}) == PLUS_ONES, "duplicate plus-one names"
    # Nobody carries both a note and a guest, so the two catches stay separate.
    assert not any(r[4] and r[5] for r in rows)

    print(f"checks pass: {INVITED} invited "
          f"({ATTENDING} attending, {DECLINED} declined, {NO_REPLY} no reply); "
          f"meals {'+'.join(str(n) for _, n in MEALS)} = {sum(meal.values())}; "
          f"{sum(restriction.values())} notes in {len(by_wording)} wordings -> "
          f"{len(restriction)} restrictions "
          f"({', '.join(f'{k} {v}' for k, v in WANT_RESTRICTIONS.items())}); "
          f"{len(clashes)} contradictions; {PLUS_ONES} plus-ones with no meal, "
          f"so {ATTENDING + PLUS_ONES} people against a column total of "
          f"{sum(meal.values())}")


if __name__ == "__main__":
    r = build()
    check(r)


# ============================================ Sun 22: BEO and run of show ===
"""BEO and Run of Show — Evening Reception, for the Sun 22 Nov slide Reel.

The Sun 22 CLAUDE CODE line: 4 pages, fictional venue and caterer, no real
names, in Reels > November > November 22, and "check the three waves add to
300, the seven stations and bars, and the two flags against the file".

The piece is about a food and beverage captain, so the file has to make the
captain's job derivable and never state it: the stations carry open, close
and refresh times, the arrivals carry three waves, and nothing anywhere adds
them up or names a busiest hour. The two flags — the raw bar at 40 minutes and
the crudités and cheese display at 35 — are the only refreshes longer than the
30-minute gap between walks, and that is what the AI is meant to notice.

Thorne Hall and Marchetti Hospitality are invented, and every number is a 555
line.
"""

WAVES = [("Doors", "6:00pm", 120), ("Keynote ends", "6:30pm", 100),
         ("Awards end", "7:15pm", 80)]

# (station, opens, closes, refresh minutes, what it needs)
STATIONS = [
    ("Raw bar",                      "6:00pm", "8:00pm", 40,
     "Ice replaced, shellfish re-laid from the walk-in"),
    ("Carving station",              "6:30pm", "8:30pm", 15,
     "Second chef brings the next joint from the kitchen"),
    ("Pasta station",                "6:00pm", "8:30pm", 20,
     "Pans swapped, sauce replenished at the range"),
    ("Crudités and cheese display",  "6:00pm", "9:00pm", 35,
     "Board rebuilt in the kitchen, garnish re-cut"),
    ("Dessert station",              "7:30pm", "9:00pm", 20,
     "Trays brought up from the pastry fridge"),
    ("Main bar",                     "6:00pm", "9:00pm", 10,
     "Ice and glassware only"),
    ("Satellite bar",                "6:30pm", "8:30pm", 10,
     "Ice and glassware only"),
]

RUN_OF_SHOW = [
    ("4:00pm", "Vendor load-in through the service entrance"),
    ("4:30pm", "Room set, linen down, bars built"),
    ("5:15pm", "Catering staff briefing in the back of house"),
    ("5:45pm", "Doors staffed, coat check open"),
    ("6:00pm", "Reception opens, first wave arrives"),
    ("6:30pm", "Keynote ends in the auditorium, second wave arrives"),
    ("7:15pm", "Awards end, third wave arrives"),
    ("8:00pm", "Raw bar closes"),
    ("8:30pm", "Carving, pasta and satellite bar close"),
    ("9:00pm", "Last call, reception ends"),
    ("9:30pm", "Breakdown begins"),
]

CONTACTS = [
    ("Kitchen", "Chef Ana Morales", "ext. 214"),
    ("Banquet captain", "Luis Grant", "(212) 555-0148"),
    ("Venue operations", "Dale Whitfield", "(212) 555-0172"),
    ("Catering office", "Marchetti Hospitality", "(212) 555-0190"),
]

WALK_GAP = 30        # minutes between the captain's walks
TOTAL_GUESTS = 300


def _mins(t):
    hh, rest = t.split(":")
    mm = int(rest[:2])
    h = int(hh) % 12 + (12 if rest.endswith("pm") else 0)
    return h * 60 + mm


def beo(path):
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from make_demo_files import Page, L, R

    c = canvas.Canvas(path, pagesize=LETTER)
    of = 4

    p = Page(c, "Thorne Hall — Banquet Event Order", 1, of)
    p.p("Event: Evening Reception, Thursday 10 December 2026", grey=True)
    p.p("Room: The Lowell Gallery    Hours: 6:00pm - 9:00pm", grey=True)
    p.p("Caterer: Marchetti Hospitality    BEO 2026-1188", grey=True)
    p.gap(0.3)
    p.h("Guest count")
    p.gap(0.06)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(L, p.y - 0.2 * inch, f"{TOTAL_GUESTS} guests")
    p.y -= 0.72 * inch
    p.p("Guests do not arrive together. The reception runs alongside the")
    p.p("conference programme, and three groups come in from it:")
    p.gap(0.16)
    for label, when, n in WAVES:
        p.row(f"{label}, {when}", f"{n} guests")
    p.gap(0.26)
    p.p("Service style: stations and bars, no seated service.", grey=True)
    p.p("Dress: business attire. Music: house playlist, no live band.", grey=True)
    c.showPage()

    p = Page(c, "Stations and bars", 2, of)
    p.p("Each station is staffed independently. Refresh time is how long it",
        grey=True)
    p.p("takes from the call going in to the station being full again.",
        grey=True)
    p.gap(0.26)
    for name, opens, closes, mins, how in STATIONS:
        p.h(name, size=11, gap=0.2)
        p.row("Service", f"{opens} - {closes}")
        p.row("Refresh time", f"{mins} minutes")
        p.p(f"    {how}", size=9, gap=0.24, grey=True)
    c.showPage()

    p = Page(c, "Run of show", 3, of)
    for when, what in RUN_OF_SHOW:
        p.row(when, what)
    p.gap(0.3)
    p.p("The kitchen takes refresh calls on the house phone or by radio on",
        grey=True)
    p.p("channel 4. Do not call a station in directly.", grey=True)
    c.showPage()

    p = Page(c, "Contacts and notes", 4, of)
    p.h("On the night")
    p.gap(0.08)
    for role, who, how in CONTACTS:
        p.row(f"{role} - {who}", how)
    p.gap(0.3)
    p.h("Notes")
    p.gap(0.08)
    p.p("Allergy requests are handled from the kitchen, not at the station.")
    p.p("The dessert station cannot open before the awards finish, because")
    p.p("the pastry team is in the auditorium until 7:15pm.")
    p.p("The satellite bar shares its ice with the main bar.")
    p.gap(0.3)
    p.p("Final guarantee due 72 hours before the event. Overage billed at",
        grey=True)
    p.p("the per-person rate. Nothing on this order is an exclusive.",
        grey=True)
    c.showPage()
    c.save()


def check_beo():
    assert sum(n for _, _, n in WAVES) == TOTAL_GUESTS, \
        f"{sum(n for _, _, n in WAVES)} guests across the waves"
    assert len(WAVES) == 3
    gaps = [_mins(WAVES[i + 1][1]) - _mins(WAVES[i][1]) for i in range(2)]
    assert gaps == [30, 45], gaps

    assert len(STATIONS) == 7, f"{len(STATIONS)} stations, guide says seven"

    # The busiest hour: all 300 are in by 7:15pm and the dessert station is
    # the only one not yet open at 6:30-7:30pm.
    def open_at(t):
        return [s for s in STATIONS if _mins(s[1]) <= t < _mins(s[2])]
    assert len(open_at(_mins("6:45pm"))) == 6, len(open_at(_mins("6:45pm")))
    assert [s[0] for s in STATIONS if _mins(s[1]) > _mins("6:45pm")] \
        == ["Dessert station"]

    flags = [s[0] for s in STATIONS if s[3] > WALK_GAP]
    assert flags == ["Raw bar", "Crudités and cheese display"], flags
    assert len(flags) == 2, flags
    assert all(s[3] <= WALK_GAP for s in STATIONS if s[0] not in flags)

    # Nothing in the file names a busiest hour or counts the stations for you.
    text = " ".join(str(x) for x in (WAVES, STATIONS, RUN_OF_SHOW, CONTACTS))
    for banned in ("busiest", "seven", "300 guests in", "captain sheet"):
        assert banned not in text.lower(), banned

    print(f"checks pass: {'+'.join(str(n) for _, _, n in WAVES)} = "
          f"{TOTAL_GUESTS} in three waves {gaps[0]} and {gaps[1]} minutes "
          f"apart; {len(STATIONS)} stations and bars; six of seven open "
          f"6:30-7:30pm; {len(flags)} refreshes longer than the "
          f"{WALK_GAP}-minute walk ({', '.join(flags)})")
