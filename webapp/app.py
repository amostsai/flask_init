from flask import Flask

from config import DevConfig
from blueprints.news import news

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py', silent=True)

app.register_blueprint(news)
