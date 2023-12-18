from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db 
from typing import List

router = APIRouter()


#Criar Usuario
@router.post('/signup', status_code=201)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

#Listar Usuarios
@router.get('/usuarios', response_model=List[schemas.Usuario])
def signup(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios