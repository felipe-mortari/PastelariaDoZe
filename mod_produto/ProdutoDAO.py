
from fastapi import APIRouter
from mod_produto.Produto import Produto  # Importe a classe de modelo correta aqui
from mod_produto.ProdutoModel import ProdutoDB  # Importe a classe de modelo do banco de dados correta aqui
import db

# import da segurança
from fastapi import Depends
import security

# dependências de forma global
router = APIRouter( dependencies=[Depends(security.verify_token), Depends(security.verify_key)] ) 

@router.get("/produto/", tags=["Produto"],
dependencies=[Depends(security.verify_token), Depends(security.verify_key)])
def get_produtos():
    try:
        session = db.Session()
        produtos = session.query(ProdutoDB).all()
        return produtos, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        produto = session.query(ProdutoDB).filter(ProdutoDB.id == id).first()
        if produto:
            return produto, 200
        else:
            return {"mensagem": "Produto não encontrado"}, 404
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()
        produto_db = ProdutoDB(
            nome=corpo.nome,
            descricao=corpo.descricao,
            foto=corpo.foto,
            valor_unitario=corpo.valor_unitario
        )
        session.add(produto_db)
        session.commit()
        return {"id": produto_db.id}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        produto_db = session.query(ProdutoDB).filter(ProdutoDB.id == id).first()
        if produto_db:
            produto_db.nome = corpo.nome
            produto_db.descricao = corpo.descricao
            produto_db.foto = corpo.foto
            produto_db.valor_unitario = corpo.valor_unitario
            session.commit()
            return {"id": produto_db.id}, 200
        else:
            return {"mensagem": "Produto não encontrado"}, 404
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try:
        session = db.Session()
        produto_db = session.query(ProdutoDB).filter(ProdutoDB.id == id).first()
        if produto_db:
            session.delete(produto_db)
            session.commit()
            return {"mensagem": "Produto excluído com sucesso"}, 200
        else:
            return {"mensagem": "Produto não encontrado"}, 404
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()