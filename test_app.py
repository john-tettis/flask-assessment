from unittest import TestCase
from app import app
from flask import session

app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class CurrencyFormCase(TestCase):
    def test_currency_form(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/converted">', html)
    def test_currency_invalid(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['invalid'] =[{
                    'c1':True,
                    'c2':False,
                    'amount':False
                },'USD','URO','']
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code,200)
            # self.assertEqual(session)
            self.assertIn('<div class="alert alert-warning" role="alert">Currency URO is not valid</div>',html)
            self.assertIn('<div class="alert alert-warning" role="alert">Amount  is not valid</div>',html)

class DisplayResultsCase(TestCase):
    def test_correct_values(self):
        with app.test_client() as client:
            resp = client.get('/converted?currency1=USD&currency2=USD&amount=100')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('100 USD is 100.0 USD', html)
    def test_no_values(self):
        with app.test_client() as client:
            resp = client.get('/converted?currency1=&currency2=&amount=')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 302)
