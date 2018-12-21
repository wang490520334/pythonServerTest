from flask import Flask

app = Flask(__name__)

#測試  http://127.0.0.1:5000/
@app.route('/')
def index():
    return "Hello, World!"


#*************************************啟動Server*****************************************
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, use_reloader=False)