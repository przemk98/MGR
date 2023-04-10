import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Wczytanie danych z pliku CSV
df = pd.read_csv('CCC.csv', parse_dates=True, index_col=0, dayfirst=True)
# Wczytanie danych z pliku CSV

# Wybranie jednej kolumny jako zmienna zależna
endog = df['Zamkniecie']

# Wyznaczenie modelu ARIMA
#model = SARIMAX(endog=endog, order=(1,0,0), seasonal_order=(1,1,1,12)).fit()

# Predykcja wartości

# Wyświetlenie wykresu szeregu czasowego
plt.plot(df)

# Wyznaczenie modelu ARIMA
model = sm.tsa.ARIMA(endog=endog , order=(1,1,1)).fit()
forecast = model.forecast(steps=10)
print(forecast)
#preds = model.predict(start='2022-01-01', end='2022-12-31')
# Wyświetlenie wyników modelowania
print(model.summary())

# Wyświetlenie wykresu dopasowanego modelu
plt.plot(model.fittedvalues, color='red')

# Wyświetlenie wykresu reszt modelu
plt.plot(model.resid, color='green')

plt.show()
