# pip install Flask -i https://pypi.tuna.tsinghua.edu.cn/simple
from flask import Flask, render_template, request

# 这样运行就启动了5000的一个本机服务器

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


# 返回一个templates文件下的一个页面
@app.route('/hello')
def hello():
    s = "这是一个测试页面"
    lst = ['HHH', 'III', "JJJ"]
    return render_template("hello.html", demo=s, lst=lst)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    print(username)
    return username


if __name__ == '__main__':
    app.run()
