# TODO 1: Import Zone
import random

import colorgram
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

# TODO 2: Fetch colors from Image
Colors = colorgram.extract("hirst-1.jpg", 25)

Colors_Tuple_list = []
for n in range(25):
    r = Colors[n].rgb.r
    g = Colors[n].rgb.g
    b = Colors[n].rgb.b
    Color = (r, g, b)
    Colors_Tuple_list.append(Color)

print(Colors_Tuple_list)

# TODO 3: Code
# Object Zone
Timmy = Turtle()
Timmy.hideturtle()
Display = Screen()

Screen_Width = 50 * 11  # "Intermittent_Spacing" * "No of Dots needed in x-axis + 1"
Screen_Height = 50 * 11  # "Intermittent_Spacing" * "No of Dots needed in x-axis + 1"
Dot_Size = 20
Intermittent_Spacing = 50

# Setting Window size
Display.setup(Screen_Width, Screen_Height)

# Setting initial location
Timmy.penup()
Timmy.goto((-Screen_Width / 2) + Intermittent_Spacing, (-Screen_Height / 2) + Intermittent_Spacing)
Timmy.speed(0)

Is_loop = True
while Is_loop:
    Timmy.pendown()
    Timmy.color(random.choice(Colors_Tuple_list))
    Timmy.dot(Dot_Size)
    Timmy.penup()
    Timmy.forward(Intermittent_Spacing)
    if Timmy.xcor() >= ((Screen_Width / 2) - Intermittent_Spacing) and Timmy.ycor() >= (
            (Screen_Height / 2) - Intermittent_Spacing):
        Timmy.color(random.choice(Colors_Tuple_list))
        Timmy.dot(Dot_Size)
        Is_loop = False
    elif Timmy.xcor() >= ((Screen_Width / 2) - Intermittent_Spacing):
        Timmy.color(random.choice(Colors_Tuple_list))
        Timmy.dot(Dot_Size)
        y = Timmy.ycor()
        Timmy.goto((-Screen_Width / 2) + Intermittent_Spacing, y + Intermittent_Spacing)

Display.exitonclick()
