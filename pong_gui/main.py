from turtle import Screen, Turtle

from pong_gui.ball import Ball
from pong_gui.player import Player
import time

from pong_gui.scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Player(350)
paddle2 = Player(-350)
ball = Ball()
middle_line = Turtle("square")
middle_line.color("green")
middle_line.shapesize(stretch_len=0.5, stretch_wid=30)

score_board = ScoreBoard()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or  (ball.distance(paddle2) < 50 and ball.xcor() > -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        score_board.l_point()
        ball.reset_position()


    if ball.xcor() < -380:
        score_board.r_point()
        ball.reset_position()


screen.exitonclick()