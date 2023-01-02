from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
import pandas as pd
import openpyxl

element_list = []
driver = webdriver.Chrome(ChromeDriverManager().install())

for page in range(1,4,1):
    page_url = 'https://www.neonet.pl/komputery/laptopy.html?p=' + str(page)
    
    driver.get(page_url)
    
    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    names = driver.find_elements(By.XPATH, "//a[contains(@class,'listingItemCss-nameLink-1rv')]")
    prices = driver.find_elements(By.XPATH, "//span[contains(@class,'uiPriceScss-integer-38D')] | //div[contains(@class,'listingItemCss-sp__integer-3NZ')]")
    
    date = datetime.datetime.now()

    
    for i in range(len(names)):
        element_list.append([names[i].text, prices[i].text,date.strftime("%d.%m.%Y")])

    for laptop in names:
        print(laptop.text)


    print("*"*50)

    for price in prices:
        print(price.text)


df = pd.DataFrame(element_list)

workbook = openpyxl.load_workbook('result.xlsx')
worksheet = workbook.active
last_row = worksheet.max_row
for _, row in df.iterrows():
    worksheet.append(row.tolist())
workbook.save('result.xlsx')


driver.quit()