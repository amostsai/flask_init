
本範本根據參考資料網頁調整而成

## 下載本專案
$ git clone https://github.com/amostsai/flask_init.git

## 啟用flask/uwsgi, nginx, mysql服務
$ docker-compose up

## 輸入測試資料
1. 打開瀏覽器，連到http://localhost
2. 輸入姓、名資料

## 備份資料庫
$ docker exec -i flask_init_mysql_1 mysqldump -u hccu -p hccu > backup_db.sql


## 參考資料
https://medium.com/bitcraft/docker-composing-a-python-3-flask-app-line-by-line-93b721105777
https://www.codementor.io/adityamalviya/python-flask-mysql-connection-rxblpje73


-----
# remote debug  （將遠端檔案傳回本機執行!!）
1. ssh -R 52698:localhost:52698 root@[遠端電腦的IP]
    a. cd [專案所在資料夾]
    b. rmate [專案第一個執行的程式]
2. vscode 會自動打開該檔案
