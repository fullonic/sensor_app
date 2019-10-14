import os


class Config:
    SECRET_KEY = "HOME SENSOR APP"
    DEBUG = True

    CACHE_TYPE = "simple"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    # CELERY CONFIGURATION
    CELERY_BROKER_URL = "amqp://rabbitmq:rabbitmq@localhost//"
    CELERY_RESULT_BACKEND = "amqp://rabbitmq:rabitmq@localhost//"
    
