from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
y_positions=[-100, -50, 0, 50, 100, 150]
turtles=[]

for turtle_index in range(6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.color(colors[turtle_index])
    turtles.append(tim)
        
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>210:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance=random.randint(0, 10)
        turtle.forward(rand_distance)
    
screen.exitonclick()