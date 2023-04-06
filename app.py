from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Wczytanie danych z pliku csv
    #df = pd.read_csv('gpw.csv')
    spolki = ['ASSECO-POLAND', 'ALE', 'CCC', 'CD-PROJEKT', 'CYFROWY-POLSAT', 'DNP', 'JSW-JASTRZEBSKA-SPOLKA-WEGLOWA',
                 'KGHM', 'KRUK', 'KETY', 'LPP',
                 'MBANK', 'ORANGE', 'PCO', 'PEKAO', 'PGE', 'PKN-ORLEN', 'PKO', 'PZU', 'SPL']
    # Tworzenie listy dostępnych spółek
    #spolki = df['Nazwa'].unique()
    wig= pd.read_csv('gpw.csv')
    return render_template('index.html', spolki=spolki,wig=wig)

@app.route('/analizy', methods=['GET', 'POST'])
def analizy():
    if request.method == 'POST':
        spolka = request.form['spolka']
        return redirect(url_for('analiza_spolki', spolka=spolka))
    else:
        return redirect(url_for('index'))

@app.route('/analiza/<spolka>')
def analiza_spolki(spolka):
    # Wczytanie danych z pliku csv
    df = pd.read_csv(spolka+'.csv')

    # Filtrowanie danych dla wybranej spółki
    df_spolka = df[df['spolka'] == spolka]

    # Tworzenie wykresów
    # ...

    return render_template('analiza.html', spolka=spolka)

    app.run(debug=True)
