import yfinance as yf
import pandas as pd

# 1. Download 1 year of historical daily data for Apple (AAPL)
print("Downloading market data...")
data = yf.download("AAPL", period="1y")

# 2. View the structural layour of our data matrix
print("\n--- Matrix Structure (Data Columns) ---")
print(data.columns)

# 3. Print the first 5 rows of data
print("\n--- First 5 Daily Data Points ---")
print(data.head())

# 4. Average Closing Price
print("\nThe mathematical average closing price over the last year is:")
print(data['Close'].mean())

# 5. Calculate Rolling Averages
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()
print("\n--- Moving Average Matrix (Last 5 Days) ---")
print(data[['Close', 'MA20', 'MA50']].tail())

# 6. Buy/Sell
latest_ma20 = data['MA20'].iloc[-1]
latest_ma50 = data['MA50'].iloc[-1]
print("\n--- Algorithmic Execution Report ---")
if latest_ma20 > latest_ma50:
    print("SIGNAL DETECTED: Bullish Momentum. Recommendation: BUY ASSET.")
else:
    print("SIGNAL DETECTED: Bearish Momentum. Recommendation: HOLD/SELL.")
