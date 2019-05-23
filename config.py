import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:default@localhost:5432/flow_chart'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True