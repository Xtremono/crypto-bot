import pandas as pd

# Load CSV data
df = pd.read_csv("data/bnb.csv")

# Ensure timestamp is datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Basic checks
print("TOTAL CANDLES:", len(df))
print("FIRST 5 ROWS:")
print(df.head())

# Get last candle
last_candle = df.iloc[-1]

print("\nLAST CANDLE:")
print("Timestamp:", last_candle["timestamp"])
print("Open:", last_candle["open"])
print("High:", last_candle["high"])
print("Low:", last_candle["low"])
print("Close:", last_candle["close"])
print("Volume:", last_candle["volume"])
