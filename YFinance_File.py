import yfinance as yf
import pandas as pd
import numpy as np

def YahooData2returns(YahooData):
    prices = YahooData['Close']
    pricevec = prices.values
    returns = pricevec[1:] / pricevec[:-1] - 1
    return returns

def get_stock_data(symbol):
    data = yf.download(symbol)
    prices = data['Close']
    return prices

# Example usage
prices = get_stock_data('GS')
print(type(prices))
pricevec = prices.values

# Compute the returns
n = len(pricevec)
ratiovec = pricevec[1:n].values / pricevec[:n-1].values

def get_returns(pricevec):
    returns = pricevec[1:] / pricevec[:-1] - 1
    return returns

# Example of using get_returns
returns = get_returns(pricevec)
print(returns)
