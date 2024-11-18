from flask import Flask, template_rendered
import random

app = Flask(__name__)
answer = random.randint(0, 9)

@app.route("/")
def home():
    return "<h1>Guess a number!</h1>"

@app.route("/<int:num>")
def guess(num):
    if answer == num:
        return "<h1>You find it!<h1>"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif answer > num:
        return "<h1>Too low!<h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1>Too high!<h1>"\
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)