import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os
from time import sleep
from random import randint
import numpy as np

headers = dict()
headers[
    "User-Agent"
] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"


def data_table():
  newurl = 'https://www.worldometers.info/coronavirus/'
  resp = requests.get(newurl, headers = headers) # send a get request to the url, get response
  soup = BeautifulSoup(resp.text, 'html5lib') # Yummy HTML soup
  table = soup.find('table', {"class": "main_table_countries"}) # get the table from html
  trs = table.findAll('tr') # extract all rows of the table
  if len(trs[1:])!=0:
    csv_filename = 'Corona Virus.csv'
    if os.path.exists(csv_filename): os.remove(csv_filename) # remove the file it already exists, can result in data duplicacy
    with open(csv_filename, 'a') as f:
      writer = csv.writer(f)
      columns = [th.text for th in trs[0].findChildren('th')]					
      writer.writerow(columns)
      for tr in trs[1:]:
        row = []
        tds = tr.findChildren('td')
        for td in tds:
          span = td.findChildren('span', {'id':'Regular_season'})
          if span:
            row.append(span[0].text.strip())
          else:
            row.append(td.text.strip())
        assert len(row) == len(columns)
        writer.writerow(row)
data_table()
