#!/usr/bin/env python3
"""
Flask app with Babel configuration and locale selection.
"""

from flask import Flask, request, render_template
from flask_babel import Babel, gettext


# Configuration class
class Config:
    """
    Configuration class for Flask app.

    Attributes:
        LANGUAGES (list): List of available languages for localization.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel, set to 'en'.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel, set to 'UTC'.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel object
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the user's locale based on the request's accepted languages.

    Returns:
        str: The best matching language code from the supported LANGUAGES.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route handler for the '/' route.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
