import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ## using MySQL
    # HOST = str(os.environ.get("DB_HOST"))
    # DATABASE = str(os.environ.get("DB_DATABASE"))
    # USERNAME = str(os.environ.get("DB_USERNAME"))
    # PASSWORD = str(os.environ.get("DB_PASSWORD"))

    JSON_SORT_KEYS = False

    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    
    ## using MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True