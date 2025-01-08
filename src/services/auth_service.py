from src.models.user import User
from sqlalchemy.orm import Session
from flask_jwt_extended import create_access_token

def register_user_service(session: Session, data):
    if session.query(User).filter_by(email=data['email']).first():
        return {"error": "Email already registered"}, 400

    new_user = User(name=data['name'], email=data['email'])
    new_user.set_password(data['password'])
    session.add(new_user)
    session.commit()

    return {"message": "User registered successfully"}, 201

def login_user_service(session: Session, data):
    user = session.query(User).filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return {"error": "Invalid email or password"}, 401

    # Generar el token de acceso
    access_token = create_access_token(identity={"id": user.id, "name": user.name})
    return {"access_token": access_token}, 200
