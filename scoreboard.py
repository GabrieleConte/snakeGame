from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.pull_data()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.push_data(self.high_score)
        self.score = 0
        self.updateScoreboard()

    def pull_data(self):
        with open("data.txt", mode="r") as data:
            x = int(data.read())
            return x

    def push_data(self, x):
        with open("data.txt", mode="w") as data:
            data.write(str(x))

#   def gameover(self):
#      self.goto(0, 0)
#      self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
