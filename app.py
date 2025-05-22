from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'una_clave_muy_secreta_y_unica'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de datos para una Tarea
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    time = db.Column(db.String(5))  # Formato HH:MM
    date = db.Column(db.String(10))  # Formato YYYY-MM-DD

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.date, Task.time).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = Task(
            title=request.form['title'],
            description=request.form['description'],
            time=request.form['time'],
            date=request.form['date']
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', task=None)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.time = request.form['time']
        task.date = request.form['date']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', task=task)

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash(
        "✅ Tarea marcada como completada" if task.completed else "⏳ Tarea marcada como pendiente",
        "success" if task.completed else "info"
    )
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
