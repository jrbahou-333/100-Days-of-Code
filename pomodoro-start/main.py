from tkinter import *
from PIL import ImageTk, Image
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 5
SHORT_BREAK_SEC = 3
LONG_BREAK_SEC = 10
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg= GREEN)
    counter.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    if reps % 8 == 0:
        countdown(LONG_BREAK_SEC)
        timer_label.config(text="Long Break - go make some tea", fg=PINK)
    elif reps % 2 ==0:
        countdown(SHORT_BREAK_SEC)
        timer_label.config(text="Short Break", fg=GREEN)
    else:
        countdown(WORK_SEC)
        timer_label.config(text="Work BITCH", fg=RED)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = floor(count / 60)
    if count_min <= 9:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checks = ""
        work_sessions = floor(reps/2)
        for n in range(work_sessions):
            checks += "✅"
        counter.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#below method for inserting an image was due to having an old version of Python
tomato_img = ImageTk.PhotoImage(Image.open("tom.jpg"))
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

counter = Label(text="️", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
counter.grid(column=1, row=3)

window.mainloop()