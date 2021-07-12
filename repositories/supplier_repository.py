from db.run_sql import run_sql
from models.supplier import Supplier
from models.product import Product

def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['company_name'], row['comany_origin'], row['id'] )
        suppliers.append(supplier)
    return suppliers