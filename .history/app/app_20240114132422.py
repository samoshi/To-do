from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


# Load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

# Initialize tasks
tasks = load_tasks()

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    global tasks
    new_task_description = request.form.get('description')
    if new_task_description:
        new_task = {"description": new_task_description, "completed": False}
        tasks.append(new_task)
        save_tasks()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks()
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        # Save your tasks or update your data structure
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)