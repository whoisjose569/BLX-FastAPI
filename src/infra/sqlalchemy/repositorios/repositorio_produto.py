from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel, usuario_id=produto.usuario_id)
        
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    
    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos
        
    
    def editar(self, produto: schemas.Produto):
        update_stmt =  update(models.Produto).where(models.Produto.id == produto.id).values(nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel, usuario_id=produto.usuario_id)
        
        self.db.execute(update_stmt)
        self.db.commit()
    
    def remover(self, id:int):
        delete_smtm = delete(models.Produto).where(models.Produto.id == id)
        self.db.execute(delete_smtm)
        self.db.commit()