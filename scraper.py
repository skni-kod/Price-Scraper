import os
import requests
from datetime import date
from bs4 import BeautifulSoup

# Dla pierwszych pięciu stron ze smartfonami
for i in range(1, 6):

  # Pobieramy stronę z listą smartfonów
  url = "https://www.morele.net/kategoria/smartfony-280/,,,,,,,,0,,,,/" + str(i) + "/"
  page = requests.get(url)

  # Tworzymy obiekt BeautifulSoup z otrzymanego kodu HTML
  soup = BeautifulSoup(page.content, "html.parser")

  # Szukamy wszystkich elementów z nazwami i cenami smartfonów
  phone_elements = soup.find_all(class_="cat-product-name__header")
  price_elements = soup.find_all(class_="price-new")

  # Otwieramy plik tekstowy do zapisu
  with open(os.path.join(os.path.dirname(__file__), "smartfony.txt"), "a") as file:
    # Dla każdego elementu z nazwą i ceną
    for a, b in zip(phone_elements, price_elements):
      # Pobieramy nazwę i cenę
      name = a.text.strip()
      price = b.text.strip()
      # Zapisujemy je w pliku
      file.write(str(date.today()) + " " + name + " " + price + "\n")

print("Nazwy i ceny zostały pobrane i zapisane w pliku smartfony.txt")