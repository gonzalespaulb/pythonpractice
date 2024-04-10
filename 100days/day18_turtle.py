from turtle import Turtle, Screen
import turtle
import colorgram 
import random

t = Turtle()

screen = Screen()

# t.shape("square")
# t.color("#1098F7")
t.speed("fastest")

# num_of_sides = 4

# while True:

#     for _ in range(num_of_sides):
#         angle = 360 / num_of_sides
#         t.forward(100)
#         t.right(angle)
#         t.color("#1098F7")

#     if num_of_sides < 9: 
#         num_of_sides += 1

#     else: 
#         break

def draw_spirograph(size_of_gap): 
    for _ in range(int(360 / size_of_gap)): 
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

rows = 0

turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('picture.jpeg', 6)
for color in colors: 
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r, g, b))

rows = 0
t.hideturtle()
t.penup()
t.setheading(225)
t.forward(250)
t.setheading(0)

while rows < 10: 

    for _ in range(10): 
        t.dot(20, random.choice(rgb_colors))
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)

    rows += 1

screen.exitonclick()

