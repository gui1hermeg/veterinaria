from sqlalchemy.orm import Session
from models import models
from schemas import schemas

# Exemplo para clínicas:
def create_clinica(db: Session, clinica: schemas.ClinicaCreate):
    db_clinica = models.Clinica(**clinica.dict())
    db.add(db_clinica)
    db.commit()
    db.refresh(db_clinica)
    return db_clinica

def get_clinicas(db: Session):
    return db.query(models.Clinica).all()

def get_clinica(db: Session, clinica_id: int):
    return db.query(models.Clinica).filter(models.Clinica.id == clinica_id).first()

# Outros métodos seguem a mesma lógica: create_veterinario, get_veterinarios, etc.
