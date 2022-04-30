from flask import Flask
import sqlite3
conn=sqlite3.connect('lite.db')
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS issue(project TEXT,issue_type TEXT,summary TEXT,description TEXT,manager TEXT, assigned_to TEXT, status TEXT)")
conn.commit()
conn.close()
def addissue(project,issue_type,summary,description,manager,assigned_to,status):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO issue VALUES (?,?,?,?,?,?,?)', (project,issue_type,summary,description,manager,assigned_to,status))
    conn.commit()
    conn.close()
    return True
def getarray():
    arr=[0,0,0]
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM issue where status="completed"')
    data=cur.fetchall()
    arr[0]=len(data)
    cur.execute('SELECT * FROM issue where status="inprogress"')
    data=cur.fetchall()
    arr[1]=len(data)
    cur.execute('SELECT * FROM issue where status="todo"')
    data=cur.fetchall()
    arr[2]=len(data)
    conn.commit()
    conn.close()

    return arr

def getprojects():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('select project,count(*),manager from issue where not status = "completed" group by project')
    data=cur.fetchall()
    return data

def mytasks(name):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('select * from issue where assigned_to=(?) order by status desc',(name,))
    data=cur.fetchall()
    return data

def update():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('select * from issue')
    data=cur.fetchall()
    return data

def change(name, status):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('update issue set status = (?) where project = (?)',(status,name))
    conn.commit()
    cur.close()
    

# mytasks("alay")
# change('Jira','completed')
