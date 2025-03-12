from flask import Blueprint, request, jsonify
from decorators.auth import login_required

case_bp = Blueprint('cases', __name__)

@case_bp.route('/Add', methods=['POST'])
@login_required
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
@login_required
def get_cases():
    from app import mysql
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cases")
    cases = cur.fetchall()
    cur.close()

    if not cases:
        return jsonify({"message": "No cases found."}), 404

    return jsonify(cases)