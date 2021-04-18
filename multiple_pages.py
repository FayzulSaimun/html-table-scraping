import pandas as pd
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep  
import concurrent.futures
from multiprocessing.dummy import Pool as ThreadPool
from csv import reader

base_url = "https://web.pgcb.gov.bd/view_generations_bn?page="

all_urls = []
ress =[]
Date = []
Time = []
Produced = []
Demand = []
Depriciation = []

def generate_urls():
  for i in range(1,50):
    all_urls.append(base_url + str(i))
    #time.sleep(0.15)
generate_urls()
def scrape(url):
  #for url in all_urls:
  sleep(randint(1,3))
  result = requests.get(url)
  sleep(randint(1,7))
  soup = BeautifulSoup(result.content, 'html.parser')
  tab = soup.find_all('table', class_ = 'table table-bordered')
  sleep(randint(1,3))
  for tabi in tab:
    for row in tabi.tbody.find_all("tr"):
      col = row.find_all("td")
      if (col != []):
        date = col[0].text
        time = col[1].text
        produced = col[2].text.strip()
        demand = col[3].text.strip()
        depriciation = col[4].text.strip()

        Date.append(date)
        Time.append(time)
        Produced.append(produced)
        Demand.append(demand)
        Depriciation.append(depriciation)

  data_df = pd.DataFrame({"Date":Date, "Time":Time, "Produced":Produced, "Demand":Demand, "Depriciation":Depriciation})  
  data_df.to_csv('Data Multiple Page.csv', index = False)
  print('Completed:', url)

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
  executor.map(scrape, all_urls)
