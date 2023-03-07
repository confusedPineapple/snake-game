from turtle import Screen
import winsound
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor('pink')
screen.title('My Snake Game <3')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 80

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        print('Nom nom nom')
        food.refresh()
        winsound.Beep(frequency, duration)
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()

    #Detect Collison with tail
    for segment in snake.snake_length[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()