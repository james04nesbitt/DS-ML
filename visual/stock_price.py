import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression



aapl = 'AAPL'


df = yf.Ticker(aapl)

hist = df.history(period="1y")
print(df.recommendations)