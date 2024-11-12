import turtle as t
import  random
from tkinter import messagebox
screen = t.Screen()
is_race_on = False
screen.setup(width=500,height=400)
colors = ["green", "pink", "orange", "purple", "yellow", "blue"]
user_bet = screen.textinput(title="Choose your turtle", prompt="Which turtle will win? Choose a color.")
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                messagebox.showinfo(message="You win")
            else:
                messagebox.showinfo(message="You lost, winner is " + winner)
            break
        random_dis = random.randint(1, 10)
        turtle.forward(random_dis)

screen.exitonclick()