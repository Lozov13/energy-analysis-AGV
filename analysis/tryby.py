import pandas as pd
import os
import plotly.graph_objects as go

def analyze_tryby(data_dir):
    files = {
        'Jazda prosto': 'jazda_prosto.txt',
        'Hamowanie': 'hamowanie.txt',
        'Przyspieszenie': 'przyspieszenie.txt',
        'Zakręt': 'zakret - sekcja3.txt',
        'Łuk': 'luk - sekcja2.txt',
        'Obrót': 'obrot - sekcja1.txt',
        'Postój': 'postoj.txt'
    }
    avg_energies = {}
    for mode, fname in files.items():
        df = pd.read_csv(os.path.join(data_dir, fname))
        energy_col = [col for col in df.columns if 'momentary energy consumption' in col.lower()][0]
        avg_energies[mode] = df[energy_col].mean()
    fig = go.Figure([go.Bar(x=list(avg_energies.keys()), y=list(avg_energies.values()))])
    fig.update_layout(title="Średnie chwilowe zużycie energii w trybach pracy", yaxis_title="mWh")
    return {
        "avg_energies": avg_energies,
        "fig": fig
    }
