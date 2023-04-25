# O que é esse projeto?

Este é uma API REST feita como parte do MVP da primeira sprint da pós graduação em Desenvolvimento Full Stack pela PUC-Rio

Esta API recebe requests do front-end e atualiza um banco de dados contendo uma lista da tarefas a serem realizadas pelo usuário.


## Rotas:

### Esta API é composta por cinco rotas:

- `Rota index:` Do método `GET`, é identificada por '/' e leva à documentação em Swagger.
- `Rota get_list:` Do método `GET`, retorna todas as tarefas presentes no banco de dados.
- `Rota add_chore:` Do método `POST`, adiciona uma nova tarefa ao banco de dados.
- `Rota delete_chore:` Do método `DELETE`, exclui uma tarefa do banco de dados.
- `Rota update_chore:` Do método `POST`, alterna o status de uma tarefa entre pendente e concluído.

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

