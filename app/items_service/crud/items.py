from sqlalchemy.orm import Session
from ..models.db import Item
from ..models.schema import ItemCreate

def get_items(db: Session):
    return db.query(Item).all()

def create_item(item: ItemCreate, db: Session):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
