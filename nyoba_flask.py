from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text

app = Flask(__name__)
db_name = 'artracking.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/debt_track'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
