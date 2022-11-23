from typing import List, Optional

from fastapi import Depends
from models.ProductModel import Product

from repositories.ProductRepository import ProductRepository
from schemas.pydantic.ProductSchema import ProductSchema

class ProductService:
    productRepository: ProductRepository

    def __init__(
        self, productRepository: ProductRepository = Depends()
    ) -> None:
        self.productRepository = productRepository

    def create(self, product_body: ProductSchema) -> Product:
        return self.productRepository.create(
            Product(
                    name=product_body.name,
                    status=product_body.status,
                    stock=product_body.stock,
                    description=product_body.description,
                    price=product_body.price
                )
        )

    def delete(self, product_id: int) -> None:
        return self.productRepository.delete(
            Product(id=product_id)
        )

    def get(self, product_id: int) -> Product:
        return self.productRepository.get(
            Product(id=product_id)
        )

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Product]:
        return self.productRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, product_id: int, product_body: ProductSchema
    ) -> Product:
        return self.productRepository.update(
            product_id, Product(name=product_body.name)
        )