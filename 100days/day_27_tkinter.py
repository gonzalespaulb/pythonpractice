# import tkinter as tk

# window = tk.Tk()
# window.title("OOEY GUI")
# window.minsize(width=500, height=300)

# my_label = tk.Label(text="I am a label", font=("Inter", 24, "bold"))
# my_label.pack(side="left")



# window.mainloop()


# Unlimited arguments

# def add(*args): 

#     print(len(args))

#     sum = 0
#     for num in args: 
#         sum += num

#     return sum

# print(add(3, 5, 6))

# **kwargs turns arguments into a dictionary
# def calculate(n, **kwargs): 
#     print(kwargs["add"])

#     n += kwargs["add"]
#     print(n)

# calculate(2, add=3, multiply=5)

class Car: 
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        # If argument is non existent will NOT return error as opposed to above
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Toyota")
print(my_car.model)