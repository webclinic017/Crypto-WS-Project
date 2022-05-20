import config, csv
from binance import Client

# connect to the binance client to access price data
client = Client(config.API_KEY, config.SECRET_KEY)

# get the cuurent 15-minute candlestick data for BTCUSDT
candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# get the historical 5-min candlestick data for BTCUSDT
# historicalCandles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2019", "24 May, 2021")

# open a csv file to write to (separated by a comma)
csv_file = open('15minutes.csv', 'w')
candlestick_writer = csv.writer(csv_file, delimiter=',')

# write each candlestick item to the csv file
for candlestick in candles:
    candlestick_writer.writerow(candlestick)
