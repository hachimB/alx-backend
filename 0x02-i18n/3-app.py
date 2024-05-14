#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home() -> str:
    """function to parametrize our templates"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
