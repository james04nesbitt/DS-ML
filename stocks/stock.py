import yfinance as yf

# Define the ticker symbol and period for the data
ticker_symbol = 'SPY'

# Download entire historical data
data = yf.download(ticker_symbol, start="1993-01-01")

# Save the data to a CSV file
csv_filename = f"{ticker_symbol}_historical_data.csv"
data.to_csv(csv_filename)

print(f"Historical data for {ticker_symbol} has been saved to {csv_filename}")
