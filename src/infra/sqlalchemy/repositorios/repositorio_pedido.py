from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import update, delete, select
from typing import List

class RepositorioPedido():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(quantidade=pedido.quantidade, local_entrega=pedido.local_entrega, tipo_entrega = pedido.tipo_entrega, observacoes= pedido.observacoes, usuario_id = pedido.usuario_id, produto_id = pedido.produto_id)
        
        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)
        return db_pedido
    
    def listar_pedidos(self):
        pedido = self.db.query(models.Pedido).all()
        return pedido
        
    
    def buscarPorId(self, id: int):
        query = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.db.execute(query).scalars().first()
        return pedido
    

    def listar_meus_pedidos_por_id(self, id: int):
        query = select(models.Pedido).where(models.Pedido.usuario_id == id)
        resultado = self.db.execute(query).scalars().all()
        return resultado
    
    def listar_minhas_vendas_por_id(self, id: int):
        query = select(models.Pedido).join_from(models.Pedido, models.Produto).where(models.Produto.usuario_id == id)
        resultado = self.db.execute(query).scalars().all()
        return resultado