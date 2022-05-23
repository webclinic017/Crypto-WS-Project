from flask import Flask, render_template, flash, request, redirect
import config, csv
from binance import Client
from binance.enums import *

client = Client(config.API_KEY, config.SECRET_KEY, tld='us')

app = Flask(__name__)

app.secret_key=b'ouweb3287bfejhsljb!?/lw23'

app.debug=True

@app.route('/')
def hello_world():
    title = 'TradingViewClone'

    account = client.get_account()
    balances = account['balances']
    
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    #print(balances)
    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")
    return redirect('/')

@app.route('/sell')
def sell():
    return 'Sell'

@app.route('/settings')
def settings():
    return 'Settings'


if __name__ == "__main__":
    app.run(debug=True)

