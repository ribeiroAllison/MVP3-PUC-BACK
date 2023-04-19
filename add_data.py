from app import db
from model import ToDo

c4 = ToDo(chores = 'submit repos')


db.session.add(c4)
db.session.commit()