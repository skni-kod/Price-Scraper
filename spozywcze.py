import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.dlahandlu.pl/koszyk/wybrany_sklep/zabka-warszawa,173.html'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table')

#Nagłówki tabeli
headers = []
for cell in table.find('tr').find_all('th'):
  divs = cell.find_all('div', class_=['basket-table-compare-shop-price', 'basket-table-compare-shop-basket', 'basket-table-compare-shop-text-strong'])
  if divs:
    headers.append(' '.join([div.text for div in divs]))
  else:
    headers.append(cell.text)

#Nazwy produktów
divs = soup.find_all('div', class_='basket-table-compare-product')
names = []
for div in divs:
  name = div.find('span')
  if name:
    names.append(name)
texts_names = [name.text for name in names]


# dane
data = []
for row in table.find_all('tr')[1:]:
  row_data = []

  for cell in row.find_all('td'):
    row_data.append(cell.text)
    
  data.append(row_data)


del headers[0]
print(headers)
print(texts_names)
print(data)

#Tworzenie ramki danych
df = pd.DataFrame(data, columns=headers)
df.insert(0, 'Produkty', texts_names)

#Zapis do pliku Excela
df.to_excel('koszyk.xlsx', index=False)