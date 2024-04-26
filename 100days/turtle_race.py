from turtle import Turtle, Screen

screen = Screen()

WIDTH = 600
HEIGHT = 600


turtles = ["Paul", "Lillian", "Memphis", "Ozzie", "Mason"]
color = ["red", "blue", "yellow", "purple", "brown"]


class My_Turtle(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.fillcolor("purple")
        # self.goto(150, 0)

for index in range(0, len(turtles)):

    t = My_Turtle()
    t.fillcolor(color[index])
    t.goto(0, index * 30)



# lillian.shape("turtle")
# lillian.penup()
# lillian.fillcolor("purple")
# lillian.goto(150, 0)

screen.exitonclick()
