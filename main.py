import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
productNameList, priceList = [], []

for pageNum in range(4):
    url = "https://www.x-kom.pl/g-4/c/1590-smartfony-i-telefony.html?page="+str(pageNum)
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")

    productNameList = productNameList + [x.text for x in doc.find_all("h3", {"class": "sc-16zrtke-0 kGLNun sc-1yu46qn-9 feSnpB"})]
    priceList = priceList + [x.text for x in doc.find_all("span", {"class": "sc-6n68ef-0 sc-6n68ef-3 guFePW"})]

df = pd.DataFrame({'titles' : productNameList,  'prices': priceList})
df.to_csv('smartphones_x_kom_'+str(date.today().strftime("%d_%m_%Y"))+'.csv', index=True, encoding='utf-8-sig')