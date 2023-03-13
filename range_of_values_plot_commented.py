import os
import csv
import matplotlib.pyplot as plt
# Nie wiem czy pojęcia "column" i "row" nie byłyby bardziej logiczne gdyby je zamienić miejscami... nie będę już zmieniał
with open(os.path.join(os.path.dirname(__file__), "smartfony.csv"), "r") as f: # Otwieramy plik z danymi (ścieżka jest zawsze automatycznie ustawiona na taką samą jak ten plik z kodem)
    columns = csv.reader(f, delimiter = ",") # Wczytujemy dane z pliku
    class product: # Tworzymy klasę do łatwego przechowywania danych produktów (data/nazwa/cena)
        def __init__(self, date, name, price):
            self.date = date
            self.name = name
            self.price = price

    products, unique_names = [], [] # Tworzymy listę produktów do przechowywania obiektów wcześniej utworzonej klasy, listę unikalnych nazw produktów (bez powtórzeń)
    for row in columns:
        formated_price = float(row[2].strip("złod").replace(" ", "").replace(",", ".")) # Formatujemy ceny tak aby przekształcić je na float'a (na mojej stronie były ceny z groszami więc dlatego float zamiast int'a)
        products.append(product(row[0], row[1], formated_price)) # Tworzymy każdemu produktowi obiekt wcześniej utworzonej klasy i dodajemy go do listy produktów
        if row[1] not in unique_names: # Jeżeli nazwa produktu jeszcze się nie pojawiła to dodajemy ją do listy unikalnych nazw
            unique_names.append(row[1])

    print("Lista produktów:") # Wypisujemy wszystkie nazwy produktów dla użytkownika żeby miał co wybrać do wykresu
    unique_names.sort()
    for element in unique_names:
        print(element)

    plt.figure("Wykres cen smartfonów") # Ustawiamy nazwę okna z wykresem
    chosen_product = " " # Tworzymy zmienną w której będziemy przechowywać ostatnio wybrany przez użytkownika produkt i ustawiamy ją na cokolwiek, żeby nie była pusta, bo inaczej nie wywoła się pętla while
    already_chosen = [] # Tworzymy listę wszystkich wybranych przez użytkownika produktów w celu walidacji danych
    while chosen_product != "": # Pętla wywołuje się, dopóki użytkownik nie wciśnie [Enter] przy prośbie podania nazwy produktu
        chosen_product = input("\nPodaj nazwę produktu, który chcesz dodać do wykresu lub naciśnij [Enter] aby wyświetlić wykres: ")
        if chosen_product in unique_names and chosen_product not in already_chosen: # Walidacja danych (czy produkt o podanej nazwie istnieje i czy nie był już wybrany)
            already_chosen.append(chosen_product)
            dates, prices = [], []
            for i in range(len(products)):
                if products[i].name == chosen_product: # Tworzymy punkty na wykresie podając listy ich współrzędnych x (daty) i y (ceny)
                    dates.append(products[i].date)
                    prices.append(products[i].price)
            plt.plot(dates, prices, marker = "o", label = chosen_product) # Tworzymy wykres dat i cen podanego produktu
        elif chosen_product in already_chosen: # Walidacja danych
            print("Już podano tą nazwę produktu. Spróbuj ponownie!")
        elif chosen_product == "" and not already_chosen: # Walidacja danych
            print("Musisz podać conajmniej jedną nazwę produktu. Spróbuj ponownie!")
            chosen_product = " "
        elif chosen_product == "": # Wyświetlenie wykresu po naciśnięciu [Enter], czyli po zakończeniu podawania nazw produktów
            plt.xlabel("data")
            plt.ylabel("cena [zł]")
            plt.legend(loc = "upper center", bbox_to_anchor = (0.5, 1.2)) # Ustawiamy legendę poza wykresem
            plt.tight_layout() # Ustawiamy legendę poza wykresem
            plt.show()
        else: # Walidacja danych
            print("Podano nieprawidłową nazwę produktu. Spróbuj ponownie!")