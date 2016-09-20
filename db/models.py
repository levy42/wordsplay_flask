from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String(45))
    player2 = db.Column(db.String(45))
    datetime = db.Column(db.DateTime)
    log = db.Column(db.Text)

    def to_dict(self):
        return {'id': self.id, 'player1': self.player1,
                'player2': self.player2, 'datetime': self.datetime,
                'log': self.log}

    def __str__(self):
        return str(self.to_dict())
