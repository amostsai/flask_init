from lib.flask_mailplus import send_template_message
from app import celeryapp


@celeryapp.task()
def deliver_contact_email(email, message):
    """
    Send a contact e-mail.

    :param email: E-mail address of the visitor
    :type user_id: str
    :param message: E-mail message
    :type user_id: str
    :return: None
    """
    ctx = {'email': email, 'message': message}

    send_template_message(subject='Contact',
                          sender=email,
                          recipients=[celeryapp.conf.get('MAIL_USERNAME')],
                          reply_to=email,
                          template='mail_index', ctx=ctx)

    return None


# test celery
@celeryapp.task
def add(x, y):
    return x + y
