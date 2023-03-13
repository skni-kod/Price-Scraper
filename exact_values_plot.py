import os
import csv
import matplotlib.pyplot as plt

with open(os.path.join(os.path.dirname(__file__), "smartfony.csv"), "r") as f:
    columns = csv.reader(f, delimiter = ",")
    class product:
        def __init__(self, date, name, price):
            self.date = date
            self.name = name
            self.price = price

    products, unique_names, unique_prices = [], [], []
    for row in columns:
        formated_price = float(row[2].strip("złod").replace(" ", "").replace(",", "."))
        products.append(product(row[0], row[1], formated_price))
        if row[1] not in unique_names:
            unique_names.append(row[1])

    print("Lista produktów:")
    unique_names.sort()
    for element in unique_names:
        print(element)

    plt.figure("Wykres cen smartfonów")
    chosen_product = " "
    already_chosen = []
    while chosen_product != "":
        chosen_product = input("\nPodaj nazwę produktu, który chcesz dodać do wykresu lub naciśnij [Enter] aby wyświetlić wykres: ")
        if chosen_product in unique_names and chosen_product not in already_chosen:
            already_chosen.append(chosen_product)
            dates, prices = [], []
            for i in range(len(products)):
                if products[i].name == chosen_product:
                    dates.append(products[i].date)
                    prices.append(products[i].price)
                    if products[i].price not in unique_prices:
                        unique_prices.append(products[i].price)
            plt.plot(dates, prices, marker = "o", label = chosen_product)
        elif chosen_product in already_chosen:
            print("Już podano tą nazwę produktu. Spróbuj ponownie!")
        elif chosen_product == "" and not already_chosen:
            print("Musisz podać conajmniej jedną nazwę produktu. Spróbuj ponownie!")
            chosen_product = " "
        elif chosen_product == "":
            plt.yticks(unique_prices)
            plt.xlabel("data")
            plt.ylabel("cena [zł]")
            plt.legend(loc = "upper center", bbox_to_anchor = (0.5, 1.2))
            plt.tight_layout()
            plt.show()
        else:
            print("Podano nieprawidłową nazwę produktu. Spróbuj ponownie!")