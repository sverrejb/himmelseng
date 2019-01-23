import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASEDIR='..'
    BASIC_AUTH_USERNAME = os.environ.get('ADMIN_USER') or 'admin'
    BASIC_AUTH_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'sudankjeks'