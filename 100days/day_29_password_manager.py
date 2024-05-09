from tkinter import *
password_file = "./100days/data.txt"

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
website_input.focus()
username_input = Entry()
password_input = Entry(width=20)

website_input.grid(row=0, column=1)
username_input.grid(row=1, column=1)
password_input.grid(row=2, column=1)

# NOTE ----------------------------------------------- BUTTONS

generate_button = Button(text="Generate Password")

generate_button.grid(row=2, column=2)

def add_password(): 

    website_value = website_input.get()
    username_value = username_input.get()
    password_value = password_input.get()

    with open(password_file, mode="a") as file:
        file.write(f"{website_value} | {username_value} | {password_value}\n")


    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=3, column=1, columnspan=2)

window.mainloop()