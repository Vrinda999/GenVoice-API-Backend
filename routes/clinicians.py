from flask import Blueprint, request, jsonify
from utils.security import hash_password, check_password

clinician_bp = Blueprint('clinicians', __name__)

@clinician_bp.route('/register', methods=['POST'])
def register():
    from app import mysql

    data = request.get_json()
    name = data['name']
    username = data['username']
    password = hash_password(data['password'])
    role = data.get('role', 'Junior')

    cur = mysql.connection.cursor()
    cur.execute("ALTER TABLE clinicians AUTO_INCREMENT=1")
    cur.execute("INSERT INTO clinicians (name, username, password, role) VALUES (%s, %s, %s, %s)", (name, username, password, role))
    mysql.connection.commit()

    cur.execute("SELECT * FROM clinicians WHERE username = %s", (username,))
    user_data = cur.fetchone()
    cur.close()
    print(user_data)

    return jsonify({"message": "Clinician registered successfully!",
                    "id": user_data[0],
                    "name": user_data[1],
                    "username": user_data[2],
                    "role": user_data[4]})


@clinician_bp.route('/login', methods=['POST'])
def login():
    from app import mysql

    data = request.get_json()
    username = data['username']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clinicians WHERE username = %s", (username,))
    user_data = cur.fetchone()
    # print(f"Fetched Password: {user[0]}")
    cur.close()

    user_pwd = user_data[3]
    role = user_data[4]

    if user_pwd and check_password(user_pwd.encode('utf-8'), password):
        return jsonify({"message": "Login successful!",
                        "id": user_data[0],
                        "name": user_data[1],
                        "username": user_data[2],
                        "role": user_data[4]})
    else:
        return jsonify({"error": "Invalid credentials."}), 401



@clinician_bp.route('/promote', methods=['PATCH'])
def promote():
    from app import mysql
    
    data = request.get_json()
    clinician_id = data.get('id')

    if not clinician_id:
        return jsonify({"error": "Clinician ID is required."}), 400

    cur = mysql.connection.cursor()
    cur.execute("UPDATE clinicians SET role = 'Senior' WHERE id = %s", (clinician_id,))
    mysql.connection.commit()

    cur.execute("SELECT role FROM clinicians WHERE id = %s", (clinician_id,))
    role = cur.fetchone()

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
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE clinicians SET role = 'Junior' WHERE id = %s", (clinician_id,))
    mysql.connection.commit()

    cur.execute("SELECT role FROM clinicians WHERE id = %s", (clinician_id,))
    role = cur.fetchone()
    cur.close()
    return jsonify({"message": "Clinician demoted to Junior.",
                    "new_role": role[0]})
