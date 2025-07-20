from fastapi import FastAPI
from app.routes import items

app = FastAPI(title="Items Service")

app.include_router(items.router)
