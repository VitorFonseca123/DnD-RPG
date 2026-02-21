from pydantic import BaseModel
from typing import Optional, List


class EscolaMagiaBase(BaseModel):
    id_escola: int
    nome_escola: str

    class Config:
        from_attributes = True


class MagiaBase(BaseModel):
    nome_magia: str
    nivel: int
    tempo_conju: Optional[str] = None
    alcance: Optional[str] = None
    duracao: Optional[str] = None
    descricao_magia: Optional[str] = None
    is_ritual: bool = False
    is_concentration: bool = False
    somatico: bool = False
    verbal: bool = False
    material: Optional[str] = None
    nome_origens: Optional[str] = None


class MagiaCreate(MagiaBase):
    id_escola: Optional[int] = None


class MagiaRead(MagiaBase):
    id_magia: int
    
    class Config:
        from_attributes = True