# O que é esse projeto?

Este é uma API REST feita como parte do MVP da terceira sprint da pós graduação em Desenvolvimento Full Stack pela PUC-Rio

Esta API recebe requests do front-end e atualiza um banco de dados contendo uma lista da tarefas a serem realizadas pelo usuário.


## Rotas:

### Esta API é pelas seguintes rotas:

#### BANCO DE DADOS DE PIADAS - JOKEBOOK:

- `Rota /:` Do método `GET`, é identificada por '/' e leva à documentação em Swagger.
- `Rota /jokes:` Do método `GET`, retorna todas as piadas do banco de dados.
- `Rota /jokes/top:` Do método `GET`, retorna as 10 piadas mais votadas do banco de dados.
- `Rota /jokes:` Do método `POST`, adiciona uma nova piada ao JokeBook.
- `Rota /jokes:` Do método `PUT`, aumenta o score de uma piada em 1 ponto.
- `Rota /jokes:` Do método `DELETE`, apaga uma piada.

#### BANCO DE DADOS DE COMBATENTES(DADS) - DAD:

- `Rota /dads:` Do método `GET`, retorna os combatentes e seus respectivos scores.
- `Rota /dads:` Do método `PUT`, adiciona 1 ponto ao score do combatente votado.


## Como instalar:

### Cenário 1, sem utilização de ambiente virtual:

- Execute no terminal:
```
pip install -r requirements.txt
```

- Inicie o servidor com este comando no terminal:
```
python -m flask run 
```
### Cenário 2, com utilização de ambiente virtual:

- Ative o ambiente virtual com o comando:
```
source .venv(ou o nome do seu ambiente)/Scripts/activate
```

- Execute no terminal:
```
pip install -r requirements.txt
```

- Inicie o servidor com este comando no terminal:
```
python -m flask run 
```

## Execução:

Abra o http://127.0.0.1:5000 no navegador para ser direcionado à documentação em Swagger.

