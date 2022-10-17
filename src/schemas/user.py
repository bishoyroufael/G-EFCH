from schemas.base import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, unique=False, nullable=False)
    lastname  = db.Column(db.String, unique=False, nullable=False)
    phone     = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    job       = db.Column(db.String, unique=False, nullable=False)
    company   = db.Column(db.String, unique=False, nullable=False)

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

    def __init__(self, firstname, 
                lastname, 
                email, 
                phone, 
                job, 
                company 
                ):
                self.firstname = firstname
                self.lastname  = lastname 
                self.phone     = phone 
                self.email     = email 
                self.job       = job       
                self.company   = company   

