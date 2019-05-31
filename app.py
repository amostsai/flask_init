from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from datetime import datetime

# 第一個參數是應用程式模組(module)或套件(package)的名稱，這樣flask才知道要去哪裡找範本、靜態檔案...
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello world!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')


# =================================================================
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])  # GET, POST方法都會由index這個函數來執行
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()


# =================================================================
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'hccu'
app.config['MYSQL_PASSWORD'] = 'hccu'
app.config['MYSQL_DB'] = 'hccu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    app.config['MYSQL_USER'], app.config['MYSQL_PASSWORD'], app.config['MYSQL_HOST'], app.config['MYSQL_DB'])
print(app.config['SQLALCHEMY_DATABASE_URI'])
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hccu:hccu@mysql/hccu'
#app.config['SQLALCHEMY_DATABASE_URI'] = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

db = SQLAlchemy()
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        createDateTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')

        sql = text('INSERT INTO MyUsers(firstName, lastName, createDateTime) VALUES ("%s", "%s", "%s")' % (
            firstName, lastName, createDateTime))
        db.engine.execute(sql)
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
