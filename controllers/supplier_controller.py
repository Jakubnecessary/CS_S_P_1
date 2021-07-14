import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("supplier", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)

# get!New
@suppliers_blueprint.route("/suppliers/new", methods = ['GET'])
def new_supplier():
    products = product_repository.select_all()
    return render_template('suppliers/new_supplier.html', all_products = products)