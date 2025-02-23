from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos
    app.run(host='0.0.0.0', port=5000)