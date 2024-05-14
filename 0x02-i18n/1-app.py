#!/usr/bin/env python3
"""Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


if __name__ == "__main__":
    app.run(debug=True)
