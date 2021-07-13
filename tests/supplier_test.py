import unittest 
from models.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("Chappels Craft" , "England")

    def test_supplier_has_a_name(self):
        self.assertEqual("Chappels Craft", self.supplier.company_name)

    def test_supplier_has_origin(self):
        self.assertEqual("England", self.supplier.company_origin)