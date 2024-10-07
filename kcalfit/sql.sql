DROP TABLE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),  -- 사용자 이름
    password VARCHAR(100)  -- 비밀번호
);

-- 예시 데이터
INSERT INTO users (username, password)
VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3');

CREATE TABLE body_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- 사용자 아이디
    height FLOAT,  -- 키 (cm)
    weight FLOAT,  -- 몸무게 (kg)
    body_fat_percentage FLOAT,  -- 체지방률 (%)
    skeletal_muscle_mass FLOAT,  -- 골격근량 (kg)
    basal_metabolic_rate FLOAT  -- 기초 대사량 (kcal)
);

INSERT INTO body_info (user_id, height, weight, body_fat_percentage, skeletal_muscle_mass, basal_metabolic_rate)
VALUES
(1, 175.5, 70.0, 15.0, 32.0, 1600),
(2, 160.0, 60.0, 20.0, 25.0, 1400),
(3, 180.0, 80.0, 18.0, 35.0, 1700);

CREATE TABLE hydration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- 사용자 아이디 (외래키로 설정 가능)
    date DATE,    -- 기록된 날짜
    daily_intake FLOAT,  -- 사용자가 입력한 일일 수분 섭취량 (리터 단위)
    target_intake FLOAT, -- 목표 수분 섭취량 (리터 단위)
    difference FLOAT     -- 목표 섭취량과 비교된 수치
);

-- 예시 데이터
INSERT INTO hydration (user_id, date, daily_intake, target_intake, difference)
VALUES
(1, '2024-10-01', 0.8, 1.5, -0.7),
(2, '2024-10-01', 2.0, 2.0, 0.0),
(3, '2024-10-01', 1.5, 1.8, -0.3);


CREATE TABLE exercise (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- 사용자 아이디
    date DATE,    -- 운동한 날짜
    intensity ENUM('저강도', '중강도', '고강도'), -- 운동 강도 (저강도, 중강도, 고강도)
    duration TIME,  -- 운동한 시간 (시간, 분 단위)
    exercise_type ENUM('유산소', '근력'), -- 운동 유형 (유산소, 근력)
    target_duration TIME,  -- 목표 운동 시간
    duration_difference TIME -- 목표와의 시간 차이
);

-- 예시 데이터
INSERT INTO exercise (user_id, date, intensity, duration, exercise_type, target_duration, duration_difference)
VALUES
(1, '2024-10-01', '중강도', '01:30:00', '유산소', '02:00:00', '00:30:00'),
(2, '2024-10-02', '고강도', '02:00:00', '근력', '02:00:00', '00:00:00'),
(3, '2024-10-03', '저강도', '00:45:00', '유산소', '01:00:00', '00:15:00');

CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- 사용자 아이디
    diet_reminder_count INT, -- 식단 알림 횟수 (0회~10회)
    diet_reminder_times VARCHAR(255), -- 식단 알림 시간 (시간 리스트)
    water_reminder_count INT, -- 물 섭취 알림 횟수 (0회~20회)
    water_reminder_times VARCHAR(255) -- 물 섭취 알림 시간 (시간 리스트)
);

-- 예시 데이터
INSERT INTO notifications (user_id, diet_reminder_count, diet_reminder_times, water_reminder_count, water_reminder_times)
VALUES
(1, 3, '07:00, 12:00, 18:00', 5, '08:00, 10:00, 14:00, 16:00, 20:00'),
(2, 2, '08:30, 13:00', 6, '09:00, 11:00, 13:00, 15:00, 17:00, 19:00'),
(3, 4, '06:00, 11:00, 17:00, 21:00', 4, '07:30, 12:30, 15:30, 19:30');

CREATE TABLE diet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- 사용자 아이디
    date DATE,    -- 식단 작성 날짜
    meal_type ENUM('아침', '점심', '저녁'),  -- 식단 타입 (아침, 점심, 저녁)
    meal_content TEXT -- 식단 내용
);

-- 예시 데이터
INSERT INTO diet (user_id, date, meal_type, meal_content)
VALUES
(1, '2024-10-01', '아침', '밥, 계란후라이, 김치'),
(2, '2024-10-01', '점심', '샐러드, 닭가슴살, 바나나'),
(3, '2024-10-01', '저녁', '스테이크, 감자, 야채');

