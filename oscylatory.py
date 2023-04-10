import pandas as pd
import talib
import matplotlib.pyplot as plt

# wczytanie danych z pliku CSV
df = pd.read_csv('CCC.csv',dayfirst=True)

# wyznaczenie wskaźników
df['macd'], df['macd_signal'], df['macd_hist'] = talib.MACD(df['Zamkniecie'])
df['rsi'] = talib.RSI(df['Zamkniecie'])
df['slowk'], df['slowd'] = talib.STOCH(df['Najwyzszy'], df['Najnizszy'], df['Zamkniecie'])

# wyświetlenie wykresu świecowego
fig, ax = plt.subplots()
ax.set_title('oscylator stochastyczny, RSI i MACD')

candlestick = ax.plot(df['Data'], df[['Otwarcie', 'Najwyzszy', 'Najnizszy', 'Zamkniecie']].values, 'k', lw=0.5, alpha=1.0)
ax.set_ylabel('Cena')
#ax.xaxis_date()

# wyświetlenie oscylatora stochastycznego
ax2 = ax.twinx()
stoch = ax2.plot(df['Data'], df['slowk'], 'b', lw=0.5, alpha=0.5)
ax2.plot(df['Data'], df['slowd'], 'r', lw=0.5, alpha=0.5)
ax2.fill_between(df['Data'], y1=20, y2=80, color='#adccff', alpha=0.2)
ax2.set_ylabel('Oscylator Stochastyczny')

# wyświetlenie RSI
ax3 = ax2.twinx()
rsi = ax3.plot(df['Data'], df['rsi'], 'm', lw=0.5, alpha=0.5)
ax3.fill_between(df['Data'], y1=30, y2=70, color='#ffa5ff', alpha=0.2)
ax3.set_ylabel('RSI')

# wyświetlenie MACD
ax4 = ax.twinx()
macd = ax4.plot(df['Data'], df['macd'], 'g', lw=0.5, alpha=0.5)
ax4.plot(df['Data'], df['macd_signal'], 'r', lw=0.5, alpha=0.5)
ax4.fill_between(df['Data'], y1=df['macd_hist'], y2=0, where=df['macd_hist']>0, facecolor='green', alpha=0.5)
ax4.fill_between(df['Data'], y1=df['macd_hist'], y2=0, where=df['macd_hist']<0, facecolor='red', alpha=0.5)
#ax4.set_ylabel('MACD')

# ustawienie legendy
lines = candlestick + stoch + rsi + macd
labels = [l.get_label() for l in lines]
#
ax.legend(lines, labels, loc='upper left')

# wyświetlenie wykresu
plt.show()
