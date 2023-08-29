#!/usr/bin/env python3
""" Flask App"""
from flask import render_template
import flask
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Handles the  route"""
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0', debug=True)