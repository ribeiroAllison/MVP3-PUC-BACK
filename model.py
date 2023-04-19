from app import db, app
from dataclasses import dataclass


@dataclass
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chores = db.Column(db.String(100), nullable=False)
    finished = db.Column(db.Boolean, unique = False, default = False)