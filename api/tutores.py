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

@router.post("/tutores", response_model=schemas.TutorOut, tags=["Tutores"])
def criar_tutor(tutor: schemas.TutorCreate, db: Session = Depends(get_db)):
    db_tutor = models.Tutor(**tutor.dict())
    db.add(db_tutor)
    db.commit()
    db.refresh(db_tutor)
    return db_tutor

@router.get("/tutores", response_model=List[schemas.TutorOut], tags=["Tutores"])
def listar_tutores(db: Session = Depends(get_db)):
    return db.query(models.Tutor).all()

@router.get("/tutores/{tutor_id}/pets", response_model=List[schemas.PetOut], tags=["Tutores"])
def get_pets_do_tutor(tutor_id: int, db: Session = Depends(get_db)):
    tutor = db.query(models.Tutor).filter(models.Tutor.id == tutor_id).first()
    if not tutor:
        raise HTTPException(status_code=404, detail="Tutor não encontrado")
    return tutor.pets