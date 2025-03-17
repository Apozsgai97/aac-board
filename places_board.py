import tkinter as tk
from text_to_speech import speak
PLACES_WORDS = [
    ["Home", "School", "Work", "Store"],
    ["Park", "Hospital", "Restaurant", "Library", "Mall"],
    ["Beach", "Mountain", "Forest", "City", "Farm"],
    ["Bathroom", "Kitchen", "Bedroom", "Living Room", "Garden"],
    ["Airport", "Bus Stop", "Train Station", "Parking Lot", "Street"]
]


def open_places(root, speak_button, delete_button, back_button, update_input):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget not in [speak_button, delete_button]:
            widget.grid_forget()

    back_button.grid(row=1, column=0, padx=5, pady=5)

    for i, row in enumerate(PLACES_WORDS):
        for index, word in enumerate(row):
            button = tk.Button(root, text=word, width=20,
                               height=4, font=("Arial", 16), highlightbackground="purple", bg="purple", command=lambda w=word: [update_input(w), speak(w)])
            start_column = 1 if i == 0 else 0
            button.grid(row=i + 1, column=start_column+index, padx=5, pady=5)
