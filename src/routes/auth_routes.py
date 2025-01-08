from flask import Blueprint, request, jsonify, current_app
from src.services.auth_service import register_user_service, login_user_service

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register_user():
    session = current_app.session
    data = request.json
    return jsonify(*register_user_service(session, data))

@auth_bp.route('/login', methods=['POST'])
def login_user():
    session = current_app.session
    data = request.json
    return jsonify(*login_user_service(session, data))
