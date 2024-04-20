from turtle import Turtle, Screen

screen = Screen()
WIDTH = 600 
HEIGHT = 600

screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

class Player(Turtle): 
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.fillcolor("green")
        self.penup()
        self.goto(0, -280)

    def move_forward(self): 
        self.forward(20)

    def move_backward(self): 
        self.backward(20)    

paulie = Player()

screen.listen()
screen.onkey(paulie.move_forward, "Up")
screen.onkey(paulie.move_backward, "Down")

game_is_on = True

while game_is_on: 
    screen.update()


screen.exitonclick()
