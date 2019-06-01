from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from datetime import datetime
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy()
db.init_app(app)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    lastLoginDateTime = db.Column(db.DateTime)

    def __init__(self, username, password, lastLoginDateTime):
        self.username = username
        self.password = password
        self.lastLoginDateTime = lastLoginDateTime

    def __repr__(self):
        return "<User '{}'>".format(self.username)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        username = details['username']
        password = details['password']
        lastLoginDateTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')

        user = Users(username=username, password=password,
                     lastLoginDateTime=lastLoginDateTime)
        db.session.add(user)
        db.session.commit()
        # sql = text('INSERT INTO Users(username, password, lastLoginDateTime) VALUES ("%s", "%s", "%s")' % (
        #     username, password, lastLoginDateTime))
        # print(sql)
        # db.engine.execute(sql)
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
