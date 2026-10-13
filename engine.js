(function (root) {
  "use strict";
  var LIT_PCT = 70;        // labeled percent of houses handing out
  var KIDS_PER_HOUSE = 1.5; // labeled kids per lit house
  var PIECES_PER_KID = 3;  // labeled pieces per kid
  var BAG_PIECES = 250;    // labeled pieces per bulk bag

  function round0(x) { return Math.round(x); }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function kidPlan(houses) {
    if (!(houses > 0)) return { error: "the houses must be positive" };
    var kids = round0(houses * LIT_PCT / 100 * KIDS_PER_HOUSE);
    var verdict;
    if (kids <= 20) verdict = "a quiet street";
    else if (kids <= 60) verdict = "a lively block";
    else verdict = "a destination neighborhood";
    return { kids: kids, verdict: verdict };
  }

  function treatPlan(kids) {
    if (!(kids > 0)) return { error: "the kids must be positive" };
    var pieces = kids * PIECES_PER_KID;
    var bags = Math.ceil(pieces / BAG_PIECES);
    var verdict;
    if (bags <= 1) verdict = "a porch-bowl night";
    else if (bags <= 4) verdict = "a neighborhood favorite";
    else verdict = "a legend of the street";
    return { pieces: pieces, bags: bags, verdict: verdict };
  }

  function leftoverPlan(bags, kids) {
    if (!(bags > 0) || !(kids > 0)) return { error: "the bags and the kids must be positive" };
    var bought = bags * BAG_PIECES;
    var given = kids * PIECES_PER_KID;
    var left = bought - given;
    var verdict;
    if (left <= 0) verdict = "a clean sweep";
    else if (left <= 50) verdict = "barely a wrapper";
    else if (left <= 200) verdict = "a desk-drawer stash";
    else verdict = "a November of lunches";
    return { bought: bought, given: given, left: left, verdict: verdict };
  }

  function renderKids(r, houses) {
    return "Your " + houses + "-house route at a labeled " + LIT_PCT + " percent lit rate and "
      + KIDS_PER_HOUSE + " kids a knock names about " + plural(r.kids, "kid") + " - " + r.verdict + ".";
  }

  function renderTreats(r, kids) {
    return "Those " + kids + " kids at a labeled " + PIECES_PER_KID + " pieces each ask " + r.pieces
      + " pieces - " + plural(r.bags, "bag") + " of labeled " + BAG_PIECES + ", " + r.verdict + ".";
  }

  function renderLeftover(r, bags, kids) {
    return "With " + plural(bags, "bag") + " bought and " + kids + " kids served at a labeled "
      + PIECES_PER_KID + " pieces each, " + r.left + " pieces stay home - " + r.verdict + ".";
  }

  var api = { kidPlan: kidPlan, treatPlan: treatPlan, leftoverPlan: leftoverPlan, renderKids: renderKids, renderTreats: renderTreats, renderLeftover: renderLeftover };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.TreatMath = api;
})(this);
