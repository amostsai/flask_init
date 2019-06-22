from flask import Flask

from config import DevConfig
from blueprints.news import news


def create_app(settings_override=None):
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    # app.config.from_pyfile('config.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(news)

    return app


app = create_app()
