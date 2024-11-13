import time
from turtle import Screen

from turtle_crossing_road_gui.car import Car
from turtle_crossing_road_gui.player import PlayerTurtle
from turtle_crossing_road_gui.scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
score_board = ScoreBoard()
player = PlayerTurtle()

car_manager = Car()

screen.listen()
screen.onkey(player.move_y, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create()
    car_manager.move()

    for car in car_manager.all_cars:

        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

        if player.is_at_finish_line():
            score_board.win()
            player.restart()
            car_manager.increase_speed(score_board.level)

screen.exitonclick()