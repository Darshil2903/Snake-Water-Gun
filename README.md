# Snake Water Gun

A Python take on **Snake–Water–Gun**, the South Asian version of rock–paper–scissors. You play **6 rounds** against a computer opponent that picks at random, and your score is shown at the end.

## Rules

| Move | Beats | Because |
|---|---|---|
| 🐍 Snake (`s`) | 💧 Water | the snake drinks the water |
| 💧 Water (`w`) | 🔫 Gun | the gun gets soaked |
| 🔫 Gun (`g`) | 🐍 Snake | the gun shoots the snake |

The same move on both sides is a tie.

## How to play

```bash
python "Snake Water Gun Game.py"
```

Each round, type `s`, `w` or `g` and press Enter. The game shows the computer's move and whether you won, lost or tied.

## How it works

- `funtion()` maps `random.randint(1, 3)` to the computer's move.
- `gamewin()` returns `True` (win), `False` (loss) or `None` (tie) from the two moves.
- A `for` loop runs 6 rounds and adds up your points.

## Ideas for next time

- Validate input so a typo doesn't count as a round
- Replace the nested `if`s with a lookup table (`BEATS = {"s": "w", "w": "g", "g": "s"}`)
- Track wins, losses and ties separately and add a best-of-N mode
