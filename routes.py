from crypt import methods
from flask import Flask, render_template, request, redirect
import os
import login_fun, issues, teams

app=Flask(__name__)
user=""

@app.route("/")
def main():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    values=[]
    values=issues.getarray()
    projects=issues.getprojects()
    allprojects=[]
    allprojects=issues.getprojectname()
    prioritydata = issues.gethighpriorityissue()
    return render_template('newdashboard.html',user=user,values=values,projects=projects,allprojects=allprojects, prioritydata=prioritydata)

@app.route("/add")
def add():
    arr=teams.getmembers()
    man=teams.getmanagers()
    return render_template('add.html',arr=arr,man=man)

@app.route("/issueadded",methods=['POST'])
def addissue():
    project=request.form['project']
    issue=request.form['issue']
    summary=request.form['summary']
    desc=request.form['description']
    manager=request.form['manager']
    ass=request.form['assigned']
    status=request.form['status']
    priority=request.form['priority']
    issues.addissue(project,issue,summary,desc,manager,ass,status,priority)
    return redirect('/dashboard')

@app.route("/tasks")
def tasks():
    tasks=issues.mytasks("alay")
    return render_template('tasks.html',tasks=tasks)

@app.route("/update")
def updates():
    update = issues.update()
    # print(request.form['name'])
    return render_template('update.html',update=update)

@app.route("/change", methods=['POST','GET'] )
def updatess():
    data = request.args.get('name')
    data2 = request.args.get('status')
    issues.change(data,data2)
    print(data,data2)
    return redirect('/update')
@app.route("/chat")
def chats():
    return render_template("chat.html")
@app.route("/calendar")
def calendar():
    return render_template('chat.html')

@app.route("/team")
def team():
    tm=teams.getmembers()
    return render_template('team.html',team=tm)

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


@app.route('/createmeet')
def redirect_to_link():
    return redirect('https://meet.google.com/new')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)