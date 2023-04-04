import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

st.markdown("<h1 style='text-align:center;color:white'>Time Series</h1>",unsafe_allow_html=True)
df = pd.read_excel('caw1.xlsx')
names = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'
         , '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016','2017','2018','2019','2020','2021','2022']

def state_case(state, case):
    for i in range(0, len(df)):
        if df.iloc[i,0] == state and df.iloc[i,1]==case:
            temp = df.iloc[i, 2:]
            train = np.array(temp)
            train = train.astype(np.int64)
            train = np.reshape(train, (-1, 1))
        
            temp1 = pd.DataFrame(train)
            st.write(sm.graphics.tsa.plot_acf(temp1.values.squeeze()))
            st.write(sm.graphics.tsa.plot_pacf(temp1.values.squeeze(),lags=5))
            model = ARIMA(train, order=(1,1,1))
            model_fit = model.fit()
            pred = model_fit.predict(start=13, end=22)
            new_data = np.append(train, pred)
            plt.figure(figsize=(16,5))
            st.bar_chart(data=new_data)
            year = [2013, 2014, 2015, 2016,2017,2018,2019,2020,2021,2022]
            for w in range(0, 10):
                print(year[w]," " ,pred[w].round(0))
            return pred

state = st.selectbox(
    'Select State Name',
    ('<select>','Assam', 'Punjab', 'Tamil Nadu', 'Kerala','Bihar','Goa','Gujarat','Haryana'))

crime = st.selectbox(
    'Select Crime Name',
    ('<select>','RAPE', 'KIDNAPPING & ABDUCTION', 'DOWRY DEATH', 'ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY','INDECENT REPRESENTATION OF WOMEN(PREVENTION)ACT'))
st.markdown("<h1 style='text-align:center;color:white'>ARIMA TIME SERIES</h1>",unsafe_allow_html=True)
pred = state_case(state, crime)
for i in range(0, 10):
    pred[i] = round(pred[i],0)
name =['2013', '2014', '2015', '2016','2017','2018','2019','2020','2021','2022']
prediction = pd.DataFrame(name, columns=['Year'])
prediction['Prediction'] = pred
st.write(prediction)



def state_case1(state, case):
    for i in range(0, len(df)):
        if df.iloc[i,0] == state and df.iloc[i,1]==case:
            temp = df.iloc[i, 2:]
            train = np.array(temp)
            train = train.astype(np.int64)
            train = np.reshape(train, (-1, 1))
        
            temp1 = pd.DataFrame(train)
            st.write(sm.graphics.tsa.plot_acf(temp1.values.squeeze()))
            st.write(sm.graphics.tsa.plot_pacf(temp1.values.squeeze(),lags=5))
            model = SARIMAX(train, order=(12,1,1))
            model_fit = model.fit()
            pred = model_fit.predict(start=13, end=22)
            new_data = np.append(train, pred)
            plt.figure(figsize=(16,5))
            st.bar_chart(data=new_data)
            year = [2013, 2014, 2015, 2016,2017,2018,2019,2020,2021,2022]
            for w in range(0, 10):
                print(year[w]," " ,pred[w].round(0))
            return pred
st.markdown("<h1 style='text-align:center;color:white'>SARIMAX TIME SERIES</h1>",unsafe_allow_html=True)
pred1 = state_case1(state, crime)
for i in range(0, 10):
    pred1[i] = round(pred1[i],0)
name1 =['2013', '2014', '2015', '2016','2017','2018','2019','2020','2021','2022']
prediction1 = pd.DataFrame(name1, columns=['Year'])
prediction1['Prediction'] = pred1
st.write(prediction1)

