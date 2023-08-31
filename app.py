from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS, cross_origin
from flask_openapi3 import OpenAPI, Info, Tag
from schema.JokeBookSchema import ListaDePiadas, AdicionaPiada, ErrorSchema, DeleteSchema, AtualizaStars
from schema.DadSchema import GetDadScore, AtualizaScore, AddDad


info = Info(title="API de Batalha de Piadas", version='1.0.0')
app = OpenAPI(__name__, info=info)
app.app_context().push()


#Cria um banco de dados em sqlite
app.config['SQLALCHEMY_BINDS'] = {
    'jokebook': 'sqlite:///JokeBook.db',
    'dad' : 'sqlite:///Dad.db'
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///default.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

CORS(app, supports_credentials=True, resources={r"/": { "origins":""} })




# definindo tags
# Piada DB:
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc") 
get_list_tag = Tag(name='Livro de Piadas', description='Retorna a lista completa de piadas')
get_top_rated_tag = Tag(name='Top 10 piadas', description='Retorna 10 piadas mais votadas')
add_joke_tag = Tag(name='Adiciona Piada', description='Adiciona uma nova piada à lista') 
delete_tag = Tag(name='Deleta uma Piada', description='Remove uma piada da lista')
update_tag = Tag(name='Atualiza Rating', description='Muda a nota da piada')

#Dad DB:
get_dads_tag = Tag(name='Busca dads', description='Retorna score total de cada Dad')
update_dad_score_tag = Tag(name='Update pontuação de Dads', description='Aumenta 1 ponto para cada dad quando sua piada é votada')


from models.model import JokeBook, Dad

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi/swagger')

@app.get('/jokes', tags=[get_list_tag],
                    responses={'200': ListaDePiadas, '404': ErrorSchema})
@cross_origin(supports_credentials=True)
def get_all():
    """Retorna todas as piadas presentes no banco de dados JokeBook.db.
    """
    joke_list = JokeBook.query.all()
    joke_list_dict = [{'id': joke.id, 'joke': joke.joke, 'stars': joke.stars} for joke in joke_list]
    return joke_list_dict

@app.get('/jokes/top', tags=[get_top_rated_tag],
                    responses={'200': ListaDePiadas, '404': ErrorSchema})
@cross_origin(supports_credentials=True)
def get_top_rated():
    """Retorna as 10 piadas com as maiores avaliações (stars) presentes no banco de dados JokeBook.db.
    """
    joke_list = JokeBook.query.order_by(JokeBook.stars.desc()).limit(10).all()
    joke_list_dict = [{'id': joke.id, 'joke': joke.joke, 'stars': joke.stars} for joke in joke_list]
    return joke_list_dict


@app.post('/jokes', tags=[add_joke_tag],
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


@app.delete('/jokes', tags=[delete_tag],
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
    

    
@app.put('/jokes', tags=[update_tag],
                                responses={'200': AtualizaStars, '400': ErrorSchema})
@cross_origin(supports_credentials=True)
def update_rating(form: AtualizaStars):
    """Atualiza a nota da piada.
    """
    selected_joke = form.joke
    stars_update = form.stars
    if selected_joke:
        joke = JokeBook.query.filter(func.lower(JokeBook.joke) == func.lower(selected_joke)).first()
        if joke:
            joke.stars = stars_update
            db.session.commit()
            return jsonify({'message': 'Joke Rating updated successfully'}), 200
        else:
            return jsonify({'error': 'Joke not found'}), 404
    

@app.get('/dads', tags=[get_dads_tag],
                                responses={'200': GetDadScore, '400': ErrorSchema})
@cross_origin(supports_credentials=True)
def get_dads():
    """Retorna os Dads e suas pontuações
    """
    dads_scores = Dad.query.all()
    dads_scores_dict = [{'dad': dad.dad, 'score': dad.score } for dad in dads_scores]
    return dads_scores_dict

@app.put('/dads', tags=[update_dad_score_tag],
                responses={'200': AtualizaScore, '400': ErrorSchema})
@cross_origin(supports_credentials=True)
def update_dad_score(form: AtualizaScore):
    """Atualiza a pontuação dos dads."""
    dad = form.dad
    if dad:
        selected_dad = Dad.query.filter(func.lower(Dad.dad) == func.lower(dad)).first()
        if selected_dad:
            selected_dad.score += 1
            db.session.commit()
            return jsonify({'message': 'Score updated successfully'}), 200
        else:
            return jsonify({'error': 'Error updating score, dad not found'}), 404
