#!/usr/bin/env python3

from flask import Flask, app

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'  # Displays this text in the browser

@app.route('/<string:username>')  # Accepts a username in the URL
def user(username):
    return f'<h1>Profile for {username}</h1>'  # Displays a custom message
