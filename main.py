from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_record()

    if snake.head.xcor() > 290 or snake.head.xcor() < -294 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    # detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
