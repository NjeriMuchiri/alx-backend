from flask import Flask, g, render_template, request

app = Flask(__name__)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# our get_user function
def get_user(user_id):
    return users.get(user_id)

# The get_locale function
def get_locale():
    # Locale from URL parameters
    user_locale = request.args.get('locale')

    # Locale from user settings
    if g.user and g.user.get('locale'):
        user_locale = g.user['locale']

    # Locale from request header
    if request.headers.get('Accept-Language'):
        header_locale = request.headers['Accept-Language'].split(',')[0]
        if header_locale:
            user_locale = header_locale

    # Default locale
    return user_locale or 'en'  # Change 'en' to your default locale

# Define before_request function
@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)
    g.locale = get_locale()

# Define route
@app.route('/')
def index():
    welcome_msg = f"You are logged in as {g.user['name']}" if g.user else "You are not logged in."

    return render_template('index.html', welcome_msg=welcome_msg, user_locale=g.locale)


if __name__ == '__main__':
    app.run(debug=True)
