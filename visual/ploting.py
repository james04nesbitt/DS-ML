import pandas as pd
import yfinance as yf
from datetime import date, timedelta
from matplotlib import pyplot as plt

Start = date.today() - timedelta(365)
Start.strftime('%Y-%m-%d')

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')

def closing_price(ticker):
    A = pd.DataFrame(yf.download(ticker, start=Start,
      end=End))
    Asset = A[['Adj Close']]
    col = 'green'
    if(A['Open'][0] > A['Open'][-1]):
        col = 'red'
    return [Asset,col]
while True:
    Ticker = input().upper()
    data = closing_price(Ticker)



    plt.figure(facecolor="darkgray")
    ax = plt.axes()
    ax.set_facecolor('gray')
    plt.plot(data[0], color=data[1], linewidth=2)
    plt.title(Ticker, color = data[1], fontsize = 22)
    plt.ylabel('Price ($)')
    plt.xlabel('Date')

    plt.show()