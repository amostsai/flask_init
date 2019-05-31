class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

    MYSQL_HOST = 'mysql'
    MYSQL_USER = 'hccu'
    MYSQL_PASSWORD = 'hccu'
    MYSQL_DB = 'hccu'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB)

    print('SQLALCHEMY_DATABASE_URI ＝ ', SQLALCHEMY_DATABASE_URI)
