import pandas as pd
import numpy as np

def calculate_indicators(stock_data):

    # Daily Returns
    stock_data['Daily Return'] = stock_data['Close'].pct_change()

    # SMA
    stock_data['SMA20'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['SMA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA200'] = stock_data['Close'].rolling(window=200).mean()

    # EMA
    stock_data['EMA12'] = stock_data['Close'].ewm(span=12, adjust=False).mean()
    stock_data['EMA26'] = stock_data['Close'].ewm(span=26, adjust=False).mean()

    # MACD
    stock_data['MACD'] = stock_data['EMA12'] - stock_data['EMA26']
    stock_data['Signal_Line'] = stock_data['MACD'].ewm(span=9, adjust=False).mean()

    # RSI
    delta = stock_data['Close'].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    stock_data['RSI'] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    stock_data['BB_Middle'] = stock_data['Close'].rolling(window=20).mean()
    std_dev = stock_data['Close'].rolling(window=20).std()

    stock_data['BB_Upper'] = stock_data['BB_Middle'] + (2 * std_dev)
    stock_data['BB_Lower'] = stock_data['BB_Middle'] - (2 * std_dev)

    # Volatility
    volatility = stock_data['Daily Return'].std()

    highest_price = stock_data['High'].max()
    lowest_price = stock_data['Low'].min()

    latest_rsi = stock_data['RSI'].iloc[-1]

    # Signal Logic
    if latest_rsi > 70:
        signal = "SELL ⚠️ Overbought"
    elif latest_rsi < 30:
        signal = "BUY 🚀 Oversold"
    else:
        signal = "HOLD 📊 Neutral"

    summary = {
        "highest_price": highest_price,
        "lowest_price": lowest_price,
        "volatility": volatility,
        "latest_rsi": latest_rsi,
        "signal": signal
    }

    return stock_data, summary