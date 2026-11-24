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

FINAL LINE (117 characters, hand-counted letter by letter):
  "I promise to love you in sickness and in health, in full charge
  and in low battery, until a factory reset do us part."
"""

import os

LINE = (
    "I promise to love you in sickness and in health, in full charge "
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
