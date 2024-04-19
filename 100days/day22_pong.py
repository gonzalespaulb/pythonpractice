from turtle import Turtle, Screen
import time

HEIGHT = 600
WIDTH = 800
screen = Screen()
screen.bgcolor("black")
screen.setup(height=HEIGHT, width=WIDTH) 


# Ball Class
class Ball(Turtle): 
    def __init__(self): 
        super().__init__()
        self.shape("circle")
        self.fillcolor("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def bounce(self): 
        self.y_move *= -1 

    def paddle_collide(self): 
        self.x_move *= -1         

    def move_right(self): 
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_left(self): 
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def move(self): 
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)        

 
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
ball = Ball()

screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")
screen.onkey(computer_paddle.go_up, "w")
screen.onkey(computer_paddle.go_down, "s")

game_is_on = True
ball_direction = "right"

while game_is_on: 
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.distance(user_paddle) < 50 and ball.xcor() > 330:
        ball.paddle_collide() 
    
    if ball.distance(computer_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_collide() 

    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce()   


screen.exitonclick()