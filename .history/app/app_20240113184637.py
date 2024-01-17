from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    global tasks
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/app', methods=['POST'])
def add_task():
    description = request.form.get('description')
    if description:
        tasks.append({'description': description, 'completed' : False})
        save_tasks()
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)