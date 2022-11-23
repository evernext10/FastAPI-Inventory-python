from typing import List, Optional
import numpy as np

from fastapi import Depends
from sqlalchemy.orm import Session

from configs.database import (
    get_db_connection,
)
from models.ProductModel import Product

class ProductRepository:
    db: Session

    arrayDiscounts : List[int] = [10, 20, 30, 40, 50, 20, 40]

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Product]:
        query = self.db.query(Product)

        if name:
            query = query.filter_by(name=name)

        products : List[Product] = query.offset(start).limit(limit).all()
        """ if products:
            for product in products:
                discount = np.random.choice(self.arrayDiscounts, size=1)
                product.discount = (product.price * discount) / 100
                product.final_price = product.price - product.discount """

        return products

    def get(self, product: Product) -> Product:
        return self.db.get(
            Product,
            product.id,
        )

    def create(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, id: int, product: Product) -> Product:
        product.id = id
        self.db.merge(product)
        self.db.commit()
        return product

    def delete(self, product: Product) -> None:
        self.db.delete(product)
        self.db.commit()
        self.db.flush()