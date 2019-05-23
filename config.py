import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'

class ProductionConfig(Config):
    DATABASE_URL = os.environ.get("DATABASE_URL", default=None)
    DEBUG = False

class DevelopmentConfig(Config):
    DATABASE_URL = os.environ.get("DATABASE_URL", default=None)
    DEBUG = True

class TestingConfig(Config):
    TESTING = True