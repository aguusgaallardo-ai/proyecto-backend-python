from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException, status
from entities.product_entity import ProductEntity
from schemas.product_schema import ProductDto, ProductResponseDto

class ProductService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_product(self, product_dto: ProductDto) -> ProductResponseDto:
        new_product = ProductEntity(
            nombre_producto=product_dto.nombre_producto,
            descripcion_producto=product_dto.descripcion_producto,
            precio_producto=product_dto.precio_producto,
            cantidad_producto=product_dto.cantidad_producto,
            proveedor=product_dto.proveedor,
            rubro=product_dto.rubro,
            categoria=product_dto.categoria
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return ProductResponseDto.model_validate(new_product)
    
    def get_all_products(self) -> List[ProductResponseDto]:
        products = self.db.query(ProductEntity).all()
        return [ProductResponseDto.model_validate(p) for p in products]
    
    def get_product_by_id(self, product_id: int) -> Optional[ProductResponseDto]:
        product = self.db.query(ProductEntity).filter(ProductEntity.id == product_id).first()
        if product:
            return ProductResponseDto.model_validate(product)
        return None
    
    def update_product(self, product_dto: ProductDto) -> ProductResponseDto:
        if not product_dto.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ID del producto es requerido para actualizar"
            )
        
        product = self.db.query(ProductEntity).filter(ProductEntity.id == product_dto.id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producto no encontrado"
            )
        
        product.nombre_producto = product_dto.nombre_producto
        product.descripcion_producto = product_dto.descripcion_producto
        product.precio_producto = product_dto.precio_producto
        product.cantidad_producto = product_dto.cantidad_producto
        product.proveedor = product_dto.proveedor
        product.rubro = product_dto.rubro
        product.categoria = product_dto.categoria
        
        self.db.commit()
        self.db.refresh(product)
        return ProductResponseDto.model_validate(product)
    
    def delete_product(self, product_id: int) -> None:
        product = self.db.query(ProductEntity).filter(ProductEntity.id == product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producto no encontrado"
            )
        
        self.db.delete(product)
        self.db.commit()