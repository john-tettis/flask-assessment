from unittest import TestCase
from currency import convert, check_currency, handle_flash,symbol
from flask import session

class CurrencyTestCase(TestCase):
    def test_convert(self):
        self.assertEqual(convert('USD','USD',100), 100)
        self.assertIsNotNone(convert('USD','EUR',100))
        self.assertEquals(convert('USD','NOTVALID',100),{
                    'c1':True,
                    'c2':False,
                    'amount':True
                })
        self.assertEquals(convert('NOTVALID','NOTVALID',100),{
            'c1':False,
            'c2':False,
            'amount':True
        })
        self.assertEquals(convert('USD','URO',''),{
                    'c1':True,
                    'c2':False,
                    'amount':False
                })
        self.assertEquals(convert('USD','URO',None),{
            'c1':True,
            'c2':False,
            'amount':False
        })
    def test_check_currency(self):
        self.assertEquals(check_currency('USD'),True)
        self.assertEquals(check_currency('usd'),True)
        self.assertEquals(check_currency('EUR'),True)
        self.assertEquals(check_currency('yes'),False)

    def test_handle_flash(self):
        self.assertEquals(handle_flash([{
        'c1':False,
        'c2':False,
        'amount':True},
        'USB','URO',100]),['Currency USB is not valid','Currency URO is not valid'])
        self.assertEquals(handle_flash([{
        'c1':True,
        'c2':True,
        'amount':False},
        'USD','EUR','']),['Amount  is not valid'])
        self.assertEquals(handle_flash([{
        'c1':True,
        'c2':True,
        'amount':False},
        'USD','EUR',None]),['Amount None is not valid'])
    
    def test_symbol(self):
        self.assertEquals(symbol('USD'),'US$')
