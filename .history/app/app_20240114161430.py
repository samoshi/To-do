from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# def save_tasks():
#     with open("tasks.json", "w") as file:
#         json.dump(tasks, file)


# # Load tasks from a file
# def load_tasks():
#     try:
#         with open("tasks.json", "r") as file:
#             lines = file.readlines()
#             tasks = []
#             for line in lines:
#                 parts = line.split(":")
#                 if len(parts) == 2:
#                     description, completed_str = parts
#                     completed = eval(completed_str)
#                     tasks.append({"description": description, "completed": completed})
#             return tasks
#     except FileNotFoundError:
#         return []  # Return an empty list if the file doesn't exist
#     except json.decoder.JSONDecodeError:
#         return []  # Return an empty list if there's an issue decoding JSON

# # Initialize tasks
# tasks = load_tasks()

@app.route('/')
def index():
    task_list = Task.query.all()
    return render_template('index.html', task_list=task_list)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title, complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:task_id>")
def update_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/clear_tasks')
def clear_tasks():
    task = Task.query.filter_by(id=task_id).first()
    db.session.query(Task).delete()
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)