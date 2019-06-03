import json
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, Response, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy()
db.init_app(app)


class Users(db.Model):
    __tablename__ = 'Users'  # 資料庫中資料表的名稱

    id = db.Column(db.Integer(), primary_key=True)  # 整數、索引key
    username = db.Column(db.String(255))  # 字串, 255字元
    password = db.Column(db.String(255))
    lastLoginDateTime = db.Column(db.DateTime)  # 日期時間格式

    def __init__(self, username, password, lastLoginDateTime):  # 新增、修改都會用到
        self.username = username
        self.password = password
        self.lastLoginDateTime = lastLoginDateTime

    def __repr__(self):  # 顯示物件內容
        return "<User '{} {}'>".format(self.username, self.lastLoginDateTime)

    @property
    def serialize(self):  # 序列化此類別，方便之後用jsonify轉成json格式
        return {
            'username': self.username,
            'lastLoginDateTime': self.lastLoginDateTime
        }


# 顯示新增使用者畫面
@app.route('/user/add', methods=['GET'])
def show_add_user_view():
    return render_template('user_new.html')  # 返回html檔內容給使用者的瀏覽器


# 顯示修改使用者畫面
@app.route('/user/update/<id>', methods=['GET'])  # 取得網址上的訊息
def show_update_user_view(id):  # 將網址上的訊息轉成變數
    user = Users.query.filter_by(id=id).first()
    # 載入user變數給範本html檔，產生真正html檔內容，返回給使用者的瀏覽器
    return render_template('user_update.html', user=user)


# 列出所有使用者帳號
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = Users.query.all()  # 取得所有使用者資料
    return jsonify(users=[i.serialize for i in users])  # 轉成json格式回傳


# 列出指定id的使用者帳號
@app.route('/api/v1/user/<id>', methods=['GET'])
def get_user(id):
    user = Users.query.get_or_404(id)  # 取得指定條件的使用者資料
    return jsonify(user=[user.serialize])


# 新增使用者帳號
# 修改指定id的使用者帳號
@app.route('/api/v1/user', methods=['POST'])
@app.route('/api/v1/user/<id>', methods=['POST'])
def update_user(id='new'):
    details = request.form
    if request.method == 'POST':
        username = details['username']
        password = details['password']
        lastLoginDateTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')

        if id == 'new':
            user = Users(  # 建立user物件，並設定初始資料
                username=username,
                password=password,
                lastLoginDateTime=lastLoginDateTime
            )
            db.session.add(user)  # 將user物件加入db的session
        else:
            user = Users.query.filter_by(id=id).update({  # 取得指定id的資料並修改成新的內容
                'username': username,
                'password': password,
                'lastLoginDateTime': lastLoginDateTime
            })
        db.session.commit()  # 執行session中所有db指令
        return redirect(url_for('get_users'))  # 重新導向到get_users函數
    return 'error'


# 刪除指定id的使用者帳號
@app.route('/api/v1/user/del/<id>', methods=['GET'])
def del_user(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)  # 設定要刪除內容的db資料
    db.session.commit()
    return redirect(url_for('get_users'))


if __name__ == '__main__':
    app.run()
