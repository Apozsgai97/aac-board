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
            button = tk.Button(root, text=word, width=10,
                               height=3, font=("Arial", 12), command=lambda w=word: speak(w))
            button.grid(row=i, column=index)


create_buttons()

root.mainloop()
