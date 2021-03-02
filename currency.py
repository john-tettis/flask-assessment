from forex_python.converter import CurrencyRates,CurrencyCodes
import sys
c = CurrencyRates()
code = CurrencyCodes()

def convert(c1,c2,amount):
    validity={
        'c1': check_currency(c1),
        'c2': check_currency(c2),
        'amount': bool(amount)
    }
    for i in validity.values():
        if not i:
            return validity
    return round(c.convert(c1.upper(), c2.upper(), float(amount)),2)


def check_currency(currency):
    if not currency: return False
    symbol = code.get_symbol(currency.upper())
    return True if symbol else False

def handle_flash(invalid):
    validity = invalid[0]
    c1 =  invalid[1]
    c2 = invalid[2]
    amount = invalid[3]
    msgs =[]
    if not validity['c1']:
        msgs.append(f'Currency {c1} is not valid')
    if not validity['c2']:
        msgs.append(f'Currency {c2} is not valid')
    if not validity['amount']:
        msgs.append(f'Amount {amount} is not valid')
    return msgs

def symbol(currency):
    return code.get_symbol(currency.upper())