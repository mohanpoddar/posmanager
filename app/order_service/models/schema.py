from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItem(BaseModel):
    item_id: int
    quantity: int

class Order(BaseModel):
    id: Optional[int] = None
    table_number: int
    items: List[OrderItem]
    status: str = "pending"
    created_at: Optional[datetime] = None