from pydantic import BaseModel


class ProductPostRequestSchema(BaseModel):
    name: str
    status: int
    stock: int
    description: str
    price: float
    discount: float
    final_price: float


class ProductSchema(ProductPostRequestSchema):
    id: int
