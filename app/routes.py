from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import User, Task
from flask_login import login_user, logout_user, login_required

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implementar lógica de login
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Implementar lógica de registro
    return render_template('register.html')

@app.route('/tasks')
@login_required
def tasks():
    # Implementar lógica para listar tareas
    return render_template('tasks.html')