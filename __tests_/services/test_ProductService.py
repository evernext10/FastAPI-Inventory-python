from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.ProductRepository import ProductRepository
from services.ProductService import ProductService

class TestProductService(TestCase):
    productRepository: ProductRepository
    productService: ProductService

    def setUp(self):
        super().setUp()
        self.productRepository = create_autospec(
            ProductRepository
        )
        self.productService = ProductService(
            self.productRepository
        )

    @patch(
        "schemas.pydantic.ProductSchema.ProductSchema",
        autospec=True,
    )
    def test_create(self, ProductSchema):
        product = ProductSchema()
        product.name = "Product1"
        product.status = 1
        product.stock = 20
        product.description = "Product1 - Prueba"
        product.price = 20000

        self.productService.create(product)

        # Should call create method on Product Repository
        self.productRepository.create.assert_called_once()

    def test_delete(self):
        self.productService.delete(product_id=1)

        # Should call delete method on Product Repository
        self.productRepository.delete.assert_called_once()

    def test_get(self):
        self.productService.get(product_id=1)

        # Should call get method on Product Repository
        self.productRepository.get.assert_called_once()

    def test_list(self):
        name = "Product1"
        pageSize = 10
        startIndex = 2

        self.productService.list(name, pageSize, startIndex)

        # Should call list method on Product Repository
        self.productRepository.list.assert_called_once_with(
            name, pageSize, startIndex
        )

    @patch(
        "schemas.pydantic.ProductSchema.ProductSchema",
        autospec=True,
    )
    def test_update(self, ProductSchema):
        product = ProductSchema()
        product.name = "Product 10"

        self.productService.update(
            product_id=1, product_body=product
        )

        # Should call update method on Product Repository
        self.productRepository.update.assert_called_once()
