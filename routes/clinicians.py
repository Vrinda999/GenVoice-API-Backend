from flask import Blueprint, request, jsonify
from utils.security import hash_password, check_password

clinician_bp = Blueprint('clinicians', __name__)

@clinician_bp.route('/register', methods=['POST'])
def register():
    from app import mysql

    data = request.get_json()
    username = data['username']
    password = hash_password(data['password'])
    role = data.get('role', 'Junior')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO clinicians (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Clinician registered successfully! Role: {role}"})

@clinician_bp.route('/login', methods=['POST'])
def login():
    from app import mysql

    data = request.get_json()
    username = data['username']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT password FROM clinicians WHERE username = %s", (username,))
    user = cur.fetchone()
    print(f"Fetched Password: {user[0]}")
    cur.close()

    if user and check_password(user[0].encode('utf-8'), password):
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"error": "Invalid credentials."}), 401



@clinician_bp.route('/promote/<int:clinician_id>', methods=['PATCH'])
def promote(clinician_id):
    from app import mysql

    cur = mysql.connection.cursor()
    cur.execute("UPDATE clinicians SET role = 'Senior' WHERE id = %s", (clinician_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Clinician promoted to Senior."})

@clinician_bp.route('/demote/<int:clinician_id>', methods=['PATCH'])
def demote(clinician_id):
    from app import mysql

    cur = mysql.connection.cursor()
    cur.execute("UPDATE clinicians SET role = 'Junior' WHERE id = %s", (clinician_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Clinician demoted to Junior."})
