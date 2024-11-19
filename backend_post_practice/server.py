from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, number_range

app = Flask(__name__)
app.secret_key = "qwertyu"
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(),number_range(6,120)])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()

    return render_template("login.html", form=login_form)

@app.route("/click", methods=["POST"])
def click():
    name = request.form["name"]
    return f"<h1>The name: {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True)