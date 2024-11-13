import pandas

import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []


answer = turtle.textinput(title=f"0/50 States correct", prompt="What's state's name?")

while len(guessed_states) < 50:
    answer = turtle.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's state's name?").title()

    if answer == "Exit":
        missing_states = []
        for state in states:
            if not state in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_states.csv")
        break

    if answer in states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_info = data[data.state == answer]
        t.goto(state_info.x.item(), state_info.y.item())
        t.write(answer)
        guessed_states.append(answer)
