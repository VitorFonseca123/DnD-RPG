from sqlalchemy.orm import Session
import models, schemas

def get_magias_filtradas(
    db: Session, 
    classe_id: int = None, 
    raca_id: int = None, 
    nivel: int = None,
    is_ritual: bool = None,
    escola_id: int = None
):
    
    query = db.query(models.Magia)
    origens = db.query(
    models.Magia.nome_magia,
    models.Classe.nome_classe,
    models.Raca.nome_raca,
    models.Subclasse.nome_subclasse
).outerjoin(models.MagiaOrigem, models.Magia.id_magia == models.MagiaOrigem.id_magia) \
 .outerjoin(models.Classe, models.MagiaOrigem.id_classe == models.Classe.id_classe) \
 .outerjoin(models.Raca, models.MagiaOrigem.id_raca == models.Raca.id_raca) \
 .outerjoin(models.Subclasse, models.MagiaOrigem.id_subclasse == models.Subclasse.id_subclasse)\
 .all()
    nome_origens = set()
    for linha in origens:
        #print(f"Magia: {linha.nome_magia} | Classe: {linha.nome_classe} | Raça: {linha.nome_raca} | Subclasse: {linha.nome_subclasse}")
        if linha.nome_classe:
            nome_classe = linha.nome_classe
            if linha.nome_subclasse :
                nome_classe += f" : {linha.nome_subclasse}"
            nome_origens.add((nome_classe))
        elif linha.nome_raca:
            nome_origens.add((linha.nome_raca))

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
    if escola_id is not None:
        query = query.filter(models.Magia.id_escola == escola_id)

    magias = query.all()
    for magia in magias:
        magia.nome_origens = "".join(nome_origens)
    

    return magias

def criar_magia(db: Session, magia: schemas.MagiaCreate):
    
    db_magia = models.Magia(**magia.dict())
    db.add(db_magia)
    db.commit()
    db.refresh(db_magia)
    return db_magia