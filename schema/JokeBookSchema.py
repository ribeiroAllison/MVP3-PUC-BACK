from pydantic import BaseModel

class ListaDePiadas(BaseModel):
    """ Define as variváveis de uma Piada
    """
    id: int
    joke:str
    stars:int
    

    

class AdicionaPiada(BaseModel):
    """ Campos a serem preenchidos na adição de uma nova Piada
    """
    joke:str



class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mesage: str

class DeleteSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    id: int

class AtualizaStars(BaseModel):
    """ Campos a serem preenchidos na adição de uma nova Piada
    """
    joke:str

