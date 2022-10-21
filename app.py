# from crypt import methods
from flask import Flask, render_template,request,redirect,url_for,session,flash
from database import *

app = Flask(__name__)
app.secret_key = 'fart'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        id = login_check(username, password)
        if id is not False:
            position = check_position(id)
            print(f"position:{position}")
            if position == 'manager':
                return redirect(url_for('main_manager'))
            elif position == 'admin_sales':
                return redirect(url_for('main_menu_as'))
            elif position == 'admin_finance':
                return redirect(url_for('main_menu_af'))
        else:
            flash("wrong username or password", category='error')
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
    customers = show_customer()
    return render_template("pelanggan.html", customers=customers)


@app.route('/new_customer', methods=['POST', 'GET'])
def new_customer_form():
    if request.method == "POST":
        name = request.form['customer_name']
        address = request.form['address']
        phone_numb = request.form['phone_number']
        insert_new_customer(name, address, phone_numb)
        return redirect(url_for('pelanggan'))
    else:
        return render_template('form_create_pelanggan.html')


@app.route('/pelunasan_invoice', methods=['POST', 'GET'])
def pelunasan_invoice():
    invoices = get_invoice_data_paid()

    if request.method == "POST":
        data = request.form.getlist('checkboxes')
        print("data", data)
        id_invoice = [int(i) for i in data]
        for id in id_invoice:
            pay_invoice(int(id))
    return render_template("pelunasan_invoice.html", invoices=invoices)


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
        id_customer = request.form.get("idcustomer")
        total = request.form.get("total")
        print(date, id_customer, total)

        if not date:
            flash('Date is required!')
        elif not id_customer:
            flash('Customer ID is required!')
        elif not total:
            flash('Total is required!')
        else:
            insert_transaction(date, id_customer, total)
            # return redirect(url_for('index'))

    return render_template("sales_invoice_form.html")


@app.route('/admin')
def admin():
    admins = get_admin()
    return render_template("admin.html", admins=admins)


@app.route('/history')
def history():
    invoices = get_invoice_data()
    return render_template('invoice_history.html', invoices=invoices)


@app.route('/invoice', methods=['POST', 'GET'])
def invoice_sales():
    invoices = show_all_invoices()
    if request.method == "POST":
        data = request.form.getlist('cancels')
        print("data", data)
        id_invoice = [int(i) for i in data]
        for id in id_invoice:
            cancel_invoice(int(id))
    return render_template('invoice.html', invoices=invoices)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    customers = show_customer_based_on_id(id)

    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        number = request.form['number']
        edit_customer(name, address, number, id)
        return redirect(url_for('pelanggan'))

    return render_template('edit.html', customers=customers)

if __name__ == "__main__":
    app.run(host='10.252.248.85', port=5000, debug=True, threaded=False)
    # app.run()
