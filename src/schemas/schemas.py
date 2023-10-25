from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id : Optional[int] = None
    nome: str
    telefone: str
    #meus_produtos: List[Produto]
    #minhas_vendas: List[Pedido]
    #meus_pedidos: List[Pedido]
    
    class Config:
        orm_mode = True
    

class Produto(BaseModel):
    id : Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    
    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    id : Optional[int] = None
    nome: str
    preco: float  
    
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
    
    