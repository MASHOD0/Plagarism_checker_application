
from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
import hashlib
from DB import db, query as q
from NLP import nlp
from datetime import datetime, timezone
import report
import history


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
        
                return redirect('/home')
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
        if request.method == "POST":
            language = request.form['Language']
            text = request.form['Text']

            sentences = nlp.get_sentences(text, language)
            session['language'] = language
            session['text'] = text
            
            timestamp = datetime.now(timezone.utc)
            history.create_history(conn, session['username'], timestamp, sentences, language)
            return redirect("/report")
        
        return render_template("home.html", username=session['username'])
    else:
        return redirect("/login")
               
                ### history Page ### 
@app.route("/history", methods=['GET', 'POST'])
def history_page():
    if 'username' in session:
        his = history.get_history(conn, session['username'])
        print(his)
        return render_template("history.html", history=his, b=len(his))
    else:
        return redirect("/login")
                
                ### Report Page ### 
@app.route("/report")
def results():
    if 'username' in session and 'language' in session and 'text' in session:
        language = session['language']
        text = session['text']      
        sentences = nlp.get_sentences(text, language)
        print(sentences)
        label, p_links, score, p_metadata = report.generate_report(sentences, language)
        print(label, p_links, score, p_metadata)
        p_sent = 0
        
        for l in label:
            if l != "Not Related":
                p_sent += 1
        return render_template("results.html",sentences=sentences, label=label, p_links=p_links, score=round(score), p_metadata = p_metadata, timestamp = datetime.now(timezone.utc), p_sent=p_sent, b=len(p_links), c= len(sentences))
    else:
        return redirect("/logout")

            ### Logout Page ###
@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('report', None)
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)