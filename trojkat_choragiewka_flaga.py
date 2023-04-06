#talib.py
import talib
import pandas as pd
#aaron nie wchodzi w loopie, dodac indeksacje
# Wczytanie danych z pliku CSV
df = pd.read_csv('ALE.csv', parse_dates=['Data'], dayfirst=True)
df.set_index('Data', inplace=True)
#print (df)
# Obliczenie wskaźnika Aroon
aroon = talib.AROON(df['Najwyzszy'], df['Najnizszy'], timeperiod=14)

# Szukanie formacji chorągiewki
for i in range(len(aroon) - 3):
    if aroon[i] > 70 and aroon[i+1] > 70 and aroon[i+2] < 30 and aroon[i+3] < 30:
        print('Znaleziono formację chorągiewki w dniu', df.index[i+3])
    else:
        print("Brak Formacji chorągiewki")

# Szukanie formacji flagi
for i in range(len(aroon) - 3):
    if aroon[i] < 30 and aroon[i+1] < 30 and aroon[i+2] > 70 and aroon[i+3] > 70:
        print('Znaleziono formację flagi w dniu', df.index[i+3])
    else:
        print("Brak Formacji chorągiewki")
print ("KOniec")
