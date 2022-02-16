
import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Score: ")
screen.tracer(0)

start_pos = [(0, 0), (-20, 0), (-40, 0)]
border = 280
segments = []

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > border or snake.head.xcor() < -border or snake.head.ycor() > border or \
            snake.head.ycor() < -border:
        score.reset_score()

    for segment in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            score.reset_score()

screen.exitonclick()
