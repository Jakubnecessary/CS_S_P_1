from flask import Flask, render_template
from flask import Blueprint
from models.product import Product
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.