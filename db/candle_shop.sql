DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;


CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    company_origin VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    product_type VARCHAR(255),
    product_description VARCHAR(255),
    stock_quantity INT,
    stock_price INT,
    supplier_id INT REFERENCES suppliers(id)
);