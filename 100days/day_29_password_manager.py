from tkinter import *

window = Tk()
window.title("PassMAN")
window.minsize(height=200, width=200)
window.config(padx=20, pady=20)

# NOTE ----------------------------------------------- LABELS

website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=0, column=0)
username_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)

# NOTE ----------------------------------------------- INPUTS

website_input = Entry(width=20)
username_input = Entry()
password_input = Entry(width=20)

website_input.grid(row=0, column=1)
username_input.grid(row=1, column=1)
password_input.grid(row=2, column=1)

# NOTE ----------------------------------------------- BUTTONS

generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36)

generate_button.grid(row=2, column=2)
add_button.grid(row=3, column=1, columnspan=2)

window.mainloop()