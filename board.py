import tkinter as tk
import pyttsx3

root = tk.Tk()
root.title("AAC Board")

words = [
    ["I", "is", "want", "Time", "More things"],
    ["you", "can", "like", "not", "Places"],
    ["it", "do", "go", "more", "Come"],
    ["People", "have", "stop", "to", "Food & Drink"],
    ["Questions", "help", "Actions", "Connecting Words", "Animals"]]


def speak(text):
    text = text.lower()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def create_buttons():
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
            button = tk.Button(root, text=word, width=20,
                               height=4, font=("Arial", 16), highlightbackground=color, bg=color, command=lambda w=word: speak(w))
            button.grid(row=i, column=index, padx=5, pady=5)


create_buttons()

root.mainloop()
