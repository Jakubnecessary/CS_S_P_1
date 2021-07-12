from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

def select_all():
    products = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['product_name'], row['product_type'], row['product_description'],row['stock_quantity'],row['selling_price'],supplier, row['id'])
        products.append(product)
    return products