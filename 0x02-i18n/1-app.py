#!/usr/bin/env python3
"""Flask Application"""
from flask_babel import Babel
from flask import Flask
from flask import render_template

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Class Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.route('/', strict_slashes=False)
def index():
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0', debug=True)