from flask import Flask
from flask import jsonify
from db import get_data_from_db

def setup_routes(app):
    @app.route('/')
    def index():
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
        with open('templates/diet.html', 'r', encoding='utf-8') as file:
            return file.read()
        
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