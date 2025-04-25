from typing import List, Optional

from sqlalchemy import Column, Date, Float, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.database import Base
import datetime

class Base(DeclarativeBase):
    pass


class Curso(Base):
    __tablename__ = 'curso'

    id_curso: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome_curso: Mapped[str] = mapped_column(String(45))

    aluno: Mapped[List['Aluno']] = relationship('Aluno', back_populates='curso')


class Residuo(Base):
    __tablename__ = 'residuo'

    id_residuo: Mapped[int] = mapped_column(Integer, primary_key=True)
    tipo: Mapped[str] = mapped_column(String(45))

    entrega: Mapped[List['Entrega']] = relationship('Entrega', secondary='entrega_has_residuo', back_populates='residuo')


class Semestre(Base):
    __tablename__ = 'semestre'

    id_semestre: Mapped[int] = mapped_column(Integer, primary_key=True)
    periodo: Mapped[int] = mapped_column(Integer)

    aluno: Mapped[List['Aluno']] = relationship('Aluno', back_populates='semestre')


class Turma(Base):
    __tablename__ = 'turma'

    id_turma: Mapped[int] = mapped_column(Integer, primary_key=True)
    codigo_turma: Mapped[Optional[str]] = mapped_column(String(45))

    aluno: Mapped[List['Aluno']] = relationship('Aluno', back_populates='turma')


class Unidade(Base):
    __tablename__ = 'unidade'

    id_unidade: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome_unidade: Mapped[Optional[str]] = mapped_column(String(45))

    aluno: Mapped[List['Aluno']] = relationship('Aluno', back_populates='unidade')


class Aluno(Base):
    __tablename__ = 'aluno'
    __table_args__ = (
        ForeignKeyConstraint(['curso_id_curso'], ['curso.id_curso'], name='fk_aluno_curso1'),
        ForeignKeyConstraint(['semestre_id_semestre'], ['semestre.id_semestre'], name='fk_aluno_semestre1'),
        ForeignKeyConstraint(['turma_id_turma'], ['turma.id_turma'], name='fk_aluno_turma'),
        ForeignKeyConstraint(['unidade_id_unidade'], ['unidade.id_unidade'], name='fk_aluno_unidade1'),
        Index('fk_aluno_curso1_idx', 'curso_id_curso'),
        Index('fk_aluno_semestre1_idx', 'semestre_id_semestre'),
        Index('fk_aluno_turma_idx', 'turma_id_turma'),
        Index('fk_aluno_unidade1_idx', 'unidade_id_unidade')
    )

    id_aluno: Mapped[int] = mapped_column(Integer, primary_key=True)
    matricula: Mapped[int] = mapped_column(Integer)
    turma_id_turma: Mapped[int] = mapped_column(Integer)
    unidade_id_unidade: Mapped[int] = mapped_column(Integer)
    curso_id_curso: Mapped[int] = mapped_column(Integer)
    semestre_id_semestre: Mapped[int] = mapped_column(Integer)

    curso: Mapped['Curso'] = relationship('Curso', back_populates='aluno')
    semestre: Mapped['Semestre'] = relationship('Semestre', back_populates='aluno')
    turma: Mapped['Turma'] = relationship('Turma', back_populates='aluno')
    unidade: Mapped['Unidade'] = relationship('Unidade', back_populates='aluno')
    entrega: Mapped[List['Entrega']] = relationship('Entrega', back_populates='aluno')


class Entrega(Base):
    __tablename__ = 'entrega'
    __table_args__ = (
        ForeignKeyConstraint(['aluno_id_aluno'], ['aluno.id_aluno'], name='fk_material_aluno1'),
        Index('fk_material_aluno1_idx', 'aluno_id_aluno')
    )

    id_entrega: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantidade: Mapped[float] = mapped_column(Float)
    data: Mapped[datetime.date] = mapped_column(Date)
    aluno_id_aluno: Mapped[int] = mapped_column(Integer)

    aluno: Mapped['Aluno'] = relationship('Aluno', back_populates='entrega')
    residuo: Mapped[List['Residuo']] = relationship('Residuo', secondary='entrega_has_residuo', back_populates='entrega')


t_entrega_has_residuo = Table(
    'entrega_has_residuo', Base.metadata,
    Column('entrega_id_entrega', Integer, primary_key=True, nullable=False),
    Column('residuo_id_residuo', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['entrega_id_entrega'], ['entrega.id_entrega'], name='fk_material_has_residuo_material1'),
    ForeignKeyConstraint(['residuo_id_residuo'], ['residuo.id_residuo'], name='fk_material_has_residuo_residuo1'),
    Index('fk_material_has_residuo_material1_idx', 'entrega_id_entrega'),
    Index('fk_material_has_residuo_residuo1_idx', 'residuo_id_residuo')
)
