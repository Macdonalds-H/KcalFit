import mysql.connector

def get_db_connection(): # DB 연결
    return mysql.connector.connect(
        host="localhost",
        user="user",
        password="1111",
        database="my_flask_app"
    )

def get_data_from_db(): # 데이터를 딕셔너리 형식으로 변환
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # dictionary=True 옵션 추가
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()  # 각 행이 딕셔너리로 반환
    conn.close()
    
    return {"data": rows}  # JSON으로 변환 가능한 딕셔너리 형태로 반환
