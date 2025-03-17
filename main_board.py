import tkinter as tk
from text_to_speech import speak
from questions_board import open_questions
from time_board import open_time
from places_board import open_places
from animals_board import open_animals
from food_drink_board import open_food_drink
from more_things_board import open_more_things
from descriptors_board import open_descriptors

WORDS = [
    ["I", "is", "want", "Time", "More things"],
    ["you", "can", "like", "not", "Places"],
    ["it", "do", "go", "more", "Descriptors"],
    ["People", "have", "stop", "to", "Food & Drink"],
    ["Questions", "help", "Actions", "Connecting Words", "Animals"]]

WORD_FUNCTIONS = {
    "Questions": open_questions,
    "Time": open_time,
    "Places": open_places,
    "Animals": open_animals,
    "Food & Drink": open_food_drink,
    "More things": open_more_things,
    "Descriptors": open_descriptors
}


def create_buttons(root, speak_button, delete_button, back_button, update_input):
    back_button.grid_forget()
    for i, row in enumerate(WORDS):
        for index, word in enumerate(row):

            if word in WORD_FUNCTIONS:
                command_function = lambda w=word: WORD_FUNCTIONS[w](root, speak_button, delete_button, back_button, update_input)
            else:
                command_function = lambda w=word: [update_input(w), speak(w)]

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
            else:
                color = "grey"

            button = tk.Button(root, text=word, width=20,
                               height=4, font=("Arial", 16), highlightbackground=color, bg=color,  command=command_function
                               )
            button.grid(row=i + 1, column=index, padx=5, pady=5)
