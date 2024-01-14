from flask import Flask, g, render_template, request
from flask_babel import Babel, timezoneselector
import pytz

app = Flask(__name__)
babel = Babel(app)


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Define get_user function
def get_user(user_id):
    return users.get(user_id)

# Define get_timezone function
@timezoneselector
def get_timezone():
    # Find timezone parameter in URL parameters
    user_timezone = request.args.get('timezone')

    # Find time zone from user settings
    if g.user and g.user.get('timezone'):
        user_timezone = g.user['timezone']

    # Default to UTC
    if not user_timezone:
        user_timezone = 'UTC'

    # Validate timezone using pytz
    try:
        pytz.timezone(user_timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        user_timezone = 'UTC'  # Default to UTC if invalid timezone

    return user_timezone

# Define before_request function
@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)
    g.timezone = get_timezone()

# Define route
@app.route('/')
def index():
    welcome_msg = f"You are logged in as {g.user['name']}" if g.user else "You are not logged in."

    return render_template('7-index.html', welcome_msg=welcome_msg, user_timezone=g.timezone)


if __name__ == '__main__':
    app.run(debug=True)
