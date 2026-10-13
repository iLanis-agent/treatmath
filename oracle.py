import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round0(x): return jsnum(math.floor(x + 0.5))

LIT_PCT = 70
KIDS_PER_HOUSE = 1.5
PIECES_PER_KID = 3
BAG_PIECES = 250

def kid_plan(houses):
    if not (houses > 0):
        return {"error": "the houses must be positive"}
    kids = round0(houses * LIT_PCT / 100 * KIDS_PER_HOUSE)
    if kids <= 20: verdict = "a quiet street"
    elif kids <= 60: verdict = "a lively block"
    else: verdict = "a destination neighborhood"
    return {"kids": kids, "verdict": verdict}

def treat_plan(kids):
    if not (kids > 0):
        return {"error": "the kids must be positive"}
    pieces = kids * PIECES_PER_KID
    bags = math.ceil(pieces / BAG_PIECES)
    if bags <= 1: verdict = "a porch-bowl night"
    elif bags <= 4: verdict = "a neighborhood favorite"
    else: verdict = "a legend of the street"
    return {"pieces": pieces, "bags": bags, "verdict": verdict}

def leftover_plan(bags, kids):
    if not (bags > 0) or not (kids > 0):
        return {"error": "the bags and the kids must be positive"}
    bought = bags * BAG_PIECES
    given = kids * PIECES_PER_KID
    left = bought - given
    if left <= 0: verdict = "a clean sweep"
    elif left <= 50: verdict = "barely a wrapper"
    elif left <= 200: verdict = "a desk-drawer stash"
    else: verdict = "a November of lunches"
    return {"bought": bought, "given": given, "left": left, "verdict": verdict}

def render_kids(r, houses):
    return ("Your " + fmt(houses) + "-house route at a labeled " + fmt(LIT_PCT) + " percent lit rate and "
            + fmt(KIDS_PER_HOUSE) + " kids a knock names about " + plural(r["kids"], "kid") + " - " + r["verdict"] + ".")

def render_treats(r, kids):
    return ("Those " + fmt(kids) + " kids at a labeled " + fmt(PIECES_PER_KID) + " pieces each ask " + fmt(r["pieces"])
            + " pieces - " + plural(r["bags"], "bag") + " of labeled " + fmt(BAG_PIECES) + ", " + r["verdict"] + ".")

def render_leftover(r, bags, kids):
    return ("With " + plural(bags, "bag") + " bought and " + fmt(kids) + " kids served at a labeled "
            + fmt(PIECES_PER_KID) + " pieces each, " + fmt(r["left"]) + " pieces stay home - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[40],[15],[10],[80],[25],[60],[5],[100],[0],[50]]:
    add("kidPlan", kid_plan, render_kids, a)
for a in [[42],[20],[84],[200],[400],[90],[10],[500],[0],[150]]:
    add("treatPlan", treat_plan, render_treats, a)
for a in [[1,42],[2,42],[1,80],[1,84],[4,400],[2,200],[3,100],[1,60],[0,42],[1,0]]:
    add("leftoverPlan", leftover_plan, render_leftover, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
