import yfinance as yf
from yahoo_fin import stock_info as si
import pprint


def get_real_time_data(ticker):
    """
    the function fetch the stock's data based on the ticker input (stock name)
    """
    stock = yf.Ticker(ticker)
    data={
        'stock_info' :stock.info,# get all stock info
        'history' :stock.history(period='1d') # get historical market data

    }
    
    return data 


# pprint.pprint(get_real_time_data("aapl"))


def top_10_gainers():
    """
    fetch the top 10 performed stocks in S&P500 market 
    """
    gainers = si.get_day_gainers().head(10)
    return gainers

    
# pprint.pprint(top_10_gainers())

