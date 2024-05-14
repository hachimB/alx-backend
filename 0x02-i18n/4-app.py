#!/usr/bin/env python3
"""Parametrize templates"""
from flask import request, Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """"get_local
    """
    locale = request.args.get('locale')
    if locale in ['en', 'fr']:
        return locale
    return request.accept_languages.best_match(['en', 'fr'])


@app.route("/")
def home() -> str:
    """function to parametrize our templates"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
