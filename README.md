##🎮 NUMBER GUESSING GAME

A simple and interactive number guessing game written in **Python**, where the user tries to guess a randomly generated number between **1 and 100** within **5 attempts**.

##🚀 How It Works

* The computer generates a **random number** using the current timestamp.
* The user has **5 attempts** to guess the correct number.
* After each guess, the game responds with:

  * 🔼 **Too high**
  * 🔽 **Too low**
  * ✅ **Correct!**
* Handles invalid inputs gracefully (e.g., if user enters letters instead of numbers).
* Offers a **rematch** after each round.

## 📁 Files

* `number_guessing_game.py` – The main Python script that contains the complete game logic.
* `guessing.txt` – A text file that describes the game (you can use this README content for it).

## 🕹️ How to Play

1. Make sure you have **Python 3** installed on your system.
2. Run the script using your terminal or any IDE like VS Code:

```bash
python number_guessing_game.py
```
3. Follow the on-screen instructions to play.

📌 Game Features

* Custom number generator using the system's time for uniqueness.
* Input validation using `try-except`.
* Replayability with a **"Do you want to play again?"** prompt.
