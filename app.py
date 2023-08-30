from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_openapi3 import OpenAPI, Info, Tag
from JokeBookSchema import *



info = Info(title="API de Batalha de Piadas", version='1.0.0')
app = OpenAPI(__name__, info=info)
app.app_context().push()
CORS(app, supports_credentials=True, resource={r"/": { "origins":""} })


#Cria um banco de dados em sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///JokeBook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
get_list_tag = Tag(name='Livro de Piadas', description='Retorna a lista completa de piadas')
get_top_rated_tag = Tag(name='Top 10 piadas', description='Retorna 10 piadas mais votadas')
add_joke_tag = Tag(name='Adiciona Piada', description='Adiciona uma nova piada à lista')
delete_tag = Tag(name='Deleta uma Piada', description='Remove uma piada da lista')
update_tag = Tag(name='Atualiza Rating', description='Muda a nota da piada')

from model import JokeBook

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi/swagger')

@app.get('/get_list', tags=[get_list_tag],
                    responses={'200': ListaDePiadas, '404': ErrorSchema})
@cross_origin(supports_credentials=True)
def get_all():
    """Retorna todas as piadas presentes no banco de dados JokeBook.db.
    """
    joke_list = JokeBook.query.all()
    joke_list_dict = [{'id': joke.id, 'joke': joke.joke, 'stars': joke.stars} for joke in joke_list]
    return joke_list_dict

@app.get('/get_top_rated', tags=[get_top_rated_tag],
                    responses={'200': ListaDePiadas, '404': ErrorSchema})
@cross_origin(supports_credentials=True)
def get_top_rated():
    """Retorna as 10 piadas com as maiores avaliações (stars) presentes no banco de dados JokeBook.db.
    """
    joke_list = JokeBook.query.order_by(JokeBook.stars.desc()).limit(10).all()
    joke_list_dict = [{'id': joke.id, 'joke': joke.joke, 'stars': joke.stars} for joke in joke_list]
    return joke_list_dict


@app.post('/add_joke', tags=[add_joke_tag],
                                responses={'200': AdicionaPiada, '400': ErrorSchema})
@cross_origin(supports_credentials=True)
def add_joke(form: AdicionaPiada):
    """Adiciona uma nova tarefa (tupla) ao banco de dados.
    """
    joke_to_add = form.joke
    stars_to_add = form.stars

    if joke_to_add:
        # Cria um novo objeto JokeBook a ser inserido no banco de dados
        new_joke = JokeBook(joke=joke_to_add , stars=stars_to_add)
        db.session.add(new_joke)
        db.session.commit()
        return jsonify({'message': 'Joke added successfully'}), 201
    else:
        return jsonify({'error': 'Joke name is required'}), 400


@app.delete('/delete_joke', tags=[delete_tag],
                                responses={'200': DeleteSchema, '400': ErrorSchema})
def delete_joke(query: DeleteSchema):
    """Delete uma tarefa do banco de dados.
    """
    joke = JokeBook.query.get(query.id)  # Get objeto do tipo 'joke' pelo id
    if joke:
        db.session.delete(joke)  # Deleta objeto do banco de dados
        db.session.commit()
        return jsonify({'message': 'Joke deleted successfully'}), 200
    else:
        return jsonify({'error': 'Joke not found'}), 404
    

    
@app.post('/update_joke', tags=[update_tag],
                                responses={'200': AtualizaStars, '400': ErrorSchema})
@cross_origin(supports_credentials=True)
def update_rating(form: AtualizaStars):
    """Atualiza a nota da piada.
    """
    joke_id = form.id
    stars_update = form.stars
    if joke_id:
        joke = JokeBook.query.get(joke_id)
        joke.stars = stars_update
        db.session.commit()
        return jsonify({'message': 'Joke Rating updated successfully'}), 200
    else:
        return jsonify({'error': 'Joke not found'}), 404
    
