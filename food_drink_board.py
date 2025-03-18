
import tkinter as tk
from text_to_speech import speak
from automation import sort_words

FOOD_DRINK_WORDS = [
    "Water", "Juice", "Milk", "Tea",
    "Apple", "Banana", "Orange", "Grapes", "Mango",
    "Bread", "Rice", "Pasta", "Pizza", "Burger",
    "Cheese", "Eggs", "Yogurt", "Butter", "Honey",
    "Coffee", "Soda", "Smoothie", "Wine", "Beer"
]


def open_food_drink(root, speak_button, delete_button, back_button, update_input):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget not in [speak_button, delete_button]:
            widget.grid_forget()

    back_button.grid(row=1, column=0, padx=5, pady=5)

    sorted_food_drink = sort_words(FOOD_DRINK_WORDS)

    for i, row in enumerate(sorted_food_drink):
        for index, word in enumerate(row):
            button = tk.Button(root, text=word, width=20,
                               height=4, font=("Arial", 16), highlightbackground="blue", bg="blue", command=lambda w=word: [update_input(w), speak(w)])
            start_column = 1 if i == 0 else 0
            button.grid(row=i + 1, column=start_column+index, padx=5, pady=5)
