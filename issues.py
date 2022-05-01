from select import select
from flask import Flask
import sqlite3
conn=sqlite3.connect('lite.db')

cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS issue(srno INTEGER PRIMARY KEY AUTOINCREMENT,project TEXT,issue_type TEXT,summary TEXT,description TEXT,manager TEXT, assigned_to TEXT, status TEXT,priority text)")
conn.commit()
conn.close()
def addissue(project,issue_type,summary,description,manager,assigned_to,status,priority):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO issue (project,issue_type,summary,description,manager,assigned_to,status,priority) VALUES (?,?,?,?,?,?,?,?)', (project,issue_type,summary,description,manager,assigned_to,status,priority))
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
    print(arr)
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
    cur.execute('select srno, project,summary,status from issue')
    data=cur.fetchall()
    return data

def change(name, status):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('update issue set status = (?) where srno = (?)',(status,name))
    conn.commit()
    cur.close()
def getprojectname():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('select distinct(project) from issue order by project')
    data=cur.fetchall()
    
    data1=[]
    for i in data:
        data1.append(i[0])
    print(data1)
    conn.commit()
    cur.close()
    return data1

def gethighpriorityissue():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('select project, summary from issue where priority = "high" and not status = "completed" order by project')
    data=cur.fetchall()
    return data

# mytasks("alay")
# change('Jira','completed')
