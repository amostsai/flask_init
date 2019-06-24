import os
from flask import Flask

from blueprints.news import news


def create_app(mode):
    app = Flask(__name__)
    app.config.from_object(mode)
    # app.config.from_pyfile('config.py', silent=True)

    app.register_blueprint(news)

    return app


# default to prod config
env = os.environ.get('FLASK_ENV', 'prod')
app = create_app('config.%sConfig' % env.capitalize())
