from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Página HTML (se estiver usando)
@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("page.html", {"request": request})

def make_crud_endpoints(name: str, model, schema_create, schema_read, id_field: str):
    @app.post(f"/{name}/", response_model=schema_read)
    def create(data: schema_create, db: Session = Depends(get_db)):
        return crud.create_item(db, model, data)

    @app.get(f"/{name}/", response_model=list[schema_read])
    def list_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
        return crud.get_items(db, model, skip, limit)

    @app.get(f"/{name}/{{item_id}}", response_model=schema_read)
    def get_by_id(item_id: int, db: Session = Depends(get_db)):
        db_item = crud.get_item(db, model, item_id, id_field)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{name.capitalize()} não encontrado")
        return db_item

    @app.put(f"/{name}/{{item_id}}", response_model=schema_read)
    def update(item_id: int, data: schema_create, db: Session = Depends(get_db)):
        db_item = crud.update_item(db, model, item_id, data, id_field)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{name.capitalize()} não encontrado para atualização")
        return db_item

    @app.delete(f"/{name}/{{item_id}}", response_model=schema_read)
    def delete(item_id: int, db: Session = Depends(get_db)):
        db_item = crud.delete_item(db, model, item_id, id_field)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{name.capitalize()} não encontrado para exclusão")
        return db_item

make_crud_endpoints("cursos", models.Curso, schemas.CursoCreate, schemas.Curso, "id_curso")
make_crud_endpoints("residuos", models.Residuo, schemas.ResiduoCreate, schemas.Residuo, "id_residuo")
make_crud_endpoints("semestres", models.Semestre, schemas.SemestreCreate, schemas.Semestre, "id_semestre")
make_crud_endpoints("turmas", models.Turma, schemas.TurmaCreate, schemas.Turma, "id_turma")
make_crud_endpoints("unidades", models.Unidade, schemas.UnidadeCreate, schemas.Unidade, "id_unidade")
make_crud_endpoints("alunos", models.Aluno, schemas.AlunoCreate, schemas.Aluno, "id_aluno")
make_crud_endpoints("entregas", models.Entrega, schemas.EntregaCreate, schemas.Entrega, "id_entrega")