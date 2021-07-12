from flask import Flask, render_template, request, redirect
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
    return render_template('products/new_product.html', all_suppliers = suppliers)

# POST '/products'
@products_blueprint.route("/products", methods=['POST'])
def create_new_product():
    product_name = request.form['product_name']
    product_type = request.form['product_type']
    product_description = request.form['product_description']
    stock_quantity = request.form['stock_quantity']
    selling_price = request.form['selling_price']
    supplier  = supplier_repository.select(request.form['author_id'])
    product = Product(product_name, product_type, product_description, stock_quantity, selling_price, supplier)
    product_repository.save(product)
    return redirect('/products')
    