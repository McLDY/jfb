import json
from flask import Flask
from flask import request
from stu import stus
app = Flask(__name__)

@app.route('/')
def home():
    with open('index.html')as f:
        f = f.read()
    return f

@app.route('/login',methods=["POST"])
def login():
    with open('cls.json')as f:
        clss = json.loads(str(f.read()))
    if request.method=="POST":
        username = request.get_data()
        #print(username)
        #print(json.loads(username))
        da = json.loads(username)
        l1 = []
        for i in clss:
            l1.append(clss[i])
        print(da)
        for i in l1:
            if da["pwd"] == i['pwd']:
                return "jmp"
                #return '{"code":"-1","msg":"错误的班级或密码"}'
            else:
                return '{"code":"-1","msg":"错误的班级或密码"}'

@app.route('/jfb', methods=['GET','POST'])
def jfb():
    if request.method == "GET":
        with open('jfb.html')as f:
            f = f.read()
        return f
    elif request.method == "POST":
        data = request.get_data()
        print(data)
        return stus.stus



@app.route('/err_ph')
def err_ph():
    with open('er.html')as f:
        f = f.read()
    return f

if __name__ == '__main__':
    app.run(debug=True, port=8800)
"""TypeError: The view function for 'login' did not return a valid response. The function either returned None or ended without a return statement."""