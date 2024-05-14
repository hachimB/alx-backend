#!/usr/bin/env python3
"""Parametrize templates
"""
from flask import Flask, render_template
from flask_babel import Babel, gettext, get_locale


app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home() -> str:
    """function to parametrize our templates"""
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template(
        '3-index.html',
        # home_title=home_title,
        # home_header=home_header,
        lang=get_locale())


if __name__ == "__main__":
    app.run(debug=True)
