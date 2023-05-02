from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_openapi3 import OpenAPI, Info, Tag
from TarefasSchema import *





info = Info(title="API de lista de tarefas", version='1.0.0')
app = OpenAPI(__name__, info=info)
app.app_context().push()
CORS(app, supports_credentials=True, resource={r"/": { "origins":""} })


#Cria um banco de dados em sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

from model import ToDo

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
get_list_tag = Tag(name='Lista de Tarefas', description='Retorna a lista completa de tarefas')
add_chore_tag = Tag(name='Adiciona Tarefa', description='Adiciona uma nova tarefa à lista')
delete_tag = Tag(name='Deleta uma Tarefa', description='Remove uma tarefa da lista')
update_tag = Tag(name='Atualiza Status', description='Muda o status de uma tarefa')

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi/swagger')

@app.get('/get_list', tags=[get_list_tag],
                    responses={'200': ListaDeTarefas, '404': ErrorSchema})
@cross_origin(supports_credentials=True)
def getList():
    """Retorna todas as tarefas a serem cumpridas, presentes no banco de dados todo.db.
    """
    chore_list = ToDo.query.all()
    chore_list_dict = [{'id': chore.id, 'chores': chore.chores, 'finished': chore.finished} for chore in chore_list]
    return chore_list_dict


@app.post('/add_chore', tags=[add_chore_tag],
                                responses={'200': AdicionaTarefa, '400': ErrorSchema})
@cross_origin(supports_credentials=True)
def add_chore(form: AdicionaTarefa):
    """Adiciona uma nova tarefa (tupla) ao banco de dados.
    """
    chore = form.chore
    finished = form.finished

    if chore:
        # Cria um novo objeto ToDo a ser inserido no banco de dados
        new_chore = ToDo(chores=chore , finished=finished)
        db.session.add(new_chore)
        db.session.commit()
        return jsonify({'message': 'Chore added successfully'}), 201
    else:
        return jsonify({'error': 'Chore name is required'}), 400


@app.delete('/delete_chore', tags=[delete_tag],
                                responses={'200': DeleteSchema, '400': ErrorSchema})
def delete_chore(query: DeleteSchema):
    """Delete uma tarefa do banco de dados.
    """
    chore = ToDo.query.get(query.id)  # Get objeto do tipo 'chore' pelo id
    if chore:
        db.session.delete(chore)  # Deleta objeto do banco de dados
        db.session.commit()
        return jsonify({'message': 'Chore deleted successfully'}), 200
    else:
        return jsonify({'error': 'Chore not found'}), 404
    

    
@app.post('/update_chore', tags=[update_tag],
                                responses={'200': AtualizaTarefa, '400': ErrorSchema})
@cross_origin(supports_credentials=True)
def update_chore(form: AtualizaTarefa):
    """Alterna o status da tarefa entre resolvido e pendente.
    """
    chore_id = form.id
    finished = form.finished
    if chore_id:
        chore = ToDo.query.get(chore_id)
        chore.finished = not finished
        db.session.commit()
        return jsonify({'message': 'Chore updated successfully'}), 200
    else:
        return jsonify({'error': 'Chore not found'}), 404