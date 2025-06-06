import pandas as pd
import os
import plotly.graph_objects as go

def get_data_dir():
    # Pobierz absolutną ścieżkę do katalogu głównego projektu (tam gdzie app.py)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def analyze_tryby():
    # Załaduj dane z różnych manewrów
    data_dir = get_data_dir()
    files = {
        'Jazda prosto': 'jazda_prosto.txt',
        'Hamowanie': 'hamowanie.txt',
        'Przyspieszenie': 'przyspieszenie.txt',
        'Zakręt': 'zakret-sekcja3.txt',
        'Łuk': 'luk-sekcja2.txt',
        'Obrót': 'obrot-sekcja1.txt',
        'Postój': 'postoj.txt'
    }
    avg_energies = {}
    for mode, fname in files.items():
        df = pd.read_csv(os.path.join(data_dir, fname))
        avg_energies[mode] = df['Momentary energy consumption mWh'].mean()
    # Wykres porównawczy
    fig = go.Figure([go.Bar(x=list(avg_energies.keys()), y=list(avg_energies.values()))])
    fig.update_layout(title="Średnie chwilowe zużycie energii w trybach pracy", yaxis_title="mWh")
    return {
        "avg_energies": avg_energies,
        "fig": fig
    }
