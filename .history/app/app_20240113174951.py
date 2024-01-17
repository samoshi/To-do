from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)