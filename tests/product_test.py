import unittest
from models.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Candle_1", "Small Candle", "Handmade Small Candle", 15, 5)

    
    def test_product_has_a_type(self):
        self.assertEqual("Small Candle", self.product.product_type)

    def test_product_has_a_quantity(self):
        self.assertEqual(15, self.test_product_has_a_quantity)
        
    def test_product_has_a_price(self):
        self.assertEqual(5, self.product.selling_price)
