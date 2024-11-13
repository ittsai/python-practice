from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVING_DISTANCE = 10
FINAL_LINE_Y = 280

class PlayerTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_y(self):
        new_y = self.ycor() + MOVING_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        if self.xcor() > -260:
            new_x = self.xcor() - MOVING_DISTANCE
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 260:
            new_x = self.xcor() + MOVING_DISTANCE
            self.goto(new_x, self.ycor())

    def restart(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINAL_LINE_Y:
            return True
        return False