from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    telefone: str = None
    cpf: str
    compra_fiado: str
    dia_fiado: str
    senha: str = None