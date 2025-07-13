from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import schemas
from repositories import crud
from typing import List

from models.models import Clinica, Veterinario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clinicas", response_model=schemas.ClinicaOut, tags=["Clínicas"])
def create_clinica(clinica: schemas.ClinicaCreate, db: Session = Depends(get_db)):
    return crud.create_clinica(db, clinica)

@router.get("/clinicas", response_model=List[schemas.ClinicaOut], tags=["Clínicas"])
def listar_clinicas(db: Session = Depends(get_db)):
    return db.query(Clinica).all()

@router.get("/clinicas/{clinica_id}", response_model=schemas.ClinicaOut, tags=["Clínicas"])
def get_clinica(clinica_id: int, db: Session = Depends(get_db)):
    clinica = db.query(Clinica).filter(Clinica.id == clinica_id).first()
    if not clinica:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")
    return clinica

@router.get("/clinicas/{clinica_id}/veterinarios", response_model=List[schemas.VeterinarioOut], tags=["Clínicas"])
def get_veterinarios_da_clinica(clinica_id: int, db: Session = Depends(get_db)):
    clinica = db.query(Clinica).filter(Clinica.id == clinica_id).first()
    if not clinica:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")
    return clinica.veterinarios
