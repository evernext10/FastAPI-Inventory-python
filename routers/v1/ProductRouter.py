from typing import List, Optional

from fastapi import APIRouter, Depends, status

from schemas.pydantic.ProductSchema import (
    ProductPostRequestSchema,
    ProductSchema
)

from services.ProductService import ProductService

ProductRouter = APIRouter(
    prefix="/v1/products", tags=["products"]
)


@ProductRouter.get("/", response_model=List[ProductSchema])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    productService: ProductService = Depends(),
):
    return [
        product.normalize()
        for product in productService.list(
            name, pageSize, startIndex
        )
    ]


@ProductRouter.get("/{id}", response_model=ProductSchema)
def get(id: int, productService: ProductService = Depends()):
    return productService.get(id).normalize()


@ProductRouter.post(
    "/",
    response_model=ProductSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    product: ProductPostRequestSchema,
    productService: ProductService = Depends(),
):
    return productService.create(product).normalize()


@ProductRouter.patch("/{id}", response_model=ProductSchema)
def update(
    id: int,
    product: ProductPostRequestSchema,
    productService: ProductService = Depends(),
):
    return productService.update(id, product).normalize()


@ProductRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int, productService: ProductService = Depends()
):
    return productService.delete(id)
