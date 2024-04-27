from dotenv import load_dotenv
from os import environ

load_dotenv()

FLASK_RUN_HOST = environ.get("FLASK_RUN_HOST")
FLASK_RUN_PORT = environ.get("FLASK_RUN_PORT")
FLASK_DEBUG = environ.get("FLASK_DEBUG")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
POSTGRES_USER = environ.get("POSTGRES_USER")
