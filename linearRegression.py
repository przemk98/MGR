import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
#firma= spolka +'csv'
# Wczytanie danych z pliku CSV
df = pd.read_csv('MBANK.csv', parse_dates=['Data'],dayfirst=True)
df.set_index('Data', inplace=True)

# Określenie okresu przewidywania
prediction_period = 30 # liczba dni

# Przygotowanie danych do analizy regresji
X = np.array(range(len(df))).reshape(-1, 1)
y = df['Zamkniecie'].values.reshape(-1, 1)

# Utworzenie modelu regresji liniowej
regression_model = LinearRegression()
regression_model.fit(X, y)

# Przewidywanie wartości dla określonego okresu
prediction_index = np.array(range(len(df), len(df) + prediction_period)).reshape(-1, 1)
predicted_values = regression_model.predict(prediction_index)

# Wyświetlenie przewidywanych wartości
print('Przewidywane wartości dla kolejnych', prediction_period, 'dni:')
for i in range(len(predicted_values)):
    print('Dzień', i+1, ':', predicted_values[i][0])
