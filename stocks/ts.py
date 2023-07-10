import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import feature_extraction, linear_model, model_selection, preprocessing, svm

df = yf.download(tickers='AAPl', period='1y')
plt.plot(df['Open'])
df['lag'] = df['Open'].shift(1)
print(df['lag'].head())
plt.show()
