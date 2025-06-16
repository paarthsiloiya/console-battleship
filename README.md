# Battleship Console Game

```
 __          __  _                            _______       ____        _   _   _           _     _        
 \ \        / / | |                          |__   __|     |  _ \      | | | | | |         | |   (_)       
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___    | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __   
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \   |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \  
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |  | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) | 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/   |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/  
                                                                                                   | |     
                                                                                                   |_|     
                                                                                                           
By Paarth Siloiya
```

---

## About

A classic command-line Battleship game. Place your ships, guess your opponent's ship locations, and sink their fleet before they sink yours!  
Built for the terminal with a focus on classic grid-based mechanics and a clean, readable interface.

---

## How to Play

- **Cell Position:**  
  Type the row letter followed by the column number (e.g., `A3`, `F5`).  
  No spaces in between.

- **Ship Placement:**  
  Place all five standard ships: Carrier, Battleship, Cruiser, Submarine, Destroyer.  
  The game first asks you the orientation of the ship, then the starting tile of the ship.

  - **Examples:**

    ```
    CRUISER - with orientation right and starting position D4

         4    5    6    7    8    9
       ──┼────┼────┼────┼────┼────┼───
     C   │    │    │    │    │    │
       ──┼────┼────┼────┼────┼────┼───
     D   │ ██████████████████████ │
       ──┼────┼────┼────┼────┼────┼───
     E   │    │    │    │    │    │

	```
	```
    SUBMARINE - with orientation down and starting point E6

         5    6    7
       ───┼────┼──
     D    │    │
       ───┼────┼──
     E    │ ██ │
       ───┼─██─┼──
     F    │ ██ │
       ───┼─██─┼──
     G    │ ██ │
       ───┼────┼──
     H    │    │
    ```

- **Confirming Placement:**  
  After placing all the ships, if you are satisfied with your placements you can confirm it, or you can reset the board and start fresh.

- **Gameplay:**  
  You always start first. To play your move, type out the cell position.  
  If you guessed correctly or incorrectly, a corresponding message will appear.

- **Tracking Progress:**  
  You can keep track of the ships you destroyed by the visual indicator at the top:

  ```
      ⦿     🞅     🞅     🞅     🞅
  ```

---

## Visual Indicators

- `██` : Your ship
- `░░` : Damaged ship
- `🞮` : Hit
- `🞅` : Miss
- `⦿` : Destroyed enemy ship

---

## Standard Rules

- Take turns with the computer to guess ship locations.
- First to sink all enemy ships wins.

---

## Getting Started

1. Clone or download this repository.
2. Run the game in your terminal:
   ```
   python main.py
   ```
3. Follow the on-screen instructions.

---

## Credits

By Paarth Siloiya

---

Enjoy the battle!
