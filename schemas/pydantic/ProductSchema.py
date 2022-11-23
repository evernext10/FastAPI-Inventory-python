from pydantic import BaseModel


class ProductPostRequestSchema(BaseModel):
    name: str
    status: int
    stock: int
    description: str
    price: int


class ProductSchema(ProductPostRequestSchema):
    id: int
