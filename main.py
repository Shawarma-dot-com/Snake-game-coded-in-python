from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()


screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.right, "d")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.refresh()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
