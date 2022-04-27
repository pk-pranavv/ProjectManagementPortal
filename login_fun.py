from flask import Flask
import sqlite3
conn=sqlite3.connect('lite.db')
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
conn.commit()
conn.close()

def check(user,password):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM accounts WHERE user = (?) AND password = (?)', (user, password))
    data=cur.fetchall()
    conn.close()
    if len(data)!=0:
        return True
    else:
        return False

def register(user,password):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO accounts VALUES (?,?)', (user, password))
    print("registered")
    conn.commit()
    conn.close()
    return True

