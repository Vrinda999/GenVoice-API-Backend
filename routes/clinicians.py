from flask import Blueprint, request, jsonify, session
from utils.security import hash_password, check_password, generate_token
import datetime
from decorators.auth import login_required

clinician_bp = Blueprint('clinicians', __name__)

@clinician_bp.route('/register', methods=['POST'])
def register():
    from app import mysql

    data = request.get_json()
    name = data['name']
    username = data['username']
    password = hash_password(data['password'])

    if not all([name, username, password]):
        return jsonify({"error": "Name, username, and password are required!"}), 400
    
    # Setting the Default Value as Junior
    role = 'Junior'
    
    cur = mysql.connection.cursor(dictionary=True)

    cur.execute("ALTER TABLE clinicians AUTO_INCREMENT=1")

    # Check for existing username
    cur.execute("SELECT * FROM clinicians WHERE username = %s", (username,))
    if cur.fetchone():
        cur.close()
        return jsonify({"error": "Username already exists!"}), 409

    # Inserting New Clinician Data into the DB.
    cur.execute("INSERT INTO clinicians (name, username, password, role) VALUES (%s, %s, %s, %s)", (name, username, password, role))
    mysql.connection.commit()

    # Fetching this Data to Cross-Validate and show results to the user.
    cur.execute("SELECT * FROM clinicians WHERE username = %s", (username,))
    user_data = cur.fetchone()
    cur.close()
    print(user_data)

    # Returning Registration Successful Message.
    return jsonify({"message": "Clinician registered successfully!",
                    "id": user_data[0],
                    "name": user_data[1],
                    "username": user_data[2],
                    "role": user_data[4]}), 201



@clinician_bp.route('/login', methods=['POST'])
def login():
    from app import mysql

    data = request.get_json()
    username = data['username']
    password = data['password']

    # Fetching Data for Authentication and Validation.
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clinicians WHERE username = %s", (username,))
    mysql.connection.commit()
    user_data = cur.fetchone()

    if user_data[3] and check_password(user_data[3].encode('utf-8'), password):
        # Generating JWT Token to Track Ongoing Sessions and Authenticate Access to Cases.
        token = generate_token(user_data[0])
        
        # Keeping Track of Valid Tokens.
        cur.execute("INSERT INTO valid_tokens (clinician_id, token, created_on) VALUES (%s, %s, %s)", (user_data[0], token, datetime.datetime.now()))
        mysql.connection.commit()
        cur.close()

        # Returning Login Successful Message.
        return jsonify({"message": "Login successful!",
                        "id": user_data[0],
                        "name": user_data[1],
                        "username": user_data[2],
                        "role": user_data[4],
                        "token": token})
    else:
        # Login Error Message.
        return jsonify({"error": "Invalid credentials."}), 401

#--------------------------------------------------------------------------------------------------------

@clinician_bp.route('/promote', methods=['PATCH'])
def promote():
    from app import mysql
    
    data = request.get_json()
    clinician_id = data.get('id')

    if not clinician_id:
        return jsonify({"error": "Clinician ID is required."}), 400

    # Checking is Clinician is already a Senior.
    cur = mysql.connection.cursor()
    cur.execute("SELECT role FROM clinicians WHERE id = %s", (clinician_id,))
    role = cur.fetchone()
    if role == "Senior":
        return jsonify({"message": "Clinician is already a Senior"})
    
    # Updating Role.
    cur.execute("UPDATE clinicians SET role = 'Senior' WHERE id = %s", (clinician_id,))
    mysql.connection.commit()

    # Fetching and Confirming Changes.
    cur.execute("SELECT role FROM clinicians WHERE id = %s", (clinician_id,))
    role = cur.fetchone()

    # Update Successful Message.
    cur.close()
    return jsonify({"message": "Clinician promoted.",
                    "new_role": role[0]})

@clinician_bp.route('/demote', methods=['PATCH'])
def demote():
    from app import mysql

    data = request.get_json()
    clinician_id = data.get('id')

    if not clinician_id:
        return jsonify({"error": "Clinician ID is required."}), 400
    
    # Checking is Clinician is already a Senior.
    cur = mysql.connection.cursor()
    cur.execute("SELECT role FROM clinicians WHERE id = %s", (clinician_id,))
    role = cur.fetchone()
    if role == "Junior":
        return jsonify({"message": "Clinician is already a Junior"})
    
    
    # Updating Role.
    cur.execute("UPDATE clinicians SET role = 'Junior' WHERE id = %s", (clinician_id,))
    mysql.connection.commit()

    # Fetching and Confirming Changes.
    cur.execute("SELECT role FROM clinicians WHERE id = %s", (clinician_id,))
    role = cur.fetchone()
    cur.close()
    
    # Update Successful Message.
    return jsonify({"message": "Clinician demoted to Junior.",
                    "new_role": role[0]})



@clinician_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    from app import mysql

    # Checking Active Token Associated with the Logged In Account.
    token = request.headers.get('Authorization')

    # Stripping the Token's Validity Away.
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM valid_tokens WHERE token = %s", (token,))
    tok = cur.fetchone()

    if not tok:
        return jsonify({"message": "User Already Logged Out"})
    
    cur.execute("DELETE FROM valid_tokens WHERE token = %s", (token,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Clinician logged out successfully!"}), 200