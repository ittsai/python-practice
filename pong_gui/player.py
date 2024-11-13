from turtle import Turtle

class Player(Turtle):
    def __init__(self, x):
       super().__init__()
       self.shape("square")
       self.color("white")
       self.shapesize(stretch_len=1, stretch_wid=5)
       self.penup()
       self.goto(x, 0)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
