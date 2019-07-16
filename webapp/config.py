class Config(object):
    pass


class ProdConfig(Config):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'dkeos;eokfeeiddaj;sief'

    # Flask-Mail.
    MAIL_DEFAULT_SENDER = 'xxxx@gmail.com'  # 要修改！
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'xxxx@gmail.com'  # 要修改！
    MAIL_PASSWORD = 'xxxxxxxx'  # 要修改！

    # Celery.
    CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'  # 可修改密碼！
    CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'  # 可修改密碼！
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_REDIS_MAX_CONNECTIONS = 5


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

    # Flask-Mail.
    MAIL_DEFAULT_SENDER = 'xxxx@gmail.com'  # 要修改！
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'xxxx@gmail.com'  # 要修改！
    MAIL_PASSWORD = 'xxxxxxxx'  # 要修改！

    # Celery.
    CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'  # 可修改密碼！
    CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'  # 可修改密碼！
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_REDIS_MAX_CONNECTIONS = 5


class TestConfig(DevConfig):
    DEBUG = True
    TESTING = True
    SERVER_NAME = 'localhost'
