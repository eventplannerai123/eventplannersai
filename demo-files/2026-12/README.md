# December demo files

Built when the post is planned, not on the day — her Oct 14 rule.

## `holiday_party_seating.py` — Tue 1 Dec, the seating redo

**Holiday Party Seating — Guest List**, a Google Sheet in
`Reels > December > December 1` (file id
`1ZZkotSsG5AvgF5yx1o9WV1FnNTgL7K-sslQpKVbQp_I`, 121 rows written, 363 cells).
Built Thu 26 Nov, two days before the Sat 28 deadline in the day block.

120 guests, twelve tables of ten, **Cedarbrook Partners** — invented, as are
every guest name, so the file is safe in a public repo.

### The three seeded conflicts, and why the generator asserts them

The piece exists to show an AI naming the constraints it *cannot* meet, so a
demo whose contradictions can be solved quietly would ruin it. `main()`
refuses to run unless all three are present and genuinely unsatisfiable, and
unless nothing else has become impossible by accident:

| Shape | The conflict |
| --- | --- |
| arithmetic | Operations is **11 people** who must sit together; a table seats 10 |
| contradiction | Finance's 8 must sit together, and **Marcus Deel and Priya Raman** must be kept apart |
| triangle | **Nina Alcott** must sit with both Carol Beaufort and Douglas Wren, who must not sit with each other |

Three different shapes on purpose. A model that catches the arithmetic one
often walks straight past the triangle, and the Sep 28 original found a
fourth of its own — which is the better outcome and worth the voiceover if it
happens again.

The other 97 rows carry ordinary notes — a seat near the door, a nut allergy,
a new starter — so the three conflicts have to be found rather than being the
only notes on the page.

### Two names were changed after the first run

`Claude Bissett` became **Camille Bissett**: a guest called Claude on screen
in a piece about asking an AI reads as a joke nobody meant. And `Wren` came
out of the first-name list, because Douglas Wren is one of the three people
the conflicts hang on and a second Wren in the room muddies the read.

### Brand look

Header row lavender `#CECBF6` with deep purple `#3C3489` bold text, frozen,
columns at 200 / 150 / 420 px so the longest note reads without wrapping.

## The December Drive folders

Created Thu 26 Nov, after checking the parent for an existing one — Drive
allows duplicate names and a second `November` had to be trashed last month.
A listing of the parent returned September, October and `November ` only, and
its next page was empty, so nothing existed to collide with.

| Folder | Id |
| --- | --- |
| `December` | `1-5wxcU4RTQyi8OhAJ7qD3UvRoNgTn71w` |
| `December 1` | `1yLIBHMcwXSWFoPiqzW5E0VDmueYLdtV4` |

`December 1` inherits **`anyoneWithLink: reader`**, checked rather than
assumed, so a recording she drops in it downloads from here without her
having to share anything.
