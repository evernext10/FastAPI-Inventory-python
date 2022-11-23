from pydantic import BaseModel


class ProductPostRequestSchema(BaseModel):
    name: str


class ProductSchema(ProductPostRequestSchema):
    id: int
