from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializar la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos
db = SQLAlchemy(app)

# Importar las rutas y modelos después de inicializar la aplicación para evitar dependencias circulares
from app import routes, models