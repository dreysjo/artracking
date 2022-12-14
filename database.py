# from os import curdir
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
    WHERE username = (%s) and password = (%s) """
    data = cur.execute(sqlry,(usr_name, passwd,))
    row = cur.fetchall()
    conn.commit()
    if data != 0:
        return row[0][0]
    else:
        return False

# login_check('jessong','12345')

def check_position(id_usr):
    cur = conn.cursor()
    cur.execute(f"SELECT position FROM login WHERE ID_user= (%s) ",(id_usr,))
    position = cur.fetchall()
    conn.commit()
    return position[0][0]

#UNTUK ADMIN SALES
def get_invoice_data():
    cur= conn.cursor()
    cur.execute('SELECT * FROM invoice')
    row = cur.fetchall()
    res = []
    for i in range(len(row)):
       data = list(row[i])
       res.append(data)
    return res

def get_invoice_data_paid():
    cur= conn.cursor()
    cur.execute("SELECT invoice.ID_invoice, invoice.ID_customer, invoice.date, invoice.total FROM invoice INNER JOIN customer WHERE invoice.ID_customer = customer.ID_customer AND customer.status = 'active'")
    row = cur.fetchall()
    res = []
    for i in range(len(row)):
       data = list(row[i])
       res.append(data)
    return res

def insert_transaction(date, customer_id, total):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO invoice (ID_customer, date, total, status) VALUES (%s, %s, %s, 'active')", (customer_id, date, total,))
    cur.execute(f"UPDATE customer SET total_piutang = total_piutang + (%s) WHERE ID_customer = (%s)", (total, customer_id,))
    conn.commit()
    cur.close()

#UNTUK ADMIN FINANCE

def get_invoice_id(id):
    cur = conn.cursor()
    cur.execute(f"SELECT ID_invoice FROM invoice WHERE ID_invoice = (%s)",(id,))
    the_id = cur.fetchall()
    if len(the_id) != 0:
        return the_id[0][0]
    else:
        return False

def check_status_invoice(id):
    cur = conn.cursor()
    check_id = get_invoice_id(id)
    if check_id != False:
        cur.execute(f"SELECT status FROM invoice WHERE ID_invoice = (%s)",(check_id))
        stat = cur.fetchall()
        if stat[0][0] == 'active':
            return 'active'
        elif stat[0][0] == 'paid':
            return 'paid'
    else:
        return False

def get_info_invoice(id):
    cur = conn.cursor()
    check_status = check_status_invoice(id)
    if check_status != False and check_status!= 'paid':
        cur.execute(f'SELECT ')
        pass


# UNTUK MANAGER
def show_customer():
    cur = conn.cursor()
    cur.execute("SELECT ID_customer, cust_name, address, number from customer WHERE status='active'",)
    customer = cur.fetchall()
    # print(customer)
    res = []
    for cust in range(len(customer)):
        data = list(customer[cust])
        res.append(data)
    return res

def get_customer(id):
     cur = conn.cursor()
     cur.execute(f'SELECT * from customer WHERE ID_customer=(%s)',(id))
     row = cur.fetchall()
     res = []
     for i in range (len(row)):
        data = list(row[i])
        res.append(data)
        print(res)
     return res

def insert_new_customer(name,adress,phone_numb):
    cur = conn.cursor()
    insert = cur.execute(f"INSERT INTO customer (cust_name, address, number, status) VALUES ((%s),(%s),(%s), 'active')",(name,adress,phone_numb,))
    conn.commit()
    return insert

def delete_customer(id):
    cur = conn.cursor()
    cur.execute('DELETE FROM customer WHERE ID_customer = (%s)', (id,))
    conn.commit()
    cur.close()

def show_customer_based_on_id(id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM customer WHERE ID_customer = (%s)', (id,))
    conn.commit()
    cur.close()

def edit_customer(name, address, number, id):
    cur = conn.cursor()
    cur.execute(f"UPDATE customer SET cust_name=%s, address=%s, number=%s WHERE ID_customer = %s", (name, address, number, id,))
    conn.commit()
    cur.close()

def disable_customer(id):
    cur = conn.cursor()
    cur.execute(f"UPDATE customer SET status = 'disabled' WHERE ID_customer = (%s)", (id,))
    conn.commit()
    cur.close()

def edit_customer(id,name,address,number,status):
    cur = conn.cursor()
    edit = cur.execute(f'UPDATE customer SET cust_name =(%s), address=(%s), number=(%s),status=(%s) WHERE ID_customer =(%s)',(name,address,number,status,id,))
    print(edit)
    conn.commit()
    print(edit)
    return edit

def delete_customer(id):
    cur = conn.cursor()
    delete = cur.execute(f"DELETE from customer WHERE ID_customer = (%s)",(id))
    conn.commit()
    return delete

def show_all_invoices():
    cur = conn.cursor()
    cur.execute('SELECT * FROM invoice ORDER BY date ASC')
    invoices = cur.fetchall()
    res = []
    for invoice in range(len(invoices)):
        data = list(invoices[invoice])
        res.append(data)
    return res

def pay_invoice(id):
    cur = conn.cursor()
    cur.execute(f"UPDATE invoice SET status = 'paid' WHERE ID_invoice = (%s)", (id,))
    conn.commit()
    cur.close()

# app.run()

def show_all_invoices():
    cur = conn.cursor()
    cur.execute("SELECT * FROM invoice WHERE NOT status = 'cancelled'",)
    invoices = cur.fetchall()
    res = []
    for invoice in range(len(invoices)):
        data = list(invoices[invoice])
        res.append(data)
    return res

def show_invoice_based_on_customer():
    cur = conn.cursor()
    cur.execute("SELECT ID_customer, cust_name FROM customer")
    customers=cur.fetchall()
    res = []
    for customer in range(len(customers)):
        data = list(customers[customer])
        res.append(data)

    return res

def cancel_invoice(id):
    cur = conn.cursor()
    cur.execute("UPDATE invoice SET status = 'cancelled' WHERE ID_invoice = (%s)", (id,))
    conn.commit()
    cur.close()

def get_admin():
    cur = conn.cursor()
    cur.execute('SELECT * FROM login')
    row = cur.fetchall()
    res = []
    for i in range(len(row)):
        data = list(row[i])
        res.append(data)
    return res

# show_customer()
# delete_customer(15)
# get_customer(16)
# app.run()