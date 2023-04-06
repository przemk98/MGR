import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

# Wczytanie danych z pliku csv
df = pd.read_csv('gpw.csv')

# Określenie daty początkowej i końcowej badanego okresu
start_date = '2022-01-01'
end_date = '2022-12-31'

# Wybranie danych dla wybranej spółki w badanym okresie
df = df.loc[(df['Nazwa spółki'] == 'CD PROJEKT') & (df['Data'] >= start_date) & (df['Data'] <= end_date)]

# Utworzenie wykresu
fig = go.Figure(data=[go.Candlestick(x=df['Data'],
                open=df['Otwarcie'],
                high=df['Najwyzszy'],
                low=df['Najnizszy'],
                close=df['Zamkniecie'])])

# Dodanie wolumenu obrotów
fig.add_trace(go.Bar(x=df['Data'], y=df['Wolumen'], name='Wolumen'))

# Dodanie trendu
fig.add_trace(go.Scatter(x=df['Data'], y=df['Trend'], mode='lines', name='Trend'))

# Konfiguracja wykresu
fig.update_layout(
    title='Wykres świecowy spółki CD PROJEKT w okresie 2022',
    yaxis_title='Cena',
    xaxis_rangeslider_visible=True)

# Wyświetlenie wykresu
pyo.plot(fig)