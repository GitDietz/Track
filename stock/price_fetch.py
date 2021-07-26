"""
build the price fetching routines in here
fetch day end prices for all stocks on holding
may require exchange rate factor too - must be able to get the currency
"""
import datetime as dt
import logging
import numpy as np
import pandas as pd
import yfinance as yf

from django.db import connection, transaction
from.models import Price
log = logging.getLogger('local_log')


def get_data(in_str_ticker, from_date, to_date):
    log.debug('Start')
    data = yf.download(in_str_ticker, start=from_date, end=to_date)
    df = pd.DataFrame(data)
    df.reset_index(inplace=True)
    df['date_only'] = df['Date'].dt.date
    log.info(f'Data frame retrieved')
    return df


'''
Next: setup object create
setup iterrows on the datafram to load all the records in
test for AS/ AX stocks for data retrieval
'''


def tester_raw():

    sql = 'Insert into stock_price (date, close, stock_id, value) values (%s,%s,%s,%s)'
    param = ['2017-05-06', 33, 1, 0.0]
    # can just as well use object.create
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, param)

            cursor.execute("commit;")
#             transaction.commit_unless_managed()
        # connection.commit()
        return 0
    except Exception as e:
        print(f'Issues: {e}')
        return 1


def add_price_data(in_param):
    '''
    confirmed this method works
    :return:
    '''
    log.debug('Start')
    local_int_success = 1
    local_str_error = ''
    try:
        new_price = Price.objects.create(date=in_param[0],
                                         close=in_param[1],
                                         stock_id=in_param[2],
                                         value=in_param[3])
        log.info(f'created {new_price} at {in_param[1]}')
        local_int_success = 0
    except Exception as e:
        local_str_error = f'{e}'
        log.error(local_str_error)
    finally:
        log.debug('END')
        return local_int_success, local_str_error


def load_orchestrator():
    log.debug('Start')
    local_int_success = 1
    local_str_error = ''
    start_date = '2020-03-01'
    end_date = '2020-03-31'
    try:
        local_str_stock = 'XOM'
        local_int_stock = 1
        local_df_price = get_data(local_str_stock, start_date, end_date)
        for index, row in local_df_price.iterrows():
            date = row['date_only']
            price = round(row['Close'], 2)
            param = [date, price, local_int_stock, 0]
            local_int_success, local_str_error = add_price_data(param)
        local_int_success = 0
        log.info(f'Loaded {index} for {local_str_stock}')
    except Exception as e:
        local_str_error = f'{e}'
        log.error(local_str_error)
    finally:
        return local_int_success, local_str_error
