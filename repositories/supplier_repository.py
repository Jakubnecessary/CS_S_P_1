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
        supplier = Supplier(result['company_name'], result['company_origin'], result['id'])
    return supplier

def delete_all():
    sql = "DELETE  FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(supplier):
    sql = "UPDATE suppliers SET (company_name, company_origin) = (%s, %s) WHERE id = %s"
    values = [supplier.company_name, supplier.last_name, supplier.id]
    run_sql(sql, values)

def products(supplier):
    books = []

    sql = "SELECT * FROM products WHERE supplier_id = %s"
    values = [supplier.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['product_name'], row['product_type'], row['product_description'], row['stock_quantity'], row['selling_price'], row['supplier'], row['id'] )
        books.append(product)
    return books