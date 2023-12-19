from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db
from typing import List

router = APIRouter()


#Criar Pedido
@router.post('/pedidos', status_code=201)
def criar_pedido(pedido: schemas.Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).criar(pedido)
    return pedido_criado

#Listar Pedidos
@router.get('/pedidos')
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos

#Buscar Pedido
@router.get('/pedidos/{id}')
def exibir_pedido_id(id: int, db : Session = Depends(get_db)):
    pedido_localizado = RepositorioPedido(db).buscarPorId(id)
    if not pedido_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Pedido nao Localizado")
    return pedido_localizado

# @router.get('/pedidos/{usuario_id}', response_model=List[schemas.Pedido])
# def listar_pedidos_id(usuario_id: int, db: Session = Depends(get_db)):
#     pedidos = RepositorioPedido(db).listar_meus_pedidos_por_id(usuario_id)
#     return pedidos

# @router.get('/pedidos/{usuario_id}/vendas', response_model=List[schemas.Pedido])
# def listar_vendas_id(usuario_id: int, db: Session = Depends(get_db)):
#     pedidos = RepositorioPedido(db).listar_minhas_vendas_por_id(usuario_id)
#     return pedidos