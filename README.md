# Bingo-Py

A terminal-based multiplayer Bingo game written in Python. 
Supports 2 to 5 players with randomized boards and a live scoreboard.

## Features
- Multiplayer support (2–5 players)
- Auto-generated randomized 5x5 Bingo boards per player
- Shared number marking across all player boards
- Detects winning rows, columns, and diagonals
- Live scoreboard with points at the end

## How to Run
```bash
python bingo.py
```

## How to Play
1. Enter number of players (2–5)
2. Each player enters their name
3. Players take turns choosing a number to mark
4. The chosen number gets marked (⭐) on all boards
5. First player to complete 5 lines wins

## Tech
- Python 3
- `random` module (standard library)
