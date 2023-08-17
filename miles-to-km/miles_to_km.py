from tkinter import *

# TODO-1: Create a Tk window and relevant title
# TODO-2: Create an entry field and a label called 'Miles' next to it
# TODO-3: Create Labels for Km value, 'is equal to 0 Km'
# TODO-4: Create a 'Calculate' button, convert Miles to Km, and display answer on a label (replace default 0)
# TODO-5: Order widgets using grid

FONT = ('Arial', 15)
DEFAULT_VAL = '0'


def calculate_in_km():
    """convert a miles val to a Km val and display on label"""
    miles_str = miles_input.get()
    if miles_str.isdigit():
        # formula to convert from miles to Km
        result_km = int(miles_input.get()) * 1.609344
        result_km = round(result_km, 2)
        km_val_label.config(text=str(result_km))


# Tk window
window = Tk()
window.minsize(width=300, height=100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Miles Entry
miles_input = Entry(width=10)
# Miles Label
miles_label = Label(text="Miles", font=FONT)
# Km Labels
label_is_equal = Label(text="is equal to", font=FONT)
km_val_label = Label(text=DEFAULT_VAL, font=FONT)
km_label = Label(text="Km", font=FONT)
# Button Calculate
calc_button = Button(text='Calculate', command=calculate_in_km)

# Position a widget in the parent widget in a grid.
miles_input.grid(column=1, row=0, padx=10, pady=10)
miles_label.grid(column=2, row=0, padx=10, pady=10)
label_is_equal.grid(column=0, row=1, padx=10, pady=10)
km_val_label.grid(column=1, row=1, padx=10, pady=10)
km_label.grid(column=2, row=1, padx=10, pady=10)
calc_button.grid(column=1, row=2, padx=10, pady=10)

window.mainloop()
