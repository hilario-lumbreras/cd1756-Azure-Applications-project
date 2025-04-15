"""
The Flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from dotenv import load_dotenv
load_dotenv()


# Initialize the Flask app
app = Flask(__name__)

# Load the configurations from the Config class
app.config.from_object(Config)

# Set up logging
if not app.debug:
    # If not in debug mode, log errors
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)  # Change logging level based on your needs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

# Initialize Flask extensions
Session(app)  # Flask-Session for session management
db = SQLAlchemy(app)  # Flask-SQLAlchemy for database integration
login = LoginManager(app)  # Flask-Login for user authentication
login.login_view = 'login'  # Name of the login view function (change if necessary)

# Import views after initializing app and extensions to avoid circular imports
from FlaskWebProject import views




# # """
# # The flask application package.
# # """
# # import logging
# # from flask import Flask
# # from config import Config
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_login import LoginManager
# # from flask_session import Session

# # app = Flask(__name__)
# # app.config.from_object(Config)
# # # TODO: Add any logging levels and handlers with app.logger
# # Session(app)
# # db = SQLAlchemy(app)
# # login = LoginManager(app)
# # login.login_view = 'login'

# # import FlaskWebProject.views
# """
# The flask application package.
# """
# import logging
# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_session import Session

# # Initialize the Flask app
# app = Flask(__name__)

# # Load the configurations from the Config class
# app.config.from_object(Config)

# # Set up logging
# if not app.debug:
#     # If not in debug mode, log errors
#     handler = logging.StreamHandler()
#     handler.setLevel(logging.INFO)  # Change logging level based on your needs
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     handler.setFormatter(formatter)
#     app.logger.addHandler(handler)

# # Initialize Flask extensions
# Session(app)  # Flask-Session for session management
# db = SQLAlchemy(app)  # Flask-SQLAlchemy for database integration
# login = LoginManager(app)  # Flask-Login for user authentication
# login.login_view = 'login'  # Name of the login view function (change if necessary)

# # Import your views (routes) after app and extensions initialization to avoid circular imports
# import FlaskWebProject.views

