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

@router.post("/pets", response_model=schemas.PetOut)
def criar_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    tutor = db.query(models.Tutor).filter(models.Tutor.id == pet.tutor_id).first()
    if not tutor:
        raise HTTPException(status_code=404, detail="Tutor não encontrado.")
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.get("/pets", response_model=List[schemas.PetOut])
def listar_pets(db: Session = Depends(get_db)):
    return db.query(models.Pet).all()

@router.get("/{pet_id}/atendimentos", response_model=List[schemas.AtendimentoOut])
def get_atendimentos_do_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    
    atendimentos = db.query(models.Atendimento).filter(models.Atendimento.pet_id == pet_id).all()
    return atendimentos