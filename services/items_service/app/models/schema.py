from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    price: float
    category: Optional[str] = None
    is_available: Optional[bool] = True

class ItemOut(ItemCreate):
    id: int
    created_at: Optional[datetime]
