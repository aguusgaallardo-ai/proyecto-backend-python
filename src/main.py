import sys
from pathlib import Path

# Agregar el directorio src al path
sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI
from database.dbconfig import engine, Base
from controllers.product_controller import router as product_router

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Productos",
    description="API REST para gestión de productos",
    version="1.0.0"
)

# Incluir los routers
app.include_router(product_router)

@app.get("/")
def root():
    return {"message": "API de Productos funcionando"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)