from flask import Flask, render_template
import datetime as dt
import random
app = Flask(__name__)

@app.route("/")
def home():
    number = random.randint(1, 10)
    year = str(dt.datetime.now().year)
    lst = ["test", "Test"]
    return render_template("index.html", num=number, y=year, lst=lst)
if __name__ == "__main__":
    app.run(debug=True)