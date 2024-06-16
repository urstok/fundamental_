import yfinance as yf
import pandas as pd

def fetch_and_save_balance_sheet(ticker):
    """
    Fetches the balance sheet data for the given ticker and saves it to a CSV file.

    Args:
    ticker (str): The ticker symbol of the company.
    """
    # Get the balance sheet data
    company = yf.Ticker(ticker)
    balance_sheet = company.balance_sheet

    if balance_sheet.empty:
        print(f"No balance sheet data found for ticker: {ticker}")
        return

    # Transpose the data for better readability
    balance_sheet = balance_sheet.T

    # Save the balance sheet to a CSV file
    filename = f'{ticker}_balance_sheet.csv'
    balance_sheet.to_csv(filename)

    print(f"{ticker} balance sheet data has been saved to '{filename}'")

if __name__ == "__main__":
    # Get the ticker symbol from the user
    ticker = input("Enter the ticker symbol (e.g., 'AAPL' for Apple Inc.): ").strip()
    fetch_and_save_balance_sheet(ticker)
