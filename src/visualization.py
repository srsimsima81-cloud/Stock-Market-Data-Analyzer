import matplotlib.pyplot as plt
import seaborn as sns

# Neon Theme
plt.style.use("dark_background")

NEON_BLUE = "#00F5FF"
NEON_PINK = "#FF00FF"
NEON_GREEN = "#39FF14"
NEON_PURPLE = "#A855F7"

def generate_charts(stock_data, ticker):

    # Closing Price Chart
    plt.figure(figsize=(14, 7))

    plt.plot(
        stock_data['Close'],
        color=NEON_BLUE,
        linewidth=2,
        label='Close Price'
    )

    plt.title(
        f'{ticker} Closing Price',
        fontsize=20,
        color='white'
    )

    plt.grid(alpha=0.3)

    plt.legend()

    plt.savefig(
        f'images/{ticker}_closing_price.png',
        facecolor='black'
    )

    plt.close()

    # SMA Chart
    plt.figure(figsize=(14, 7))

    plt.plot(stock_data['Close'], label='Close', color='white')
    plt.plot(stock_data['SMA20'], label='SMA20', color=NEON_BLUE)
    plt.plot(stock_data['SMA50'], label='SMA50', color=NEON_PINK)
    plt.plot(stock_data['SMA200'], label='SMA200', color=NEON_GREEN)

    plt.title(
        f'{ticker} Moving Averages',
        fontsize=20,
        color='white'
    )

    plt.grid(alpha=0.3)

    plt.legend()

    plt.savefig(
        f'images/{ticker}_moving_averages.png',
        facecolor='black'
    )

    plt.close()

    # RSI Chart
    plt.figure(figsize=(14, 5))

    plt.plot(stock_data['RSI'], color=NEON_PURPLE)

    plt.axhline(70, linestyle='--', color='red')
    plt.axhline(30, linestyle='--', color='green')

    plt.title(
        f'{ticker} RSI Indicator',
        fontsize=20,
        color='white'
    )

    plt.grid(alpha=0.3)

    plt.savefig(
        f'images/{ticker}_rsi_chart.png',
        facecolor='black'
    )

    plt.close()

    # Return Distribution
    plt.figure(figsize=(12, 6))

    sns.histplot(
        stock_data['Daily Return'].dropna(),
        bins=50,
        color=NEON_BLUE
    )

    plt.title(
        f'{ticker} Return Distribution',
        fontsize=20,
        color='white'
    )

    plt.grid(alpha=0.3)

    plt.savefig(
        f'images/{ticker}_return_distribution.png',
        facecolor='black'
    )

    plt.close()