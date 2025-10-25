from fastapi import FastAPI
from src.controllers.producto_controller import router as productos_router

def register_routes(app: FastAPI):
    app.include_router(productos_router)