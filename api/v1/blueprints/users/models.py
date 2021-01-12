from api import db


class Users(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(200))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.password = email
