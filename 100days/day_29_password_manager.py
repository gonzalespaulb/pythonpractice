from tkinter import *
from tkinter import messagebox
import string
import random
import json
password_file = "./100days/data.txt"
password_file_json = "./100days/data.json"

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

# NOTE ----------------------------------------------- ADD NEW PASSWORD

def add_password(): 

    website_value = website_input.get()
    username_value = username_input.get()
    password_value = password_input.get()
    new_data = {
        website_value: {
            "username":username_value,
            "password": password_value
        }
        }

    def check_and_update_file(): 
        
        try: 
            with open(password_file_json, mode="r") as file:
                data = json.load(file)

        # NOTE ------------- CREATES THE INITIAL DICTIONARY FOR THE FINALLY TO DUMP
        except (FileNotFoundError, json.JSONDecodeError): 
            print("File not found. Creating new file.")
            data = new_data

        # NOTE ------------- TAKES THE OLD DATA AND ADDS THE NEW ONE
        else: 
            print("File loaded successfully.")
            data.update(new_data)
        
        # NOTE ------------- STILL OVERWRITES BUT INCLUDING NEW DATA, NO MATTER WHAT IT WILL WRITE TO THE JSON OR CREATE THE FILE
        finally: 
            with open(password_file_json, mode="w") as file:
                json.dump(data, file, indent=4)
                print("Data written to file.")
                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)

    check_and_update_file()

# NOTE ----------------------------------------------- ADD NEW PASSWORD

def find_password(): 
    try: 
        with open(password_file_json, mode="r") as file:
            data = json.load(file)
            key_to_find = data[f"{website_input.get()}"]
    except KeyError: 
        print(f"Password key does not exist.")
        messagebox.showinfo(title="Error", message="Password key does not exist")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Password file does not exist")
    else: 
        username_input.delete(0, END)
        password_input.delete(0, END)
        username_input.insert(0, key_to_find["username"])
        password_input.insert(0, key_to_find["password"])

# NOTE ----------------------------------------------- BUTTONS

find_button = Button(text="Find Website", command=find_password)
find_button.grid(row=0, column=2)

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