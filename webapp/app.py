import os
from flask import Flask
from extensions import debug_toolbar

from blueprints.news import news


def create_app(mode):
    app = Flask(__name__)
    app.config.from_object(mode)
    # app.config.from_pyfile('config.py', silent=True)

    app.register_blueprint(news)
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)

    return None


# default to prod config
env = os.environ.get('FLASK_ENV', 'prod')
app = create_app('config.%sConfig' % env.capitalize())
