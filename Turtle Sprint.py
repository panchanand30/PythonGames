from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Choose a Turtle", prompt="Which turtle according to you will win?")

colours = ["Red", "Blue", "Green", "Yellow", "Orange"]
y_position = [-100, -50, 0, 50, 100]
all_turtles = []

for turtles in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtles])
    # new_turtle = my_screen.textinput(title=f"Name the turtle", prompt=f"What is the name of {new_turtle.color()}
    # colour turtle")
    new_turtle.goto(x=-230, y=y_position[turtles])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You have won! The {winning_colour} turtle is the winner.")
            else:
                print(f"You have lost! The {winning_colour} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

my_screen.exitonclick()
