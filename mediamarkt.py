from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
import pandas as pd
import os.path


driver = webdriver.Chrome(ChromeDriverManager().install())

links = {
          'https://mediamarkt.pl/komputery-i-tablety/laptopy-laptopy-2-w-1/notebooki': 'laptops.csv',
          'https://mediamarkt.pl/telefony-i-smartfony/smartfony/wszystkie-smartfony': 'smartphones.csv',
          'https://mediamarkt.pl/komputery-i-tablety/monitory-led/wszystkie-monitory': 'monitors.csv',
          'https://mediamarkt.pl/komputery-i-tablety/tablety-multimedialne/tablety': 'tablets.csv',
          'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639': 'HDD_external.csv',
          'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/dyski-ssd': 'SSD_internal.csv'

        }


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--charset=UTF-8')
driver = webdriver.Chrome(options=options)

for link, filename in links.items():
        time.sleep(10)
        driver.get(link)
        time.sleep(1)
        if link == 'https://mediamarkt.pl/komputery-i-tablety/laptopy-laptopy-2-w-1/notebooki':
                driver.find_element(By.XPATH, "//i[contains(@class, 'icon close-icon icon-close')]").click()
        
        
        cos = True
        cos1 = True
        while cos == True:
                try:
                        element = driver.find_element(By.XPATH, "//a[contains(@class, 'spark-button button is-primary is-default icon-left')]")
                        desired_y = (element.size['height'] / 2) + element.location['y']
                        window_h = driver.execute_script('return window.innerHeight')
                        window_y = driver.execute_script('return window.pageYOffset')
                        current_y = (window_h / 2) + window_y
                        scroll_y_by = desired_y - current_y

                        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
                        time.sleep(2)
                        driver.find_element(By.XPATH, "//a[contains(@class, 'spark-button button is-primary is-default icon-left')]").click()
                        if cos1 == False:
                                break
                except:
                        driver.execute_script("arguments[0].scrollIntoView();", element)
                        if cos1 == False:
                                break
                page = driver.find_elements(By.XPATH, "//p[contains(@class, 'info')]")
                page = str(page[0].text)
                count = page.split(" ")
                all = float(count[3])
                notall = float(count[1])
                time.sleep(6)
                print(notall)
                print(all)
                # if all - notall < 830:
                #         break
                if all - notall < 40:
                        cos1 = False

      
        producent = []        
        laptop = driver.find_elements(By.XPATH, "//h2[contains(@class, 'title')]")
        for i in range(len(laptop)):
                producent.append(laptop[i])
        
        
        if link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639' or link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/dyski-ssd':
                for i in range(len(producent)):
                        element = producent[i]
                        text = element.get_attribute('textContent')  # Pobierz tekst z obiektu WebElement
                        print(text)
                        if 'Laptop/Tablet 2w1' not in text and not (link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639' and ('HDD'  in text or 'gry' in text)):
                                words = text.split()
                                producent[i] = ' '.join(words[2:3])
                        elif 'Laptop/Tablet 2w1' in text:
                                producent[i] = text.split('2w1')[1].split()[0]
                        elif link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639' and 'gry' in text:
                                words = text.split()
                                producent[i] = ' '.join(words[3:4])
                        elif link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639' and 'LA CIE' in text:
                                words = text.split()
                                producent[i] = ' '.join(words[3:5])
                        elif link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639' and 'HDD' in text and ('zewnętrzny' in text or 'Zewnętrzny' in text):
                                words = text.split()
                                producent[i] = ' '.join(words[3:4])
                        elif link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639' and ('HDD' in text and 'zewnętrzny' not in text):
                                words = text.split()
                                producent[i] = ' '.join(words[2:3])
                        else:
                                words = text.split()
                                producent[i] = ' '.join(words[1:2])
        else:
                producent = [element.text.split()[1] if 'Laptop/Tablet 2w1' not in element.text else element.text.split('2w1')[1].split()[0] for element in laptop]
    
        print(producent)

        
        model = []
        ciag_znakow = "/" 
        for element in laptop:
                words = element.text.split()
                # print(f"słówka: {words}")
                if len(words) > 1:
                        if '2w1' in words:
                                start_index = 3
                                end_index = next((i for i, word in enumerate(words[1:]) if ciag_znakow in word), len(words))
                                fragment = ' '.join(words[start_index:end_index])
                                model.append(fragment)
                        elif link == 'https://mediamarkt.pl/komputery-i-tablety/monitory-led/wszystkie-monitory':
                                start_index = 2
                                end_index = 4
                                fragment = ' '.join(words[start_index:end_index])
                                model.append(fragment)
                        
                        elif link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639':
                                start_index = 3
                                end_index = next((i for i, word in enumerate(words) if ciag_znakow in word), len(words))
                                fragment = ' '.join(words[start_index:end_index])
                                
                                words_to_remove = ['TOSHIBA', 'SEAGATE', 'WD_BLACK', 'LA CIE', 'WD']
                                for word in words_to_remove:
                                        if word in fragment:
                                                fragment = fragment.replace(word, '')
                                
                                model.append(fragment.strip())  # Usuń spacje z początku i końca fragmentu
                        else:
                                start_index = 2
                                end_index = next((i for i, word in enumerate(words[1:]) if ciag_znakow in word), len(words))
                                fragment = ' '.join(words[start_index:end_index])
                                model.append(fragment)

                        



        print(model)
        print(len(model))



        prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'main-price is-big')]//span[contains(@class, 'whole')]")
        
        
        prices1 = []
        
        for i in range(len(prices)):
                prices1.append(prices[i].text)
        print(prices1)
        prices1 = [x for x in prices1 if x != '']


        list_elements = driver.find_elements(By.CSS_SELECTOR, "div.product-attributes ul.list")

        
        def create_dict_from_list(list_element):
                dictionary = {}
                items = list_element.find_elements(By.CSS_SELECTOR, "li.attribute")
                for item in items:
                        try:
                                label_element = item.find_element(By.CSS_SELECTOR, "span.product-attribute-label")
                                value_element = item.find_element(By.CSS_SELECTOR, "span.product-attribute-value")
                                label = label_element.text.strip()
                                value = value_element.text.strip()
                                dictionary[label] = value
                        except:
                                continue
                return dictionary

        dictionaries = []
        for list_element in list_elements:
                dictionary = create_dict_from_list(list_element)
                dictionaries.append(dictionary)

        df2 = pd.DataFrame(dictionaries)
        print(df2)

        if link == 'https://mediamarkt.pl/komputery-i-tablety/laptopy-laptopy-2-w-1/notebooki':
                df2 = df2[["Wyświetlacz:", "Procesor:", "Pamięć RAM:", "Grafika:"]]
                df2["Wyświetlacz:"] = df2["Wyświetlacz:"].str.split('(').str[0].str.strip()

                print(df2)
                columns = ["Sklep", "Nazwa", "Model", "Cena", "Data", "Ekran (przekątna)", "Procesor", "Pamięć RAM", "Dedykowany układ graficzny"]
        elif link == 'https://mediamarkt.pl/telefony-i-smartfony/smartfony/wszystkie-smartfony':
                columns = ["Sklep", "Nazwa", "Model", "Cena", "Data", "Ekran", "Procesor", "Pamięć RAM", "Pamięć wbudowana"]
                df2 = df2[['Wyświetlacz:', 'Model procesora:', 'Pamięć RAM:', 'Pamięć wbudowana:']]
        elif link == 'https://mediamarkt.pl/komputery-i-tablety/monitory-led/wszystkie-monitory':
                columns = ["Sklep", "Nazwa", "Model", "Cena", "Data", "Złącza", "Czas reakcji", "Przekątna", "Rozdzielczość", "Matryca"]
                df2 = df2[['Podstawowe złącza:', 'Ekran:', 'Czas reakcji [ms]:']]
                df2[['Przekątna', 'Rozdzielczość', 'Matryca']] = df2['Ekran:'].str.extract(r'(.*?") \((.*?)\), (.*?)\)')
                df2['Rozdzielczość'] = df2['Rozdzielczość'].str.strip('(')
                df2['Rozdzielczość'] = df2['Rozdzielczość'].apply(lambda x: x + ')')
                df2['Matryca'] = df2['Matryca'].str.rstrip(')')
                df2 = df2.drop('Ekran:', axis=1)

        elif link == 'https://mediamarkt.pl/komputery-i-tablety/tablety-multimedialne/tablety':
                columns = ["Sklep", "Nazwa", "Model", "Cena", "Data", "Procesor", "Pamięć RAM", "System operacyjny", "Przekątna", "Rozdzielczość", "Matryca"]
                df2 = df2[['Model procesora:', 'Pamięć RAM:', 'Wyświetlacz:', 'System operacyjny:']]
                df2['Wyświetlacz:'] = df2['Wyświetlacz:'].astype(str)
                df2[['Przekątna', 'Rozdzielczość', 'Matryca']] = df2['Wyświetlacz:'].str.extract(r'^(.*?") \((.*?), (.*?)\)$')
                df2 = df2.drop('Wyświetlacz:', axis=1)

                


        elif link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/akcesoria-do-laptopow/dyski-twarde-zewnetrzne./rodzaj-dysku=hdd?priceFilter%5Bmin%5D=0&priceFilter%5Bmax%5D=3639':
                columns = ["Sklep", "Nazwa", "Model", "Cena", "Data", "Pojemność", "Typ podłączenia", "Format"]
                df2 = df2[['Pojemność dysku:', 'Interfejs:', 'Format dysku:']]
        elif link == 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/dyski-ssd':
                columns = ["Sklep", "Nazwa", "Model", "Cena", "Data", "Pojemność", "Format", "Typ podłączenia", "MaksPredkoscOdczytu", "Maks prędkość zapisu"]
                df2 = df2[['Pojemność dysku:', 'Format dysku:', 'Interfejs:', 'Szybkość odczytu [MB/s]:', 'Szybkość zapisu [MB/s]:']]


        date = datetime.datetime.now()
        element_list = []
        at = []
        for i in range(len(prices1)):
                element_list.append(["MediaMarkt", producent[i], model[i], prices1[i], date.strftime("%Y.%m.%d")])

        df1_2 = pd.DataFrame(element_list)
        print(f'ramka pzred połączeniem: {df1_2}')
        
        if len(df1_2) == len(df2):
                df = pd.concat([df1_2, df2], axis=1)
                df.columns = columns
        else:
                print("Liczba wierszy w obu ramkach danych jest różna.")
        print(df)
        
        if not os.path.isfile(filename):
                with open(filename, mode='a', newline='', encoding='utf-8') as file:
                        df.to_csv(file, index=False, header=True, sep=';')     
        else:
                with open(filename, mode='a', newline='', encoding='utf-8') as file:
                        df.to_csv(file, index=False, header=False, sep=';')            


driver.quit()