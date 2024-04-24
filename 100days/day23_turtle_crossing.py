from turtle import Turtle, Screen
import time
import random

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
        self.shapesize(stretch_wid=0.8)

    def move_forward(self): 
        self.forward(20)

    def move_backward(self): 
        self.backward(20)    

class Scoreboard(Turtle): 
    def __init__(self): 
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self): 
        self.clear()
        self.goto(-100, 200)
        self.write(self.score, align="center", font=("Courier",80,  "normal"))

    def player_scores(self): 
        self.score += 1
        self.update_score()        


class Car(Turtle): 
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.fillcolor("green")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2)

    def drive(self): 
        self.forward(20)

paulie = Player()
scoreboard = Scoreboard()
cars = []

def generate_cars():

    for index in range(15): 
        car = Car()
        car.goto(random.randint(300, 540), -280 + (40 * index))
        cars.append(car)

generate_cars()

screen.listen()
screen.onkey(paulie.move_forward, "Up")
screen.onkey(paulie.move_backward, "Down")

game_is_on = True

while game_is_on: 
    screen.update()
    time.sleep(0.1)

    for car in cars: 
        if car.distance(paulie) < 20: 
            game_is_on = False

        elif paulie.ycor() > 280: 
            scoreboard.player_scores()
            paulie.goto(0, -280)
            for car in cars: 
                car.goto(random.randint(270, 540), car.ycor())     

        elif car.xcor() < -300: 
            car.goto(random.randint(270, 540), car.ycor())
        else: 
            car.drive()

screen.exitonclick()