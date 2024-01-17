from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import time

app = Flask(__name__)

# Configure Flask app to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
socketio = SocketIO(app)
# Create SQLAlchemy object and associate it with the app
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Route to connect socketio
@socketio.on('connect')
def handle_connect():
    with app.app_context():
        task_list = Task.query.all()
    emit('update_tasks', {'task_list': task_list})

# Route to display tasks
@app.route('/')
def index():
    with app.app_context():
        task_list = Task.query.all()
    return render_template('index.html', task_list=task_list)


# Route to add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title, complete=False)
    try:
        with app.app_context():
            db.session.add(new_task)
            db.session.commit()
        emit('task_update', broadcast=True)
    except Exception as e:
        print(f"Error adding task: {e}")
    return redirect(url_for("index"))

# Route to update the completion status of a task
@app.route("/update/<int:task_id>")
def update_task(task_id):
    with app.app_context():
        task = Task.query.filter_by(id=task_id).first()
        if task:
            task.complete = not task.complete
            try:
                db.session.commit()
                emit('task_update')
            except Exception as e:
                print(f"Error updating task: {e}")
    return redirect(url_for("index"))

# Route to toggle the completion status of a task
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    with app.app_context():
        task = Task.query.filter_by(id=task_id).first()
        if task:
            task.complete = not task.complete
            try:
                db.session.commit()
                emit('task_update')
            except Exception as e:
                print(f"Error completing task: {e}")
    return redirect(url_for('index'))

# Route to remove a task
@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    print("Remove task ()")
    with app.app_context():
        task = Task.query.filter_by(id=task_id).first()
        if task:
            try:
                db.session.delete(task)
                db.session.commit()
                emit('task_update')
            except Exception as e:
                print(f"Error removing task: {e}")
    return redirect(url_for('index'))

# Route to clear all tasks
@app.route('/clear_tasks')
def clear_tasks():
    with app.app_context():
        try:
            db.session.query(Task).delete()
            db.session.commit()
            emit('task_update')
        except Exception as e:
            print(f"Error clearing tasks: {e}")
    return redirect(url_for('index'))


# WebSocket event to send updates to the client
@socketio.on('task_update')
def handle_task_update():
    with app.app_context():
        task_list = Task.query.all()
    socketio.emit('update_tasks', {'task_list': task_list})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
