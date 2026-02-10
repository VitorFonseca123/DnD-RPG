from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, SmallInteger
from sqlalchemy.orm import relationship
from database import Base


class EscolaMagia(Base):
    __tablename__ = "escola_magia"
    id_escola = Column(Integer, primary_key=True, index=True)
    nome_escola = Column(String(50), nullable=False)

class Classe(Base):
    __tablename__ = "classe"
    id_classe = Column(Integer, primary_key=True, index=True)
    nome_classe = Column(String(50), nullable=False)

class Raca(Base):
    __tablename__ = "raca"
    id_raca = Column(Integer, primary_key=True, index=True)
    nome_raca = Column(String(50), nullable=False)
    descricao_raca = Column(Text)
    aprim_val_hab = Column(String(50))
    tamanho = Column(String(20))
    deslocamento = Column(Integer)
    proficiencias = Column(Text)
    idiomas = Column(Text)

class Habilidade(Base):
    __tablename__ = "habilidade"
    id_habilidade = Column(Integer, primary_key=True, index=True)
    nome_skill = Column(String(50), nullable=False)
    descricao = Column(Text)
    lvl = Column(SmallInteger)


class SubRaca(Base):
    __tablename__ = "sub_raca"
    id_subraca = Column(Integer, primary_key=True, index=True)
    id_raca = Column(Integer, ForeignKey('raca.id_raca', ondelete="CASCADE"))
    nome_subraca = Column(String(50))
    descricao_subraca = Column(Text)
    aprim_val_hab = Column(String(50))
    proficiencias = Column(Text)

class Subclasse(Base):
    __tablename__ = "subclasse"
    id_subclasse = Column(Integer, primary_key=True, index=True)
    id_classe = Column(Integer, ForeignKey('classe.id_classe', ondelete="CASCADE"))
    nome_subclasse = Column(String(50))
    desc_subclasse = Column(Text)

class Magia(Base):
    __tablename__ = "magia"
    id_magia = Column(Integer, primary_key=True, index=True)
    nome_magia = Column(String(100), nullable=False)
    nivel = Column(Integer, nullable=False)
    id_escola = Column(Integer, ForeignKey('escola_magia.id_escola'))
    tempo_conju = Column(String(50))
    alcance = Column(String(50))
    duracao = Column(String(50))
    descricao_magia = Column(Text)
    is_ritual = Column(Boolean, default=False)
    is_concentration = Column(Boolean, default=False)
    somatico = Column(Boolean, default=False)
    verbal = Column(Boolean, default=False)
    material = Column(Text)


class HabilidadeOrigem(Base):
    __tablename__ = "habilidade_origem"
    id_habilidadeor = Column(Integer, primary_key=True, index=True)
    id_habilidade = Column(Integer, ForeignKey('habilidade.id_habilidade'))
    id_raca = Column(Integer, ForeignKey('raca.id_raca'))
    id_subraca = Column(Integer, ForeignKey('sub_raca.id_subraca'))
    id_classe = Column(Integer, ForeignKey('classe.id_classe'))
    id_subclasse = Column(Integer, ForeignKey('subclasse.id_subclasse'))

class MagiaOrigem(Base):
    __tablename__ = "magia_origem"
    id_magiaor = Column(Integer, primary_key=True, index=True)
    id_magia = Column(Integer, ForeignKey('magia.id_magia'))
    id_raca = Column(Integer, ForeignKey('raca.id_raca'))
    id_subraca = Column(Integer, ForeignKey('sub_raca.id_subraca'))
    id_classe = Column(Integer, ForeignKey('classe.id_classe'))
    id_subclasse = Column(Integer, ForeignKey('subclasse.id_subclasse'))