from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
import hashlib
from DB import db, query as q
from NLP import nlp
from datetime import timestamp
from Report import report

app = Flask(__name__)
app.secret_key = 'Lydoydodpdo6do6dpd_5#y2L"F4Q8z\n\xec]/'
conn = db.SihDB_Connect()

                ### Home Page ###
@app.route('/')
def hello():
    return render_template("main.html")

                ### Login Page ###
@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        if request.method == "POST":
            name = request.form['Name']
            password = request.form['Password']

            dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)
            
            fetch_password = db.fetch(conn, q.get_pw.format(name))

            if fetch_password[0][0] == dk.hex():
                print("login successful!!!!")
                session['username']= name
        
                return redirect('/')
        else:
            return render_template("login.html")
    except:
        return redirect('/login')

                ### Signup Page ###
@app.route("/register", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        password = request.form['Password']
        name = request.form['Name']
        c_password = request.form['Confirm Password']

        dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)
        
        if password == c_password:
            db.execute(conn,q.add_new_user.format(name, dk.hex()))
            return redirect("/home")
        else:
            return redirect("/register")
    else:
        return render_template("register.html")

            ### Home Page ###
@app.route("/home", methods=['GET', 'POST'])
def home():
    if 'username' in session:
        if method == "POST":
            language = request.form['Language']
            text = request.form['Text']

            sentences = nlp.get_sentences(language, text)
            report = report.generate_report(sentences, language)
            return render_template("home.html", report=report)
        history = db.fetch(conn, q.get_history.format(session['username']))
        return render_template("home.html", history=history())
    else:
        return redirect("/login")

            ### Logout Page ###
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)