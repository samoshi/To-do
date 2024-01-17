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