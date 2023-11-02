from typing import List
from fastapi import FastAPI, Depends, status
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

#criar_bd()

app = FastAPI()

#Criar Produto
@app.post('/produtos', status_code=201, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

#Listar Produtos
@app.get('/produtos', status_code=200, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

#Atualizar Produto
@app.put('/produtos/{id}', response_model=List[ProdutoSimples])
def atualizar_produto(id: int, produto: schemas.Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id, produto)
    produto.id = id
    return produto

#Remover Produto
@app.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return
    

#Criar Usuario
@app.post('/signup', status_code=201)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

#Listar Usuarios
@app.get('/usuarios', response_model=List[schemas.Usuario])
def signup(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

#Criar Pedido
@app.post('/pedidos', status_code=201)
def criar_pedido(pedido: schemas.Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).criar(pedido)
    return pedido_criado

#Listar Pedidos
@app.get('/pedidos')
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos

