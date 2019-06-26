class Config(object):
    pass


class ProdConfig(Config):
    DEBUG = False
    TESTING = False

    # SECRET_KEY = ''


class DevConfig(Config):
    DEBUG = True
    TESTING = False

    MYSQL_HOST = 'mysql'
    MYSQL_USER = 'hccu'
    MYSQL_PASSWORD = 'hccu'
    MYSQL_DB = 'hccu'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB)

    # print('SQLALCHEMY_DATABASE_URI ＝ ', SQLALCHEMY_DATABASE_URI)

    SECRET_KEY = 'dkeos;eokfeeiddaj;sief'


class TestConfig(DevConfig):
    DEBUG = True
    TESTING = True
    SERVER_NAME = 'localhost'
