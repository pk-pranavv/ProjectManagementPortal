from flask import Flask
import sqlite3
conn=sqlite3.connect('lite.db')
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS team(name TEXT,profile TEXT,summary TEXT)")
conn.commit()
conn.close()
def addmember(name,profile,summary):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO team VALUES (?,?,?)', (name,profile,summary))
    conn.commit()
    conn.close()
    return True
def getmembers():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('SELECT * from team')
    data=cur.fetchall()
    conn.close()
    return data
def getmanagers():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute('SELECT * from team where profile="manager"')
    data=cur.fetchall()
    conn.close()
    return data

