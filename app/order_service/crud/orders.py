from sqlalchemy.orm import Session
from ..models.db import SessionLocal, Order, OrderItem
from ..models.schema import Order as OrderSchema, OrderItem as OrderItemSchema

def place_order(order_data: OrderSchema):
    db: Session = SessionLocal()
    db_order = Order(table_number=order_data.table_number, status=order_data.status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    for item in order_data.items:
        db_item = OrderItem(order_id=db_order.id, item_id=item.item_id, quantity=item.quantity)
        db.add(db_item)
    db.commit()
    db.close()
    return db_order

def list_orders():
    db: Session = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return orders