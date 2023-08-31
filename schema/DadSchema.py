from pydantic import BaseModel

class GetDadScore(BaseModel):
    # Busca todos os dads e suas respectivas pontuações
    dad: str
    score: int

class AtualizaScore(BaseModel):
    """ Atualiza Score do Dad
    """
    dad: str
    score: int