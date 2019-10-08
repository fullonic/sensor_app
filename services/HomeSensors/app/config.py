import os

class Config:
    SECRET_KEY = "HOME SENSOR APP"
    CACHE_TYPE = "simple"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True
