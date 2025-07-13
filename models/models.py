from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base

class Clinica(Base):
    __tablename__ = "clinicas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    veterinarios = relationship("Veterinario", back_populates="clinica")

class Veterinario(Base):
    __tablename__ = "veterinarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"))
    clinica = relationship("Clinica", back_populates="veterinarios")
    atendimentos = relationship("Atendimento", back_populates="veterinario")

class Tutor(Base):
    __tablename__ = "tutores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    pets = relationship("Pet", back_populates="tutor")

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    tutor_id = Column(Integer, ForeignKey("tutores.id"))
    tutor = relationship("Tutor", back_populates="pets")
    atendimentos = relationship("Atendimento", back_populates="pet")

class Atendimento(Base):
    __tablename__ = "atendimentos"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime)
    descricao = Column(Text)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"))
    pet = relationship("Pet", back_populates="atendimentos")
    veterinario = relationship("Veterinario", back_populates="atendimentos")
