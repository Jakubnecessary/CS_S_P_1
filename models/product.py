class Product:
    def __init__(self, product_name, product_type, product_description, stock_quantity, selling_price, id = None):
        self.product_name = product_name
        self.product_type = product_type
        self.product_description = product_description
        self.stock_quantity = stock_quantity
        self.selling_price = selling_price
        self.id = id
