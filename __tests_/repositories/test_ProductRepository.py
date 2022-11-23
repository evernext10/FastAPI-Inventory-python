from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.ProductRepository import ProductRepository

class TestProductRepository(TestCase):
    session: Session
    productRepository: ProductRepository

    def setUp(self):
        super().setUp()
        self.session = create_autospec(Session)
        self.productRepository = ProductRepository(
            self.session
        )

    @patch("models.ProductModel.Product", autospec=True)
    def test_create(self, Product):
        product = Product(
                    name = "Product 1",
                    status = 1,
                    stock = 10,
                    description = "Product - description test",
                    price = 10000
                )
        self.productRepository.create(product)

        # Should call add method on Session
        self.session.add.assert_called_once_with(product)

    @patch("models.ProductModel.Product", autospec=True)
    def test_delete(self, Product):
        product = Product(id=1)
        self.productRepository.delete(product)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(product)

    @patch("models.ProductModel.Product", autospec=True)
    def test_get(self, Product):
        product = Product(id=1)
        self.productRepository.get(product)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.ProductModel.Product", autospec=True)
    def test_list(self, Product):
        self.productRepository.list(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.productRepository.list("Product 1", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(
            Product
        ).filter_by.assert_called_once_with(
            name="Product 1"
        )

    @patch("models.ProductModel.Product", autospec=True)
    def test_update(self, Product):
        product = Product(name="Ray Dalio")
        self.productRepository.update(id=1, product=product)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(product)
