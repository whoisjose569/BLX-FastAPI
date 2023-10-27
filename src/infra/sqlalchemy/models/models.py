from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String)

class Usuario(Base):
    
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)

class Pedido(Base):
    
    __tablename__ = 'pedido'
    
    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    entrega = Column(Boolean)
    endereco = Column(String)
    observacoes = Column(String)