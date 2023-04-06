import requests
from bs4 import BeautifulSoup
import csv

# URL strony z danymi giełdowymi
url = 'https://www.biznesradar.pl/gielda/indeks:WIG20'

# Pobieranie strony internetowej
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Wyodrębnienie tabeli z danymi giełdowymi
table = soup.find('table', class_='qTableFull')

# Pobranie wierszy z danymi giełdowymi
rows = table.find_all('tr')

# Otwarcie pliku CSV do zapisu
with open('gpw.csv', 'w', newline='') as csvfile:
    # Utworzenie obiektu writer do zapisu danych do pliku CSV
    writer = csv.writer(csvfile)

    # Zapisanie nagłówków kolumn
    writer.writerow(['Nazwa', 'Cena', 'Zmiana %','Wolumen'])

    # Pętla po wierszach tabeli
    for row in rows:
        # Pobranie kolumn z nazwą spółki, ceną i zmianą procentową
        columns = row.find_all('td')
        if len(columns) == 0:  # pomijamy wiersze bez kolumn
            continue
        name = columns[0].text.strip()
        price = columns[2].text.strip()
        change = columns[4].text.strip()
        volume = columns[9].text.strip()

        # Zapisanie danych do pliku CSV
        writer.writerow([name, price, change,volume])
