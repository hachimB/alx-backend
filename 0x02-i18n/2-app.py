#!/usr/bin/env python3
"""Get locale from request
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """"get_local
    """
    return request.accept_languages.best_match(app.config['en', 'fr'])


@app.route("/")
def task2():
    """task2"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
