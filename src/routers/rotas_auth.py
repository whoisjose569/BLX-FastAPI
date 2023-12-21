from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db 
from typing import List
from src.infra.providers import hash_provider

router = APIRouter()


#Criar Usuario
@router.post('/signup', status_code=201, response_model=UsuarioSimples)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    
    # Verificar se ja existe um para o telefone
    usuario_localizado = RepositorioUsuario(db).obter_por_telefone(usuario.telefone)
    
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= 'Ja existe um Usuario para esse telefone')
    
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
