

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

# class Car: 
#     def __init__(self, **kw):
#         # self.make = kw["make"]
#         # self.model = kw["model"]

#         # If argument is non existent will NOT return error as opposed to above
#         self.make = kw.get("make")
#         self.model = kw.get("model")


# my_car = Car(make="Toyota")
# print(my_car.model)

# GUI Layout and Widget run through ----------------------------------- GUI Layout and Widget run through

# from tkinter import *

# window = Tk()
# window.title("OOEY GUI")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# my_label = Label(text="I am a label", font=("Inter", 24, "bold"))
# # my_label.pack()
# # my_label.place(x=0, y=0)
# my_label.grid(row=0, column=0)

# # BUTTON

# def button_clicked(): 
#     new_text = input.get()
#     # new_text = scale.get()
#     my_label.config(text=new_text)

# button = Button(text="Click Me", command=button_clicked)
# # button.pack()
# button.grid(row=1, column=2)

# new_button = Button(text="New Button")
# new_button.grid(column=3, row=0)

# # Entry

# input = Entry(width=10)
# # input.pack()
# input.grid(row=2, column=4)
# input.get()

# # Text area
# text = Text(height=5, width=30)
# # text.pack()

# # Spin box
# def spinbox_used(): 
#     spinbox.get()
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# # spinbox.pack()

# # Scale 
# def scaled_used(val): 
#     pass
#     # return val
# scale = Scale(from_=0, to=100)
# # scale.pack()

# window.mainloop()

# Miles to Km converter ----------------------------------- Miles to Km converter

from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


input = Entry(width=10)
input.grid(row=0, column=1)
input.get()

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def calculate(): 
    miles = input.get()
    km = int(miles) * 1.61
    result_label.config(text=km)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=1)

window.mainloop()