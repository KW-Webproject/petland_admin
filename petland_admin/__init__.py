from flask import Flask, render_template, session, url_for, request, redirect
import mariadb

app = Flask(__name__)
app.debug = True
app.secret_key = b'aaa!111/'

def get_conn():
    conn = mariadb.connect(user="root",
                           password="000000",
                           host="193.123.233.236",
                           port=3306,
                           database="testPetland")
    return conn

def user(form_id, form_passwd):
    data = []
    conn = get_conn()
    cur = conn.cursor()
    sql = """
        SELECT * FROM admin WHERE id="{}" AND password="{}"
    """.format(form_id, form_passwd)
    cur.execute(sql)
    # for num, id, password, name in cur:
    #     data += num, name
    data = cur.fetchone()
    return data

@app.route('/')
def base():
    return render_template("base.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        passwd = request.form['passwd']
        try:
            data = user(id, passwd)
            print(data)
            if data != None:
                session['user'] = id
                print(session['user'])
                return redirect(url_for('base'))
            else:
                return "여기서? Don't Login"
        except:
            return "Don't Login"


@app.route('/test')
def test():
    return "hello flask test!!"


if  __name__ == "__main__":
    app.run(host='0.0.0.0')