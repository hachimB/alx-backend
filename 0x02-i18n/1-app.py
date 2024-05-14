#!/usr/bin/env python3
"""Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/task1")
def task1():
    """Task 1"""
    return render_template("1-index.html")

if __name__ == "__main__":
    app.run(debug=True)
