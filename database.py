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
    cur = conn.cursor()
    cur.execute('SELECT * FROM invoice')
    row = cur.fetchall()
    return row
    # print(yaa[0][2])
            

    # print(data)
get_invoice_data()