import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
my_snake = Snake()
food = Food()
screen.listen()
scoreboard = ScoreBoard()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increment_score()

    if my_snake.head.xcor() > 290 or my_snake.head.ycor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.xcor() < -290:
        scoreboard.reset()
        my_snake.reset()

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.reset()
            my_snake.reset()

screen.exitonclick()
