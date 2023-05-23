from requests import get
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import time
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

producers= []
models = []
sizes = []
prices = []
classes = []
dates = []
seasons = []

link = []


p = 0
num_page = 1

df = pd.DataFrame(columns=['Producent', 'Model', 'Cena', 'Rok produkcji', 'Klasa', 'Sezon', 'Rozmiar', 'Data scrapowania'])

#Opony letnie 205/55 R16 wszystkie klasy
while p <= 700:


    URL = 'https://www.sklepopon.com/szukaj-opony?sezon=letnie&rozmiar=205/55R16&ofs='+str(p)  
    page = get(URL, headers=headers)
    print(page.status_code)
    bs = BeautifulSoup(page.content, 'html.parser')

    if(page.status_code == 200):

        for div in bs.find_all('div', class_='w-full flex js-clickable-link'):
            data_url = div['data-url']
            
            #bezpośrednia strona produktu
            URL_2 = 'https://www.sklepopon.com'+data_url
            page_2 = get(URL_2)
            print(URL_2)
            bs_2 = BeautifulSoup(page_2.content, 'html.parser')
            #time.sleep(2)
            
        
            #producent   
            producer = bs_2.find('h1', class_='w-full')
            spans = producer.find_all('span')
            values = []
            for span in spans:
                values.append(span.get_text().strip())
            print(values[0])
            producer = values[0]
            
            #model
            model = bs_2.find('span', class_='font-normal')
            model = model.get_text().strip()
            print(model)

            #price
            price = bs_2.find('span', class_='lg:text-p0d text-p0m md:text-p1m md:pr-0 pr-1')
            price = price.get_text().strip()
            fraction = bs_2.find('span', class_='font-extraBold xl:text-p3d xl:pr-2 text-p3m')
            fraction = fraction.get_text().strip()
            price = price + fraction
            print(price)

            #rok produkcji
            year_production_elem = bs_2.find('span', class_='hidden lg:block')

            
            numbers_only_regex = re.compile(r'\d+')
            numbers_only = numbers_only_regex.findall(year_production_elem.get_text().strip())
            if numbers_only:
                year_production = numbers_only[0]
            else:
                year_production = 'None'

            print(year_production)

            #klasa
            container = bs_2.find('div', class_='w-full md:w-1/2 mt-3 md:mt-0')
            
            words_to_find = ['Klasa Premium','Klasa Średnia']
            regex_pattern = '|'.join(words_to_find)
            match = re.search(regex_pattern, container.get_text().strip())

            if match:
                quality = match.group()
            else:
                quality = 'Klasa Ekonomiczna'

            print(quality)

            #sezon
            season = 'letnie'
            print(season)
            

            #size
            size = '205/55 R16'
            

            # dd/mm/YY
            today = datetime.date.today()
            day_scrap = today.strftime("%Y.%m.%d")

            new_row = {'Producent': producer, 'Model': model, 'Cena': price, 'Rok produkcji': year_production, 
               'Klasa': quality, 'Sezon': season, 'Rozmiar': size, 'Data scrapowania': day_scrap}
            df = df.append(new_row, ignore_index=True)

            


        p = p + 20
        num_page = num_page + 1
        print('================================================================================================')
        print(f'strona: {num_page}')
        print('================================================================================================')

    else:
        print("FINISH")
        break


p = 0
num_page = 1

#Opony zimowe 205/55 R16 wszystkie klasy
while p <= 700:


    URL = 'https://www.sklepopon.com/szukaj-opony?sezon=zimowe&rozmiar=205/55R16&ofs='+str(p)  
    page = get(URL, headers=headers)
    print(page.status_code)
    bs = BeautifulSoup(page.content, 'html.parser')

    if(page.status_code == 200):

        for div in bs.find_all('div', class_='w-full flex js-clickable-link'):
            data_url = div['data-url']
            
            #bezpośrednia strona produktu
            URL_2 = 'https://www.sklepopon.com'+data_url
            page_2 = get(URL_2)
            print(URL_2)
            bs_2 = BeautifulSoup(page_2.content, 'html.parser')
            #time.sleep(2)
            
        
            #producent   
            producer = bs_2.find('h1', class_='w-full')
            spans = producer.find_all('span')
            values = []
            for span in spans:
                values.append(span.get_text().strip())
            print(values[0])
            producer = values[0]
            
            #model
            model = bs_2.find('span', class_='font-normal')
            model = model.get_text().strip()
            print(model)

            #price
            price = bs_2.find('span', class_='lg:text-p0d text-p0m md:text-p1m md:pr-0 pr-1')
            price = price.get_text().strip()
            fraction = bs_2.find('span', class_='font-extraBold xl:text-p3d xl:pr-2 text-p3m')
            fraction = fraction.get_text().strip()
            price = price + fraction
            #price = float(price)
            print(price)

            #rok produkcji
            year_production_elem = bs_2.find('span', class_='hidden lg:block')

            
            numbers_only_regex = re.compile(r'\d+')
            numbers_only = numbers_only_regex.findall(year_production_elem.get_text().strip())
            if numbers_only:
                year_production = numbers_only[0]
            else:
                year_production = 'None'

            print(year_production)

            #klasa
            container = bs_2.find('div', class_='w-full md:w-1/2 mt-3 md:mt-0')
            
            words_to_find = ['Klasa Premium','Klasa Średnia']
            regex_pattern = '|'.join(words_to_find)
            match = re.search(regex_pattern, container.get_text().strip())

            if match:
                quality = match.group()
            else:
                quality = 'Klasa Ekonomiczna'

            print(quality)

            #sezon
            season = 'zimowe'
            print(season)
            

            #size
            size = '205/55 R16'
            

            # dd/mm/YY
            today = datetime.date.today()
            day_scrap = today.strftime("%Y.%m.%d")

            new_row = {'Producent': producer, 'Model': model, 'Cena': price, 'Rok produkcji': year_production, 
               'Klasa': quality, 'Sezon': season, 'Rozmiar': size, 'Data scrapowania': day_scrap}
            df = df.append(new_row, ignore_index=True)

            


        p = p + 20
        num_page = num_page + 1
        print('================================================================================================')
        print(f'strona: {num_page}')
        print('================================================================================================')

    else:
        print("FINISH")
        break



p = 0
num_page = 1

#Opony wielosezonowe 205/55 R16 wszystkie klasy
while p <= 700:


    URL = 'https://www.sklepopon.com/szukaj-opony?sezon=całoroczne&rozmiar=205/55R16&ofs='+str(p)  
    page = get(URL, headers=headers)
    print(page.status_code)
    bs = BeautifulSoup(page.content, 'html.parser')

    if(page.status_code == 200):

        for div in bs.find_all('div', class_='w-full flex js-clickable-link'):
            data_url = div['data-url']
            
            #bezpośrednia strona produktu
            URL_2 = 'https://www.sklepopon.com'+data_url
            page_2 = get(URL_2)
            print(URL_2)
            bs_2 = BeautifulSoup(page_2.content, 'html.parser')
            #time.sleep(2)
            
        
            #producent   
            producer = bs_2.find('h1', class_='w-full')
            spans = producer.find_all('span')
            values = []
            for span in spans:
                values.append(span.get_text().strip())
            print(values[0])
            producer = values[0]
            
            #model
            model = bs_2.find('span', class_='font-normal')
            model = model.get_text().strip()
            print(model)

            #price
            price = bs_2.find('span', class_='lg:text-p0d text-p0m md:text-p1m md:pr-0 pr-1')
            price = price.get_text().strip()
            fraction = bs_2.find('span', class_='font-extraBold xl:text-p3d xl:pr-2 text-p3m')
            fraction = fraction.get_text().strip()
            price = price + fraction
            print(price)

            #rok produkcji
            year_production_elem = bs_2.find('span', class_='hidden lg:block')

            
            numbers_only_regex = re.compile(r'\d+')
            numbers_only = numbers_only_regex.findall(year_production_elem.get_text().strip())
            if numbers_only:
                year_production = numbers_only[0]
            else:
                year_production = 'None'

            print(year_production)

            #klasa
            container = bs_2.find('div', class_='w-full md:w-1/2 mt-3 md:mt-0')
            
            words_to_find = ['Klasa Premium','Klasa Średnia']
            regex_pattern = '|'.join(words_to_find)
            match = re.search(regex_pattern, container.get_text().strip())

            if match:
                quality = match.group()
            else:
                quality = 'Klasa Ekonomiczna'

            print(quality)

            #sezon
            season = 'wielosezonowe'
            print(season)
            

            #size
            size = '205/55 R16'
            

            # dd/mm/YY
            today = datetime.date.today()
            day_scrap = today.strftime("%Y.%m.%d")

            new_row = {'Producent': producer, 'Model': model, 'Cena': price, 'Rok produkcji': year_production, 
               'Klasa': quality, 'Sezon': season, 'Rozmiar': size, 'Data scrapowania': day_scrap}
            df = df.append(new_row, ignore_index=True)

            


        p = p + 20
        num_page = num_page + 1
        print('================================================================================================')
        print(f'strona: {num_page}')
        print('================================================================================================')

    else:
        print("FINISH")
        break



print(df.head())
current_date = datetime.date.today().strftime('%d_%m_%Y')
file_name = f'opony_sklepopon_{current_date}.csv'
df.to_csv(file_name, index=True, encoding='utf-8-sig')