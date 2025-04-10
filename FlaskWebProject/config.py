from dotenv import load_dotenv
load_dotenv()
import os

class Config(object):
    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')  # 'audacitystorageazureapps'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')  # 'images'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')  # full key
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING')  # full conn string

    # SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER')  # 'audacityazureapps.database.windows.net'
    SQL_DATABASE = 'FlaskAppDB'  # Change to your DB name if different
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')  # 'Azureappssqlusername'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')  # 'Azureappsaqlpassword2025#$@%'

    # Authentication
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')  # 'm2x8Q~...'
    CLIENT_ID = os.environ.get('CLIENT_ID')  # '6a4b54ac-6ecf-41bf-9993-3d16ad557f1e'
    AUTHORITY = 'https://login.microsoftonline.com/common'  # supports personal + work
    REDIRECT_PATH = '/getAToken'
    SCOPE = ['User.Read']

    # Misc
    SECRET_KEY = os.environ.get('SECRET_KEY')  # for Flask sessions

    # Optional: if you're using SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}/{SQL_DATABASE}?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
