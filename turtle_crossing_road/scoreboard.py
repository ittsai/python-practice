from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 260)
        self.write( f"Level {self.level}", align="center", font=("Arial", 30, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 50, "normal"))
        self.level = 1

    def win(self):
        self.level += 1
        self.update_scoreboard()