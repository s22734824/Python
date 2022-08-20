from flask import  Flask,request,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/')
def print_hi():
    return 'hello!!'


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
