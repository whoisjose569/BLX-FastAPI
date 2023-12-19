from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db
from typing import List

router = APIRouter()

#Criar Produto
@router.post('/produtos', status_code=201, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

#Listar Produtos
@router.get('/produtos', status_code=200, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

#Atualizar Produto
@router.put('/produtos/{id}', response_model=List[ProdutoSimples])
def atualizar_produto(id: int, produto: schemas.Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id, produto)
    produto.id = id
    return produto

#Remover Produto
@router.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return

# Buscar por ID
@router.get('/produtos/{id}')
def exibir_produto(id: int, db: Session = Depends(get_db) ):
    produto_localizado = RepositorioProduto(db).buscarPorID(id)
    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Produto nao Localizado")
    return produto_localizado