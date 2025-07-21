from fastapi import APIRouter
from ..models.schema import Order
from ..crud.orders import place_order, list_orders

router = APIRouter()

@router.post("/place", response_model=Order)
async def create_order(order: Order):
    return await place_order(order)

@router.get("/list", response_model=list[Order])
async def get_orders():
    return await list_orders()