from typing import List
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.routers import rotas_produtos, rotas_usuarios, rotas_pedidos

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

# ROTAS USUARIOS
app.include_router(rotas_usuarios.router)

# Rotas PEDIDOS
app.include_router(rotas_pedidos.router)


