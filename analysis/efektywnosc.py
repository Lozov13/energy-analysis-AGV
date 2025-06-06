import pandas as pd
import os
import plotly.express as px

def get_data_dir():
    # Pobierz absolutną ścieżkę do katalogu głównego projektu (tam gdzie app.py)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def analyze_efektywnosc():
    # Przykład: analiza dla jazdy prosto
    data_dir = get_data_dir()
    df = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    df['Time stamp'] = pd.to_datetime(df['Time stamp'])
    avg_energy = df['Momentary energy consumption mWh'].mean()
    total_energy = df['Total energy consumption uWh'].iloc[-1] - df['Total energy consumption uWh'].iloc[0]
    total_energy_mWh = total_energy / 1000
    # Wykres zużycia energii w czasie
    fig = px.line(df, x='Time stamp', y='Momentary energy consumption mWh', title='Chwilowe zużycie energii (jazda prosto)')
    return {
        "avg_energy": avg_energy,
        "total_energy_mWh": total_energy_mWh,
        "fig": fig
    }
