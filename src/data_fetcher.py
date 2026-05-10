import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker, start_date, end_date):

    print(f"\n📡 Fetching {ticker} stock data...")

    stock_data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    if stock_data.empty:
        print("⚠️ No online data found. Trying CSV fallback...")

        csv_path = f"data/{ticker}.csv"

        if os.path.exists(csv_path):
            stock_data = pd.read_csv(csv_path)
            print("✅ CSV loaded successfully.")
        else:
            raise Exception("❌ No data available.")

    stock_data.dropna(inplace=True)

    stock_data.to_csv(f"data/{ticker}_raw_stock_data.csv")

    print("✅ Stock data fetched successfully.")

    return stock_data