from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.db import SessionLocal, Item
from ..models.schema import ItemCreate, ItemOut
from ..crud import items as crud
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError
from ..models.db import engine


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/list-all", response_model=list[ItemOut])
def list_items(db: Session = Depends(get_db)):
    print(crud.get_items(db))
    return crud.get_items(db)

@router.post("/create", response_model=ItemOut)
def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(item, db)

@router.get("/health/db")
def check_database_connection():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return JSONResponse(status_code=200, content={"status": "ok", "message": "Database connected"})
    except OperationalError as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
