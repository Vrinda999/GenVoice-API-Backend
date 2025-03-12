from functools import wraps
from flask import request, jsonify
from utils.security import verify_token

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing!"}), 401
        
        clinician_id = verify_token(token)
        if not clinician_id:
            return jsonify({"error": "Invalid or expired token!"}), 401
        
        # return f(clinician_id, *args, **kwargs)

        return f(*args, **kwargs)

    return decorated_function
