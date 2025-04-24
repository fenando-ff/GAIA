from pydantic import BaseModel

class MaterialCreate(BaseModel):
    quantidade: float
    data_id_data: int
    aluno_id_aluno: int
