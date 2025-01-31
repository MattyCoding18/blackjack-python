# 🃏 Blackjack Game (Python)

This is a **command-line Blackjack game** written in Python. The game follows standard **Blackjack rules**, where a player competes against the computer (dealer). The objective is to get a hand value **as close to 21 as possible without exceeding it**.

## 📌 Features
- **Randomized card draws** for both the player and the dealer.
- **Handles special rules** such as Blackjack, busts, and dealer auto-drawing.
- **Simple user inputs** to hit or stand.
- **Automatic game restart** after each round.

## 🛠 How to Play
1. **Run the Python script** to start the game.
2. You will be asked:  
   ➤ *"Do you want to play a game of Blackjack? Type 'y' or 'n'"*  
   - If **'y'**, the game starts.  
   - If **'n'**, the game exits.

3. You and the dealer receive **two starting cards**.
   - If you get **Blackjack (21)** immediately, you **win!**
   - If the dealer has **Blackjack**, you **lose!**
   - Otherwise, you decide your next move.

4. You can **hit ('y')** to take another card or **stand ('n')** to hold your hand.
   - If you go **over 21**, you **lose!**
   - If you hit **exactly 21**, you **win!**
   - The dealer **draws cards until at least 17**.

5. The game determines the **winner based on hand values**:
   - **Closest to 21 wins**.
   - If both have the same value, it's a **draw**.

## 💾 Requirements
- Python 3.x

## 🚀 How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/MattyCoding18/blackjack-python.git
   ```
2. **Navigate into the folder**:
   ```bash
   cd blackjack-python
   ```
3. **Run the script**:
   ```bash
   python blackjack.py
   ```

## 📷 Preview
```
Do you want to play a game of Blackjack? Type 'y' or 'n'
> y
Your cards: [10, 9], current score: 19
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass:
> n
Computer's cards: [8, 7], current score: 15
Computer drew a card: 5. Current score: 20
You Lose!
```

## 📌 Future Improvements
- Add **betting system** for more engagement.
- Improve **graphics/UI** for better visualization.
- Implement **multiple rounds with chip counting**.

---

🎯 **Enjoy playing Blackjack! Let me know if you have any suggestions for improvements.** 🚀
