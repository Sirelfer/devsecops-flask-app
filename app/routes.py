from flask import render_template, redirect, url_for, flash, request
from app import app, db  # Importar la instancia de app y db
from app.models import User, Task
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('tasks'))
        else:
            flash('Usuario o contraseña incorrectos.', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado con éxito!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Por favor, completa todos los campos.', 'error')
    return render_template('register.html')

@app.route('/tasks')
@login_required
def tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/create', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title and description:
            task = Task(title=title, description=description, user_id=current_user.id)
            db.session.add(task)
            db.session.commit()
            flash('Tarea creada con éxito!', 'success')
            return redirect(url_for('tasks'))
        else:
            flash('Por favor, completa todos los campos.', 'error')
    return render_template('create_task.html')

@app.route('/tasks/update/<int:task_id>', methods=['GET', 'POST'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        db.session.commit()
        flash('Tarea actualizada con éxito!', 'success')
        return redirect(url_for('tasks'))
    return render_template('update_task.html', task=task)

@app.route('/tasks/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Tarea eliminada con éxito!', 'success')
    return redirect(url_for('tasks'))