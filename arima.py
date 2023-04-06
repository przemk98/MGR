import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
## Poprawic zmnienne
# Wczytanie danych z pliku csv
data = pd.read_csv('CCC.csv', parse_dates=['Data'], dayfirst=True)

# Ustawienie indeksu na kolumnę "Data"
data = data.set_index(pd.DatetimeIndex(data['Data']).to_period('M'))

# Usunięcie kolumny "Data"
data.drop('Data', axis=1, inplace=True)
#data.index = pd.DatetimeIndex(data.index).to_period('D')
# Podział danych na zbiór treningowy i testowy
train_size = int(len(data) * 0.8)
train, test = data.iloc[:train_size], data.iloc[train_size:]

# Wykonanie modelu ARIMA
model = ARIMA(train, order=(2, 1, 2), seasonal_order=(1, 1, 1, 12))
model_fit = model.fit()

# Prognozowanie dla zbioru testowego
forecast = model_fit.forecast(steps=len(test))[0]

# Obliczenie błędu prognozowania
mse = mean_squared_error(test, forecast)

# Wykres przedstawiający dane oraz prognozę
plt.plot(train, label='Dane treningowe')
plt.plot(test, label='Dane testowe')
plt.plot(test.index, forecast, label='Prognoza')
plt.legend(loc='best')
plt.show()

# Wyświetlenie wyników
print('Wyniki modelu ARIMA:')
print(f'RMSE: {np.sqrt(mse)}')
print(f'Prognoza dla kolejnego miesiąca: {model_fit.forecast(steps=1)[0][0]}')

# Określenie, czy należy kupować, trzymać czy sprzedawać akcje
last_month_data = data.iloc[-1]
last_month_forecast = model_fit.forecast(steps=1)[-1]
if last_month_forecast > last_month_data:
    print('Należy kupować akcje.')
elif last_month_forecast < last_month_data:
    print('Należy sprzedawać akcje.')
else:
    print('Należy trzymać akcje.')
