#!/usr/bin/env python
# coding: utf-8

# # BASED Coinbase Bot Trader

# In[68]:


#get_ipython().system('pip3 install dash')


# Import the necessary libraries

# In[70]:


import pandas as pd
import numpy as np
import plotly
import getpass
import json as js

# IMPORTS

import pandas as pd
import json as js
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
# Uncomment this if you like to use the old MPL library
#from mpl_finance import candlestick_ohlc
import mplfinance as mpf
import matplotlib.dates as mpl_dates
import matplotlib.ticker as tkr

import seaborn as sns
import dash
import dash_core_components as dcc
import dash_html_components as html



# #### FUNCTION DECLARATION

# In[15]:


def connect(url, *args, **kwargs):
    try:
        if kwargs.get('param', None) is not None:
            response = requests.get(url,params)
        else:
            response = requests.get(url)
        response.raise_for_status()
        #print('HTTP connection success!')
        return response
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')




# In[53]:


btc_import = pd.read_csv("data/btc_history.csv")
btc_import


# In[56]:


btc_import.info()


# In[55]:


btc_import.describe()


# We will add a few more columns just for better readability

# In[65]:


btc_import['date'] = pd.to_datetime(btc_import['Timestamp'], unit='s')
btc_import['year'] = pd.DatetimeIndex(btc_import['date']).year
btc_import['month'] = pd.DatetimeIndex(btc_import['date']).month
btc_import['day'] = pd.DatetimeIndex(btc_import['date']).day
btc_import['hour'] = pd.DatetimeIndex(btc_import['date']).hour
btc_import['minute'] = pd.DatetimeIndex(btc_import['date']).hour
btc_import['day of the week'] = pd.DatetimeIndex(btc_import['date']).weekday

# Display the last 5 rows
btc_import.tail(5)


# In[ ]:




# ## PHASE 4: Visualization

# In[74]:


app = dash.Dash(__name__)


# In[75]:


app.layout = html.Div(
    children=[
        html.H1(children="Bitcoin Analytics",),
            html.P(
            children="Analyze the behavior of Bitcoin"
            " and the number of avocados sold in the US"
            " between 2012 and 2020",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": btc_import["date"],
                        "y": btc_import["Close"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Daily Closing Price"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": btc_import["date"],
                        "y": btc_import["Volume_(BTC)"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Daily Volume"},
            },
        ),
    ]
)


# In[76]:


if __name__ == "__main__":
    app.run_server(debug=True)


# In[ ]:
# %%

# %%
