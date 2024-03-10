import time

# TIP Calculator

bill = 0
tip_percent = 0
total = 0

while True: 

    bill = input("How much was the bill?\n")

    if bill.isdigit():
        bill = int(bill)

        tip_percent_str = input("Tip percent? 15, 20, 35 etc..\n")

        if tip_percent_str.isdigit():
            tip_percent = int(tip_percent_str)
            break

        else:
            print("Please enter a valid integer for the tip percentage.")

    else:
        print("Please enter a valid integer for the bill.")

total = bill + (bill * (tip_percent / 100))

split_number = 0

while True: 
    split = input("How many people are splitting this? \n")

    if split.isdigit():
        split_number = int(split)
        break

    else: 
        print("Please enter a valid integer for the number of people splitting the bill.")

individual_bill = total / split_number

print(f"The total is {total} divided by {split_number} of people. Each person owes ${individual_bill.__round__(2)}. ")

time.sleep(3)

payment_method = input("So how are we paying? card or cash?\n")

if payment_method == "card":
    print("Not mine, nose goes!!!")