#!/usr/bin/python3
"""
Flask Application for displaying products from JSON or CSV files
"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    """Read product data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    """Read product data from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float for consistency
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except (FileNotFoundError, ValueError, KeyError):
        return []
    return products

@app.route('/products')
def display_products():
    """Display products from JSON or CSV file with optional id filter"""
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Initialize variables
    products = []
    error = None
    filtered_products = []
    
    # Read data based on source parameter
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        error = "Wrong source"
        return render_template('product_display.html', 
                             error=error, 
                             products=[], 
                             source=source)
    
    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            for product in products:
                if product.get('id') == product_id:
                    filtered_products = [product]
                    break
            if not filtered_products:
                error = "Product not found"
        except ValueError:
            error = "Invalid product ID"
    else:
        filtered_products = products
    
    # Pass data to template
    return render_template('product_display.html', 
                         error=error, 
                         products=filtered_products, 
                         source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
