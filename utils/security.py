import bcrypt
import jwt
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")   # Replace with an environment variable in production

def hash_password(password):
    # Store the hash as a string
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(hashed_password, plain_password):
    # If hashed_password is already bytes, don't encode again
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

def generate_token(clinician_id):
    payload = {
        'clinician_id': clinician_id,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # Token valid for 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['clinician_id']
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None