from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.db import SessionLocal, Item
from app.models.schema import ItemCreate, ItemOut
from app.crud import items as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items", response_model=list[ItemOut])
def list_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router.post("/items", response_model=ItemOut)
def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(item, db)
