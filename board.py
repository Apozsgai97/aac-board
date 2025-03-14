import tkinter as tk
from text_to_speech import speak
from main_board import create_buttons

root = tk.Tk()
root.title("AAC Board")

text_input = tk.Entry(root, width=70, font=("Arial", 16))
text_input.grid(row=0, column=1, columnspan=3)

speak_button = tk.Button(root, text="Speak", width=20,
                         height=2, font=("Arial", 16), highlightbackground="red", command=lambda: speak(text_input.get()))
speak_button.grid(row=0, column=0)

delete_button = tk.Button(root, text="Delete", width=20,
                          height=2, font=("Arial", 16), highlightbackground="red", command=lambda: text_input.delete(0, tk.END))
delete_button.grid(row=0, column=4)

back_button = tk.Button(root, text="Back", width=20,
                        height=4, font=("Arial", 16), highlightbackground="black", command=lambda: create_buttons(root, speak_button, delete_button, back_button, update_input))


def update_input(text):
    text_input.insert(tk.END, " " + text)

create_buttons(root, speak_button, delete_button, back_button, update_input)

root.mainloop()
