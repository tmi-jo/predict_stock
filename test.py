import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def tiker_from_name(stock_name):
    try:
        # Search for the stock ticker symbol using the stock name
        stock = yf.Ticker(stock_name)

        # Get the stock name and symbol
        stock_info = {
            'Ticker': stock.ticker,
            'Stock Name': stock_name
        }

        return stock_info['Ticker']
    except Exception as e:
        return {
            'Error': str(e)
        }

def get_kospi_closing_prices():
    # Define the ticker symbol for KOSPI
    # kospi_ticker = "^KS11"

    kospi_ticker = tiker_from_name('kospi')

    # Calculate the date range for the past 365 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=10000)

    # Fetch the KOSPI data from Yahoo Finance
    kospi_data = yf.download(kospi_ticker, start=start_date, end=end_date)

    print(kospi_data)

    # Select only the 'Close' column
    kospi_closing_prices = kospi_data['Close']

    return kospi_closing_prices

if __name__ == "__main__":
    print('initiate')
    stock_symbol = "kospi"  # Replace with the desired stock symbol
    stock_info = tiker_from_name(stock_symbol)    
    print(stock_info)


    # Call the function to get the KOSPI closing prices as a DataFrame
    kospi_df = get_kospi_closing_prices()

    # Print the DataFrame
    print(kospi_df)
