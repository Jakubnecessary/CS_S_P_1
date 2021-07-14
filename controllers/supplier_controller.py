import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)

# get!New
@suppliers_blueprint.route("/suppliers/new", methods = ['GET'])
def new_supplier():
    suppliers = supplier_repository.select_all()
    return render_template('suppliers/new_supplier.html', all_suppliers = suppliers)

# POST '/suppliers'
@suppliers_blueprint.route("/suppliers", methods=['POST'])
def create_new_supplier():
    company_name = request.form['company_name']
    company_origin = request.form['company_origin']
    supplier = Supplier(company_name, company_origin)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

# show 
@suppliers_blueprint.route("/suppliers/<id>", methods=['GET'])
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/show_new_supplier.html', supplier = supplier)

# edit
@suppliers_blueprint.route("/suppliers/<id>/edit", methods=['GET'])
def edit_supplier(id):
    product = product_repository.select(id)
    suppliers = supplier_repository.select_all()
    return render_template('suppliers/edit.html', product = product, all_suppliers = suppliers)

# updtae
@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_supplier(id):
    company_name = request.form['company_name']
    company_origin = request.form['company_origin']
    supplier  = supplier_repository.select(request.form['supplier_id'])
    supplier = Supplier(company_name, company_origin, id)
    supplier_repository.update(supplier)
    return redirect('/suppliers')



# delete by id
@suppliers_blueprint.route("/suppliers/<id>/delete", methods=['POST'])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect('/suppliers')



