from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Aluno(Base):
    __tablename__ = "aluno"
    id_aluno = Column(Integer, primary_key=True, index=True)
    matricula = Column(Integer, nullable=False)
    turma_id_turma = Column(Integer, ForeignKey("turma.id_turma"))
    unidade_id_unidade = Column(Integer, ForeignKey("unidade.id_unidade"))
    curso_id_curso = Column(Integer, ForeignKey("curso.id_curso"))
    semestre_id_semestre = Column(Integer, ForeignKey("semestre.id_semestre"))

class Material(Base):
    __tablename__ = "material"
    id_material = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Float, nullable=False)
    data_id_data = Column(Integer, ForeignKey("data.id_data"))
    aluno_id_aluno = Column(Integer, ForeignKey("aluno.id_aluno"))
