from typing import List
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.routers import rotas_produtos, rotas_usuarios

#criar_bd()

app = FastAPI()

# Cors
origins = ["http://localhost:8000", "127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas PRODUTOS
app.include_router(rotas_produtos.router)

# RITAS USUARIOS
app.include_router(rotas_usuarios.router)


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

