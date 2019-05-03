
本範本根據參考資料網頁調整而成

## 下載本專案
$ git clone https://github.com/amostsai/flask_init.git

## 啟用flask/uwsgi, nginx, mysql服務
$ docker-compose up

## 登入mysql container，建立資料庫
$ docker exec -it flask_init_mysql_1 mysql -u hccu -p
  USE hccu;
  CREATE TABLE MyUsers ( firstname VARCHAR(30) NOT NULL,  lastname VARCHAR(30) NOT NULL);
  exit

## 輸入測試資料
1. 打開瀏覽器，連到http://localhost
2. 輸入姓、名資料

## 備份資料庫
$ docker exec -i flask_init_mysql_1 mysqldump -u hccu -p hccu > backup_db.sql


## 參考資料
https://medium.com/bitcraft/docker-composing-a-python-3-flask-app-line-by-line-93b721105777
https://www.codementor.io/adityamalviya/python-flask-mysql-connection-rxblpje73
