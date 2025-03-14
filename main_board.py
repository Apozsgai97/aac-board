import tkinter as tk
from text_to_speech import speak
from questions_board import open_questions

words = [
    ["I", "is", "want", "Time", "More things"],
    ["you", "can", "like", "not", "Places"],
    ["it", "do", "go", "more", "Descriptors"],
    ["People", "have", "stop", "to", "Food & Drink"],
    ["Questions", "help", "Actions", "Connecting Words", "Animals"]]


def create_buttons(root, speak_button, delete_button, back_button, update_input):
    back_button.grid_forget()
    for i, row in enumerate(words):
        for index, word in enumerate(row):
            if index == 0 and i == 4:
                color = "blue"
            elif index == 0:
                color = "#FFCC00"
            elif index == 1 or index == 2:
                color = "green"
            elif index == 4 or index == 3 and i == 0:
                color = "purple"
            elif index == 3:
                color = "orange"

            if word == "Questions":
                button = tk.Button(root, text=word, width=20,
                                   height=4, font=("Arial", 16), highlightbackground=color, bg=color, command=lambda: [open_questions(root, speak_button, delete_button, back_button, update_input)])
                button.grid(row=i + 1, column=index, padx=5, pady=5)
            else:
                button = tk.Button(root, text=word, width=20,
                                   height=4, font=("Arial", 16), highlightbackground=color, bg=color, command=lambda w=word: [update_input(w), speak(w)])
                button.grid(row=i + 1, column=index, padx=5, pady=5)
