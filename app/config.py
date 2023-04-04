import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    JWT_SECRET_KEY = "samba"