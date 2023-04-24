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