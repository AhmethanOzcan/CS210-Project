import os, sys, glob, re
import json
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Encoding for writing the page html files
# Do not change unless you are getting a UnicodeEncodeError
ENCODING = "utf-8"


def get_USDTRY():

    API_KEY = "ca757de167514db4a4998696f8dccf64"
    response = requests.get(f'https://api.twelvedata.com/time_series?symbol=USD/TRY&interval=1day&start_date=2005-01-01&end_date=2023-05-31&apikey={API_KEY}')
    data = response.json()
    with open('usd-try.json', 'w') as f:
        json.dump(data, f)

def get_LineChartFromJSON(filename, x, y, title, valueName):
    # Load the data
    with open(filename) as f:
        data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(data['values'])

    # Convert the 'datetime' column to datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    df[valueName] = pd.to_numeric(df[valueName])

    # Set 'datetime' as the index
    df.set_index('datetime', inplace=True)

    # Sort the DataFrame by the index (date)
    df.sort_index(inplace=True)

    # Plot the 'valueName' values
    df[valueName].plot()

    # Set the title and labels
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    get_USDTRY()
    get_LineChartFromJSON('usd-try.json', 'Date', 'Exchange Rate', 'USD to TRY Over Time', 'close')