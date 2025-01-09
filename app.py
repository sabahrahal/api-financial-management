from sqlalchemy_utils import database_exists, create_database
from src import create_app, db

app = create_app()

with app.app_context():
    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])
    else:
        print("La base de datos ya existe. No se crearán tablas nuevamente.")

    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)