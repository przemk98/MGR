import requests
from bs4 import BeautifulSoup
import csv

# URL bazowy dla danych historycznych
url_base = 'https://www.biznesradar.pl/notowania-historyczne/'

# Lista nazw firm
companies = ['ASSECO-POLAND', 'ALE', 'CCC', 'CD-PROJEKT', 'CYFROWY-POLSAT', 'DNP', 'JSW-JASTRZEBSKA-SPOLKA-WEGLOWA', 'KGHM', 'KRUK', 'KETY', 'LPP',
             'MBANK', 'ORANGE', 'PCO', 'PEKAO','PGE','PKN-ORLEN','PKO','PZU','SPL']

# Pętla po nazwach firm
for company in companies:
    strona = 1
    # URL strony z danymi historycznymi dla danej firmy
    url = url_base + company + "," + str(strona)
    # Pobieranie strony internetowej
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Wyodrębnienie tabeli z danymi historycznymi
    table = soup.find('table')

    # Pobranie wierszy z danymi historycznymi
    rows = table.find_all('tr')

    # Otwarcie pliku CSV do zapisu
    with open(company + '.csv', 'w', newline='') as csvfile:
        # Utworzenie obiektu writer do zapisu danych do pliku CSV
        writer = csv.writer(csvfile)

        # Zapisanie nagłówków kolumn
        writer.writerow(['Data', 'Otwarcie', 'Najwyzszy', 'Najnizszy', 'Zamkniecie', 'Wolumen', 'Zmiana %'])

        # Pętla po wierszach tabeli (pomiń pierwszy wiersz z nagłówkami kolumn)
        for i in range(6):
            for row in rows[1:]:
                # Pobranie kolumn z danymi historycznymi
                columns = row.find_all('td')
                if len(columns) == 0:  # pomijamy wiersze bez kolumn
                    continue
                date = columns[0].text.strip()
                open_price = columns[1].text.strip()
                high = columns[2].text.strip()
                low = columns[3].text.strip()
                close = columns[4].text.strip()
                volume = str.replace(columns[5].text.strip(),' ','')
                change = round((float(open_price)/float(close) *100 -100),2)

                # Zapisanie danych do pliku CSV
                writer.writerow([date, open_price, high, low, close, volume, change])
            strona += 1