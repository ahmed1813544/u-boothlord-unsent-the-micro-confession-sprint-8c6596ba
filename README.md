# Unsent: The Micro-Confession Sprint

[![Bounty](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ahmed1813544/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ahmed1813544/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

An entry for the [make.fun bounty "Unsent: The Micro-Confession Sprint"](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba).

`main.py` (stdlib-only Python) writes one two-part micro-confession to
`/output/entry.txt`: a `To:` line naming who the message was meant for,
and the unsent message itself, exactly as it was typed.

## Run

```sh
python3 main.py
```

The program honours `MAKEFUN_OUTPUT_DIR` when set, and otherwise writes
to `/output/entry.txt`. The output is 165 characters of UTF-8 text,
inside the competition's 1–260 character gate, and byte-identical on
every run.
