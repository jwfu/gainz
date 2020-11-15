import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import requests
import json
import random
import sys

# surpress SettingWithCopyWarning warnings.  I could not determine a slick vectorized way of doing the computations since it had to be done row-wise; rationale behind this is implementation is in this SO thread: https://stackoverflow.com/questions/34855859/is-there-a-way-in-pandas-to-use-previous-row-value-in-dataframe-apply-when-previ/34856727#34856727
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def totalReturn(startDate, endDate, ticker, apiKey):
    numYears = (endDate - startDate).days/365

    # hit api for dataset
    df = pdr.av.time_series.AVTimeSeriesReader(symbols=ticker, function='TIME_SERIES_DAILY_ADJUSTED', start=None, end=None, retry_count=3, pause=0.1, session=None, chunksize=25, api_key=apiKey).read()
    df = df[['close','dividend amount']]
    # df

    # shorten dataset and precalculate number of shares purchased per period with dividend
    dg = df[df['dividend amount'] > 0]
    dg.index = pd.to_datetime(dg.index)
    dg['shares purchased'] = dg['dividend amount']/ dg['close']
    # dg

    dgTruncated = dg[startDate:endDate]
    dgTruncated['total shares'] = 1
    dgTruncated['total shares'] = 1 + dgTruncated['shares purchased']
    # dgTruncated.to_csv('output.csv')

    for row in range(1, len(dgTruncated)):
        dgTruncated.iloc[row, 3] = dgTruncated.iloc[row-1, 3] + dgTruncated.iloc[row, 2]

    # dgTruncated

    # determine money from stock appreciation
    stockAppreciation = dgTruncated['close'].iloc[-1] - dgTruncated['close'].iloc[0]
    stockAppreciation/dgTruncated['close'].iloc[0]/numYears

    # determine money from sale of drip
    dripSale = (dgTruncated['total shares'].iloc[-1]-1)*dgTruncated['close'].iloc[-1]
    dripSale/dgTruncated['close'].iloc[0]/numYears

    # determine total gainz
    return (stockAppreciation + dripSale)/dgTruncated['close'].iloc[0]/numYears
