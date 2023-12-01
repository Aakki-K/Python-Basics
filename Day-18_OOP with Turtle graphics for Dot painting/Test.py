# TODO 1 : Import Zone
from turtle import Turtle, Screen
import random
import turtle

# TODO 2: Function Zone


# TODO 3: Container Zone
Color_List = ["blue", "magenta", "yellow", "red", "green", "black", "violet", "pink", "grey"]
Direction_is_at_East = [90.0, 270, 0.0]
Direction_is_at_North = [180, 270, 90]
Direction_is_at_West = [90.0, 270, 180.0]
Direction_is_at_South = [180.0, 270, 0.0]
All_Directions = [0.0, 90.0, 180.0, 270.0]
# TODO
Timmy = Turtle()

Display = Screen()


# Multiple shapes

# for n in range(0, 4):
#     Timmy.forward(100)
#     Timmy.right(90)

# Timmy.penup()
# Timmy.goto(-300, 0)
# Timmy.pendown()
#
# for n in range(0, 15):
#     Timmy.pendown()
#     Timmy.forward(10)
#     Timmy.penup()
#     Timmy.forward(10)

# for n in range(3, 11):
#     Timmy.color(random.choice(Color_List))
#     for _ in range(0, n):
#         Timmy.forward(100)
#         Timmy.right(360/n)

# Random Walk

# def Random_direction(Initial_heading):
#     if Initial_heading == 0.0:
#         Timmy.setheading(random.choice(Direction_is_at_East))
#     elif Initial_heading == 90.0:
#         Timmy.setheading(random.choice(Direction_is_at_North))
#     elif Initial_heading == 180.0:
#         Timmy.setheading(random.choice(Direction_is_at_West))
#     elif Initial_heading == 270:
#         Timmy.setheading(random.choice(Direction_is_at_South))
#
#
def Random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    Color = (r, g, b)
    return Color


#
turtle.colormode(255)
# Timmy.width(15)
# Timmy.speed(0)
#
# Is_Loop = True
# while Is_Loop:
#     Timmy.color(Random_color())
#     Timmy.forward(25)
#     # Initial_Heading = Timmy.heading()
#     # Random_direction(Initial_Heading)
#     Timmy.setheading(random.choice(All_Directions))

# Circles with different colors and offset
Timmy.speed(0)
for n in range(0, 72):
    Timmy.color(Random_color())
    Timmy.circle(100)
    Timmy.left(5)

Display.exitonclick()
