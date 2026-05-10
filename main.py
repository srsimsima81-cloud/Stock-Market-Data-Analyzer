from src.utils import create_project_folders
from src.data_fetcher import fetch_stock_data
from src.indicators import calculate_indicators
from src.visualization import generate_charts
from src.report_generator import generate_report

# Create folders automatically
create_project_folders()

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("   NEUROTRADE AI ANALYTICS")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

ticker = input("Enter Stock Ticker (Example: AAPL): ").upper()
start_date = input("Enter Start Date (YYYY-MM-DD): ")
end_date = input("Enter End Date (YYYY-MM-DD): ")

# Fetch stock data
stock_data = fetch_stock_data(ticker, start_date, end_date)

# Calculate indicators
stock_data, summary = calculate_indicators(stock_data)

# Generate charts
generate_charts(stock_data, ticker)

# Generate report
generate_report(ticker, start_date, end_date, summary)

# Save processed data
stock_data.to_csv(f"outputs/{ticker}_processed_data.csv")

print("\n✅ Analysis Completed Successfully!")
print("📊 Charts saved in images/")
print("📄 Reports saved in reports/")
print("💾 Processed data saved in outputs/")