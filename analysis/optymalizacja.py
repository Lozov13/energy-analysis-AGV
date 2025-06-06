import pandas as pd
import os
import plotly.express as px

def get_data_dir():
    # Pobierz absolutną ścieżkę do katalogu głównego projektu (tam gdzie app.py)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def analyze_optymalizacja():
    # Przykład: porównanie profilu prędkości i zużycia energii podczas przyspieszania i jazdy prosto

    data_dir = get_data_dir()
    df_acc = pd.read_csv(os.path.join(data_dir, 'przyspieszenie.txt'))
    df_cruise = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    # Tworzymy wykresy do porównania
    fig = px.line(
        pd.concat([
            df_acc.assign(Tryb='Przyspieszenie'),
            df_cruise.assign(Tryb='Jazda prosto')
        ]),
        x='Time stamp', y='Momentary energy consumption mWh', color='Tryb',
        title='Zużycie energii: przyspieszenie vs jazda prosto'
    )
    # Propozycja: optymalizacja – np. wyliczenie ile można zaoszczędzić energii przy łagodniejszym przyspieszaniu (tu tylko przykład, szczegóły zależą od danych)
    avg_acc = df_acc['Momentary energy consumption mWh'].mean()
    avg_cruise = df_cruise['Momentary energy consumption mWh'].mean()
    return {
        "avg_acc": avg_acc,
        "avg_cruise": avg_cruise,
        "fig": fig
    }
