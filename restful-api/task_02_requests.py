#!/usr/bin/python3
"""
Task 02: Fetch and process posts from JSONPlaceholder API.
"""

import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code and titles.
    """
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Print all post titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Structure the data into a list of dictionaries
        structured_posts = []
        for post in posts:
            structured_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(structured_post)
        
        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Define the fieldnames/columns
            fieldnames = ['id', 'title', 'body']
            
            # Create DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header
            writer.writeheader()
            
            # Write all posts
            writer.writerows(structured_posts)
        
        print("Data has been saved to posts.csv")
