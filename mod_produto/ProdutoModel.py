from sqlalchemy import Column, VARCHAR, Integer
from db import Base

class ProdutoDB(Base):
    __tablename__ = 'tb_produto'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(200), nullable=False)
    foto = Column(VARCHAR(200), nullable=True)
    valor_unitario = Column(Integer, nullable=False)

    def __init__(self, nome, descricao, foto, valor_unitario):
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario