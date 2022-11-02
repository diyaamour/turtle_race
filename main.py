import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# names = ["raphael", "leonardo", "donatello", "michelangelo", "splinter", "yushi"]
# names_color = {"raphael": "red", "leonardo": "blue", "donatello": "purple", "michelangelo": "orange",
#                "splinter": "yellow", "yushi": "purple"}
all_turtles = []
y_positions = [-100, -50, 0, 50, 100, 150]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won the race!")
            else:
                print(f"You've lost! the {winning_color} turtle lost the race!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()


