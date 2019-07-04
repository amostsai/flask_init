import os
from flask import Flask
from flask import url_for
import celery.states as states

from worker import celery
from blueprints.news import news
from extensions import debug_toolbar


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


# test celery
@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.cal.add', args=[param1, param2], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)
