import pymysql
from flask import Flask,render_template,request
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='debt_track',
)

app = Flask(__name__)


#LOGIN QUERIES 

def login_check(usr_name,passwd):
    cur = conn.cursor()
    sqlry = f"""
    SELECT ID_user 
    FROM login 
    WHERE username = %s and password = %s """
    data = cur.execute(sqlry,(usr_name, passwd,))
    row = cur.fetchall()
    conn.commit()
    if data != 0:
        # print('tru')
        return row[0][0]
    else:
        # print('no')
        return False
# login_check('udey','suga')
def check_position(id_usr):
    cur = conn.cursor()
    cur.execute(f"SELECT position FROM login WHERE ID_user= (%s) ",(id_usr,))
    position = cur.fetchall()
    conn.commit()
    # print(position[0][0])
    return position[0][0]

def get_invoice_data():
    cur= conn.cursor()
    cur.execute('SELECT ID_trans,ID_customer,date,total FROM invoice')
    row = cur.fetchall()
    res = []
    for i in range(len(row)):
       data = list(row[i]) 
       res.append(data)
    # print(res)
    return res

def insert_transaction(date, customer_name, total):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO invoice (customer_name, date_invoice, total, status) VALUES (%s, %s, %s, 0)", (customer_name, date, total,))
    conn.commit()
    cur.close()

# app.run()