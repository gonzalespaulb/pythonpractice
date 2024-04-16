from turtle import Turtle, Screen
import time
import random

screen = Screen()

WIDTH = 600
HEIGHT = 600
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Paulies Snake Game")
screen.tracer(0)
screen.listen()

dots_eaten = 2
snake_length = []


def render_length(): 
    for index in range(0, dots_eaten):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(index * -20, 0)
        snake_length.append(t)

render_length()

snake_head = snake_length[0]

def get_divisible_coordinate():
  """Generates a random integer divisible by 20 within the specified range."""
  while True:
    value = random.randint(-290, 290)
    if value % 20 == 0:
      return value

food = Turtle(shape="square")
food.penup()
food.color("white")
food.goto(get_divisible_coordinate(), get_divisible_coordinate())

while True: 

    screen.update()
    time.sleep(0.1)

    # Start from the end of the list and assign the coords of the segment before to the current segment
    for seg_num in range(len(snake_length) - 1, 0, -1): 
        if snake_length[seg_num].distance(snake_head) < 10:
            game_over = Turtle()
            game_over.penup()
            game_over.color("white")
            game_over.goto(0, 0)
            game_over.write(f"Game Over! Score: {dots_eaten - 2}", align="center", font=("Courier", 24, "normal"))
            break

        else:
            new_x = snake_length[seg_num - 1].xcor()
            new_y = snake_length[seg_num - 1].ycor()
            snake_length[seg_num].goto(new_x, new_y)

    # If statement is to prevent from going backwards on itself
    def move_up(): 
        if snake_head.heading() != DOWN:
            snake_head.setheading(UP)
    def move_down(): 
        if snake_head.heading() != UP:
            snake_head.setheading(DOWN)
    def move_left(): 
        if snake_head.heading() != RIGHT:
            snake_head.setheading(LEFT)
    def move_right(): 
        if snake_head.heading() != LEFT:
            snake_head.setheading(RIGHT)

    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    screen.onkey(key="Left", fun=move_left)
    screen.onkey(key="Right", fun=move_right)

    # Rerender food in random spot and grow snake
    if snake_head.distance(food) < 15: 
        dots_eaten += 1
        food.goto(get_divisible_coordinate(), get_divisible_coordinate())

        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(snake_length[-1].xcor(), snake_length[-1].ycor())
        snake_length.append(t)

    # End game if snake hits the wall
    if snake_head.xcor() > 280 or snake_head.xcor() < -280 or snake_head.ycor() > 280 or snake_head.ycor() < -280: 
        game_over = Turtle()
        game_over.penup()
        game_over.color("white")
        game_over.goto(0, 0)
        game_over.write(f"Game Over! Score: {dots_eaten - 2}", align="center", font=("Courier", 24, "normal"))
        
        break

    snake_head.forward(20)

screen.exitonclick()


# class Animal: 
#     def __init__(self): 
#         self.num_eyes = 2

#     def breathe(self): 
#         print("Inhale, Exxhale")

# class Fish(Animal): 
#     def __init__(self): 
#         super().__init__()

#     # Takes an existing class' and add more
#     def breathe(self):
#         super().breathe()
#         print("doing it underwater")

#     def swim(self): 
#         print("Swimming")

# paul = Animal()
# paul.breathe()

# nemo = Fish()
# nemo.breathe()
# print(nemo.num_eyes)
