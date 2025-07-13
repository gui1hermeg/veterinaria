from fastapi import APIRouter, Depends
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

@router.post("/tutores", response_model=schemas.TutorOut)
def criar_tutor(tutor: schemas.TutorCreate, db: Session = Depends(get_db)):
    db_tutor = models.Tutor(**tutor.dict())
    db.add(db_tutor)
    db.commit()
    db.refresh(db_tutor)
    return db_tutor

@router.get("/tutores", response_model=List[schemas.TutorOut])
def listar_tutores(db: Session = Depends(get_db)):
    return db.query(models.Tutor).all()
