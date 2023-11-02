from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List

class ProdutoSimples(BaseModel):
    id : Optional[int] = None
    nome: str
    preco: float 
    disponivel: bool
    
    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id : Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []

    
    class Config:
        orm_mode = True
        

class UsuarioSimples(BaseModel):
    id : Optional[int] = None
    nome: str
    telefone: str

    
    class Config:
        orm_mode = True



class Produto(BaseModel):
    id : Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int] = None
    usuario: Optional[UsuarioSimples] = None
    
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
    
    