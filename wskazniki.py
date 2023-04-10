import pandas as pd
import talib

# Wczytanie danych z pliku CSV
df = pd.read_csv('CCC.csv')

# Obliczenie wskaźnika MACD
macd, macdsignal, macdhist = talib.MACD(df['Zamkniecie'], fastperiod=12, slowperiod=26, signalperiod=9)

# Obliczenie punktów Pivot
high = df['Najwyzszy']
low = df['Najnizszy']
close = df['Zamkniecie']

# Obliczenie pasm Bollingera
upper, middle, lower = talib.BBANDS(df['Zamkniecie'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

# Wypisanie wyników
print("Wskaźnik MACD:\n", macd.tail())
print("\nPasma Bollingera:\n", upper.tail(), middle.tail(), lower.tail())
