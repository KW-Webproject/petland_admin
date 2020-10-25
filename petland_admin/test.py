from flask import Flask, request, render_template, redirect, url_for, abort, session 
import mariadb 
app = Flask(__name__) 
app.secret_key = b'aaa!111/' 


@app.route('/nate')
def naver():
    return render_template("naver.html")

@app.route('/test')
@app.route('/daum')
def daum():
    return redirect("https://www.daum.net")

@app.route('/url_test')
def url_test():
    print(url_for("naver"))
    return redirect(url_for("naver"))


@app.route('/') 
def index(): 
    return '메인페이지' 
# 로그인 
@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'GET': 
        return render_template('login.html') 
    else: 
        id = request.form['id'] 
        pw = request.form['passwd'] 
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다 
        if id == 'abc' and pw == '1234': 
            session['user'] = id 
            return ''' 
                <script> alert("안녕하세요~ {}님"); 
                location.href="/form" 
                </script> '''.format(id) 
        else: 
            return "아이디 또는 패스워드를 확인 하세요." 

# 로그아웃(session 제거) 
@app.route('/logout') 
def logout(): 
    session.pop('user', None) 
    return redirect(url_for('form')) 
    
# 로그인 사용자만 접근 가능으로 만들면 
@app.route('/form') 
def form(): 
    if 'user' in session: 
        return render_template('test.html') 
    return redirect(url_for('login')) 
    
@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        return 'GET 으로 전송이다.' 
    else: 
        num = request.form["num"] 
        name = request.form["name"] 
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name) 
        
        
if __name__ == '__main__': 
    app.run(debug=True, port=5002)
    print(url_for('daum'))
