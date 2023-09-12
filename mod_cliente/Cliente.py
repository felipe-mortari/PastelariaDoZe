from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    email: str
    telefone: str = None