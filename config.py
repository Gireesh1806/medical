import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  
    '''SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")'''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
