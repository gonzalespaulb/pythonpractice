flour = 500
yeast = 10
water = 300
knead_time = 10
salt = 3
rise_time = 2
bake_temp = 200
bake_time = 30

print(f"Mix {flour}g of Flour, {yeast}g Yeast and {water}ml Water in a bowl.")
print(f"Knead the dough for {knead_time} minutes.")
print(f"Add {salt}g of Salt.")
print(f"Leave to rise for {rise_time} hours.")
print(f"Bake at {bake_temp} degrees C for {bake_time} 30 minutes.")

paired_with = input("What drink would you pair a donut with?\n")

me_too = f"I like eating donuts with {paired_with} too!"

print(me_too)