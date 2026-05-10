from datetime import datetime

def generate_report(ticker, start_date, end_date, summary):

    report = f"""
╔══════════════════════════════════════╗
        NEUROTRADE AI REPORT
╚══════════════════════════════════════╝

Ticker:
{ticker}

Analysis Period:
{start_date} to {end_date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Highest Price:
{summary['highest_price']:.2f}

Lowest Price:
{summary['lowest_price']:.2f}

Volatility:
{summary['volatility']:.4f}

Latest RSI:
{summary['latest_rsi']:.2f}

AI Trading Signal:
{summary['signal']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Insights:
• SMA trends indicate market direction
• RSI identifies overbought/oversold levels
• MACD helps detect momentum shifts
• Volatility measures market risk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated On:
{datetime.now()}

DISCLAIMER:
This project is for educational purposes only.
This is NOT financial advice.
"""

    report_path = f"reports/{ticker}_analysis_report.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    print("✅ Report generated successfully.")