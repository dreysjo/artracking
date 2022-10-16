from multiprocessing import connection
from os import curdir
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='debt_track',
)

cur = conn.cursor()

# cur.execute("INSERT INTO customer(cust_name,address,number,total_piutang)values('udey','yareyare street','0999','5000')")
cur.execute("INSERT INTO login(username,password,position)values('jejes','nct','manager')")
cur.execute("INSERT INTO login(username,password,position)values('udey','suga','admin_sales')")
cur.execute("INSERT INTO login(username,password,position)values('ping','jojo','admin_finance')")
conn.commit()
conn.close()