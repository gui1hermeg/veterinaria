from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import models
from schemas import schemas
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/atendimentos", response_model=schemas.AtendimentoOut, tags=["Atendimentos"])
def criar_atendimento(atendimento: schemas.AtendimentoCreate, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == atendimento.pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado.")
    vet = db.query(models.Veterinario).filter(models.Veterinario.id == atendimento.veterinario_id).first()
    if not vet:
        raise HTTPException(status_code=404, detail="Veterinário não encontrado.")
    db_atendimento = models.Atendimento(**atendimento.dict())
    db.add(db_atendimento)
    db.commit()
    db.refresh(db_atendimento)
    return db_atendimento

@router.get("/atendimentos", response_model=List[schemas.AtendimentoOut], tags=["Atendimentos"])
def listar_atendimentos(db: Session = Depends(get_db)):
    return db.query(models.Atendimento).all()
