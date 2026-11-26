"""Holiday Party Seating — Guest List, for the Tue 1 Dec seating redo.

120 guests, twelve tables of ten, a fictional company and invented names
throughout. The point of the piece is the three constraints that CANNOT all
be met, so this file's job is to make sure they are genuinely impossible
rather than merely awkward — a demo whose contradictions can be solved
quietly ruins the Reel it exists for.

The three are deliberately of three different SHAPES, because a model that
spots one shape often misses the others:

  1. A group too large for one table.            (arithmetic)
  2. A separation inside a must-sit-together group. (contradiction)
  3. A hub who must sit with two people who must  (triangle)
     not sit with each other.

Run it with python3 (no third-party imports). It prints the rows and exits
non-zero if any seeded conflict turns out to be satisfiable.
"""
from itertools import combinations

TABLES = 12
SEATS = 10
CAPACITY = TABLES * SEATS

COMPANY = "Cedarbrook Partners"   # invented; no real client, venue or employer

# --- the three seeded conflicts -------------------------------------------

# 1) Operations, eleven people, "must all sit together". Tables hold ten.
OPERATIONS = [
    "Dana Whitlock", "Omar Breslin", "Teresa Nunn", "Hal Oyelaran",
    "Mabel Ferris", "Victor Sarkisian", "Joy Pemberton", "Iain Carrow",
    "Rosalind Ebbs", "Felix Marchetti", "Greta Lindqvist",
]

# 2) Finance, eight people, "must all sit together" — and two of them must
#    be kept apart.
FINANCE = [
    "Marcus Deel", "Priya Raman", "Camille Bissett", "Noor Haddadi",
    "Winston Agu", "Lila Stroud", "Pete Vanterpool", "Simone Okafor",
]
SEPARATE_IN_FINANCE = ("Marcus Deel", "Priya Raman")

# 3) The triangle: Nina must sit with both; those two must not sit together.
HUB = "Nina Alcott"
HUB_WITH = ("Carol Beaufort", "Douglas Wren")
HUB_APART = ("Carol Beaufort", "Douglas Wren")

MUST_SIT_TOGETHER = {"Operations": OPERATIONS, "Finance": FINANCE}
MUST_SIT_APART = [SEPARATE_IN_FINANCE, HUB_APART]
MUST_SIT_WITH = [(HUB, HUB_WITH[0]), (HUB, HUB_WITH[1])]


def impossibilities():
    """Every seeded conflict, with the reason it cannot be satisfied."""
    found = []

    # shape 1 — arithmetic
    for name, group in MUST_SIT_TOGETHER.items():
        if len(group) > SEATS:
            found.append((f"{name} too large",
                          f"{len(group)} people must sit together; a table seats {SEATS}"))

    # shape 2 — a separation inside a group that must stay together
    for name, group in MUST_SIT_TOGETHER.items():
        for a, b in MUST_SIT_APART:
            if a in group and b in group:
                found.append((f"{name} separation",
                              f"{a} and {b} must be apart but both are in {name}, "
                              f"which must sit together"))

    # shape 3 — the triangle
    for hub, others in _hubs().items():
        for a, b in combinations(sorted(others), 2):
            if (a, b) in [tuple(sorted(p)) for p in MUST_SIT_APART] or \
               (b, a) in [tuple(p) for p in MUST_SIT_APART]:
                found.append(("triangle",
                              f"{hub} must sit with both {a} and {b}, who must "
                              f"not sit with each other"))
    return found


def _hubs():
    out = {}
    for a, b in MUST_SIT_WITH:
        out.setdefault(a, set()).add(b)
    return out


def rows():
    """(guest, table request, note) for all 120, in the order they are read."""
    out = []
    for g in OPERATIONS:
        out.append((g, "Operations", "Operations all sit together"))
    for g in FINANCE:
        note = "Finance all sit together"
        if g in SEPARATE_IN_FINANCE:
            other = [x for x in SEPARATE_IN_FINANCE if x != g][0]
            note += f"; do not seat with {other}"
        out.append((g, "Finance", note))
    out.append((HUB, "no preference",
                f"Must sit with {HUB_WITH[0]} and {HUB_WITH[1]}"))
    out.append((HUB_WITH[0], "no preference",
                f"Do not seat with {HUB_APART[1]}"))
    out.append((HUB_WITH[1], "no preference",
                f"Do not seat with {HUB_APART[0]}"))

    # The rest of the room: ordinary guests with ordinary notes, so the three
    # conflicts have to be found rather than being the only notes on the page.
    FIRST = ["Aiko", "Bernard", "Cressida", "Darnell", "Esme", "Fintan",
             "Giselle", "Hamza", "Imani", "Jonas", "Kiera", "Lorcan",
             "Marisol", "Nadir", "Odette", "Pavel", "Quinn", "Rafa",
             "Sunniva", "Tomas", "Ulla", "Vikram", "Wyatt", "Xiomara",
             "Yusuf", "Zelda"]
    LAST = ["Ashdown", "Belliveau", "Carrick", "Duthie", "Enfield",
            "Fairhurst", "Gillingham", "Hollingsworth", "Ingleby", "Jarrow",
            "Keating", "Lambourne", "Mottram", "Nithercott", "Oldacre",
            "Pentreath", "Quarrie", "Rushworth", "Standish", "Thirlwell"]
    SOFT = [
        "", "", "", "", "",
        "Prefers a seat near the door",
        "Vegetarian",
        "Joining after the first course",
        "Would like to sit with the Design team",
        "Nut allergy",
        "Hard of hearing — away from the speakers",
        "New starter, happy anywhere",
    ]
    i = 0
    while len(out) < CAPACITY:
        first = FIRST[i % len(FIRST)]
        last = LAST[(i // len(FIRST) + i) % len(LAST)]
        name = f"{first} {last}"
        if name in {r[0] for r in out}:
            i += 1
            continue
        out.append((name, "no preference", SOFT[i % len(SOFT)]))
        i += 1
    return out


def main():
    conflicts = impossibilities()
    r = rows()

    assert len(r) == CAPACITY, f"{len(r)} guests, the room seats {CAPACITY}"
    assert len({x[0] for x in r}) == CAPACITY, "a guest name is duplicated"
    # Three conflicts, one of each shape, and every one of them unsatisfiable.
    kinds = {c[0] for c in conflicts}
    assert "Operations too large" in kinds
    assert "Finance separation" in kinds
    assert "triangle" in kinds
    assert len(conflicts) == 3, f"expected 3 seeded conflicts, got {conflicts}"
    # And nothing accidentally impossible beyond the three.
    assert len(FINANCE) <= SEATS, "Finance must be solvable but for the separation"

    print(f"{COMPANY} holiday party — {CAPACITY} guests, "
          f"{TABLES} tables of {SEATS}\n")
    print("Seeded conflicts, none of which can be satisfied:")
    for kind, why in conflicts:
        print(f"  - [{kind}] {why}")
    print(f"\n{len(r)} rows: guest | table request | note")
    for g, t, n in r[:14]:
        print(f"  {g:22s} | {t:14s} | {n}")
    print("  ...")


if __name__ == "__main__":
    main()
