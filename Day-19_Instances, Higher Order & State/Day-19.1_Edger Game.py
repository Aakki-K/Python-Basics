# TODO 1: Import Zone
from turtle import Turtle, Screen

# TODO 2: Object Zone
# Turtle
Timmy = Turtle()
# Screen
Display = Screen()
Display.listen()


# TODO 3: Function Zone
def forward():
    Timmy.forward(15)


def backward():
    Timmy.backward(15)


def Clockwise():
    Timmy.right(10)


def Anti_Clockwise():
    Timmy.left(10)


def Clear_Screen():
    Display.resetscreen()


# TODO 4: Code
Display.onkeypress(forward, "6")
Display.onkeypress(backward, "4")
Display.onkeypress(Anti_Clockwise, "8")
Display.onkeypress(Clockwise, "2")
Display.onkeypress(Clear_Screen, "c")

Display.exitonclick()
