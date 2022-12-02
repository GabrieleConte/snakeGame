from time import sleep
from snake import Snake
from food import *
from scoreboard import Scoreboard
from tkinter import PhotoImage


scoreboard = Scoreboard()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
segments = []

snake = Snake()
food = Food()

screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True


def check():
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()


while game_on:
    screen.update()
    sleep(0.1)
    game_on = snake.move()
    check()

scoreboard.gameover()

screen.exitonclick()
