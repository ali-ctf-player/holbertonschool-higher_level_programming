#!/usr/bin/python3
"""
Script to create and populate the SQLite database
"""
import sqlite3

def create_database():
    """Create the database and table with sample data"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Create Products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # Clear existing data and insert fresh data
        cursor.execute('DELETE FROM Products')
        
        # Insert sample data
        sample_data = [
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Wireless Headphones', 'Electronics', 89.99),
            (4, 'Desk Chair', 'Furniture', 149.99),
            (5, 'Notebook Set', 'Stationery', 12.50),
            (6, 'Smartphone', 'Electronics', 699.99),
            (7, 'Water Bottle', 'Accessories', 24.99)
        ]
        
        cursor.executemany('''
            INSERT INTO Products (id, name, category, price)
            VALUES (?, ?, ?, ?)
        ''', sample_data)
        
        conn.commit()
        conn.close()
        print("Database created successfully with 7 products")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == '__main__':
    create_database()
