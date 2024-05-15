#!/usr/bin/env python3
"""Force locale with URL parameter"""
from flask import request, Flask, render_template, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get_locale"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.get('locale')
    return request.accept_languages.best_match(['en', 'fr'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """get_user"""
    if not login_as:
        return None
    try:
        return users.get(int(login_as))
    except ValueError:
        return None


@app.before_request
def before_request():
    """before_request"""
    user_id = request.args.get('login_as')
    user = get_user(user_id)
    if user is not None:
        g.user = user
    else:
        g.user = None


@app.route("/")
def home() -> str:
    """function to parametrize our templates"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
