#!/usr/bin/env python3
"""
Task 3: Parametrize templates with Flask-Babel integration.
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext


class Config:
    """Config class for Flask app."""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieve the locale for a web page."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Default route handler."""
    return render_template(
        "3-index.html",
        title=gettext('home_title'),
        header=gettext('home_header')
    )


if __name__ == "__main__":
    app.run()
