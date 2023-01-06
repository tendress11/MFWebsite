import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt


###########
# Sidebar #
###########



option = st.sidebar.selectbox('Select a symbol', ('ABRYX', 'AMINX', 'AQLGX', 'BIIEX', 'CISIX', 'DHLTX', 'FVADX', 'IMIDX', 'PIFYX', 'POIIX', 'POLIX', 'SBHAX', 'SBLYX', 'SMBYX', 'SOPYX', 'SWPPX', 'VADDX', 'VFTAX', 'ZDIIX'))
today = dt.date.today() 
oneyearago = today - dt.timedelta(days=365)

start_date = st.sidebar.date_input('Start date', oneyearago)
end_date = st.sidebar.date_input('End date', today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date: `%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: end date must be after start date')


#########
# Stock Data
#########

df = yf.download(option, start=start_date, end=end_date, progress=False)
bb = df
bb = bb[['Adj Close']]


#### Calculate Performance Numbers ####
df2 = df['Adj Close'].tail(1)
df2 = df2.iloc[0]
df3 = df['Adj Close'].head(1)
df3 = df3.iloc[0]

performancePercentage = ((df2-df3)/df2)*100
performancePercentage = round(performancePercentage, ndigits=2)
performancePercentage = str(performancePercentage)

####### Fund Holdings ########

ticker = yf.Ticker(option)
df4 = ticker.stats()
df4=pd.DataFrame(df4)
df5 = df4.iloc[57]['topHoldings']
df5 = pd.DataFrame(df5)
df5['NormalPercent'] = df5['holdingPercent']*100
HoldingsSum = pd.DataFrame.sum(df5['NormalPercent'])

df7 = df4.iloc[104]['fundPerformance']
df6 = df4.iloc[50]['fundProfile']
df6 = pd.DataFrame(df6)
df6 = df6.reset_index()







###################
# Set up main app #
###################




### Fund Name ###
fundname = df4.iloc[73]['price']
assetclass = df4.iloc[42]['fundProfile']

st.title(fundname)

col1, col2 = st.columns(2)

with col1:  
    st.header(assetclass) 
    expenseratio = (df4.iloc[10]['defaultKeyStatistics'])*100
    expenseratio = round(expenseratio, ndigits=2)
    expenseratio = 'Expense Ratio: {}%'.format(expenseratio)
    expenseratio = str(expenseratio)
    st.write(expenseratio)

with col2:
    
    image_url = df4.iloc[48]['fundProfile']
    st.image(image_url)




# Plot the prices and the bolinger bands

st.subheader('{} to {}'.format(start_date, end_date))
st.subheader('Performance: {}%'.format(performancePercentage))
st.line_chart(bb)


# Holdings
st.write('Top 10 Holdings')
st.dataframe(df5)


# MPT Stats

st.write('MPT stats')
st.json(df7)
