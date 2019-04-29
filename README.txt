
## 啟用flask, nginx, mysql服務
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
