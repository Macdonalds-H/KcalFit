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
    def data():ㄷㄴ 
        print(result)
        return jsonify(result)  # result는 JSON으로 변환 가능한 딕셔너리
    
    @app.route('/diet')
    def diet():
        user_id = session.get('user_id')
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM body_info WHERE user_id = %s", (user_id,))
        body_info = cursor.fetchone()
        with open('templates/diet.html', 'r', encoding='utf-8', body_info=body_info) as file:
            return file.read()
        
    @app.route('/get_diet', methods=['POST'])
    def get_diet():
        user_id = session.get('user_id')
        
        # DB에서 사용자 인바디 정보 가져오기
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM body_info WHERE user_id = %s", (user_id,))
        body_info = cursor.fetchone()
        print("aaa")
        print(user_id)
        print(body_info)
        
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

    
    

     









    @app.route('/exercise')
    def exercise():
        with open('templates/exercise.html', 'r', encoding='utf-8') as file:
            return file.read()

    @app.route('/alarm')
    def alarm():
        with open('templates/alarm.html', 'r', encoding='utf-8') as file:
            return file.read()

    @app.route('/mypage')
    def mypage():
        with open('templates/mypage.html', 'r', encoding='utf-8') as file:
            return file.read()                
        
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