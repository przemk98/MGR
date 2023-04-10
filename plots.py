import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# wczytanie danych z pliku CSV do obiektu DataFrame
data = pd.read_csv('CCC.csv', parse_dates=['Data'],dayfirst=True)

# przygotowanie danych do wykresu świecowego
ohlc = data[['Data', 'Otwarcie', 'Najwyzszy', 'Najnizszy', 'Zamkniecie']]
ohlc['Data'] = pd.to_datetime(ohlc['Data'])
ohlc['Data'] = ohlc['Data'].apply(mdates.date2num)
ohlc = ohlc.astype(float).values.tolist()

# generowanie wykresu świecowego
fig, ax = plt.subplots()
candlestick_ohlc(ax, ohlc, width=0.7, colorup='green', colordown='red')

# dodanie podpisów osi i tytułu
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%y'))
ax.set_xlabel('Data')
ax.set_ylabel('Cena')
ax.set_title('Wykres')

# wyświetlenie wykresu
plt.savefig("wykres.png", dpi=300)
