import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# connection database
# db = sqlite3.connect("test.db")

# control database
# cursor = db.cursor()

# create table
# cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE, author VARCHAR(250) NOT NULL,"
#                "rating FLOAT NOT NULL")
# cursor.execute("INSERT INTO test VALUES(1, 'test', 'test', '10.0')")
# db.commit()

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///backend_sqlite_practice.db"

db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email:Mapped[str] = mapped_column(unique=True)

with app.app_context():
    db.create_all()
    new_user = User(id = 1, username="test", email="test")
    db.session.add(new_user)
    db.session.commit()

