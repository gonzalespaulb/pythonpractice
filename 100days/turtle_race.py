from turtle import Turtle, Screen

screen = Screen()

WIDTH = 600
HEIGHT = 600


names = ["Paul", "Lillian", "Memphis", "Ozzie", "Mason"]
color = ["red", "blue", "yellow", "purple", "brown"]
turtles = []


class My_Turtle(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape("turtle")
        self.penup()

for index in range(0, len(names)):

    t = My_Turtle()
    t.fillcolor(color[index])
    t.goto(-290, index * 30)
    turtles.append(t)

game_is_on = True

while game_is_on:
    for turtle in turtles: 
        turtle.forward(10)
    

screen.exitonclick()




def hello():
    print("hello")

hello()