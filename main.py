from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.mode("standard")
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  screen.update()

  # detect collision with food and update scoreboard.
  if snake.head.distance(food) < 16:
    food.refresh()
    snake.extend_snake()
    scoreboard.score_update()

  # if snake collides with the wall, game is over
  if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
    game_on = False
    scoreboard.game_over()

  # if snake collides with its own tail then the game is over using slicing method in list
  for i in snake.snake_body[1:]: # (this is slicing method used to start the list with the second element of the list as the first is the head.)
    if snake.head.distance(i) < 10:
      game_on = False
      scoreboard.game_over()

  
  























screen.exitonclick()