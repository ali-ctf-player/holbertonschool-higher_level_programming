from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_file():
    """Read and parse data from products.json file."""
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_file():
    """Read and parse data from products.csv file."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert price to float and id to int
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []
    except ValueError:
        return []

@app.route('/products')
def products():
    """Display products from JSON or CSV file with optional ID filtering."""
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error=f"Wrong source: '{source}'. Please use 'json' or 'csv'.")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json_file()
    else:  # source == 'csv'
        products_data = read_csv_file()
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p.get('id') == product_id]
            
            if not filtered_products:
                return render_template('product_display.html',
                                     error=f"Product with ID {product_id} not found.",
                                     source=source)
            
            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                 error=f"Invalid ID: '{product_id}'. ID must be a number.",
                                 source=source)
    
    return render_template('product_display.html', 
                         products=products_data, 
                         source=source,
                         has_id=bool(product_id))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
