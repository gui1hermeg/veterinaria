from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ClinicaBase(BaseModel):
    nome: str
    cidade: str

class ClinicaCreate(ClinicaBase):
    pass


class VeterinarioBase(BaseModel):
    nome: str
    especialidade: str
    clinica_id: int

class VeterinarioCreate(VeterinarioBase):
    pass

class VeterinarioOut(VeterinarioBase):
    id: int
    class Config:
        orm_mode = True

class ClinicaOut(ClinicaBase):
    id: int
    veterinarios: List[VeterinarioOut] = []
    class Config:
        orm_mode = True

class TutorBase(BaseModel):
    nome: str
    telefone: str

class TutorCreate(TutorBase):
    pass

class TutorOut(TutorBase):
    id: int
    class Config:
        orm_mode = True

class PetBase(BaseModel):
    nome: str
    especie: str
    idade: int
    tutor_id: int

class PetCreate(PetBase):
    pass

class PetOut(PetBase):
    id: int
    class Config:
        orm_mode = True

class AtendimentoBase(BaseModel):
    data: datetime
    descricao: str
    pet_id: int
    veterinario_id: int

class AtendimentoCreate(AtendimentoBase):
    pass

class AtendimentoOut(AtendimentoBase):
    id: int
    class Config:
        orm_mode = True
