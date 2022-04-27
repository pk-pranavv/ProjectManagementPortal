from flask import Flask
import sqlite3
conn=sqlite3.connect('lite.db')
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS issues(description TEXT, assigned_to TEXT, status TEXT)")
conn.commit()
conn.close()