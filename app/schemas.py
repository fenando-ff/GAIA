from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# CURSO
class CursoBase(BaseModel):
    nome_curso: str

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id_curso: int
    class Config:
        orm_mode = True

# RESIDUO
class ResiduoBase(BaseModel):
    tipo: str

class ResiduoCreate(ResiduoBase):
    pass

class Residuo(ResiduoBase):
    id_residuo: int
    class Config:
        orm_mode = True

# SEMESTRE
class SemestreBase(BaseModel):
    periodo: int

class SemestreCreate(SemestreBase):
    pass

class Semestre(SemestreBase):
    id_semestre: int
    class Config:
        orm_mode = True

# TURMA
class TurmaBase(BaseModel):
    codigo_turma: Optional[str] = None

class TurmaCreate(TurmaBase):
    pass

class Turma(TurmaBase):
    id_turma: int
    class Config:
        orm_mode = True

# UNIDADE
class UnidadeBase(BaseModel):
    nome_unidade: Optional[str] = None

class UnidadeCreate(UnidadeBase):
    pass

class Unidade(UnidadeBase):
    id_unidade: int
    class Config:
        orm_mode = True

# ALUNO
class AlunoBase(BaseModel):
    matricula: int
    curso_id_curso: int
    semestre_id_semestre: int
    turma_id_turma: int
    unidade_id_unidade: int

class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id_aluno: int
    class Config:
        orm_mode = True

# ENTREGA
class EntregaBase(BaseModel):
    quantidade: float
    data: date
    aluno_id_aluno: int

class EntregaCreate(EntregaBase):
    pass

class Entrega(EntregaBase):
    id_entrega: int
    class Config:
        orm_mode = True
