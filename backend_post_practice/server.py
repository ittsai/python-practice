from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/click", methods=["POST"])
def click():
    name = request.form["name"]
    return f"<h1>The name: {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True)