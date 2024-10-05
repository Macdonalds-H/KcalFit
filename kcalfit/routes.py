from flask import Flask, render_template, request, redirect, session, flash
from flask import jsonify
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
        with open('templates/moisture.html', 'r', encoding='utf-8') as file:
            return file.read()

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