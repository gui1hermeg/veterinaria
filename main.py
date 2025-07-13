from fastapi import FastAPI
from api import clinicas, veterinarios, tutores, pets, atendimentos
from database import engine
from models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clinicas.router, prefix="/clinicas")
app.include_router(veterinarios.router, prefix="/veterinarios")
app.include_router(tutores.router, prefix="/tutores")
app.include_router(pets.router, prefix="/pets")
app.include_router(atendimentos.router, prefix="/atendimentos")
