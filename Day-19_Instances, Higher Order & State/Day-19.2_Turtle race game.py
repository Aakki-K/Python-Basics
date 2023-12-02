# TODO 1: Import Zone
from turtle import Turtle, Screen
import random

# TODO 2: Objects Zone
Turtle_List = []
for turtle in range(7):
    My_Turtle = Turtle("turtle")
    Turtle_List.append(My_Turtle)

Display = Screen()

Intermittent_Spacing = 50
Screen_Width = Intermittent_Spacing * 8  # Intermittent_Spacing * (No. of turtles + 1)
Screen_Height = Intermittent_Spacing * 8  # Intermittent_Spacing * (No. of turtles + 1)

Display.setup(Screen_Width, Screen_Height)

# TODO 3: Container Zone
Colors_List = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
Random_jump = [3, 5, 7, 10, 12, 13, 15]


# TODO 4: Function Zone
def Color_assign(Object_List, Color_List):
    for Object in Object_List:
        Random_Color = random.choice(Color_List)
        Object.color(Random_Color)
        Colors_List.remove(Random_Color)


def Positioning(Object_List, Screen_width, Screen_height):
    x = -(Screen_width / 2) + Intermittent_Spacing
    y = -(Screen_height / 2) + Intermittent_Spacing
    for n in range(0, len(Object_List)):
        tortoise = Object_List[n]
        tortoise.penup()
        tortoise.goto(x, y)
        y += Intermittent_Spacing


def Race(Object_List, Screen_width, Intermittent_spacing):
    Is_race_on = True
    while Is_race_on:
        for Racer in Object_List:
            Racer.forward(random.choice(Random_jump))
            x = (Racer.xcor())
            if x >= float((Screen_width / 2) - (Intermittent_spacing/2)):
                return Racer.color()


# TODO 5: Code
User_Bet = Display.textinput("Race", "Which color Turtle will win? (Colors : VIBGYOR)")
Color_assign(Turtle_List, Colors_List)
Positioning(Turtle_List, Screen_Width, Screen_Height)
Output = Race(Turtle_List, Screen_Width, Intermittent_Spacing)
if User_Bet.lower() == Output[0].lower():
    print(f"You WON, Because the winner turtle is {Output[0].lower()}")
else:
    print(f"You LOST, Because the winner turtle is {Output[0].lower()}")


Display.exitonclick()
