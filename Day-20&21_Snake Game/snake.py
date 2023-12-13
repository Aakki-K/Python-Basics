# TODO 1: Import Zone
from turtle import Turtle, Screen

# TODO 2: Constants Zone
INITIAL_SEGMENTS_OF_SNAKE = 3
TURTLE_COLOR = "white"
UP = 90.0
DOWN = 270.0
RIGHT = 0.0
LEFT = 180.0


# TODO 2: Class

class Snake:
    def __init__(self):
        self.turtle_list = []

    def create_snake(self):
        x = 0
        y = 0
        for n in range(0, INITIAL_SEGMENTS_OF_SNAKE):
            segment = Turtle("square")
            segment.penup()
            segment.color(TURTLE_COLOR)
            segment.goto(x, y)
            x -= 20
            self.turtle_list.append(segment)

    def move(self):
        for n in range(len(self.turtle_list) - 1, 0, -1):
            position = self.turtle_list[n - 1].pos()
            self.turtle_list[n].goto(position)
        self.turtle_list[0].forward(20)

    def Right(self):
        if self.turtle_list[0].heading() != LEFT:
            self.turtle_list[0].setheading(RIGHT)

    def Left(self):
        if self.turtle_list[0].heading() != RIGHT:
            self.turtle_list[0].setheading(LEFT)

    def Up(self):
        if self.turtle_list[0].heading() != DOWN:
            self.turtle_list[0].setheading(UP)

    def Down(self):
        if self.turtle_list[0].heading() != UP:
            self.turtle_list[0].setheading(DOWN)

    def hit_on_wall(self, Wall_at_x, Wall_at_y):
        """Returns True if 1st turtle reaches the x or -x or y or -y or else false"""
        if self.turtle_list[0].xcor() >= Wall_at_x or self.turtle_list[0].xcor() <= (-Wall_at_x):
            return False
        elif self.turtle_list[0].ycor() >= Wall_at_y or self.turtle_list[0].ycor() <= (-Wall_at_y):
            return False
        else:
            return True

    def game_over(self):
        game_over = Turtle()
        game_over.hideturtle()
        game_over.color("orange")
        game_over.write("Game Over", font=20, align= "center")

    def add_segment(self):
        x = self.turtle_list[-1].xcor()
        y = self.turtle_list[-1].ycor()
        heading = self.turtle_list[-1].heading()
        if heading == 0.0:
            x -= 20
        elif heading == 90.0:
            y -= 20
        elif heading == 180.0:
            x += 20
        elif heading == 270.0:
            y += 20
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.speed("fastest")
        segment.goto(x, y)
        self.turtle_list.append(segment)





