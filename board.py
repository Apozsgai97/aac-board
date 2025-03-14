import tkinter as tk


root = tk.Tk()
root.title("AAC Board")

words = [
    ["I", "is", "want", "Time", "More things"],
    ["you", "can", "like", "not", "Places"],
    ["it", "do", "go", "more", "Come"],
    ["People", "have", "stop", "to", "Food & Drink"],
    ["Questions", "help", "Actions", "Connecting Words", "Animals"]]


def create_buttons():
    for i, row in enumerate(words):
        for index, word in enumerate(row):
            button = tk.Button(root, text=word, width=10,
                               height=3, font=("Arial", 12))
            button.grid(row=i, column=index)


create_buttons()

root.mainloop()
