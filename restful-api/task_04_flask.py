from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/')
def home():
    """Root endpoint that returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Endpoint that returns all usernames as JSON."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Endpoint that returns the status of the API."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint that returns user data for a specific username.
    
    Args:
        username: The username to look up
        
    Returns:
        JSON object with user data or error message if not found
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user via POST request.
    
    Expected JSON format:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    Returns:
        Confirmation message or error with appropriate status code
    """
    # Check if request has JSON data
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    
    # Check if data is None (invalid JSON)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Check if username is provided
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Store the entire user data object (not just name, age, city)
    # This ensures the user object contains all fields including username
    user_data = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }
    
    # Add user to the dictionary (store without the username key in the value)
    users[username] = {
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }
    
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
