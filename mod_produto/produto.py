from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    foto: str
    valor_unitario: int