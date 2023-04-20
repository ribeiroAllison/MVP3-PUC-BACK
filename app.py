from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.app_context().push()
CORS(app, support_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

from model import ToDo

@app.route('/get_list')
@cross_origin(supports_credentials=True)
def getList():
    chore_list = ToDo.query.all()
    chore_list_dict = [{'id': chore.id, 'chores': chore.chores, 'finished': chore.finished} for chore in chore_list]
    return chore_list_dict


@app.route('/add_chore', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_chore():
    data = request.get_json()  # Get data from request body
    chore = data.get('chore')
    finished = data.get('finished')
    if chore:
        # Create a new ToDo object and add it to the database
        new_chore = ToDo(chores=chore, finished=finished)
        db.session.add(new_chore)
        db.session.commit()
        return jsonify({'message': 'Chore added successfully'}), 201
    else:
        return jsonify({'error': 'Chore name is required'}), 400


@app.route('/delete_chore/<int:chore_id>', methods=['DELETE'])
def delete_chore(chore_id):
    chore = ToDo.query.get(chore_id)  # Get chore object by ID
    if chore:
        db.session.delete(chore)  # Delete chore object from the database
        db.session.commit()
        return jsonify({'message': 'Chore deleted successfully'}), 200
    else:
        return jsonify({'error': 'Chore not found'}), 404
    

    
@app.route('/update_chore', methods=['POST'])
def update_chore():
    data = request.get_json()  # Get data from request body
    chore_id = data.get('id')
    finished = data.get('finished')
    if chore_id:
        chore = ToDo.query.get(chore_id)
        chore.finished = not finished
        db.session.commit()
        return jsonify({'message': 'Chore updated successfully'}), 200
    else:
        return jsonify({'error': 'Chore not found'}), 404