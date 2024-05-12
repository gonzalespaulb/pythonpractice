from tkinter import *
import string
import random
password_file = "./100days/data.txt"

window = Tk()
window.title("PassMAN")
window.minsize(height=200, width=200)
window.config(padx=20, pady=20)

# NOTE ----------------------------------------------- PASSWORD GENERATOR LOGIC

all_letters = list(string.ascii_letters)
all_punctuations = list(string.punctuation)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def password_generate(): 
    all_choices = []
    for _ in range(3): 
        all_choices.append(random.choice(all_letters))
        all_choices.append(random.choice(all_punctuations))
        all_choices.append(random.choice(numbers))

    random.shuffle(all_choices)
    password = ''.join(map(str, all_choices))
    password_input.insert(0, password)
    

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


generate_button = Button(text="Generate Password", command=password_generate)
generate_button.grid(row=2, column=2)

window.mainloop()

# NOTE ----------------------------------------------- TRY EXCEPT LOGIC

# fruits = ["Apple", "Peach", "Pineapple"]

# def make_pie(index): 
#     try:
#         fruit = fruits[int(index)]
#     except ValueError: 
#         print("The input you added is not a number.")
#     except IndexError: 
#         new_fruit = input("This fruit does not exist, let's add it to the list.\n")
#         fruits.append(new_fruit)
#         make_pie(fruits.index(new_fruit))
#     else: 
#         print(fruit + "pie")


# make_pie(4)