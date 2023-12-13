# TODO 1: Import Zone
from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food

# TODO 2: CONSTANTS ZONE
Score = 0

# TODO 3: code
Display = Screen()
Display.bgcolor("black")
Display.setup(600, 600)
Display.title(f"My Snake Game                                                  Score = {Score}")
Display.listen()
Display.tracer(0)

Game_over = Turtle()

Snake_game = Snake()
Snake_game.create_snake()

Display.onkeypress(Snake_game.Up, "Up")
Display.onkeypress(Snake_game.Left, "Left")
Display.onkeypress(Snake_game.Right, "Right")
Display.onkeypress(Snake_game.Down, "Down")

food = Food()

Is_game_ON = True
while Is_game_ON:
    Display.update()
    time.sleep(0.1)
    Snake_game.move()

    if Snake_game.turtle_list[0].distance(food) < 15:
        food.refresh()
        Score += 1
        Display.title(f"My Snake Game                                                  Score = {Score}")
        Snake_game.add_segment()

    for seg in Snake_game.turtle_list[1:]:
        if Snake_game.turtle_list[0].distance(seg) < 10:
            Snake_game.game_over()
            Is_game_ON = False



Display.exitonclick()






