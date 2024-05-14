#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


@app.context_processor
def inject_user():
    return dict(_=_)


@app.route("/")
def home() -> str:
    """function to parametrize our templates"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
