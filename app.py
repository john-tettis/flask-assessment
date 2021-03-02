from flask import Flask, session, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from currency import convert, check_currency, handle_flash, symbol

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY']='bananaman'

toolbar = DebugToolbarExtension(app)

@app.route('/')
def currency_form():
    invalid = session.get('invalid')
    if invalid:
        session.pop('invalid') 
        msgs = handle_flash(invalid)
        for msg in msgs:
            flash(msg)
        return render_template('currency_form.html',c1=invalid[1],c2=invalid[2],amount=invalid[3])
    return render_template('currency_form.html')

@app.route('/converted')
def display_results():
    currency1 = request.args.get('currency1')
    currency2 = request.args.get('currency2')
    amount = request.args.get('amount')
    new_amount = convert(currency1,currency2,amount)
    if type(new_amount) is dict:
        validity = new_amount
        session['invalid'] = [validity, currency1, currency2, amount ]
        return redirect('/')


    return render_template('results.html',c1=symbol(currency1),c2=symbol(currency2),amount=amount, new_amount=new_amount)