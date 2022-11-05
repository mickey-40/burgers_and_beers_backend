from flask import Flask, jsonify
from flask_login import LoginManager

import os
from dotenv import load_dotenv
from resources.places import places
from resources.user import user
import models
DEBUG = True
PORT=8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

app.secret_key = os.environ.get("APP_SECRET")

login_manager = LoginManager()

login_manager.init_app(app)

app.register_blueprint(places, url_prefix='/api/v1/places')

app.register_blueprint(user, url_prefix='/api/v1/user')
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except:
        return None

# @app.before_request
# def before_request():
#     """Connect to the database before each request."""
#     g.db = models.DATABASE
#     g.db.connect()


# @app.after_request
# def after_request(response):
#     """Close the database connection after each request."""
#     g.db.close()
#     return response


# The default URL ends in / ("my-website.com/").
# @app.route('/')
# def index():
#     return 'hi'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
