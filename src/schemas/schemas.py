from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id : Optional[int] = None
    nome: str
    telefone: str
    senha: str
    #produtos: List[Produto] = []

    
    class Config:
        orm_mode = True
    

class Produto(BaseModel):
    id : Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    usuario: Optional[Usuario] = None
    
    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    id : Optional[int] = None
    nome: str
    preco: float 
    usuario_id: int
    
    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id : Optional[int] = None
    # usuario: Usuario
    # Produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'

    class Config:
        orm_mode = True
    
    