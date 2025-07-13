from fastapi import FastAPI
from veterinaria.api import clinicas, veterinarios, tutores, pets, atendimentos
from veterinaria.database import Base, engine

# Garante a criação das tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registro das rotas
app.include_router(clinicas.router)
app.include_router(veterinarios.router)
app.include_router(tutores.router)
app.include_router(pets.router)
app.include_router(atendimentos.router)
