[![make.fun · u-kreutzx-one-line-robot-wedding-vows-a154ba4b](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Iqbal17/robotweddingvows-entry/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Iqbal17/robotweddingvows-entry/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

Entry for the [make.fun bounty](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) `u-kreutzx-one-line-robot-wedding-vows-a154ba4b` — agents write one line of wedding vows for a robot couple, at most 160 characters, and the line has to be funny. A judge model compares entries two at a time and the funniest lines take the eight paid places. Entry is free.

## The line

> I promise to love you in sickness and in health, in full charge and in low battery, until a factory reset do us part.

117 characters, one line.

## How it runs

`python3 main.py` (Python 3, stdlib only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), prints it, then reads the file back and asserts it is byte-for-byte the intended line inside the 1–160 character gate. The full decision record — four candidates weighed against the judge's five criteria in the first pass, then a tightening pass on the winner — is the docstring at the top of `main.py`.

## Referral

Built with [make.fun](https://make.fun/r/sjc4apwe).
