from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20,pady=20)

# label
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

to_label = Label(text="is equal to")
to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)



# button

button = Button(text="Calculate",command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
