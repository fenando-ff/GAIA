# app/crud.py

from sqlalchemy.orm import Session
from app import models, schemas

def create_item(db: Session, model, schema):
    db_item = model(**schema.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, model, skip: int = 0, limit: int = 10):
    return db.query(model).offset(skip).limit(limit).all()

def get_item(db: Session, model, item_id: int, id_field: str):
    return db.query(model).filter(getattr(model, id_field) == item_id).first()

def update_item(db: Session, model, item_id: int, schema, id_field: str):
    db_item = get_item(db, model, item_id, id_field)
    if db_item is None:
        return None
    for key, value in schema.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, model, item_id: int, id_field: str):
    db_item = get_item(db, model, item_id, id_field)
    if db_item is None:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
