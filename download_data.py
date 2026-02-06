import ccxt
import pandas as pd

exchange = ccxt.binance()

symbol = "BNB/USDT"
timeframe = "1h"
limit = 1000

ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

df = pd.DataFrame(
    ohlcv,
    columns=["timestamp", "open", "high", "low", "close", "volume"]
)

df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

df.to_csv("data/bnb.csv", index=False)

print(f"✅ Downloaded {len(df)} candles")
print(df.head())
