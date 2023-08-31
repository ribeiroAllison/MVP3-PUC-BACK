from app import db
from dataclasses import dataclass


@dataclass
class JokeBook(db.Model):
    __tablename__ = 'jokebook'
    __bind_key__ = 'jokebook'

    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(100), nullable=False)
    stars = db.Column(db.Integer)


@dataclass
class Dad(db.Model):
    __tablename__ = 'dad'
    __bind_key__ = 'dad'

    dad = db.Column(db.String(100), primary_key=True)
    score = db.Column(db.Integer)