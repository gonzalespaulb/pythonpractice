from turtle import Turtle, Screen

HEIGHT = 600
WIDTH = 800
screen = Screen()
screen.bgcolor("black")
screen.setup(height=HEIGHT, width=WIDTH) 
 
#  Paddle class
class Paddle(Turtle):
    def __init__(self, position):
        # Super will allow to use everything from Turtle
        super().__init__()
        self._tracer(0)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.ycor()
        self.xcor()
        self.fillcolor("white")

    def go_up(self): 
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self): 
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    

user_paddle = Paddle(position=(350, 0))
computer_paddle = Paddle(position=(-350, 0))

screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")
screen.onkey(computer_paddle.go_up, "w")
screen.onkey(computer_paddle.go_down, "s")

game_is_on = True

while game_is_on: 
    screen.update()

screen.exitonclick()