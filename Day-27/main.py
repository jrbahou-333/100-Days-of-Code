from tkinter import *

window = Tk()
window.title("My TK")
window.minsize(height=500, width= 500)


def update_text():
    new_text = input.get()
    label.config(text=new_text)

label = Label(text="My text")
label.pack()

button = Button(command=update_text)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()