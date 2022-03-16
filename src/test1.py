from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("main.html")
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
    
if __name__ == '__main__':
    app.run(debug=True)
    
    