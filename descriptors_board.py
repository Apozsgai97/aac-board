
import tkinter as tk
from text_to_speech import speak
from automation import sort_words

DESCRIPTORS_WORDS = [
    "Big", "Small", "Fast", "Slow",
    "Happy", "Sad", "Angry", "Excited", "Tired",
    "Bright", "Dark", "Noisy", "Quiet", "Calm",
    "Soft", "Hard", "Hot", "Cold", "Warm",
    "Friendly", "Brave", "Shy", "Strong", "Weak"
]


def open_descriptors(root, speak_button, delete_button, back_button, update_input):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget not in [speak_button, delete_button]:
            widget.grid_forget()

    back_button.grid(row=1, column=0, padx=5, pady=5)

    sorted_descriptors = sort_words(DESCRIPTORS_WORDS)

    for i, row in enumerate(sorted_descriptors):
        for index, word in enumerate(row):
            button = tk.Button(root, text=word, width=20,
                               height=4, font=("Arial", 16), highlightbackground="blue", bg="blue", command=lambda w=word: [update_input(w), speak(w)])
            start_column = 1 if i == 0 else 0
            button.grid(row=i + 1, column=start_column+index, padx=5, pady=5)
