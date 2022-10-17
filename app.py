from flask import Flask, render_template,request,redirect,url_for,session,flash
from database import *


app = Flask(__name__)
app.secret_key = 'fart'
@app.route('/',methods=['GET','POST'])
def login():
    # apa_gitu = ['temen','nowel','batu','nole','leyon']
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        id= login_check(username,password)
        if id != False:
            position = check_position(id)
            print(f"position:{position}")
            if position== 'manager':
                return redirect(url_for('main_manager'))
            elif position== 'admin_sales':
                return redirect(url_for('main_menu_as'))
            elif position== 'admin_finance':
                return redirect(url_for('main_menu_af'))
        else:
            flash("wrong username or password", category= 'error')
            return render_template('log_in_page.html')
            # return redirect(render_template('log_in_page.html'))
    else:
        return render_template('log_in_page.html')

@app.route('/main_manager')
def main_manager():
    return render_template("main_manager.html")

@app.route('/main_menu_af')
def main_menu_af():
    return render_template("main_menu_af.html")

@app.route('/main_menu_as')
def main_menu_as():
    return render_template("main_menu_as.html")

@app.route('/pelanggan')
def pelanggan():
    return render_template("pelanggan.html")

@app.route('/pelunasan_invoice')
def pelunasan_invoice():
    return render_template("pelunasan_invoice.html")

@app.route('/piutang_perusahaan')
def piutang_perusahaan():
    return render_template("piutang_perusahaan.html")

@app.route('/sales_invoice_form')
def sales_invoice_form():
    return render_template("sales_invoice_form.html")

@app.route('/invoice')
def invoice():
    return render_template("invoice.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/history')
def history():
    invoices = get_invoice_data()
    return render_template('invoice_history.html',invoices=invoices)
    
app.run(host='10.252.248.85', port=5000, debug=True, threaded=False)

