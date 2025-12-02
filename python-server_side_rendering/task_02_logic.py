from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Render the items page with data from JSON file."""
    try:
        # Read items from JSON file
        if os.path.exists('items.json'):
            with open('items.json', 'r') as file:
                data = json.load(file)
                items_list = data.get('items', [])
        else:
            items_list = []
            print("items.json not found, using empty list")
    except json.JSONDecodeError:
        print("Error decoding JSON, using empty list")
        items_list = []
    except Exception as e:
        print(f"Error reading items.json: {e}")
        items_list = []
    
    # Pass items to template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
