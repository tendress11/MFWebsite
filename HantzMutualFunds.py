import datetime as dt
import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf

#####  List of all MFs  ######

mfticker = ['ABRYX', 'AMINX', 'AQLGX', 'BIIEX', 'CISIX', 'DHLTX', 'FVADX', 'IMIDX', 'PIFYX', 'POIIX', 'POLIX', 'SBHAX', 'SBLYX', 'SMBYX', 'SOPYX', 'SWPPX', 'VADDX', 'VFTAX', 'ZDIIX']
df_mutualfunds = []
for t in mfticker:
    df_mutualfunds.append(pd.DataFrame([yf.Ticker(t).info]))
dfmfs = pd.concat(df_mutualfunds)
dfmfs2 = dfmfs.loc[:, ['symbol', 'regularMarketPrice', 'ytdReturn', 'longName', 'annualReportExpenseRatio', 'totalAssets',  'morningStarOverallRating']]
st.dataframe(dfmfs2)

