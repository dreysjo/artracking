from flask import Flask, render_template,request,redirect,url_for,session,flash
from database import *


app = Flask(__name__)
app.secret_key = 'fart'
@app.route('/',methods=['GET','POST'])
def login():
    apa_gitu = ['temen','nowel','batu','nole','leyon']
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        id= login_check(username,password)
        if id != False:
            position = check_position(id)
            print(f"position:{position}")
            if position == 'manager':
                return redirect(url_for('main_manager'))
            elif position == 'admin_sales':
                return redirect(url_for('main_menu_as'))
            elif position == 'admin_finance':
                return redirect(url_for('main_menu_af'))
        else:
            flash("wrong username or password", category= 'error')
            return render_template('log_in_page.html')
            # return redirect(render_template('log_in_page.html'))
    else:
        return render_template('log_in_page.html',apa_gitu=apa_gitu)

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

# @app.route('/sales_invoice_form')
# def sales_invoice_form():
#     return render_template("sales_invoice_form.html")

@app.route('/sales_invoice_form', methods=['POST', 'GET'])
def invoice():
    # invoices = [[1,'20-12-22','4','6.000.000'],[2,'21-12-22','5','7.000.000'],[3,'22-12-22','6','8.000.000']]
    if request.method == "POST":
        date = request.form.get("date")
        customer_name = request.form.get("namecustomer")
        total = request.form.get("total")
        print(date, customer_name, total)

        if not date:
            flash('Date is required!')
        elif not customer_name:
            flash('Customer name is required!')
        elif not total:
            flash('Total is required!')
        else:
            insert_transaction(date, customer_name, total)
            return redirect(url_for('invoice'))

    return render_template("sales_invoice_form.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    # app.run(host='10.252.248.85', port=5000, debug=True, threaded=False)
    app.run()
