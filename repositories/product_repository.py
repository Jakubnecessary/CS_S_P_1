from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

def select_all():
    products = []

    sql = "SELECT * FROM books"