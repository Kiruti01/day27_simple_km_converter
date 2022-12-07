from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometers_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# label

miles_label = Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(column=3, row=0)

km_label = Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(column=3, row=2)

is_equal_to = Label(text="is equal to", font=("Arial", 20, "bold"))
is_equal_to.grid(column=0, row=2)

kilometers_result_label = Label(text="0", font=("Arial", 20, "bold"))
kilometers_result_label.grid(column=2, row=2)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=3)



# Entry
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=2, row=0)

window.mainloop()

