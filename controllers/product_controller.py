from flask import Flask, render_template
from flask import Blueprint
from models.product import Product
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

# First route home/products
@products_blueprint.route("/products")
def products():
    # products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

# GET /new product

@products_blueprint.route("/products/new", methods = ['GET'])
def new_product():
    suppliers = supplier_repository.select_all()
    return render_template('products/new_product', all_suppliers = suppliers)