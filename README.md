# KcalFit
칼로리핏

### ⚙ 개발환경구축
1. MySQL 설치 [MySQL Installer](https://downloads.mysql.com/archives/installer/)  <br>
[설치방법](https://code-angie.tistory.com/158) - 비밀번호 1111으로 설정하기 <br>
[환경변수설정](https://e2e2e2.tistory.com/22)

2. MySQL 서버 실행
```
mysql -u root -p
```

3. 데이터베이스 생성
```
CREATE DATABASE my_flask_app;

SHOW DATABASES;

CREATE USER 'user'@'localhost' IDENTIFIED BY '1111';

GRANT ALL PRIVILEGES ON my_flask_app.* TO 'user'@'localhost';

FLUSH PRIVILEGES;

USE my_flask_app;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid VARCHAR(50) NOT NULL,
    userpw VARCHAR(50) NOT NULL
);

INSERT INTO users (userid, userpw) VALUES ('user1', 'pw1');

SELECT * FROM users;

```
![image](https://github.com/user-attachments/assets/afe3bf64-cade-48ca-8f26-02ee0262e94f)
이렇게 나온다면 성공

4. Flask 설치
```
pip install Flask

pip install mysql-connector-python
```

5. Flask 서버 실행 (kcalfit 폴더 안에서)
```
python app.py
```

6. http://127.0.0.1:5000 접속<br>
![image](https://github.com/user-attachments/assets/a6641c3a-1475-45ba-877b-d65b551923a8)
