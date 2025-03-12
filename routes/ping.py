from flask import Flask, jsonify, Blueprint

ping_bp = Blueprint('ping', __name__)

@ping_bp.route('', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200