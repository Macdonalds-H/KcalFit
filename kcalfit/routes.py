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