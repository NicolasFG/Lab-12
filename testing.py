import unittest
from unittest.mock import Mock
from sqlalchemy.orm import Session
from crud import *
from datetime import datetime

class TestGetProducts(unittest.TestCase):
    def test_get_products(self):
        db = Mock(spec=Session)
        product1 = models.Product(id=1, owner_id=1,created_at=datetime,updated_at=datetime)
        product2 = models.Product(id=2, owner_id=2,created_at=datetime,updated_at=datetime)
        products = [product1, product2]
        db.query.return_value.offset.return_value.limit.return_value.all.return_value = products
        result = get_products(db)
        self.assertEqual(result, products)  

    def test_create_cart_product(self):
        db = Mock(spec=Session)

        product_data = {
            'product': schemas.ProductCreate(title="titulo",price=2.1,description="description", category="category", image="image", rating="rating"),
            'cart_id': 1
        }
        product1 = models.Product(title="titulo",price=2.1, description="description", category="category", image="image", rating="rating", owner_id=1)

        db.add.return_value = product1
        result = create_cart_product(db, product_data['product'], product_data['cart_id'])

        self.assertEqual(result.title, product1.title)
        self.assertEqual(result.price, product1.price)
        self.assertEqual(result.description, product1.description)
        self.assertEqual(result.category, product1.category)
        self.assertEqual(result.image, product1.image)
        self.assertEqual(result.rating, product1.rating)
        self.assertEqual(result.owner_id, product1.owner_id)

    def test_get_product(self):
        db = Mock(spec=Session)
        product1 = models.Product(id=1, owner_id=1, created_at=datetime,updated_at=datetime)
        db.query().filter().first.return_value = product1
        result = get_product(db,1)
        self.assertEqual(result, product1)  
    def test_update_product(self):
        db = Mock(spec=Session)
        product_id = 1
        product_data = schemas.UpdateProduct(id=1,updated_at=datetime.now(),title="titulo",price=2.1,description="description", category="category", image="image", rating="rating")
        existing_product = models.Product(id=1, updated_at=datetime.now())
        db.query().filter().first.return_value = existing_product
        result = update_product(product_id, product_data, db)
        self.assertEqual(result, existing_product)
        self.assertEqual(existing_product.id, product_id)
    

    def test_delete_product(self):
        db = Mock(spec=Session)
        product_id = 1
        product = models.Product(id=1, owner_id=1, created_at=datetime,updated_at=datetime)
        db.query().filter().first.return_value = product
        result = delete_product(product_id, db)
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)


    def test_create_cart(self):
        db = Mock(spec=Session)
        cart_data = schemas.CartCreate(id=1)
        created_cart = models.Cart(id=1, created_at=datetime,updated_at=datetime)
        db.add.return_value = created_cart
        result = create_cart(db, cart_data)
        self.assertEqual(result.id, created_cart.id)

    def test_get_cart(self):
        db = Mock(spec=Session)
        cart_id = 1
        cart = models.Cart(id=cart_id,created_at=datetime,updated_at=datetime)
        db.query().filter().first.return_value = cart
        result = get_cart(db, cart_id)
        self.assertEqual(result, cart)
    
    def test_get_carts(self):
        db = Mock(spec=Session)
        carts = [
            models.Cart(id=1, created_at=datetime,updated_at=datetime),
            models.Cart(id=2, created_at=datetime,updated_at=datetime),
        ]
        db.query().offset().limit().all.return_value = carts
        result = get_carts(db)
        self.assertEqual(result, carts)

if __name__ == '__main__':
    unittest.main()