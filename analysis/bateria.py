import pandas as pd
import os
import plotly.express as px

def get_data_dir():
    # Pobierz absolutną ścieżkę do katalogu głównego projektu (tam gdzie app.py)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def analyze_bateria():
    # Analiza na podstawie jazdy prosto (lub innego pliku z dłuższego cyklu)
    data_dir = get_data_dir()
    df = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    df['Time stamp'] = pd.to_datetime(df['Time stamp'])
    # Trend napięcia baterii
    fig_voltage = px.line(df, x='Time stamp', y='Battery cell voltage mV', title='Napięcie ogniwa w czasie')
    # Trend SoC (jeśli masz taką kolumnę)
    soc_col = [col for col in df.columns if 'SoC' in col or 'state of charge' in col.lower()]
    fig_soc = None
    if soc_col:
        fig_soc = px.line(df, x='Time stamp', y=soc_col[0], title='Stan naładowania baterii (SoC) w czasie')
    # Średnie i minimalne wartości
    avg_voltage = df['Battery cell voltage mV'].mean()
    min_voltage = df['Battery cell voltage mV'].min()
    return {
        "avg_voltage": avg_voltage,
        "min_voltage": min_voltage,
        "fig_voltage": fig_voltage,
        "fig_soc": fig_soc
    }
