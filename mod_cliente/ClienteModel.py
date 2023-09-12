import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ClienteDB(db.Base):
    __tablename__ = 'tb_cliente'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    telefone = Column(CHAR(11), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    def __init__(self, id_cliente, nome, telefone, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email