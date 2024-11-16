import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
current_card = {}

def flip_card():
    english = current_card["English"]
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=f"{english}", fill="white")
    canvas.itemconfig(img, image=card_back_img)

flip_timer = window.after(3000, func=flip_card)

french_words = pandas.read_csv("french_words.csv")
to_learn =  french_words.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french = current_card["French"]

    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{french}", fill="black")
    canvas.itemconfig(img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="wrong.png")
check_img = PhotoImage(file="right.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()