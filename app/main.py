from fastapi import FastAPI
from .items_service.routes import items
from .order_service.routes import orders  # Import the order routes

app = FastAPI(title="POSManager API", version="1.0.0")

app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])  # Register order routes
