# Blackjack Game

Welcome to the Blackjack Game! This Python script allows you to play the classic game of Blackjack against the computer. Try to get a hand value as close to 21 as possible without exceeding it. Face cards are worth 10, and Aces can be worth either 1 or 11, depending on which value benefits you more.

## How to Play

1. Run the `main.py` script.
2. Follow the on-screen instructions to receive your initial hand and decide whether to draw additional cards ("hit") or pass.
3. Your goal is to have a hand value closer to 21 than the computer without going over.
4. After your turn, the computer will draw cards until its hand value is 17 or higher.
5. The winner will be determined based on the hand values.


## Features

- Standard Blackjack rules.
- Interactive user interface.
- ASCII art for visual appeal.

## Art

The ASCII art logo for the game is stored in `art.py` and adds a thematic touch to the Blackjack experience.

```python
# art.py
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
```

## How to Run

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:Sakib-Dalal/Black-Jack-Game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Black-Jack-Game
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

*Enjoy the game of Blackjack!*

---

*This project is developed by Sakib Dalal. For more details, please visit the [GitHub repository](git@github.com:Sakib-Dalal/Black-Jack-Game.git).*
