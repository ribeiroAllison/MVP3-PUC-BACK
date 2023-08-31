from flask_openapi3 import OpenAPI, Info, Tag
from app import app

info = Info(title="API de Batalha de Piadas", version='1.0.0')
openapi = OpenAPI(app, info=info)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
get_list_tag = Tag(name='Livro de Piadas', description='Retorna a lista completa de piadas')
get_top_rated_tag = Tag(name='Top 10 piadas', description='Retorna 10 piadas mais votadas')
add_joke_tag = Tag(name='Adiciona Piada', description='Adiciona uma nova piada à lista')
delete_tag = Tag(name='Deleta uma Piada', description='Remove uma piada da lista')
update_tag = Tag(name='Atualiza Rating', description='Muda a nota da piada')