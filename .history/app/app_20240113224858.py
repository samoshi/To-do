from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

tasks = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['description']}:{task['completed']}\n")

# Load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            return [
                {"description": line.split(":")[0], "completed": eval(line.split(":")[1])}
                for line in lines
            ]
    except FileNotFoundError:
        return []

# Initialize tasks
tasks = load_tasks()

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task_description = request.form.get('description')
    if new_task_description:
        new_task = {"description": new_task_description, "completed": False}
        tasks.append(new_task)
        save_tasks()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)