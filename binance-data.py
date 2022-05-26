import config, csv
from binance import Client

# connect to the binance client to access price data
client = Client(config.API_KEY, config.SECRET_KEY)

# get the curent 15-minute candlestick data for BTCUSDT
# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# This year 15 minute
# candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2022", "23 May, 2022")

# This year daily
# candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2022", "23 May, 2022")

# Test that follows along with tutorial video
# candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 July, 2020")

# open a csv file to write to (separated by a comma)
csv_file = open('Test_daily.csv', 'w', newline='')
candlestick_writer = csv.writer(csv_file, delimiter=',')

# get the historical 5-min candlestick data for BTCUSDT
candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 July, 2020")

# write each candlestick item to the csv file
for candlestick in candles:
    candlestick[0] = candlestick[0]/1000
    candlestick_writer.writerow(candlestick)

csv_file.close()