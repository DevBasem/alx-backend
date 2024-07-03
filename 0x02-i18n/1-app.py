#!/usr/bin/env python3
"""
Basic Flask app with Babel configuration
"""

from flask import Flask
from flask_babel import Babel


# Configuration class
class Config:
    """
    Configuration class for Flask app.

    Attributes:
        LANGUAGES (list): available languages for localization.
        BABEL_DEFAULT_LOCALE (str): for Babel, set to 'en'.
        BABEL_DEFAULT_TIMEZONE (str): for Babel, set to 'UTC'.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel object
babel = Babel(app)


@app.route('/')
def index():
    """
    Route handler for the '/' route.

    Returns:
        str: A simple "Hello, world!" message.
    """
    return "Hello, world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
