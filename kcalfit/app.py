from flask import Flask
from routes import setup_routes

app = Flask(__name__)
app.secret_key = 'kcalfit'  
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
