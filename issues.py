from flask import Flask
import sqlite3
conn=sqlite3.connect('lite.db')
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS issues(description TEXT, assigned_to TEXT, status TEXT)")
conn.commit()
conn.close()
def addissue(description,assigned,status):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO issues VALUES (?,?,?)', (description,assigned,status))
    conn.commit()
    conn.close()
    return True
def getarray():
    arr=[0,0,0]
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM issues where status="completed"')
    data=cur.fetchall()
    arr[0]=len(data)
    cur.execute('SELECT * FROM issues where status="inprogress"')
    data=cur.fetchall()
    arr[1]=len(data)
    cur.execute('SELECT * FROM issues where status="todo"')
    data=cur.fetchall()
    arr[2]=len(data)
    conn.commit()
    conn.close()
    print(arr)
    return arr

