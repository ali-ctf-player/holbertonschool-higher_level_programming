#!/usr/bin/python3
"""
Flask API with Authentication
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, create_refresh_token
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-key'  # Change this in production

# Initialize auth extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Store users in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication verification
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


# JWT error handlers (all return 401 as specified)
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# Routes
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Basic Auth protected route
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# JWT Login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400
    
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Create JWT token with user identity and role
    access_token = create_access_token(
        identity={'username': username, 'role': users[username]['role']}
    )
    
    return jsonify({
        "access_token": access_token
    })


# JWT protected route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Admin only route (role-based access control)
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    
    if isinstance(current_user, dict):
        role = current_user.get('role')
    else:
        # Fallback for string identity
        username = current_user
        role = users.get(username, {}).get('role', 'user')
    
    if role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(debug=True)
