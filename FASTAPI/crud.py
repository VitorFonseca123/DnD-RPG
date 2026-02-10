from sqlalchemy.orm import Session
import models, schemas

def get_magias_filtradas(
    db: Session, 
    classe_id: int = None, 
    raca_id: int = None, 
    nivel: int = None,
    is_ritual: bool = None
):
    
    query = db.query(models.Magia)

      # Filtros por Relação com MagiaOrigem
    if classe_id or raca_id:
        query = query.join(models.MagiaOrigem)
        
        if classe_id:
            query = query.filter(models.MagiaOrigem.id_classe == classe_id)
        if raca_id:
            query = query.filter(models.MagiaOrigem.id_raca == raca_id)

    # Filtros Diretos na Tabela Magia
    if nivel is not None:
        query = query.filter(models.Magia.nivel == nivel)
    if is_ritual is not None:
        query = query.filter(models.Magia.is_ritual == is_ritual)

    return query.all()

def criar_magia(db: Session, magia: schemas.MagiaCreate):
    
    db_magia = models.Magia(**magia.dict())
    db.add(db_magia)
    db.commit()
    db.refresh(db_magia)
    return db_magia