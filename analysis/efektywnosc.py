import pandas as pd
import os
import plotly.express as px

def analyze_efektywnosc(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    # Szukamy kolumn po fragmencie nazwy
    energy_col = [col for col in df.columns if 'momentary energy consumption' in col.lower()][0]
    total_energy_col = [col for col in df.columns if 'total energy consumption' in col.lower()][0]
    time_col = [col for col in df.columns if 'time' in col.lower()][0]

    df[time_col] = pd.to_datetime(df[time_col])
    avg_energy = df[energy_col].mean()
    total_energy = df[total_energy_col].iloc[-1] - df[total_energy_col].iloc[0]
    total_energy_mWh = total_energy / 1000

    fig = px.line(df, x=time_col, y=energy_col, title='Chwilowe zużycie energii (jazda prosto)')
    return {
        "avg_energy": avg_energy,
        "total_energy_mWh": total_energy_mWh,
        "fig": fig
    }
