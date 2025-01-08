from src import create_app, db

app = create_app()

tables_created = False

@app.before_request
def create_tables():
    global tables_created
    if not tables_created:
        db.create_all()
        tables_created = True

if __name__ == "__main__":
    app.run(debug=True)
