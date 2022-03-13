from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
import hashlib
from DB import db, query as q

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dodpdo6do6dpd_5#y2L"F'
app.secret_key = 'Lydoydodpdo6do6dpd_5#y2L"F4Q8z\n\xec]/'

conn = db.fypDB_Connect()
# Home Page
@app.route('/')
def hello():
    return render_template("main.html")
    # login
@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        if request.method == "POST":
            name = request.form['Name']
            password = request.form['Password']

            dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)
            
            fetch_password = db.fetch(conn, q.get__pw.format(name))

            if fetch_password[0][0] == dk.hex():
                print("login successful!!!!")
                session['username']= name
        
                return redirect('/')
        else:
            return render_template("login.html")
    except:
        return redirect('/login')
# register
@app.route("/register", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        password = request.form['Password']
        name = request.form['Name']
        email = request.form['Email']
        c_password = request.form['Confirm Password']

        dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)
        

        if password == c_password:
            db.execute(conn,q.add_new_user.format(name, dk.hex(), email))
            return redirect("/index.html")
        else:
            return redirect("/register")
    else:
        return render_template("register.html")
