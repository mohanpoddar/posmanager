from fastapi import FastAPI
from .items_service.routes import items

app = FastAPI(title="POSManager API", version="1.0.0")

app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
