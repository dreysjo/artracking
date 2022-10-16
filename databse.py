import pymysql
from flask import Flask,render_template
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
    
    # print(data)

# check_position(3)
@app.route('/login')
def login(user_name,pswd):
    cur = conn.cursor()
    id= login_check(user_name,pswd)
    if id != False:
        position = check_position(id)
        if position == 'manager':
            return render_template('main_manager.html')
        elif position == 'admin_sales':
            return render_template('main_menu_as.html')
        elif position == 'admin_finance':
            return render_template('main_menu_af.html')
    else:
        #kyknya nanti masukin java yg ngubah text jdi 'failed to login'
        return False

login('udey','suga')