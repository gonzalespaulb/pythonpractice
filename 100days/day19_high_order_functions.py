from turtle import Turtle, Screen
import random

# t = Turtle()
screen = Screen()

# screen.listen()

# def move_forward(): 
#     t.forward(10)
# def move_left(): 
#     t.left(10)
# def move_right(): 
#     t.right(10)
# def move_back(): 
#     t.backward(10)
# def clear(): 
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()

# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="c", fun=clear)

# Turtle race

TURTLE_COLORS = ["red", "blue", "yellow", "green"]
all_turtles = []
HEIGHT = 400
WIDTH = 500
screen.setup(WIDTH, HEIGHT)
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle wins the race? Enter a color").lower()

start = -(WIDTH / 2) + 10

for index in range(0, len(TURTLE_COLORS)): 
    t = Turtle(shape="turtle")
    t.penup()
    t.color(TURTLE_COLORS[index])
    t.goto(start, (index * 20))
    all_turtles.append(t)

is_race_on = False

if user_bet: 
    is_race_on = True

while is_race_on: 


    for turtle in all_turtles: 
        turtle.forward(random.randint(0, 10))


        if turtle.xcor() > 230:
            is_race_on = False

            if user_bet == turtle.pencolor(): 
                print(f"You bet right! {turtle.pencolor()} turtle won!")
            
            else: 
                print(f"Wrong bet. {turtle.pencolor()} turtle won.") 

 


screen.exitonclick()