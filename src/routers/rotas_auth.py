from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db 
from typing import List
from src.infra.providers import hash_provider,token_provider
from src.routers.auth_utils import obter_usuario_logado

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

@router.post('/token')
def login(login_data: schemas.LoginData, db: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone
    
    usuario = RepositorioUsuario(db).obter_por_telefone(telefone)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estão incorretos!')
    
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estão incorretos!')
    
    token = token_provider.criar_access_token({'sub': usuario.telefone})
    return {'usuario': usuario, 'access_token': token}

@router.get('/me', response_model=schemas.UsuarioSimples)
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario
    
