from fastapi import FastAPI, Depends
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd

criar_bd()

app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/usuarios')
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios')
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@app.post('/pedidos')
def criar_pedido(pedido: schemas.Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).criar(pedido)
    return pedido_criado

@app.get('/pedidos')
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos