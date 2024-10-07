from flask import Flask, render_template, request, redirect, session, flash
from flask import jsonify
from datetime import date, timedelta
import calendar
from db import get_data_from_db, get_user_by_credentials, get_db_connection
import openai  # ChatGPT API 사용


def setup_routes(app):
    @app.route('/')
    def index():
        # 로그인 여부 확인
        if 'user_id' not in session:
            return redirect('/login')
        
        # 인코딩을 명시적으로 UTF-8로 지정
        with open('templates/index.html', 'r', encoding='utf-8') as file:
            return file.read()
        
    @app.route('/data')
    def data():
        result = get_data_from_db()
        print(result)
        return jsonify(result)  # result는 JSON으로 변환 가능한 딕셔너리
    
    @app.route('/diet')
    def diet():
        user_id = session.get('user_id')
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM body_info WHERE user_id = %s", (user_id,))
        body_info = cursor.fetchone()
        print(body_info)
        return render_template('diet.html', body_info=body_info)
        
    @app.route('/get_diet', methods=['POST'])
    def get_diet():
        user_id = session.get('user_id')
        
        # DB에서 사용자 인바디 정보 가져오기
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM body_info WHERE user_id = %s", (user_id,))
        body_info = cursor.fetchone()
        
        if not body_info:
            return jsonify({"error": "Body information not found"}), 404
        
        # ChatGPT API 요청 준비 (한국어 요청 + 한국 음식 포함)
        diet_type = request.json.get('diet_type')  # 'day' 또는 'week'
        prompt = f"제 키는 {body_info['height']}cm, 몸무게는 {body_info['weight']}kg, 체지방률은 {body_info['body_fat_percentage']}%, 골격근량은 {body_info['skeletal_muscle_mass']}kg, 기초대사량은 {body_info['basal_metabolic_rate']}kcal입니다. 한국 요리를 포함한 {diet_type} 다이어트식단을 추천해주세요."

        # ChatGPT API 요청
        openai.api_key = ""
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 모델을 명시합니다.
        messages=[
            {"role": "user", "content": prompt}
        ]
        )

        diet_plan = response['choices'][0]['message']['content']  # 응답에서 내용 추출
    
        return jsonify({"diet_plan": diet_plan})
    
    @app.route('/diet_write')
    def diet_write():
        with open('templates/diet_write.html', 'r', encoding='utf-8') as file:
            return file.read()
    
    from collections import defaultdict

    # DB에서 로그인된 사용자에 해당하는 날짜별 식단 데이터를 가져오는 라우트 (달력에 표시)
    @app.route('/get_diet_data')
    def get_diet_data():
        # 로그인된 사용자의 ID 가져오기
        user_id = session.get('user_id')
        
        if not user_id:
            return jsonify({"error": "사용자가 로그인되지 않았습니다."}), 401

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # 해당 사용자와 월(10월)의 모든 데이터를 가져오는 쿼리
        cursor.execute("""
            SELECT date, meal_type, meal_content 
            FROM diet 
            WHERE user_id = %s AND MONTH(date) = 10 AND YEAR(date) = 2024
        """, (user_id,))
        diet_data = cursor.fetchall()

        cursor.close()
        conn.close()

        # 데이터를 날짜별로 묶음
        diet_by_date = defaultdict(dict)
        for row in diet_data:
            date = str(row['date'])
            meal_type = row['meal_type']
            meal_content = row['meal_content']
            diet_by_date[date][meal_type] = meal_content

        return jsonify(diet_by_date)
        
    # 식단 정보를 저장하거나 업데이트하는 라우트
    @app.route('/save_diet', methods=['POST'])
    def save_diet():
        user_id = session.get('user_id')
        date = request.form['date']
        meal_type = request.form['meal_type']
        meal_content = request.form['meal_content']

        connection = get_db_connection()
        cursor = connection.cursor()

        # 해당 날짜와 식사 타입에 이미 데이터가 있는지 확인
        cursor.execute("SELECT id FROM diet WHERE user_id = %s AND date = %s AND meal_type = %s", (user_id, date, meal_type))
        existing_diet = cursor.fetchone()

        if existing_diet:
            # 기존 데이터가 있으면 업데이트
            cursor.execute("UPDATE diet SET meal_content = %s WHERE id = %s", (meal_content, existing_diet[0]))
        else:
            # 새로운 데이터 삽입
            cursor.execute("INSERT INTO diet (user_id, date, meal_type, meal_content) VALUES (%s, %s, %s, %s)",
                        (user_id, date, meal_type, meal_content))

        connection.commit()
        cursor.close()
        connection.close()

        return redirect('/diet_write')



        
    @app.route('/moisture')
    def moisture():
        user_id = session.get('user_id')

        if not user_id:
            return redirect('/login')  # 로그인 여부 확인

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # 사용자 정보 가져오기
        cursor.execute("SELECT * FROM body_info WHERE user_id = %s", (user_id,))
        body_info = cursor.fetchone()

        if not body_info:
            flash("사용자 정보를 찾을 수 없습니다.", 'error')
            return redirect('/')

        # 목표 수분 섭취량 계산 (체중 * 30ml)
        target_intake = body_info['weight'] * 30

        # 현재 날짜 설정
        today = date.today()
        month = today.month
        year = today.year

        # 달력 생성
        cal = calendar.Calendar(firstweekday=6)  # 일요일을 시작으로 한 달력
        month_days = cal.monthdayscalendar(year, month)

        # 수분 섭취 기록 가져오기
        cursor.execute("SELECT date, daily_intake FROM hydration WHERE user_id=%s AND MONTH(date)=%s", (user_id, month))
        hydration_data = cursor.fetchall()
        print(hydration_data)
        # 수분 섭취 데이터를 변환하여 딕셔너리에 저장
        hydration_dict = {entry['date'].strftime("%Y-%m-%d"): entry['daily_intake'] for entry in hydration_data}
        print(hydration_dict)
        # 오늘의 수분 섭취량 및 진행률 계산
        today_str = today.strftime('%Y-%m-%d')
        current_intake = hydration_dict.get(today_str, 0)  # 기록이 없으면 0ml로 처리
        percentage = int((current_intake / target_intake) * 100) if target_intake > 0 else 0

        conn.close()
        print(today)

        return render_template('moisture.html', 
                            body_info=body_info,
                            month_days=month_days, 
                            hydration_data=hydration_dict, 
                            target_intake=target_intake, 
                            current_intake=current_intake, 
                            percentage=percentage,
                            today=today)

    @app.route('/save_moisture', methods = ['POST'])
    def save_moisture():
        user_id = session['user_id']
        daily_intake = float(request.form['target_intake'])  # 사용자가 입력한 수분 섭취량 (리터 단위)

        # 음수 값 입력 방지
        if daily_intake < 0:
            flash("음수 값은 입력할 수 없습니다.", 'error')
            return redirect('/moisture')

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered = True)


        # 사용자 정보에서 목표 섭취량 계산을 위한 weight 가져오기
        cursor.execute("SELECT weight FROM body_info WHERE user_id = %s", (user_id,))
        user_info = cursor.fetchone()

        if not user_info:
            flash("사용자 정보를 찾을 수 없습니다.", 'error')
            return redirect('/moisture')

        # 목표 수분 섭취량 계산 (체중 * 30ml -> 리터로 변환)
        target_intake = int(user_info['weight']) * 0.03  # kg당 30ml, 리터 단위로 변환
        difference = target_intake - daily_intake  # 목표 섭취량과 실제 섭취량의 차이

        # 수분 섭취량 저장 또는 업데이트
        # 오늘 날짜에 이미 수분 섭취량이 기록되었는지 확인
        cursor.execute("SELECT * FROM hydration WHERE user_id = %s AND date = CURDATE()", (user_id,))
        existing_record = cursor.fetchall()
        if existing_record:
            # 기록이 이미 있으면 업데이트
            daily_intake += existing_record[0]['daily_intake']  # 기존 수분 섭취량에 현재 섭취량 더하기
            difference = target_intake - daily_intake  # 차이도 다시 계산

            cursor.execute("""
                UPDATE hydration
                SET daily_intake = %s, target_intake = %s, difference = %s
                WHERE user_id = %s AND date = CURDATE()
            """, (daily_intake, target_intake, difference, user_id))
        else:
            # 기록이 없으면 새로 삽입
            cursor.execute("""
                INSERT INTO hydration (user_id, date, daily_intake, target_intake, difference)
                VALUES (%s, CURDATE(), %s, %s, %s)
            """, (user_id, daily_intake, target_intake, difference))

        conn.commit()


        conn.close()

        flash('섭취량이 저장되었습니다.', 'success')
        return redirect('/moisture')

    @app.route('/get_moisture_goal')
    def get_moisture_goal():
        user_id = session.get('user_id')
        
        # DB에서 사용자 인바디 정보 가져오기
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM body_info WHERE user_id = %s", (user_id,))
        body_info = cursor.fetchone()
        
        if not body_info:
            return jsonify({"error": "Body information not found"}), 404
        
        # ChatGPT API 요청 준비 (한국어 요청 + 한국 음식 포함)
        prompt = f"제 키는 {body_info['height']}cm, 몸무게는 {body_info['weight']}kg, 체지방률은 {body_info['body_fat_percentage']}%, 골격근량은 {body_info['skeletal_muscle_mass']}kg, 기초대사량은 {body_info['basal_metabolic_rate']}kcal입니다. 일일 수분 섭취량을 나에게 맞춤으로 추천해줘."

        # ChatGPT API 요청
        openai.api_key = ""
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 모델을 명시합니다.
        messages=[
            {"role": "user", "content": prompt}
        ]
        )

        moisture_goal = response['choices'][0]['message']['content']  # 응답에서 내용 추출
    
        return jsonify({"moisture_goal": moisture_goal})


    @app.route('/exercise')
    def exercise():
        with open('templates/exercise.html', 'r', encoding='utf-8') as file:
            return file.read()

    @app.route('/alarm', methods=['GET', 'POST'])
    def alarm():
        user_id = session.get('user_id')  # 로그인된 사용자 ID를 세션에서 가져옴

        if request.method == 'POST':
            diet_reminder_count = request.form['meal-frequency']
            diet_reminder_times = ','.join([request.form[f'meal-time-{i}'] for i in range(1, int(diet_reminder_count) + 1) if request.form[f'meal-time-{i}']])
            water_reminder_count = request.form['water-frequency']
            water_reminder_times = ','.join([request.form[f'water-time-{i}'] for i in range(1, int(water_reminder_count) + 1) if request.form[f'water-time-{i}']])

            # 데이터베이스 연결
            connection = get_db_connection()
            cursor = connection.cursor()

            # 사용자 알림 설정이 이미 존재하는지 확인
            cursor.execute("SELECT COUNT(*) FROM notifications WHERE user_id = %s", (user_id,))
            notification_exists = cursor.fetchone()[0] > 0

            if notification_exists:
                # 기존 데이터가 있으면 업데이트
                query = """
                    UPDATE notifications
                    SET diet_reminder_count = %s, diet_reminder_times = %s, water_reminder_count = %s, water_reminder_times = %s
                    WHERE user_id = %s
                """
                cursor.execute(query, (diet_reminder_count, diet_reminder_times, water_reminder_count, water_reminder_times, user_id))
            else:
                # 데이터가 없으면 새로운 데이터 삽입
                query = """
                    INSERT INTO notifications (user_id, diet_reminder_count, diet_reminder_times, water_reminder_count, water_reminder_times)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (user_id, diet_reminder_count, diet_reminder_times, water_reminder_count, water_reminder_times))

            # 변경 사항 저장
            connection.commit()
            cursor.close()
            connection.close()

        # GET 요청 시 저장된 알림 가져오기
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT diet_reminder_count, diet_reminder_times, water_reminder_count, water_reminder_times FROM notifications WHERE user_id = %s", (user_id,))
        notifications = cursor.fetchall()
        cursor.close()
        connection.close()
        print(notifications)

        # 알림 정보 구조화
        reminders = []
        for notification in notifications:
            reminders.append({
                'diet_count': notification[0],
                'diet_times': notification[1].split(',') if notification[1] else [],
                'water_count': notification[2],
                'water_times': notification[3].split(',') if notification[3] else []
            })

        return render_template('alarm.html', reminders=reminders)

        
    

    @app.route('/mypage', methods=['GET', 'POST'])
    def mypage():
        if request.method == 'GET':
            user_id = session.get('user_id')
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM body_info WHERE user_id = %s", (user_id,))
            body_info = cursor.fetchone()
            return render_template('mypage.html', body_info=body_info)    
        if request.method == 'POST':
            height = request.form['height']        
            weight = request.form['weight']        
            body_fat_percentage = request.form['body_fat_percentage']        
            skeletal_muscle_mass = request.form['skeletal_muscle_mass']        
            basal_metabolic_rate = request.form['basal_metabolic_rate']    

            user_id = session.get('user_id')
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True) 
            update_query = """
                UPDATE body_info 
                SET height = %s, weight = %s, body_fat_percentage = %s, skeletal_muscle_mass = %s, basal_metabolic_rate = %s
                WHERE user_id = %s
            """
            cursor.execute(update_query, (height, weight, body_fat_percentage, skeletal_muscle_mass, basal_metabolic_rate, user_id))   
            conn.commit()
            return redirect('/mypage')           
        
    # 로그인 라우트
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            # 데이터베이스에서 사용자 확인
            user = get_user_by_credentials(username, password)

            if user:
                # 세션에 사용자 정보 저장
                session['user_id'] = user['id']
                session['username'] = user['username']
                return redirect('/')
            else:
                flash('아이디 또는 비밀번호가 잘못되었습니다.')
                return redirect('/login')

        return render_template('login.html')
    



    # dayExer 추가사항
    # 추가되는 코드 (print 포함)

# Exercise 페이지에서 사용자 운동 기록을 DB에서 가져오기
    # @app.route('/save.exercise', methods = ['POST'])
    # def save_exercise():
    # # 세션에서 사용자 ID 확인
    #     user_id = session.get['user_id']
    
    # # DB에서 운동 기록 가져오기
    # conn = get_db_connection()
    # cursor = conn.cursor(dictionary=True)
    # cursor.execute("SELECT * FROM Workouts WHERE user_id = %s", (user_id,))
    # workouts = cursor.fetchall()
    
    # # 터미널에서 운동 기록 확인
    # print(f"사용자 ID: {user_id}의 운동 기록:", workouts)
    
    # return render_template('exercise.html', workouts=workouts)






