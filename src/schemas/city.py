
from schemas.base import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)
    lat  = db.Column(db.Float, unique=False, nullable=False)
    lon  = db.Column(db.Float, unique=False, nullable=False)

    users = db.relationship('User', backref='city', lazy=True)

    def __init__(self,  
                name, lat, lon):
                self.name = name
                self.lat = lat
                self.lon = lon