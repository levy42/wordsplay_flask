from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context

db = SQLAlchemy()


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String(45))
    player2 = db.Column(db.String(45))
    datetime = db.Column(db.DateTime)
    log = db.Column(db.Text)
