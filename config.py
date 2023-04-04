import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    JWT_SECRET_KEY = "samba"
    SERP_API_KEY = "fa98c1c7a774afeeaad1fdcbddc67b058c463d3467cf6f4346d1ae7541ca9670"
    OPENAI_API_KEY = "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"


class TestConfig:
    FLASK_ENV = 'test'
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    JWT_SECRET_KEY = "samba"
    SERP_API_KEY = "fa98c1c7a774afeeaad1fdcbddc67b058c463d3467cf6f4346d1ae7541ca9670"
    OPENAI_API_KEY = "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"
