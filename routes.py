from cProfile import label
from crypt import methods
from flask import Flask, render_template, request, redirect
import os
import login_fun
app=Flask(__name__)
user=""
@app.route("/")
def main():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    data=[
        ("jan", 100),
        ("feb", 670),
        ("mar", 600),
        ("apr", 871),
        ("may", 674),
        ("jun", 1000)
    ]
    labels=[row[0] for row in data]
    values=[row[1] for row in data]
    return render_template('dashboard.html',user=user,labels=labels,values=values)

@app.route("/tasks")
def tasks():
    return render_template('tasks.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login/success", methods=['POST'])
def logfun():
    user=request.form['user']
    password=request.form['password']
    flag=login_fun.check(user,password)
    if(flag):
        return redirect('/dashboard')
    else:
        return render_template('/login.html',log="unsuccess")
@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/register/success", methods=['POST'])
def registersuccess():
    user=request.form['user']
    password=request.form['password']
    flag=login_fun.register(user,password)
    if(flag):
        return redirect('/dashboard')
    else:
        return render_template('register.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)