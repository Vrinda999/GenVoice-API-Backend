from flask import Blueprint, request, jsonify

case_bp = Blueprint('cases', __name__)

@case_bp.route('/Add', methods=['POST'])
def add_case():
    from app import mysql

    data = request.get_json()
    name = data['name']
    description = data['description']

    cur = mysql.connection.cursor()
    cur.execute("ALTER TABLE cases AUTO_INCREMENT=1")
    cur.execute("INSERT INTO cases (name, description) VALUES (%s, %s)", (name, description))
    mysql.connection.commit()

    cur.execute("SELECT * FROM cases WHERE name = %s", (name,))
    user_data = cur.fetchone()
    cur.close()

    return jsonify({"message": "Case Added Successfully!",
                    "id": user_data[0]})

@case_bp.route('/Fetch', methods=['GET'])
def get_cases():
    from app import mysql
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cases")
    cases = cur.fetchall()
    cur.close()

    return jsonify(cases)