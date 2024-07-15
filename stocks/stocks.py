import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickerSymbol = 'qqq'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='max')


# Calculate 50-day and 200-day moving averages
tickerDf['SMA_50'] = tickerDf['Close'].rolling(window=50).mean()
tickerDf['SMA_200'] = tickerDf['Close'].rolling(window=200).mean()

# Calculate 12-day and 26-day exponential moving averages for MACD
tickerDf['EMA_12'] = tickerDf['Close'].ewm(span=12, adjust=False).mean()
tickerDf['EMA_26'] = tickerDf['Close'].ewm(span=26, adjust=False).mean()

plt.figure(figsize=(12,6))
plt.plot(tickerDf['Close'], label='Close Price')
plt.plot(tickerDf['SMA_50'], label='50-Day SMA')
plt.plot(tickerDf['SMA_200'], label='200-Day SMA')
plt.title('Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plot MACD
tickerDf['MACD'] = tickerDf['EMA_12'] - tickerDf['EMA_26']

