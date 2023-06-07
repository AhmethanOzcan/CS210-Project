import os, sys, glob, re
import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np



# Encoding for writing the page html files
# Do not change unless you are getting a UnicodeEncodeError
ENCODING = "utf-8"
save_path ="inflation.html"

def get_page_content(page_url):
    """
    This function should take the URL of a page and return the html
    content (string) of that page.
    """

    # WRITE YOUR CODE HERE
    ###############################

    # Save the page content (html) in the variable "page_html"
    resp = requests.get(page_url, verify=False)

    page_html = resp.text

    ###############################

    return page_html


def save_html_pages():
    try:
        # Save the html content of the page in the variable page_html
        page_html = get_page_content("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri")

    except Exception as e:
        page_html = ""

    try:
        

        with open(save_path, "w", encoding=ENCODING) as f:
            f.write(page_html)

    except Exception as e:
        with open(save_path, "w", encoding=ENCODING) as f:
            f.write("")
        print("Error saving page {page_id} html:" + str(e))


if __name__ == "__main__":
    save_html_pages()
