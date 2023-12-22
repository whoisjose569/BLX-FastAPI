from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select


class RepositorioUsuario():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome=usuario.nome, telefone=usuario.telefone, senha=usuario.senha)
        
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    
    def listar(self):
        usuario = self.db.query(models.Usuario).all()
        return usuario
        
    
    def obter_por_telefone(self, telefone) -> models.Usuario:
        query = select(models.Usuario).where(models.Usuario.telefone == telefone)
        return self.db.execute(query).scalars().first()
