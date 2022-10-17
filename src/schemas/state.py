from schemas.base import db


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    cities = db.relationship('City', backref='state', lazy=True)


    def __init__(self,  
                name):
                self.name = name