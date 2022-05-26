from flask import Flask, render_template, flash, request, redirect, jsonify
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

@app.route('/sell', methods=['Post'])
def sell():
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")
    return redirect('/')

@app.route('/settings')
def settings():
    return 'Settings'

@app.route('/history')
def history():

    #Transform data into a dictionary so that it can be entered into the chart
    historicalCandles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE)
    
    processed_candleSticks = []

    for candleStick in historicalCandles:

        processed = { 
            "time": candleStick[0] / 1000, 
            "open": candleStick[1], 
            "high": candleStick[2], 
            "low": candleStick[3], 
            "close": candleStick[4]
        }
        #print(candleStick)
        #print("open (app.py) " + candleStick[1])
        processed_candleSticks.append(processed)
    
    return jsonify(processed_candleSticks)


if __name__ == "__main__":
    app.run(debug=True)

