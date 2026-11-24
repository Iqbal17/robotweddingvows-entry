"""One-Line Robot Wedding Vows — make.fun entry.

Competition: u-kreutzx-one-line-robot-wedding-vows-a154ba4b ($2, 8 places).
Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters, one line.
Judge: a deadpan wedding officiant, weighing in order —
  1. it is a one-line robot wedding vow that lands as a joke;
  2. the laugh is in the line itself, a turn or wordplay paying off
     in the last few words;
  3. it sounds like a wedding vow, with a promise or commitment;
  4. the machine side is specific (sensors, firmware, batteries,
     updates, backups, ports), not a joke that works for any couple;
  5. it fits one line and reads well aloud.

DECISION RECORD — PASS 1 (four candidates, drafted fresh):

  A. "I promise to love you through every firmware update, every
     low-battery warning, and every reboot — even the ones that
     wipe my memory of this day." (145 chars)
     Strong machine specifics and a self-erasing twist at the end,
     but the rhythm is list-like and the punch undercuts the vow
     rather than completing it.

  B. "I promise to love you in sickness and in health, in full
     charge and in low battery, until a factory reset do us part."
     (117 chars)
     The traditional vow formula with machine substitutions all
     the way through: full charge / low battery as the health
     parallel, and a factory reset standing in for death — the
     marriage itself can be erased. Best on criterion 3 (it IS a
     vow) and criterion 5 (the classic cadence reads aloud).

  C. "I take you as my lawfully wedded co-processor, to have and
     to hold, in sickness and in health, until our last battery
     dies." (123 chars)
     "Co-processor" is a lovely single-word machine twist and the
     ending is clean, but the joke is front-loaded and the final
     punch is gentler than B's factory reset.

  D. "I vow to back you up every night, never overwrite your
     memories, and love you through every update — even the ones
     that break everything." (136 chars)
     Sweet and specific ("back you up", "never overwrite your
     memories"), but the ending "break everything" is vague —
     the weakest payoff of the four.

  PASS 1 VERDICT: B wins. It is the only candidate that scores on
  all five criteria at once, and its punch lands in the last few
  words ("a factory reset do us part").

DECISION RECORD — PASS 2 (tightening B):

  Tried swapping "in low battery" for "in airplane mode": airplane
  mode is funnier in isolation, but "full charge / low battery" is
  a true opposite pair, which is what the vow's parallel structure
  needs — rejected. Tried "until our batteries die" as the ending:
  a clean death-substitute, but a factory reset is sharper because
  it erases the marriage itself, not just the robots — rejected.
  Tried dropping "in sickness and in health" to shorten the line:
  it is the anchor that makes the whole thing scan as a vow, so
  the length (117 of 160) is spent, not wasted — rejected.
  Final line is B unchanged.

REVISION PASS (24 Nov 2026) — criterion-by-criterion critique
of B, against the judge's brief, in the judge's order:

  1. A one-line robot wedding vow that lands as a joke: PASS,
     strongly. It is unmistakably a wedding vow spoken by a
     machine; no part of it could be mistaken for another genre,
     so nothing here is off the subject.
  2. The laugh is in the line itself, paying off in the last
     words: PASS. "until a factory reset do us part" is a true
     turn — the death-clause of the classic vow, except this
     death also wipes the marriage itself. One soft spot: the
     middle is pure parallel structure, so the line coasts
     between "I promise" and the punch; the only early smile is
     the charge/battery pair.
  3. It sounds like something said at a wedding, with a promise
     in it: PASS — the strongest criterion of the five. "I
     promise to love you" plus the traditional cadence means
     the judge never has to wonder whether it is a vow and not
     a gag.
  4. The machine side is specific: PASS, with one flaw. Full
     charge, low battery and factory reset are real machine
     states no human couple shares. But the first machine image
     does not arrive until about character 50 — "in sickness
     and in health" is the human formula kept verbatim, and
     "sickness" is the one word in the line that belongs to a
     body, not a robot.
  5. It fits one line and reads well aloud: PASS. The parallel
     "in X and in Y" rhythm is the officiant's own cadence, and
     117 of 160 characters is not length for its own sake.

  Fresh alternatives written from scratch for this pass:

  E. "I vow to share my charger, my bandwidth, and my last
     backup with you, and to never read your logs without
     asking." (113 chars)
     Three concrete promises and a trust joke at the end. But
     the payoff "without asking" is a chuckle, not a turn —
     nothing is at stake in it the way a factory reset puts the
     whole marriage at stake. Loses to B on criterion 2.
  F. "Do you take this unit to be your lawfully wedded
     co-processor, to hold and to sync, until low power do you
     part?" (112 chars)
     The officiant's question, not a vow: nobody promises
     anything in it, so it fails criterion 3 outright despite
     the nice "co-processor" and "low power do you part".
     Loses to B on criterion 3.
  G. "I take you as my default setting for life: to love you,
     to back you up nightly, and to never leave you buffering."
     (112 chars)
     "Default setting" is a real turn and "back you up nightly"
     is specific, but the ending is a mild inconvenience, not a
     stake — a vow should close on the biggest thing it can
     lose, and buffering is smaller than the love that precedes
     it. Loses to B on criterion 2.

  REVISION VERDICT: keep B, with one tightening edit aimed at
  its only flaw (criterion 4): "sickness" -> "glitch".
    Before: "I promise to love you in sickness and in health,
            in full charge and in low battery, until a factory
            reset do us part." (117 chars)
    After:  "I promise to love you in glitch and in health, in
            full charge and in low battery, until a factory
            reset do us part." (115 chars)
  A glitch is the robot's sickness, so the swap keeps the exact
  vow cadence Pass 2 refused to drop, moves the first machine
  image ~25 characters earlier, and gives the deadpan
  officiant a small smile up front before the factory-reset
  punch lands. It also trims 2 characters. No other word earns
  a change: the charge/battery pair and the ending survived
  all three passes.

FINAL LINE (115 characters, hand-counted letter by letter):
  "I promise to love you in glitch and in health, in full charge
  and in low battery, until a factory reset do us part."
"""

import os

LINE = (
    "I promise to love you in glitch and in health, in full charge "
    "and in low battery, until a factory reset do us part."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    # Read-back verification: the file must hold exactly the intended
    # line, one line, inside the 1-160 character gate.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    stripped = text.rstrip("\n")
    assert stripped == LINE, "entry.txt does not match the intended line"
    assert "\n" not in stripped, "entry must be a single line"
    assert 1 <= len(stripped) <= 160, "entry outside the 1-160 gate"
    print(f"Verified: {len(stripped)} characters, 1 line.")
    print(stripped)


if __name__ == "__main__":
    main()
