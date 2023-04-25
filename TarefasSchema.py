from pydantic import BaseModel

class ListaDeTarefas(BaseModel):
    """ Define as variváveis de uma tarefa
    """
    id: int
    chore:str
    finished: bool = False
    

class AdicionaTarefa(BaseModel):
    """ Campos a serem preenchidos na adição de uma nova tarefa
    """
    chore:str
    finished: bool = False


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mesage: str

class DeleteSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    id: int = 7

class AtualizaTarefa(BaseModel):
    """ Campos a serem preenchidos na adição de uma nova tarefa
    """
    id:int = 6
    finished: bool = True