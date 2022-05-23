import talib
from numpy import genfromtxt

# store data from csv file to numpy array
my_data = genfromtxt('15minutes.csv', delimiter=',')

# create array from the 4th (closing price) element in each array from the csv file
close = my_data[:,4]

rsi=talib.RSI(close)

