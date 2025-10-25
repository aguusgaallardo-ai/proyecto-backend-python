from fastapi import APIRouter, HTTPException, status
from typing import List
from database.dbconfig import db_dependency
from services.product_service import ProductService
from schemas.product_schema import ProductDto, ProductResponseDto

router = APIRouter(
    prefix="/api/productos",
    tags=["productos"]
)

@router.post("/crear", response_model=ProductResponseDto, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductDto, db: db_dependency):
    service = ProductService(db)
    return service.create_product(product)

@router.get("", response_model=List[ProductResponseDto])
def get_all_products(db: db_dependency):
    service = ProductService(db)
    return service.get_all_products()

@router.get("/{id}", response_model=ProductResponseDto)
def get_product_by_id(id: int, db: db_dependency):
    service = ProductService(db)
    product = service.get_product_by_id(id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    return product

@router.patch("/actualizar", response_model=ProductResponseDto)
def update_product(product: ProductDto, db: db_dependency):
    service = ProductService(db)
    return service.update_product(product)

@router.delete("/eliminar/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: db_dependency):
    service = ProductService(db)
    service.delete_product(id)
    return None