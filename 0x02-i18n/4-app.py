#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Check if the 'locale' parameter is present in the URL"""
    request_locale = request.args.get('locale')

    """If the 'locale' parameter is a supported language, return it"""
    if request_locale and request_locale in app.config['LANGUAGES']:
        return request_locale

    """Otherwise, resort to the previous default behavior"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """method that renders our html page"""
    return render_template('4-index.html', home_title=_('home_title'), home_header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
