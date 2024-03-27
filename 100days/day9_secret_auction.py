# test = {
#     "Paul":27,
#     "Lilly":25,
# }

# for key in test: 
#     print(f"{key} is {test[key]} years old.")

employee = {
    "first_name":"Paul", 
    "last_name": "Gonzales", 
    "age": 27, 
    "performance": {
        "lates": 2,
        "absences": 1, 
        "promotion_status": True 
    }, 
    "lifts_worked": ["Assay Hill", "Skittles", "Sheer Bliss"]
}


introduction = f"The current admin is {employee['first_name']} {employee['last_name']} and he is {employee['age']} years old."
employee_performance = f"He currently has {employee['performance']['lates']} lates."

# print(introduction)
# print(employee_performance)

# Modify existing key
def add_late(number_to_add): 
    employee["performance"]["lates"] += number_to_add

add_late(2)

# Add another key
employee["position"] = "Admin"

print(employee)


# Auction

bidders = {}

while True:
    bid_option = input("Are there any other bidders?\n").lower()

    if bid_option == "y": 
        name = input("What is your name?\n")
        bid = input("How much is your bid?\n")
        bidders[f"{name}"] = int(bid)
        continue
    else: 
        break

top_bid = 0
winning_bidder = ""

for key in bidders: 
    if top_bid < bidders[key]: 
        top_bid = bidders[key]
        winning_bidder = f"The winning bidder is {key} with a bid of ${bidders[key]}."

print(winning_bidder)