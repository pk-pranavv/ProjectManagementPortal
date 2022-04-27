from crypt import methods
from flask import Flask, render_template, request
import os

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/tasks")
def tasks():
    return render_template('tasks.html')

@app.route("/team")
def team():
    return render_template('team.html')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)