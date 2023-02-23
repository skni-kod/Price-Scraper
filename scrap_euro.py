from bs4 import BeautifulSoup
import requests
import unicodedata
from csv import writer
from datetime import datetime


scrappedData1 = []
scrappedData = []

def remove_unicode(s):
    return unicodedata.normalize("NFKD", s).strip()

with open('housing.csv', 'a', encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price', 'Date']
    thewriter.writerow(header)


    for i in range(1,4):
        if i == 1:
            url = "https://www.euro.com.pl/laptopy-i-netbooki.bhtml"
        else:
            url = f"https://www.euro.com.pl/laptopy-i-netbooki,strona-{i}.bhtml"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('div', class_="product-row")
        # print(len(lists))


        for list in lists:

            title = list.find('h2', class_="product-name")
            # ifs prevent "out of index error" and "trying to access index of None"
            if title and title.contents[1] and title.contents[1].contents[0]:
                title = remove_unicode(title.contents[1].contents[0])
            else:
                print("no title", title)
            title1 = title.replace('"','')

            price = list.find('div', class_="price-normal")
            if price and price.contents[0]:
                price = remove_unicode(price.contents[0])
            else:
                print("no price")
            price1 = price

            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            date1 = date
            info = [title1, price1, date1]

            thewriter.writerow(info)
            # scrappedData.append(info)

        # scrappedData1.append(scrappedData)

