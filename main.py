import logging
import numpy as np
import pandas as pd

import yfinance as yf
import plotly.graph_objs as go

logger = logging.getLogger('__name__')


def get_data(in_ticker, in_period, in_interval):
    logger.debug('START')
    data = yf.download(tickers=in_ticker,period=in_period, interval=in_interval)
    return data


def current_stocks_old():
    stock_list = 'XOM EXEL MRK'
    try:
        tickers = yf.Tickers(stock_list) # this is a dict - need to turn the dict into a list
        # ticker_list = list(tickers.items())
        XOM_rec = tickers.tickers['XOM'].recommendations[-2:]

        return 0
    except Exception as e:
        return 1


def current_stocks():
    stock_list = ['XOM', 'EXEL', 'MRK']
    try:    #timestamp / open/high/low/close/adjclose/vol
        for stock in stock_list:
            data = get_data(stock, '7d', '60m')
            # add each row to database if it does not exist


        # end of loop do a valuation based on holding
         # future bring in buy /sell calcs
        return 0
    except Exception as e:
        return 1

"""
DASH-USD
BTC-USD
XOM
EXEL
MRK
Build viewer, recommandation based on the oving aves

"""

def make_chart():
    logger.info('Start')
    try:
        data = get_data('XOM', '8d', '90m')
        # Moving average using Python Rolling function
        data['MA5'] = data['Close'].rolling(5).mean()
        data['MA20'] = data['Close'].rolling(20).mean()

        # declare figure
        fig = go.Figure()

        # Candlestick
        fig.add_trace(go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'], name='market data'))

        # Add Moving average on the graph
        fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
        fig.add_trace(
            go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))

        # Updating X axis and graph
        # X-Axes
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=3, label="3d", step="day", stepmode="backward"),
                    dict(count=5, label="5d", step="day", stepmode="backward"),
                    dict(count=7, label="WTD", step="day", stepmode="todate"),
                    dict(step="all")
                ])
            )
        )

        # Show
        fig.show()
        print('gotit')
    except Exception as e:
        print(f'{e}')

if __name__ == '__main__':
    print('Main')
    local_return = current_stocks()

