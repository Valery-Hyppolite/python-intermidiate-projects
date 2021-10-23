from tkinter import *


def miles_to_km():
    miles = float(new_input.get())
    km = round(miles * 1.609)
    result_input.insert(0, km)
    #result_input.config(text=f"{km}")
def reset():
    new_input.delete(0, END)
    result_input.delete(0, END)

# create window
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

#Create input
new_input = Entry(text='Enter number', width=10)
new_input.grid(column=1, row=0)
new_input.get()

# create labels
mile_label = Label(text='Miles')
mile_label.grid(column=2, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

result_input = Entry(text='0', width=10)
result_input.grid(column=1, row=1)

km_label = Label(text='KM')
km_label.grid(column=2, row=1)

button = Button(text="Calculate", width=10, command=miles_to_km)
button.grid(column=0, row=2, columnspan=1)
reset_button = Button(text='Reset', width=10, command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()