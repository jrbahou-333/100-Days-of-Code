from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 30, "italic")
WORD_FONT = ("Arial", 50, "bold")
# Functionality
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def new_word():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="FRENCH", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=img_bg_front)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card_background, image=img_bg_back)
    canvas.itemconfig(title_text, text="ENGLISH", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# UI Setup
window = Tk()
window.title("Flashy")
window.minsize(width=900, height=600)
window.config(padx=20, pady=20, background="#B1DDC6")

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=900, height=600, highlightthickness=0, background="#B1DDC6")
img_bg_front = PhotoImage(file="./images/card_front.png")
img_bg_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(450, 300, image=img_bg_front)
title_text = canvas.create_text(450, 200, text="FRENCH", font=TITLE_FONT, fill="black")
word_text = canvas.create_text(450, 280, text="Click a button", font=WORD_FONT, fill="black")
canvas.grid(column=0, row=0, columnspan=2)

img_right = PhotoImage(file="./images/right.png")
right_button = Button(image=img_right, highlightthickness=0, background="#B1DDC6", command=is_known)
right_button.grid(row=1, column=0)

img_wrong = PhotoImage(file="./images/wrong.png")
right_button = Button(image=img_wrong, highlightthickness=0, background="#B1DDC6", command=new_word)
right_button.grid(row=1, column=1)










window.mainloop()

