from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# read file .env
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-server-1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'UdacityLab1DB'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacitylab1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'mkManh@123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/common" # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = os.environ.get('CLIENT_ID')

    REDIRECT_PATH = os.environ.get(
        'REDIRECT_PATH') or "/getLab1Token" # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = os.environ.get('SCOPE') or ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = os.environ.get('SESSION_TYPE') or "filesystem" # Token cache will be stored in server-side session
