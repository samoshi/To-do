from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Load environment-specific configuration
env = os.environ.get('FLASK_ENV', 'prd')
app = Flask(__name__)
app.config.from_pyfile(f'instance/config_{env}.py', silent=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


# Route to display tasks
@app.route('/')
def index():
    with app.app_context():
        task_list = Task.query.order_by(Task.created_at).all()
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
        except Exception as e:
            print(f"Error clearing tasks: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)