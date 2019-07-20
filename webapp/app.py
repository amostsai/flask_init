import os
from flask import Flask
from flask import url_for
from celery import Celery
import celery.states as states
from itsdangerous import URLSafeTimedSerializer

# from worker import celery
from blueprints.news import news
from blueprints.contact import contact
from blueprints.user import user
from blueprints.user.models import User
from extensions import debug_toolbar, mail, csrf, db, login_manager

CELERY_TASK_LIST = [
    'blueprints.contact.tasks',
    'blueprints.user.tasks',
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
    app.register_blueprint(user)

    extensions(app)
    authentication(app, User)

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
    db.init_app(app)
    login_manager.init_app(app)

    return None


def authentication(app, user_model):
    """
    Initialize the Flask-Login extension (mutates the app passed in).

    :param app: Flask application instance
    :param user_model: Model that contains the authentication information
    :type user_model: SQLAlchemy model
    :return: None
    """
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)

    @login_manager.token_loader
    def load_token(token):
        duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
        serializer = URLSafeTimedSerializer(app.secret_key)

        data = serializer.loads(token, max_age=duration)
        user_uid = data[0]

        return user_model.query.get(user_uid)


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
