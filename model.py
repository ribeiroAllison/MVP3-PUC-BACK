from app import db, app
from dataclasses import dataclass


@dataclass
class JokeBook(db.Model):
    __tablename__ = 'jokebook'

    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(100), nullable=False)
    stars = db.Column(db.Integer)