from os import environ, path
from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Recaptcha Config
    RECAPTCHA_PUBLIC_KEY = "iubhiukfgjbkhfvgkdfm"
    RECAPTCHA_PARAMETERS = {"size": "100%"}

    # Database URI 
    SQLALCHEMY_DATABASE_URI = "sqlite:///users_info.db?charset=utf8"