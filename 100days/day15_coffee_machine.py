# Machine max resource capacity
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function for resource deduction

def use_resource(resource_amount, deduction_amount):

    final_amount = resource_amount - deduction_amount

    if final_amount < 0: 
        print("Not enough resources")
        return resource_amount
    else: 
        return final_amount

# resources["coffee"] = use_resource(resources["coffee"], 50)
    

# Function for resource addition

# Dictionary for recipes and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Translate money into numbers

while True: 
    order = input("What drink would you like? espresso, latte, or cappuccino?\n").lower()

    if order != "espresso" and order != "latte" and order != "cappuccino": 
        print("We don't have that in our menu sorry!")
        continue
    else:
        resources[order] = use_resource(resources[order], MENU[order]["ingredients"]) 
        break
    
