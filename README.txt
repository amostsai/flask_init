
本範本根據參考資料網頁調整而成

## 下載本專案
$ git clone https://github.com/amostsai/flask_init.git

## 啟用flask/uwsgi, nginx, mysql服務
$ docker-compose up

## 輸入測試資料
1. 打開瀏覽器，連到http://localhost/news

## 修改資料
env
    flask
        setup.py
            name='newproject-CLI',
            newproject=cli.cli:cli
    mysql
        Dockerfile-mysql
            ENV MYSQL_DATABASE=hccu \
            MYSQL_USER=hccu \
            MYSQL_PASSWORD=hccu \
            MYSQL_ROOT_PASSWORD=hccu_root
    nginx
        app.conf
            server_name localhost;
docker-compose.yml
    - "8888:8888" # 測試用，正式環境需刪除
    # restart: always # 正式環境解除註解
webapp
    config.py
        MYSQL_USER = 'hccu'
        MYSQL_PASSWORD = 'hccu'
        MYSQL_DB = 'hccu'

        MAIL_DEFAULT_SENDER = 'xxxx@gmail.com'
        MAIL_SERVER = 'smtp.gmail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USE_SSL = False
        MAIL_USERNAME = 'xxxx@gmail.com'
        MAIL_PASSWORD = 'xxxxxxxx'

        CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
        CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'




## 測試環境
uwsgi --module app --callable app --http :8888 --master --enable-threads --py-autoreload=1

## 執行測試
# docker-compose exec flask py.test tests
1. docker-compose exec flask webcli test    # 執行測試
2. docker-compose exec flask webcli cov     # 測試覆蓋率
3. docker-compose exec flask webcli flake8  #

## 備份資料庫
$ docker exec -i flask_init_mysql_1 mysqldump -u hccu -p hccu > backup_db.sql


## 參考資料
https://medium.com/bitcraft/docker-composing-a-python-3-flask-app-line-by-line-93b721105777
https://www.codementor.io/adityamalviya/python-flask-mysql-connection-rxblpje73

