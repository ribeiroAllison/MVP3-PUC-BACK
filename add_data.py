from app import db
from model import ToDo

c1 = ToDo(chores = 'create an API')
c2 = ToDo(chores = 'make a front-end')
c3 = ToDo(chores = 'finish MVP')

db.session.add(c1)
db.session.add(c2)
db.session.add(c3)
db.session.commit()