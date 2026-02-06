import ccxt
import pandas as pd

# Initialize exchange (public data, no API keys)
exchange = ccxt.binance()

# Market config
symbol = "BNB/USDT"
timeframe = "1h"
limit = 1000

# Fetch OHLCV data
ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

# Convert to DataFrame
df = pd.DataFrame(
    ohlcv,
    columns=["timestamp", "open", "high", "low", "close", "volume"]
)

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

# Save to CSV
df.to_csv("data/bnb.csv", index=False)

print(f"✅ Downloaded {len(df)} candles")
