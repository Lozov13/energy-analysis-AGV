import pandas as pd
import os
import plotly.express as px

def analyze_optymalizacja(data_dir):
    df_acc = pd.read_csv(os.path.join(data_dir, 'przyspieszenie.txt'))
    df_cruise = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    energy_col = [col for col in df_acc.columns if 'momentary energy consumption' in col.lower()][0]
    time_col = [col for col in df_acc.columns if 'time' in col.lower()][0]

    df_acc['Tryb'] = 'Przyspieszenie'
    df_cruise['Tryb'] = 'Jazda prosto'
    df_all = pd.concat([df_acc, df_cruise])

    fig = px.line(df_all, x=time_col, y=energy_col, color='Tryb',
                  title='Zużycie energii: przyspieszenie vs jazda prosto')
    avg_acc = df_acc[energy_col].mean()
    avg_cruise = df_cruise[energy_col].mean()
    return {
        "avg_acc": avg_acc,
        "avg_cruise": avg_cruise,
        "fig": fig
    }
