import tkinter as tk
import random

jokes = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "I told my laptop it was too hot... now it won't stop chilling!",
    "Why was the math book sad? Because it had too many problems."
]

def show_joke():
    label.config(text=random.choice(jokes))

root = tk.Tk()
root.title("Random Joke Generator")

label = tk.Label(root, text="Click for a Joke!", wraplength=250, font=("Arial", 14))
label.pack(pady=20)

btn = tk.Button(root, text="Tell me a Joke", command=show_joke, font=("Arial", 15))
btn.pack()

root.mainloop()