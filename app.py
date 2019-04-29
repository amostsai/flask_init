#from flask import Flask
#
#app = Flask(__name__)
#@app.route('/')
#def hello_world():
#    return 'Hello world!'
#
#if __name__ == '__main__':
#    app.run(host='0.0.0.0')



#from flask import Flask, render_template
#
#app = Flask(__name__)
#
#@app.route('/', methods=['GET', 'POST'])
#def index():
#    return render_template('index.html')
#
#if __name__ == '__main__':
#    app.run()



from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'hccu'
app.config['MYSQL_PASSWORD'] = 'hccu'
app.config['MYSQL_DB'] = 'hccu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hccu:hccu@mysql/hccu'
#app.config['SQLALCHEMY_DATABASE_URI'] = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

db = SQLAlchemy()
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']

        sql = text('INSERT INTO MyUsers(firstName, lastName) VALUES ("%s", "%s")' % (firstName, lastName))
        db.engine.execute(sql)
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
