import tkinter as tk
import pyttsx3

root = tk.Tk()
root.title("AAC Board")

words = [
    ["I", "is", "want", "Time", "More things"],
    ["you", "can", "like", "not", "Places"],
    ["it", "do", "go", "more", "Descriptors"],
    ["People", "have", "stop", "to", "Food & Drink"],
    ["Questions", "help", "Actions", "Connecting Words", "Animals"]]

text_input = tk.Entry(root, width=70, font=("Arial", 16))
text_input.grid(row=0, column=1, columnspan=3)

speak_button = tk.Button(root, text="Speak", width=20,
                         height=2, font=("Arial", 16), highlightbackground="red", command=lambda: speak(text_input.get()))
speak_button.grid(row=0, column=0)

delete_button = tk.Button(root, text="Delete", width=20,
                          height=2, font=("Arial", 16), highlightbackground="red", command=lambda: text_input.delete(0, tk.END))
delete_button.grid(row=0, column=4)

back_button = tk.Button(root, text="Back", width=20,
                        height=4, font=("Arial", 16), highlightbackground="black", command=lambda: create_buttons())


def update_input(text):
    text_input.insert(tk.END, " " + text)


def speak(text):
    if text:
        text = text.lower()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


def open_questions():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget not in [speak_button, delete_button]:
            widget.grid_forget()

    back_button.grid(row=1, column=0, padx=5, pady=5)

    questions_words = [
        ["What", "Where", "Who", "When"],
        ["Question", "Why", "Which", "Whose", "Whom"],
        ["How", "How much", "How many", "How often", "How long"]]

    for i, row in enumerate(questions_words):
        for index, word in enumerate(row):
            button = tk.Button(root, text=word, width=20,
                               height=4, font=("Arial", 16), highlightbackground="blue", bg="blue", command=lambda w=word: [update_input(w), speak(w)])
            start_column = 1 if i == 0 else 0
            button.grid(row=i + 1, column=start_column+index, padx=5, pady=5)


def create_buttons():
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
                                   height=4, font=("Arial", 16), highlightbackground=color, bg=color, command=lambda: [open_questions()])
                button.grid(row=i + 1, column=index, padx=5, pady=5)
            else:
                button = tk.Button(root, text=word, width=20,
                                   height=4, font=("Arial", 16), highlightbackground=color, bg=color, command=lambda w=word: [update_input(w), speak(w)])
                button.grid(row=i + 1, column=index, padx=5, pady=5)


create_buttons()

root.mainloop()
