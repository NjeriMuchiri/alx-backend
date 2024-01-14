from flask import Flask, g, render_template, request

app = Flask(__name__)

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

# Define before_request function
@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)

# Define route
@app.route('/')
def index():
    if g.user:
        welcome_msg = f"You are logged in as {g.user['name']}."
    else:
        welcome_msg = "You are not logged in."

    return render_template('index.html', welcome_msg=welcome_msg)


if __name__ == '__main__':
    app.run(debug=True)
