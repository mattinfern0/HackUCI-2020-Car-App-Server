#import app
from app.app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    body_type = db.Column(db.String)
    price = db.Column(db.Float)
    
    def __repr__(self):
        return f"Make: {self.make}; Price: {self.price}"

    def serialize(self):
        return {
            'id': self.id,
            'make': self.make,
            'body_type': self.body_type,
            'price': self.price
        }