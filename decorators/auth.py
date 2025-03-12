from functools import wraps
from flask import request, jsonify
from utils.security import verify_token

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from app import mysql
        
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing!"}), 401

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM valid_tokens WHERE token = %s", (token,))
        valid_token = cur.fetchone()

        if not valid_token:
            return jsonify({"error": "Invalid or expired token!"}), 401

        return f(*args, **kwargs)

    return decorated_function
