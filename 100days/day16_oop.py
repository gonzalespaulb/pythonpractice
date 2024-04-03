import os
from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Employee", "ID", "Hire Date", "Position"]
table.align["Employee"] = "l"
table.align["ID"] = "l"
table.align["Hire Date"] = "l"
table.align["Position"] = "l"

print(table)

# Function to clear the terminal screen
def clear_screen():
    # Clear screen command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear screen command for Unix/Linux/MacOS
    else:
        os.system('clear')


while True: 

    add_employee_question = input("Add an employee? y or n.\n").lower()

    if add_employee_question == "n": 
        break

    else: 
        name = input("Employee name.\n")
        employee_id = input("ID Number\n")
        hire_date = input("Hire date. mm/dd/yyyy.\n")
        position = input("Position\n")

        table.add_row([name, employee_id, hire_date, position])

        clear_screen()

        print(table)

        continue

