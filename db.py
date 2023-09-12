from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import STR_DATABASE

engine = create_engine(STR_DATABASE)
engine = create_engine("sqlite:///pastelaria_db.db") 

Session = sessionmaker(bind=engine)
# para trabalhar com tabelas
Base = declarative_base()

# cria, caso não existam, as tabelas de todos os modelosque encontrar na aplicação (importados)
def criaTabelas():
    Base.metadata.create_all(engine)

    import sqlite3

# Conecte-se ao banco de dados SQLite
    conn = sqlite3.connect('pastelaria_db.db')
    cursor = conn.cursor()
    import sqlite3

# Conecte-se ao banco de dados SQLite
conn = sqlite3.connect('pastelaria_db.db')
cursor = conn.cursor()

# Execute consultas SQL
cursor.execute("SELECT * FROM tabela")
resultados = cursor.fetchall()

# Feche a conexão
conn.close()
