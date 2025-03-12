import bcrypt
import jwt
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

'''
Actual Value stored in an environment variable. 
This ensures that sensitive data like Secret Hashes, API Keys, Passwords etc are not shared or visible publicly. 
The Environment File (.env) has been added to .gitignore and not uploaded on Github, though it has been thoroughly talked about in the README. 
'''
SECRET_KEY = os.getenv("SECRET_KEY")

def hash_password(password):
    # Store the hash as a string. It's originally returned in bytes.
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(hashed_password, plain_password):
    # If hashed_password is already bytes, don't encode again.
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

# Generating JWT Token for Auth.
def generate_token(clinician_id):
    payload = {
        'clinician_id': clinician_id,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # Token valid for 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')