from tkinter import *

def m_to_km():
    m = miles_input.get()
    km = float(m) * 1.689
    kilometer_result.config(text=f"{round(km,2)}")


window = Tk()
window.title("Miles to Kilometers")
window.minsize(height=20, width= 30)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to: ")
is_equal_to.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=3, row=1)

calculate_button = Button(text="Calculate", command=m_to_km)
calculate_button.grid(column=1, row=3)

window.mainloop()
