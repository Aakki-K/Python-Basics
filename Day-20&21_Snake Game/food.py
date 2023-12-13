# TODO 1: Import Zone
from turtle import Turtle
import turtle
from snake import Snake
import random

turtle.resizemode("user")

# TODO 2: CONSTANTS ZONE
Segments = Snake()
Segment_list = Segments.turtle_list
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# TODO 3: Code
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
