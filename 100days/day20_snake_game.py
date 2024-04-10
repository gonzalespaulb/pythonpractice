from turtle import Turtle, Screen
import time

screen = Screen()

WIDTH = 600
HEIGHT = 600

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Paulies Snake Game")
screen.tracer(0)
screen.listen()

dots_eaten = ["_","_","_","_","_","_","_","_",]
snake_length = []

for index in range(0, len(dots_eaten)):
    t = Turtle(shape="square")
    t.penup()
    t.color("white")
    t.goto(index * -20, 0)
    snake_length.append(t)



while True: 

    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake_length) - 1, 0, -1): 
        new_x = snake_length[seg_num - 1].xcor()
        new_y = snake_length[seg_num - 1].ycor()
        snake_length[seg_num].goto(new_x, new_y)

    def move_up(): 
        snake_length[0].setheading(90)
    def move_down(): 
        snake_length[0].setheading(270)
    def move_left(): 
        snake_length[0].setheading(180)
    def move_right(): 
        snake_length[0].setheading(0)

    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    screen.onkey(key="Left", fun=move_left)
    screen.onkey(key="Right", fun=move_right)

    snake_length[0].forward(20)


screen.exitonclick()
