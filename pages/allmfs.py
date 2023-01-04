import datetime as dt
import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator


#mfticker = ['ABRYX', 'AMINX', 'AQLGX', 'BIIEX', 'CISIX', 'DHLTX', 'FVADX', 'IMIDX', 'PIFYX', 'POIIX', 'POLIX', 'SBHAX', 'SBLYX', 'SMBYX', 'SOPYX', 'SWPPX', 'VADDX', 'VFTAX', 'ZDIIX']
mfticker = ['ABRYX', 'AMINX', 'AQLGX']


df_mutualfunds = []

for t in mfticker:
    df_mutualfunds.append(pd.DataFrame([yf.Ticker(t).info]))

df = pd.concat(df_mutualfunds)

df2 = df.loc[:, ['symbol', 'regularMarketPrice', 'ytdReturn', 'longName', 'annualReportExpenseRatio', 'totalAssets',  'morningStarOverallRating']]

print(df2)

#df.to_csv('allmfs.csv')