from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_index = 0
next_word = {}
to_learn = pandas.read_csv("data/german_words.csv").to_dict(orient="records")
random.shuffle(to_learn)

def next_card():
    global current_index, flip_card_after, next_word
    window.after_cancel(flip_card_after)

    next_word = to_learn[current_index % len(to_learn)]
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=next_word["German"], fill="black")

    flip_card_after = window.after(ms=3000, func=flip_card)

    current_index += 1

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=next_word["English"], fill="white")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, font=("Arial", 40, 'italic'), fill="black")
card_word = canvas.create_text(400, 263, font=("Arial", 60, 'italic'), fill="black")

canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, border=0, command=next_card)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, border=0, command=next_card)
tick_button.grid(row=1, column=1)

flip_card_after = window.after(ms=3000, func=flip_card)
next_card()


window.mainloop()


