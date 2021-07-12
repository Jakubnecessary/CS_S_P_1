from db.run_sql import run_sql
from models.supplier import Supplier
from models.product import Product

def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['company_name'], row['company_origin'], row['id'] )
        suppliers.append(supplier)
    return suppliers

def save(supplier):
    sql = "INSERT INTO suppliers (company_name, company_origin) VALUES (%s, %s) RETURNING *"
    values = [supplier.company_name, supplier.company_origin]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result['company_name'], result['company_origin'])