from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Instancia global de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    JWTManager(app)

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    app.session = Session()

    return app
