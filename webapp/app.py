import os
from flask import Flask
from flask import url_for
from celery import Celery
import celery.states as states

# from worker import celery
from blueprints.news import news
from blueprints.contact import contact
from extensions import debug_toolbar, mail, csrf

CELERY_TASK_LIST = [
    'blueprints.contact.tasks',
]


def create_celery_app(app):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    celery = Celery(
        app.import_name, broker=app.config['CELERY_BROKER_URL'], include=CELERY_TASK_LIST)

    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(mode):
    app = Flask(__name__)
    app.config.from_object(mode)
    # app.config.from_pyfile('config.py', silent=True)

    app.register_blueprint(news)
    app.register_blueprint(contact)
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    return None


# default to prod config
env = os.environ.get('FLASK_ENV', 'prod')
app = create_app('config.%sConfig' % env.capitalize())

celeryapp = create_celery_app(app)


# test celery
@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celeryapp.send_task('blueprints.contact.tasks.add', args=[
                               param1, param2], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celeryapp.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)
