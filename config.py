import os

class Config:
    SECRET_KEY = 'your_secret_key'
    """ hello this is configuration file"""
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
