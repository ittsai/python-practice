from flask import Flask, render_template, request, flash, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db.init_app(app)
login_manager =LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

class User(UserMixin, db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable= False)
    password: Mapped[str] = mapped_column(String, nullable= False)

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Register")

with app.app_context():
     db.create_all()

@app.route("/")
def home():
    return render_template("index.html", logged_in= current_user.is_authenticated)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    form.validate_on_submit()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = db.session.execute(db.select(User).where(User.username == username))
        user = result.scalar()
        if not user or check_password_hash(user.password, password):
            flash("Wrong username or password", "error")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("authenticated"))

    return render_template("login.html", form=form, logged_in= current_user.is_authenticated)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    form.validate_on_submit()

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = db.session.execute(db.select(User).where(User.username == username))
        user = result.scalar()
        if user:
            flash("Already registered", "error")
            return redirect(url_for("login"))
        else:
            hash_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
            new_user = User(username=username, password=hash_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("authenticated"))

    return render_template("register.html", form=form, logged_in= current_user.is_authenticated)

@app.route("/logout")
def logout():
    logout_user()
    return render_template("logout.html", logged_in= current_user.is_authenticated)

@app.route("/authenticated-page")
def authenticated():
    return render_template("authenticated-page.html", logged_in=True)

if __name__ == "__main__":
    app.run(debug=True)