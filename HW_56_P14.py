import tkinter as tk
import random

# Game logic
def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""

    if player_choice == computer_choice:
        result = "It's a Draw!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=f"🤖 Computer chose: {computer_choice}\n🧠 {result}")
    score_label.config(text=f"🏆 Your Score: {player_score} | 🤖 Computer: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

player_score = 0
computer_score = 0

tk.Label(root, text="Choose Rock, Paper or Scissors:", font=("Arial", 14)).pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="🪨 Rock", width=12, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="📄 Paper", width=12, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="✂️ Scissors", width=12, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

# Score Display
score_label = tk.Label(root, text="🏆 Your Score: 0 | 🤖 Computer: 0", font=("Arial", 12))
score_label.pack()

root.mainloop()
