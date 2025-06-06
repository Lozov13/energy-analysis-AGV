import pandas as pd
import os
import plotly.express as px

def analyze_bateria(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    time_col = [col for col in df.columns if 'time' in col.lower()][0]
    voltage_col = [col for col in df.columns if 'battery cell voltage' in col.lower()][0]
    soc_col = [col for col in df.columns if 'state of charge' in col.lower() or 'soc' in col.lower()]
    df[time_col] = pd.to_datetime(df[time_col])

    fig_voltage = px.line(df, x=time_col, y=voltage_col, title='Napięcie ogniwa w czasie')
    avg_voltage = df[voltage_col].mean()
    min_voltage = df[voltage_col].min()

    fig_soc = None
    if soc_col:
        fig_soc = px.line(df, x=time_col, y=soc_col[0], title='Stan naładowania baterii (SoC) w czasie')
    return {
        "avg_voltage": avg_voltage,
        "min_voltage": min_voltage,
        "fig_voltage": fig_voltage,
        "fig_soc": fig_soc
    }
