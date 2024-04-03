# Machine max resource capacity
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

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
# Function for resource deduction

def use_resource(resource_amount, deduction_amount):

    final_amount = resource_amount - deduction_amount

    if final_amount < 0: 
        return resource_amount
    else: 
        return final_amount
    

# Function for resource addition
def replenish_resource(resource_amount, addition_amount): 
    final_amount = resource_amount + addition_amount
    return final_amount


while True: 
    order = input("What drink would you like? espresso, latte, or cappuccino?\n").lower()

    if order != "espresso" and order != "latte" and order != "cappuccino": 
        print("We don't have that in our menu sorry!")
        continue

    else:
        order_ingredients = MENU[order]["ingredients"]
        able_to_make = []

        # Checks if there is enough of all ingredients
        for ingredient in order_ingredients: 
            ingredient_amount = order_ingredients[ingredient]
            resource_to_deduct = resources[ingredient]
            if resource_to_deduct >= ingredient_amount: 
                able_to_make.append(True)
            else: 
                able_to_make.append(False)

        if False in able_to_make: 
            print("Not enough resources to make your drink.")
            print(resources)


            # Ask if they would like to add more of any resource
            while True: 
                add_more_resource = input("Are we replenishing a resource? y or n.\n").lower()

                if add_more_resource == "y": 
                    which_resource = input("Which resource would you like to add to? water, milk, or coffee?\n").lower()
                    quantity_to_add = int(input("How much of it?\n"))
                    resources[which_resource] = replenish_resource(resources[which_resource], quantity_to_add)

                    add_more = input("Any other resource to replenish? y or n.\n")
                    print(resources)

                    if add_more == "y": 
                        continue

                    else:
                        break

                else: 
                    print("Thank you come again!")
                    break
                    
        else: 

            penny = int(input("# of Pennies\n"))
            nickel = int(input("# of Nickels\n"))
            dime = int(input("# of Dimes\n"))
            quarter = int(input("# of Quarters\n"))

            payment = (penny * 0.01) + (nickel * 0.05) + (dime * 0.1) + (quarter * 0.25)

            if payment >= MENU[order]["cost"]: 
                for ingredient in order_ingredients: 
                    ingredient_amount = order_ingredients[ingredient]
                    resource_to_deduct = resources[ingredient]
                    resources[ingredient] = use_resource(resource_to_deduct, ingredient_amount)
                change = payment - MENU[order]["cost"]

                print(f"Heres the {order} you ordered. Your change is ${change}.")
                continue
            
            else: 
                print(f"You don't have enough money for this order]")
                continue
    continue