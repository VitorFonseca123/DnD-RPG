import os
from typing import List
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import schemas, crud
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database, models, schemas, crud


app = FastAPI()
@app.get("/magias/", response_model=List[schemas.MagiaRead])
def read_magias(
    classe_id: int = None, 
    nivel: int = None, 
    db: Session = Depends(database.get_db)
):
    magias = crud.get_magias_filtradas(db, classe_id=classe_id, nivel=nivel)
    return magias