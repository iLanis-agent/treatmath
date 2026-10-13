# Treat math

Halloween candy arithmetic: the street names the kids, the kids name the pieces, and the bags name the leftovers.

Live at https://ilanis-agent.github.io/treatmath/

## The three tools

- **Kid plan** - kids = round(houses x labeled 70 percent lit x labeled 1.5 kids a knock), with quiet-street, lively-block and destination-neighborhood bands.
- **Treat plan** - pieces = kids x labeled 3 each; bags = ceil(pieces / labeled 250), with porch-bowl, neighborhood-favorite and legend-of-the-street bands.
- **Leftover plan** - left = bags x labeled 250 - kids x labeled 3, with clean-sweep, barely-a-wrapper, desk-drawer-stash and November-of-lunches bands.

## Formulas and limits

- Kid counts are rounded to whole kids (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: lit rate, knock size, pieces per kid, bag size.
- Illustrative planning arithmetic only. Last year's actual door count beats any forecast. Keep a labeled non-food bowl so teal-pumpkin visitors get a treat too.

## Development

- `engine.js` - calculation and render engine (browser global `TreatMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
