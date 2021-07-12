import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository


supplier_1 = Supplier("England", "Smbullion")

supplier_2 = Supplier("Scotland", "CandleShack")


product_1 = Product("Candle_2", "Big Candle", "Handmade Big Candle", 10, 12, supplier_2)

product_2 = Product("Straw_1", "Small Set", "Small Set of handmade straws", 15, 3, supplier_1)

