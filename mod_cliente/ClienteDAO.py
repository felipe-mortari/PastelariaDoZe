from fastapi import APIRouter
from mod_cliente.Cliente import Cliente  # Importe a classe de modelo correta aqui
from mod_cliente.ClienteModel import ClienteDB  # Importe a classe de modelo do banco de dados correta aqui
import db

router = APIRouter()

@router.get("/cliente/", tags=["Cliente"])
def get_clientes():
    try:
        session = db.Session()
        clientes = session.query(ClienteDB).all()
        return clientes, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    try:
        session = db.Session()
        cliente = session.query(ClienteDB).filter(ClienteDB.cliente_id == id).first()
        if cliente:
            return cliente, 200
        else:
            return {"mensagem": "Cliente não encontrado"}, 404
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(corpo: Cliente):
    try:
        session = db.Session()
        cliente_db = ClienteDB(
            nome=corpo.nome,
            cpf=corpo.cpf,
            telefone=corpo.telefone,
            senha=corpo.senha,
            cliente_id=corpo.cliente_id,
            dia_fiado=corpo.dia_fiado,
            compra_fiado=corpo.compra_fiado
        )
        session.add(cliente_db)
        session.commit()
        return {"id": cliente_db.id}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        cliente_db = session.query(ClienteDB).filter(ClienteDB.cliente_id == id).first()
        if cliente_db:
            cliente_db.nome = corpo.nome
            cliente_db.cpf = corpo.cpf
            cliente_db.telefone = corpo.telefone
            cliente_db.senha = corpo.senha
            cliente_db.cliente_id = corpo.cliente_id
            cliente_db.dia_fiado = corpo.dia_fiado
            cliente_db.compra_fiado = corpo.compra_fiado
            session.commit()
            return {"id": cliente_db.id}, 200
        else:
            return {"mensagem": "Cliente não encontrado"}, 404
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()
        cliente_db = session.query(ClienteDB).filter(ClienteDB.cliente_id == id).first()
        if cliente_db:
            session.delete(cliente_db)
            session.commit()
            return {"mensagem": "Cliente excluído com sucesso"}, 200
        else:
            return {"mensagem": "Cliente não encontrado"}, 404
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()