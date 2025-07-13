from fastapi import FastAPI
from api import clinicas, veterinarios, tutores, pets, atendimentos
from database import engine
from models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clinicas.router)
app.include_router(veterinarios.router)
app.include_router(tutores.router)
app.include_router(pets.router)
app.include_router(atendimentos.router)
