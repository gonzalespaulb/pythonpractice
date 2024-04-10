from turtle import Turtle, Screen

screen = Screen()

WIDTH = 600
HEIGHT = 600

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Paulies Snake Game")

dots_eaten = ["_","_","_","_","_","_","_","_",]
snake_length = []

for index in range(0, len(dots_eaten)):
    t = Turtle(shape="square")
    t.penup()
    t.color("white")
    t.goto(index * -20, 0)
    snake_length.append(t)


# direction = "w"

# def move_forward(): 
#     t.forward(20)
# def move_left(): 
#     t.left(20)
# def move_right(): 
#     t.right(20)
# def move_back(): 
#     t.backward(20)

# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="s", fun=move_back)

while True: 
    for segment in snake_length: 

        segment.forward(20)

screen.exitonclick()
