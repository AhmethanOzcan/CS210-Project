import os, sys, glob, re
import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

file_path = "inflation.html"
soup = bs(open(file_path, encoding="utf8"), 'lxml')
#soup = bs(open("\data\raw_html\inflation.html", 'r').read(), 'lxml')

#print(soup)



def save_data_to_file(parsed_data):
    
    try:
        
        #print(f"Parsed month: {parsed_data['time']}")

        # Saving the parsed data
        with open("/data/inflation.jsons", "a", encoding="utf8") as f:
            f.write("{}\n".format(json.dumps(parsed_data)))

    except Exception as e:
        print(f"Failed to parse month {parsed_data['time']}: {e}")


open("inflation.jsons", "w", encoding="utf8")

monthly_data = {}

for item in soup.find('tbody'):
    #print (item)
    #extract title
    try:
        
        td_elements = item.find_all('td')

        # Extract the text from each 'td' element
        text_values = [td.get_text() for td in td_elements]
        print (text_values)
        
        
        monthly_data['datetime'] = text_values[0]
        print(monthly_data['datetime'])
        
        monthly_data['TUFE (Yearly % Change)'] = text_values[1]
        print(monthly_data['TUFE (Yearly % Change)'])
        

        monthly_data['TUFE (Monthly % Change)'] = text_values[2]
        print(monthly_data['TUFE (Monthly % Change)'])


        print(monthly_data)
        
        with open("inflation.jsons", "a", encoding="utf8") as f:
                f.write("{}\n".format(json.dumps(monthly_data)))
        print ("aaa")

            
            
    except:
        print("")
    #extract content
    #parsed_data['content'] = soup.find('div', {'class': 'journal-content-article'}).text


