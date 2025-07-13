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

@router.post("/veterinarios", response_model=schemas.VeterinarioOut, tags=["Veterinários"])
def criar_veterinario(vet: schemas.VeterinarioCreate, db: Session = Depends(get_db)):
    clinica = db.query(models.Clinica).filter(models.Clinica.id == vet.clinica_id).first()
    if not clinica:
        raise HTTPException(status_code=404, detail="Clínica não encontrada.")
    db_vet = models.Veterinario(**vet.dict())
    db.add(db_vet)
    db.commit()
    db.refresh(db_vet)
    return db_vet

@router.get("/veterinarios", response_model=List[schemas.VeterinarioOut], tags=["Veterinários"])
def listar_veterinarios(db: Session = Depends(get_db)):
    return db.query(models.Veterinario).all()

@router.get("/{veterinario_id}/atendimentos", response_model=List[schemas.AtendimentoOut], tags=["Veterinários"])
def get_atendimentos_do_veterinario(veterinario_id: int, db: Session = Depends(get_db)):
    veterinario = db.query(models.Veterinario).filter(models.Veterinario.id == veterinario_id).first()
    if not veterinario:
        raise HTTPException(status_code=404, detail="Veterinário não encontrado")
    
    atendimentos = db.query(models.Atendimento).filter(models.Atendimento.veterinario_id == veterinario_id).all()
    return atendimentos