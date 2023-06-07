import os, sys, glob, re
import json
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
# Encoding for writing the page html files
# Do not change unless you are getting a UnicodeEncodeError
ENCODING = "utf-8"


def get_USDTRY():

    API_KEY = "ca757de167514db4a4998696f8dccf64"
    response = requests.get(f'https://api.twelvedata.com/time_series?symbol=USD/TRY&interval=1day&start_date=2005-01-01&end_date=2023-05-31&apikey={API_KEY}')
    data = response.json()
    with open('usd-try.json', 'w') as f:
        json.dump(data, f)




if __name__ == "__main__":
    get_USDTRY()

