from flask import Flask, jsonify
from flask_login import LoginManager

import os
from dotenv import load_dotenv
load_dotenv()

from resources.places import places
from resources.user import user
import models

from flask_cors import CORS


DEBUG = True
PORT=8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

app.secret_key = os.environ.get("APP_SECRET")

login_manager = LoginManager()

login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except:
        return None

CORS(places, origins=['http://localhost:3000','*'], supports_credentials=True)

CORS(user, origins=['http://localhost:3000','*'], supports_credentials=True)

app.register_blueprint(places, url_prefix='/api/v1/places')

app.register_blueprint(user, url_prefix='/api/v1/user')

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
