from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('login.html',msg='yo dud')
    return"Hello! this is home page"
