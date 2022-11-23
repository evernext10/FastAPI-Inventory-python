from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    Float
)

from models.BaseModel import EntityMeta


class Product(EntityMeta):
    __tablename__ = "product"

    id = Column(Integer)
    name = Column(String(36), nullable=False)
    status = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    description = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=True)
    final_price = Column(Float, nullable=True)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "status": self.status.__str__(),
            "stock": self.stock.__str__(),
            "description": self.description.__str__(),
            "price": self.price.__str__(),
            "discount": self.discount.__str__(),
            "final_price": self.final_price.__str__(),
        }
