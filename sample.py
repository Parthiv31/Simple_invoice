from flask import Flask, render_template, request ,redirect,url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('input.html')
@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    customer_name = request.form['customer_name']
    business_name = request.form['business_name']
    invoice_number = request.form['invoice_number']
    item_names = request.form.getlist('item_name')
    quantities = request.form.getlist('quantity')
    prices = request.form.getlist('price')
    tax_rate = float(request.form['tax_rate'])
    items = []
    subtotal = 0
    tax_amount = 0
    for i in range(len(item_names)):
        item = {
            'item_name': item_names[i],
            'quantity': int(quantities[i]),
            'price': float(prices[i])
        }
        amount = item['quantity'] * item['price']
        subtotal += amount
        items.append(item)
    tax_amount = subtotal * (tax_rate / 100)
    total_amount = subtotal + tax_amount
    return render_template('output.html', customer_name=customer_name, business_name=business_name,
                           invoice_number=invoice_number, items=items, tax_rate=tax_rate,
                           subtotal=subtotal, tax_amount=tax_amount, total_amount=total_amount)
@app.route('/back')
def back():
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
