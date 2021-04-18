import requests
from bs4 import BeautifulSoup
import pandas as pd
def table_data():
    newurl = 'https://www.worldometers.info/coronavirus/'
    resp = requests.get(newurl) # send a get request to the url, get response
    soup = BeautifulSoup(resp.text, 'html5lib') # Yummy HTML soup
    table = soup.find('table', {"class": "main_table_countries"}) # get the table from html

    data_col = pd.DataFrame(columns=['Country', 'Total Cases',	'New Cases',	'Total Deaths', 'New Deaths'])

    for row in table.tbody.find_all("tr"):
        col = row.find_all("td")
        if (col != []):
            Country = col[1].text.strip()
            Total_Cases = col[2].text.strip()
            New_Cases = col[3].text.strip()
            Total_Deaths = col[4].text.strip()
            New_Deaths = col[5].text.strip()
            data_col = data_col.append({"Country":Country, "Total Cases":Total_Cases, 
                                        "New Casses":New_Cases, "Total Deaths":Total_Deaths, 
                                        "New Deaths":New_Deaths}, ignore_index=True)
    data_col.to_csv('Corona Data.csv', index = False)
    print(data_col.head())
table_data()
