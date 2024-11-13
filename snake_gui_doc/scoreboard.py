from os import write
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        file = open("score.txt", mode="r")
        self.score = 0
        self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        file.close()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("score.txt", mode="w")
            file.write(f"{self.high_score}")
            file.close()
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

