#!/usr/bin/env python3
"""
Basic Flask app with Babel configuration
"""

from flask import Flask
from flask_babel import Babel


# Configuration class
class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel object
babel = Babel(app)


@app.route('/')
def index():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
